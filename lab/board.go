package main

import (
	"fmt"
	"strings"
)

func renderBoard(s *LabState) string {
	var proposed, experimenting, done []Hypothesis
	for _, h := range s.Hypotheses {
		switch h.Status {
		case "proposed":
			proposed = append(proposed, h)
		case "experimenting":
			experimenting = append(experimenting, h)
		case "done":
			done = append(done, h)
		}
	}

	var sb strings.Builder

	sb.WriteString("| | 💡 Proposed | 🧪 Experimenting | 📊 Result |\n")
	sb.WriteString("|---|---|---|---|\n")

	max := len(proposed)
	if len(experimenting) > max {
		max = len(experimenting)
	}
	if len(done) > max {
		max = len(done)
	}
	if max == 0 {
		sb.WriteString("| **—** | *No hypotheses yet — be the first!* | — | — |\n")
	}

	for i := 0; i < max; i++ {
		p, e, d := "—", "—", "—"
		if i < len(proposed) {
			h := proposed[i]
			p = fmt.Sprintf("#%d: %s · `%d 👍`", h.ID, truncate(h.Text, 40), h.Votes)
		}
		if i < len(experimenting) {
			h := experimenting[i]
			bar := progressBar(h.Progress)
			e = fmt.Sprintf("#%d: %s · %s %d%%", h.ID, truncate(h.Text, 28), bar, h.Progress)
		}
		if i < len(done) {
			h := done[i]
			d = fmt.Sprintf("✓ #%d: %s", h.ID, truncate(h.Result, 38))
		}
		sb.WriteString(fmt.Sprintf("| **%d** | %s | %s | %s |\n", i+1, p, e, d))
	}

	sb.WriteString(fmt.Sprintf(
		"\n*Last updated: %s · %d hypotheses · %d contributors*",
		s.UpdatedAt, len(s.Hypotheses), s.Contributors,
	))

	return sb.String()
}

func progressBar(pct int) string {
	filled := pct / 10
	empty := 10 - filled
	return strings.Repeat("█", filled) + strings.Repeat("░", empty)
}

func truncate(s string, n int) string {
	if len(s) <= n {
		return s
	}
	return s[:n-1] + "…"
}
