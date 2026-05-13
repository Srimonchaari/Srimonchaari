package main

import (
	"encoding/json"
	"os"
	"time"
)

type Hypothesis struct {
	ID          int    `json:"id"`
	Text        string `json:"text"`
	Status      string `json:"status"` // "proposed", "experimenting", "done"
	Votes       int    `json:"votes"`
	Progress    int    `json:"progress"` // 0-100, only used when experimenting
	Result      string `json:"result"`   // only set when done
	Contributor string `json:"contributor"`
}

type LabState struct {
	Hypotheses  []Hypothesis `json:"hypotheses"`
	UpdatedAt   string       `json:"updated_at"`
	Contributors int         `json:"contributors"`
}

func loadState(path string) (*LabState, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return &LabState{UpdatedAt: today(), Contributors: 0}, nil
	}
	var s LabState
	if err := json.Unmarshal(data, &s); err != nil {
		return nil, err
	}
	return &s, nil
}

func saveState(path string, s *LabState) error {
	s.UpdatedAt = today()
	data, err := json.MarshalIndent(s, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(path, data, 0644)
}

func (s *LabState) nextID() int {
	max := 0
	for _, h := range s.Hypotheses {
		if h.ID > max {
			max = h.ID
		}
	}
	return max + 1
}

func (s *LabState) findByID(id int) *Hypothesis {
	for i := range s.Hypotheses {
		if s.Hypotheses[i].ID == id {
			return &s.Hypotheses[i]
		}
	}
	return nil
}

func today() string {
	return time.Now().UTC().Format("2006-01-02")
}
