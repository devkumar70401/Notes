# Antigravity CLI (`agy`) Slash Commands, Cautions & Failure Modes

A definitive reference for Antigravity CLI (`agy`) slash commands, shell execution mechanics, precautions, and technical failure mode breakdowns.

---

## ⚡ Direct CLI Slash Commands Reference

Slash commands starting with `/` are intercepted directly by the `agy` CLI client before any prompt is processed by the AI model.

| Slash Command | Action / Behavior | Purpose |
| :--- | :--- | :--- |
| **`/clear`** *(or `/reset`)* | Clears terminal screen and purges active transient chat context. | Resets memory context without quitting CLI. |
| **`/new`** | Initializes a brand new conversation session. | Starts a clean task context from scratch. |
| **`/exit`** *(or `/quit`)* | Exits `agy` immediately to the host shell. | Terminates the CLI session (or press `Ctrl+D`). |
| **`/help`** | Displays built-in CLI slash command reference. | Quick offline help guide. |
| **`/config`** | Opens CLI interactive configuration manager. | Manages theme, trusted workspaces, and settings. |
| **`/plan`** | Activates structured step-by-step planning mode. | Forces explicit pre-execution design blueprints. |
| **`/grill-me`** | Starts interactive design interview mode. | Aligns architectural decisions before coding. |
| **`/learn`** | Saves a newly learned workflow behavior or rule. | Persists custom rules for future sessions. |

---

## ⚠️ Cautions & 💥 Vulnerability / Failure Mode Breakdown

### 1. Context Purging & State Loss (`/clear` & `/reset`)
* **Failure Mode**: Executing `/clear` mid-debugging permanently erases active stack tracebacks, variable states, and diagnostic history from the LLM context window.
* **Caution**: Never run `/clear` while troubleshooting an unresolved bug unless you intend to start a completely fresh diagnostic chain.

### 2. Shell History Expansion Collisions (`!command` & `$command`)
* **Failure Mode**: In bash/zsh, prefixing unquoted text with `!` (e.g. `!clear` or `!git`) triggers shell history expansion, executing whichever past command matches the prefix—potentially running destructive commands without confirmation.
* **Caution**: Always use official slash syntax (`/clear`, `/new`) instead of exclamation marks or shell sigils.

### 3. Subshell vs. Host Shell Isolation
* **Failure Mode**: Environmental changes executed inside `agy` (such as `export VAR=val` or `cd /path`) apply to background tool subshells, but do not mutate the host terminal environment after `agy` exits.
* **Caution**: To run raw uninterpreted bash commands, open a second VS Code terminal tab (`Ctrl + Shift + \`) alongside `agy`.

---

## 💡 Best Practices for AGY CLI Productivity

1. **Dual Terminal Setup**: Keep `agy` in Terminal Tab 1, and standard Bash shell in Terminal Tab 2.
2. **Context Preservation**: Use `/new` when starting an entirely unrelated coding feature to keep LLM context clean and efficient.
