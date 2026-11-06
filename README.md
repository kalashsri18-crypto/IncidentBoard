<div align="center">

# 🚨 IncidentBoard

### Lightweight Issue Reporting & Resolution Tracker

Report issues, assign ownership, and follow every task through to resolution.

![Status](https://img.shields.io/badge/Status-Implemented-brightgreen?style=for-the-badge)
![Planned Python](https://img.shields.io/badge/Planned-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Planned Flask](https://img.shields.io/badge/Planned-Flask-black?style=for-the-badge&logo=flask&logoColor=white)

</div>

---

## 📌 Overview

**IncidentBoard** is a Flask + SQLite issue tracker for student teams and small organizations to report, prioritize, assign, and resolve issues. It is designed to make it easier to report problems, assign responsibility, set priorities, and track issues until they are resolved.

> **Current status:** Implemented with issue creation, priority and assignee updates, status transitions, filtering, and an activity history.

## ✨ Features

- 📝 Create issues with a title, description, and category
- 🎯 Set priority: Low, Medium, High, or Critical
- 👤 Assign issues to team members
- 🔄 Track status from Open to In Progress to Resolved
- 🔎 Filter issues by status, priority, or assignee
- 🕒 Maintain a timestamped activity history
- 📊 View summaries of open and resolved issues

## 🛠️ Tech Stack

| Technology | Intended use |
|---|---|
| Python 3.10+ | Core programming language |
| Flask | Web application |
| SQLite | Local data storage |
| HTML, CSS, JavaScript | User interface |
| pytest | Automated testing |

## 🔄 Issue Workflow

```text
Open → In Progress → Resolved
  └────────────────→ Closed
```

Important status and assignment changes should create an activity entry containing the issue ID, action, timestamp, and relevant details.

## 🗺️ Roadmap

- [ ] Set up Flask application and SQLite schema
- [ ] Implement issue creation and editing
- [ ] Add assignment and priority controls
- [ ] Build status transitions and activity history
- [ ] Add filters and dashboard summaries
- [ ] Write automated tests and add sample issues
- [ ] Add screenshots and deployment instructions

## 🚀 Getting Started

```bash
git clone https://github.com/kalashsri18-crypto/IncidentBoard.git
cd IncidentBoard
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Run tests with `pytest -q`.

## 📁 Project Structure

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

## 👨‍💻 Author

**Kalash Srivastava**  
[GitHub](https://github.com/kalashsri18-crypto) · [LinkedIn](https://www.linkedin.com/in/kalash-srivastava-b6592a3b3) · [Email](mailto:kalashsri18@gmail.com)

---

<div align="center">
  Documentation and project direction by Kalash
</div>
