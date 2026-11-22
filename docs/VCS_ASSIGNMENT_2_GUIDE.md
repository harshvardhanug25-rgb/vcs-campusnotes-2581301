# VCS Assignment 2 - Harsh Vardhan Singh

URN: 2581301  
Section: 3F  
Course: CSE25303 - Version Control System

This file is a working checklist, not fabricated evidence. The repository contents and commit history are online. The local command demonstrations and screenshots below must be captured by the student on the machine where Git is configured.

## Q1 - Remote repository workflow

Repository: https://github.com/harshvardhanug25-rgb/vcs-campusnotes-2581301

The public repository has a `main` branch and a remote `features/notes-list` branch. To collect the required local evidence, run:

```bash
git clone https://github.com/harshvardhanug25-rgb/vcs-campusnotes-2581301.git campusnotes
cd campusnotes
git remote -v
git branch -a
git switch --track -c features/notes-list origin/features/notes-list
git branch -vv

# In a second folder:
cd ..
git clone https://github.com/harshvardhanug25-rgb/vcs-campusnotes-2581301.git campusnotes-second
cd campusnotes-second
echo "Second clone workflow check" >> README.md
git add README.md
git commit -m "docs: record second clone workflow"
git push origin main

# Return to the original clone:
cd ../campusnotes
git pull origin main
git log --oneline -5
```

Capture terminal screenshots showing `git remote -v`, the push from the second clone and the pull in the first clone. The GitHub connector cannot run commands on the student's own computer, so these screenshots remain to be captured.

## Q2 - Fork, feature branch and pull request

The selected partner repository is Parivesh Singh's `parivesh25/vcs-campusnotes-2581138`. Its current access is read-only for this connected GitHub session. No fork or pull request was created from this session. To complete Q2, Harsh must fork the partner repository from GitHub, clone that fork, set the original as `upstream`, create a branch named `feature/harshvardhan-<change>`, commit one useful change, push the branch, and open a pull request to the partner repository. Link the PR to a real issue and capture its description.

Suggested contribution: add a concise `CONTRIBUTING.md` with setup, branch naming, commit-message and pull-request instructions.

## Q3 - Code review and merge

Q3 needs a genuine partner pull request in Harsh's repository and a genuine review cycle. No partner PR was available in Harsh's new repository during this setup, so no review comments, suggested change, approval, reply or merge are claimed here. After the partner opens a PR, add at least three specific inline comments, use one GitHub suggested change, submit a review decision, reply to the review comments on Harsh's PR, push a follow-up commit, and merge as repository owner. Record the review, reply and merged-PR URLs.

Suggested two-line merge justification (use only if this is the actual strategy chosen): "Squash merge keeps the main branch history focused by combining the review iterations into one contribution commit. The feature branch retains the detailed discussion and incremental changes for reference."

## Q4 - Commit conventions, tags and release

The repository history includes `feat:`, `fix:`, `docs:`, `refactor:` and `chore:` messages, plus a `test:` commit. The `.gitignore` excludes Python cache/test files and local `.sqlite3` databases.

After reviewing the history locally, create and push the required tags:

```bash
git log --oneline -10
git tag -a v0.1.0
```

For the assignment, `v0.1.0` must be a lightweight tag, so use `git tag v0.1.0` (not `-a`) if it does not exist. Create the annotated release tag and push both:

```bash
git tag v0.1.0
git tag -a v1.0.0 -m "CampusNotes v1.0.0 release"
git push origin v0.1.0 v1.0.0
git tag -n
```

Then publish a GitHub Release from `v1.0.0` with notes describing the CLI, validation, search, tests and hooks. Record the release URL. Tags and the release were not created by the connected GitHub actions in this session.

## Q5 - Git hooks

The executable hook scripts are stored in `.githooks/pre-commit` and `.githooks/commit-msg`. Enable them locally:

```bash
git config core.hooksPath .githooks
git config --get core.hooksPath
```

Demonstrate the pre-commit hook by staging a temporary file containing a prohibited unfinished-work marker and attempting a commit; then remove the marker, stage the corrected file and commit successfully. Demonstrate the commit-msg hook by trying a short message and a non-conventional message, then committing with a valid message such as `docs: add a useful campus note`. Capture each blocked and successful terminal result.

**Analysis (4-5 lines):** Hooks in `.git/hooks` are local Git metadata, not tracked project files, so they are not transferred by `git push` and are absent from a fresh clone. A team can keep hook scripts in a tracked `.githooks` folder and configure each clone with `git config core.hooksPath .githooks`. The pre-commit hook can inspect staged file contents, while commit-msg can validate the message file. `git commit --no-verify` bypasses client-side checks, so equivalent checks should also run in CI or server-side branch protection.

## AI-use disclosure

AI was used to help draft the starter application, tests, documentation and hook scripts. Harsh must run and verify the local Git commands, tests and hook demonstrations before submission and should update this disclosure if the actual use differs.
