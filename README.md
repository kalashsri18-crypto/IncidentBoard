# IncidentBoard

A small-team issue reporting and resolution board with priorities, status transitions, assignment, and an audit trail.

## Status

Initial project scaffold. The application, tests, setup guide, and usage documentation are being added directly to the `main` branch.

## Planned stack

- Python 3.10+
- Flask
- SQLite (built-in Python database driver)
- HTML, CSS, and vanilla JavaScript
- pytest

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000.

## Tests

```bash
pytest
```

## License

MIT. See [LICENSE](LICENSE).
