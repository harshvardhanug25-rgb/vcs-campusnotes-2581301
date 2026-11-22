"""CampusNotes command-line application."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def default_store() -> Path:
    """Return the per-user JSON store path."""
    return Path.home() / ".campusnotes" / "notes.json"


def load_notes(store: Path) -> list[dict]:
    if not store.exists():
        return []
    with store.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("The notes file must contain a JSON list.")
    return data


def save_notes(notes: list[dict], store: Path) -> None:
    store.parent.mkdir(parents=True, exist_ok=True)
    temporary = store.with_suffix(".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(notes, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    temporary.replace(store)


def add_note(title: str, body: str, store: Path | None = None) -> dict:
    destination = store or default_store()
    notes = load_notes(destination)
    note = {
        "id": uuid4().hex[:8],
        "title": title,
        "body": body,
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    notes.append(note)
    save_notes(notes, destination)
    return note


def find_notes(query: str, store: Path | None = None) -> list[dict]:
    notes = load_notes(store or default_store())
    term = query.casefold()
    return [
        note for note in notes
        if term in note["title"].casefold() or term in note["body"].casefold()
    ]


def format_note(note: dict) -> str:
    return f'[{note["id"]}] {note["title"]}\n{note["body"]}\n'


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create and search campus notes.")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="save a new note")
    add.add_argument("title")
    add.add_argument("body")

    commands.add_parser("list", help="list saved notes")

    search = commands.add_parser("search", help="search titles and note text")
    search.add_argument("query")

    show = commands.add_parser("show", help="display a note by its ID")
    show.add_argument("note_id")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    store = default_store()

    if args.command == "add":
        note = add_note(args.title, args.body, store)
        print(f'Saved note {note["id"]}: {note["title"]}')
    elif args.command == "list":
        notes = load_notes(store)
        if not notes:
            print("No notes yet. Add one with: python -m src.campusnotes add TITLE BODY")
        for note in notes:
            print(format_note(note))
    elif args.command == "search":
        matches = find_notes(args.query, store)
        for note in matches:
            print(format_note(note))
        if not matches:
            print("No matching notes.")
    elif args.command == "show":
        matches = [note for note in load_notes(store) if note["id"] == args.note_id]
        if not matches:
            print(f"No note found with ID {args.note_id}.")
            return 1
        print(format_note(matches[0]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
