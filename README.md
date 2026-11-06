# IncidentBoard
### Lightweight Issue Reporting & Resolution Tracker

IncidentBoard is a small-team issue tracking project for reporting problems, assigning ownership, setting priorities, and following each issue through to resolution. It is intended for student teams, labs, and small internal projects that need a simple shared workflow.

> **Repository description:** A lightweight issue-tracking board concept with priorities, assignment, status changes, and an activity history.

## Planned product features
- Create issues with title, description, and category
- Set priority (Low, Medium, High, Critical)
- Assign an issue to a team member
- Track status from Open to In Progress to Resolved
- Filter issues by status, priority, or assignee
- Record a timestamped activity trail for important changes
- View summary counts for open and resolved issues

## Planned technology
- Python 3.10+
- Flask
- SQLite
- HTML, CSS and vanilla JavaScript
- pytest

## Intended project structure
```text
.
├── app.py
├── requirements.txt
├── templates/
├── static/
├── tests/
├── .gitignore
├── LICENSE
└── README.md
```

## Development status
**Planning / README scaffold.** Only the project overview is currently present in this repository. The issue board, database, tests, and interface are not implemented yet. Features listed above describe the intended scope.

## Proposed issue lifecycle
```text
Open → In Progress → Resolved
  └──────────────→ Closed
```
A status or assignment change should create an activity entry with the issue ID, action, timestamp, and relevant details.

## Roadmap
- [ ] Implement Flask application and SQLite schema
- [ ] Add issue creation and editing
- [ ] Add assignment and priority controls
- [ ] Implement status transitions and activity history
- [ ] Add filtering and dashboard summaries
- [ ] Add tests, sample issues, and screenshots

## License
See [LICENSE](LICENSE) if a license file is added to this repository.
