# 🐙 Git & GitHub Mastery Guide

> **Domain**: `10_CS_&_Engineering/14_DevOps_&_Tools/Git_&_GitHub`  
> **Purpose**: Master version control, GitHub CLI (`gh`), advanced workflows, and repository management directly from the terminal.

---

## 📌 1. Core Git Architecture & Lifecycle

```
[ Working Directory ] ──(git add)──> [ Staging Area ] ──(git commit)──> [ Local Repo ] ──(git push)──> [ Remote GitHub ]
```

- **Working Directory**: Your actual files on local disk.
- **Staging Area (Index)**: Transient space where changes are prepared before committing.
- **Local Repository (`.git`)**: Committed snapshot history stored locally.
- **Remote Repository**: GitHub cloud repository (`git@github.com:...`).

---

## ⚡ 2. Essential Commands Cheatsheet

### Branching & Merging
```bash
# Create and switch to a new feature branch
git checkout -b feature/login-page

# Switch back to main branch
git checkout main

# Merge feature branch into main
git merge feature/login-page

# Delete feature branch after merge
git branch -d feature/login-page
```

### Undoing & Stashing
```bash
# Temporarily save uncommitted changes
git stash

# Re-apply stashed changes
git stash pop

# Discard local uncommitted modifications in a file
git checkout -- <file>

# Soft reset (keep changes in staging, undo commit)
git reset --soft HEAD~1
```

---

## 🚀 3. Terminal GitHub CLI (`gh`) Master Commands

Since `gh` is authenticated with your PAT token (`GH_TOKEN`), you can run all GitHub operations browserless:

| Task | Command |
| :--- | :--- |
| **Create Public Repo** | `gh repo create <repo_name> --public --source=. --push` |
| **Create Private Repo** | `gh repo create <repo_name> --private --source=. --push` |
| **List Repos** | `gh repo list devkumar70401` |
| **Clone Repo** | `gh repo clone devkumar70401/<repo_name>` |
| **Delete Repo** | `gh repo delete <repo_name> --yes` |
| **Create Pull Request**| `gh pr create --title "Feature" --body "Details"` |
| **Merge Pull Request** | `gh pr merge <pr_number> --merge` |

---

## 🔬 4. Advanced Concepts to Explore Next

- [ ] **Git Rebase vs. Merge**: Keeping clean linear commit histories vs preserving branch topology.
- [ ] **Git Worktrees**: Working on multiple branches simultaneously without switching checkouts.
- [ ] **GitHub Actions (CI/CD)**: Automating unit tests, linting, and Docker builds on every `git push`.
- [ ] **Git Submodules**: Nesting secondary Git repositories inside a parent project.
