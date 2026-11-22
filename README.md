# CampusNotes

CampusNotes is a small Python command-line application for creating, listing, searching and displaying personal campus notes. It stores data as JSON in the current user's home directory and uses only the Python standard library.

## Quick start

```bash
python -m src.campusnotes add "Operating Systems" "Revise process scheduling"
python -m src.campusnotes list
python -m src.campusnotes search scheduling
```

## Features

- Add notes with non-empty titles and bodies.
- List saved notes and search their contents without case sensitivity.
- Display one note by its generated short ID.
- Persist notes safely in a per-user JSON file.
- Unit tests using Python's built-in `unittest` framework.
- Shared Git hooks for staged unfinished-work markers and commit-message conventions.

See [docs/USAGE.md](docs/USAGE.md) for installation, all commands, testing and contribution guidance.
