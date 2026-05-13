// Open Research Lab engine — processes visitor commands from GitHub issue titles
// and updates the README board section between <!-- LAB_START --> and <!-- LAB_END -->.
//
// Issue title format: lab|<action>|<args...>
//
//   lab|propose|Your hypothesis text here        → adds to proposed column
//   lab|vote|<id>                                → upvotes a hypothesis
//   lab|experiment|<id>|<progress 0-100>         → moves to experimenting column
//   lab|result|<id>|<finding text>               → marks as done with result
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	statePath   = "lab_state.json"
	readmePath  = "README.md"
	labStart    = "<!-- LAB_START -->"
	labEnd      = "<!-- LAB_END -->"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "usage: lab <issue-title>")
		os.Exit(1)
	}

	title := os.Args[1]
	contributor := ""
	if len(os.Args) >= 3 {
		contributor = os.Args[2]
	}

	if !strings.HasPrefix(strings.ToLower(title), "lab|") {
		fmt.Println("Not a lab command — skipping.")
		os.Exit(0)
	}

	parts := strings.SplitN(title, "|", 5)
	if len(parts) < 3 {
		fmt.Fprintln(os.Stderr, "invalid lab command format")
		os.Exit(1)
	}

	action := strings.ToLower(strings.TrimSpace(parts[1]))

	state, err := loadState(statePath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "failed to load state: %v\n", err)
		os.Exit(1)
	}

	switch action {
	case "propose":
		if len(parts) < 3 || strings.TrimSpace(parts[2]) == "" {
			fmt.Fprintln(os.Stderr, "propose requires hypothesis text")
			os.Exit(1)
		}
		text := strings.TrimSpace(parts[2])
		h := Hypothesis{
			ID:          state.nextID(),
			Text:        text,
			Status:      "proposed",
			Votes:       1,
			Contributor: contributor,
		}
		state.Hypotheses = append(state.Hypotheses, h)
		if contributor != "" {
			state.Contributors++
		}
		fmt.Printf("✅ Added hypothesis #%d: %s\n", h.ID, text)

	case "vote":
		if len(parts) < 3 {
			fmt.Fprintln(os.Stderr, "vote requires hypothesis id")
			os.Exit(1)
		}
		id, err := strconv.Atoi(strings.TrimSpace(parts[2]))
		if err != nil {
			fmt.Fprintln(os.Stderr, "invalid id")
			os.Exit(1)
		}
		h := state.findByID(id)
		if h == nil {
			fmt.Fprintf(os.Stderr, "hypothesis #%d not found\n", id)
			os.Exit(1)
		}
		h.Votes++
		fmt.Printf("👍 Voted on hypothesis #%d — now at %d votes\n", id, h.Votes)

	case "experiment":
		if len(parts) < 4 {
			fmt.Fprintln(os.Stderr, "experiment requires id and progress")
			os.Exit(1)
		}
		id, err := strconv.Atoi(strings.TrimSpace(parts[2]))
		if err != nil {
			fmt.Fprintln(os.Stderr, "invalid id")
			os.Exit(1)
		}
		progress, err := strconv.Atoi(strings.TrimSpace(parts[3]))
		if err != nil || progress < 0 || progress > 100 {
			fmt.Fprintln(os.Stderr, "progress must be 0-100")
			os.Exit(1)
		}
		h := state.findByID(id)
		if h == nil {
			fmt.Fprintf(os.Stderr, "hypothesis #%d not found\n", id)
			os.Exit(1)
		}
		h.Status = "experimenting"
		h.Progress = progress
		fmt.Printf("🧪 Hypothesis #%d moved to experimenting at %d%%\n", id, progress)

	case "result":
		if len(parts) < 5 {
			fmt.Fprintln(os.Stderr, "result requires id and finding text")
			os.Exit(1)
		}
		id, err := strconv.Atoi(strings.TrimSpace(parts[2]))
		if err != nil {
			fmt.Fprintln(os.Stderr, "invalid id")
			os.Exit(1)
		}
		finding := strings.TrimSpace(parts[4])
		if finding == "" {
			fmt.Fprintln(os.Stderr, "finding text cannot be empty")
			os.Exit(1)
		}
		h := state.findByID(id)
		if h == nil {
			fmt.Fprintf(os.Stderr, "hypothesis #%d not found\n", id)
			os.Exit(1)
		}
		h.Status = "done"
		h.Result = finding
		fmt.Printf("📊 Hypothesis #%d marked done: %s\n", id, finding)

	default:
		fmt.Fprintf(os.Stderr, "unknown action: %s\n", action)
		os.Exit(1)
	}

	if err := saveState(statePath, state); err != nil {
		fmt.Fprintf(os.Stderr, "failed to save state: %v\n", err)
		os.Exit(1)
	}

	if err := updateReadme(state); err != nil {
		fmt.Fprintf(os.Stderr, "failed to update README: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("✅ README board updated.")
}

func updateReadme(state *LabState) error {
	data, err := os.ReadFile(readmePath)
	if err != nil {
		return err
	}

	content := string(data)
	startIdx := strings.Index(content, labStart)
	endIdx := strings.Index(content, labEnd)
	if startIdx == -1 || endIdx == -1 {
		return fmt.Errorf("LAB_START/LAB_END markers not found in README")
	}

	board := renderBoard(state)
	newSection := labStart + "\n" + board + "\n" + labEnd
	content = content[:startIdx] + newSection + content[endIdx+len(labEnd):]

	return os.WriteFile(readmePath, []byte(content), 0644)
}
