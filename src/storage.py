"""Persistence helpers for CampusNotes JSON data."""

import json
from pathlib import Path


def default_store() -> Path:
    """Return the per-user JSON store path."""
    return Path.home() / ".campusnotes" / "notes.json"


def load_notes(store: Path) -> list[dict]:
    """Load notes from disk, treating a missing file as an empty collection."""
    if not store.exists():
        return []
    with store.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("The notes file must contain a JSON list.")
    return data


def save_notes(notes: list[dict], store: Path) -> None:
    """Write notes atomically to avoid leaving a partially-written JSON file."""
    store.parent.mkdir(parents=True, exist_ok=True)
    temporary = store.with_suffix(".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(notes, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    temporary.replace(store)
