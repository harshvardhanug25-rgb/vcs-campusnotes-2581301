# CampusNotes - Setup and Usage

## Requirements

- Python 3.10 or newer
- Git
- No third-party Python packages are required

## Get the project

```bash
git clone https://github.com/harshvardhanug25-rgb/vcs-campusnotes-2581301.git
cd vcs-campusnotes-2581301
```

## Use the CLI

Create a note:

```bash
python -m src.campusnotes add "Data Structures" "Revise trees and graph traversal"
```

List all notes:

```bash
python -m src.campusnotes list
```

Search in titles and bodies (case-insensitive):

```bash
python -m src.campusnotes search traversal
```

Show one note by its short ID (printed when the note is created):

```bash
python -m src.campusnotes show 1a2b3c4d
```

The JSON store is created at `~/.campusnotes/notes.json`. The application writes updates to a temporary file and then replaces the store, reducing the chance of a partially written JSON document.

## Run the tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests cover persisted notes, whitespace validation, case-insensitive search and invalid store data.

## Shared Git hooks

Enable the tracked hooks in a fresh clone:

```bash
chmod +x .githooks/pre-commit .githooks/commit-msg
git config core.hooksPath .githooks
```

The pre-commit hook checks staged text files for prohibited unfinished-work markers. The commit-msg hook requires a message of at least 10 characters and one of the prefixes `feat:`, `fix:`, `docs:`, `refactor:` or `chore:`.

To inspect the configured hook directory:

```bash
git config --get core.hooksPath
```

## Contribution workflow

1. Create a feature branch from `main`.
2. Keep each change focused and use a Conventional Commit message.
3. Run the unit tests before pushing.
4. Open a pull request that explains what changed, why it is useful, and which issue it addresses.
