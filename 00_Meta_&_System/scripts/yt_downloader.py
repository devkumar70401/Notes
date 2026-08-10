import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox, ttk

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# DOWNLOAD_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), "music")

DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "music")

def format_size(bytes):
    if not bytes:
        return "0 MB"
    return f"{bytes / (1024*1024):.2f} MB"

def format_speed(speed):
    if not speed:
        return "0 KB/s"
    if speed > 1024*1024:
        return f"{speed / (1024*1024):.2f} MB/s"
    return f"{speed / 1024:.2f} KB/s"

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        speed = d.get('speed', 0)
        eta = d.get('eta', 0)

        if total:
            percent = (downloaded / total) * 100
            progress_bar['value'] = percent

            status_label.config(
                text=f"{percent:.1f}% | {format_size(downloaded)} / {format_size(total)}"
            )

        speed_label.config(
            text=f"Speed: {format_speed(speed)} | ETA: {eta}s"
        )

        root.update_idletasks()

    elif d['status'] == 'finished':
        progress_bar['value'] = 100
        status_label.config(text="Converting to MP3...")

def download():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please paste a URL")
        return

    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_PATH}/%(title)s.%(ext)s',
        'noplaylist': True,
        'progress_hooks': [progress_hook],
    }

    try:
        status_label.config(text="Starting download...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed!")
        status_label.config(text="Done!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Error occurred")

# GUI
root = tk.Tk()
root.title("YouTube → MP3 Downloader")
root.geometry("420x220")

tk.Label(root, text="Paste YouTube URL:").pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Download", command=download).pack(pady=10)

progress_bar = ttk.Progressbar(root, length=350, mode='determinate')
progress_bar.pack(pady=5)

status_label = tk.Label(root, text="Idle")
status_label.pack()

speed_label = tk.Label(root, text="")
speed_label.pack()

root.mainloop()