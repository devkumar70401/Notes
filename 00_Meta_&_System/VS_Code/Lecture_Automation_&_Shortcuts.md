# Zero-Mouse Lecture Workflow & Custom Shortcuts Guide

A complete guide to the automated "zero-mouse" note-taking workflow, background video media controls, custom Ubuntu keyboard shortcuts, and environment setup for IITM BS Online Degree lectures and VS Code.

---

## 🚀 Quick Reference: Custom Keyboard Shortcuts

| Shortcut Key | Action | Function / Description |
| :--- | :--- | :--- |
| **`Ctrl` + `Alt` + `Space`** | **Toggle Lecture Video** | Pauses or plays the Firefox lecture video in the background without shifting focus from VS Code. |
| **`Ctrl` + `Alt` + `Left`** | **Rewind 5 Seconds** | Rewinds the lecture video back 5 seconds if you missed a point while typing notes. |
| **`Alt` + `Esc`** | **Fast Focus Cycle** | Instantly cycles window focus between Browser, VS Code Editor, and Terminal without laggy OS popups. |
| **`Alt` + `Tab`** | **Toggle Previous Window** | Switches focus directly back and forth between your active note-taking window and browser. |

---

## 🛠️ Background Automation & Scripts

The background video controls use native Linux **MPRIS DBus interfaces** to control Firefox HTML5 / YouTube players without needing cursor interaction or window switching.

### 1. Toggle Lecture Script (`~/.local/bin/toggle-lecture`)
* **Location**: [`~/.local/bin/toggle-lecture`](file:///home/dev/.local/bin/toggle-lecture)
* **Code**:
  ```python
  #!/usr/bin/env python3
  import subprocess

  try:
      cmd = "dbus-send --session --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames"
      output = subprocess.check_output(cmd, shell=True).decode()
      for line in output.splitlines():
          if "org.mpris.MediaPlayer2" in line:
              bus_name = line.split('"')[1]
              subprocess.run(f"dbus-send --session --dest={bus_name} --type=method_call /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause", shell=True)
  except Exception:
      pass
  ```

### 2. Rewind Lecture Script (`~/.local/bin/rewind-lecture`)
* **Location**: [`~/.local/bin/rewind-lecture`](file:///home/dev/.local/bin/rewind-lecture)
* **Code**:
  ```python
  #!/usr/bin/env python3
  import subprocess

  try:
      cmd = "dbus-send --session --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames"
      output = subprocess.check_output(cmd, shell=True).decode()
      for line in output.splitlines():
          if "org.mpris.MediaPlayer2" in line:
              bus_name = line.split('"')[1]
              subprocess.run(f"dbus-send --session --dest={bus_name} --type=method_call /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Seek int64:-5000000", shell=True)
  except Exception:
      pass
  ```

---

## ⚙️ GNOME Shortcut Configuration (Commands)

To recreate or rebind these custom keybindings in Ubuntu GNOME desktop:

```bash
# Register custom keybindings slots
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/']"

# Slot 0: Toggle Lecture Play/Pause
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "Toggle Lecture Video"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "/home/dev/.local/bin/toggle-lecture"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "<Primary><Alt>space"

# Slot 1: Rewind Lecture 5s
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ name "Rewind Lecture 5s"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ command "/home/dev/.local/bin/rewind-lecture"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ binding "<Primary><Alt>Left"
```

---

## 💻 Environment & Workspace Setup Summary

* **Default Global Venv**: [`/home/dev/SE/Notes/.venv`](file:///home/dev/SE/Notes/.venv)
  * **Python**: 3.14+
  * **Node.js**: v24.19.0 (via `nodeenv`)
  * **NPM**: v11.17.0
* **VS Code Settings**:
  * `"files.autoSave": "afterDelay"`
  * `"python.defaultInterpreterPath": "/home/dev/SE/Notes/.venv/bin/python"`
  * `"python.terminal.activateEnvironment": true`
