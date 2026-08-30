# 🗄️ Antigravity Rules & Behavior Backup Archive

This folder contains a complete, restorable backup of all previous Antigravity workspace rules, global configuration rules, and behavior blueprints prior to switching to **Mentor-Only (Zero-Execution) Mode**.

---

## 📂 Backup Contents

1. **`GEMINI.md.bak`**: The full previous master workspace rule blueprint (dynamic mode router, vulnerability breakdown, mentor tip, mode matrix).
2. **`agents_rules/`**:
   - `god_level_teacher.md`
   - `master_notes_generator.md`
3. **`global_rules/`**:
   - `god_level_teacher.md`
   - `master_notes_generator.md`

---

## 🔄 How to Restore Previous Rules

To revert back to the previous god-level autonomous execution setup at any time, run:

```bash
# 1. Restore workspace root rule
cp /home/dev/SE/Notes/00_Meta_\&_System/Antigravity/Rules_Backup/GEMINI.md.bak /home/dev/SE/GEMINI.md

# 2. Restore .agents rules
cp /home/dev/SE/Notes/00_Meta_\&_System/Antigravity/Rules_Backup/agents_rules/* /home/dev/SE/.agents/rules/

# 3. Restore global rules
cp /home/dev/SE/Notes/00_Meta_\&_System/Antigravity/Rules_Backup/global_rules/* ~/.gemini/config/rules/
```
