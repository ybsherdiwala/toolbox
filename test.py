import json
import tkinter as tk
import os
import sys
import requests



base_url = f"https://api.github.com/repos/{cloud_owner}/{cloud_repo}/contents/main/"
headers = {
    "Authorization": f"Bearer {cloud_token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

if hasattr(sys, 'frozen'):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAMES_DIR = os.path.join(BASE_DIR, "games")
MYDATA_DIR = os.path.join(BASE_DIR, "mydata.json")

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(GAMES_DIR, exist_ok=True)
os.makedirs(os.path.dirname(MYDATA_DIR), exist_ok=True)

data = None
with open(MYDATA_DIR, "r", encoding="utf-8") as file:
    data = json.load(file)

window = tk.Tk()
window.title("Toolbox")
window.geometry("600x350")

visible_games = None
listbox = tk.Listbox(window, width=65, height=12, font=("Arial", 12))

i = 0
if data.get("os"):
    for software in data["os"]:
        if software.get("visible"):
            listbox.insert(tk.END, software["display_name"])
            listbox.itemconfig(i, fg="red")
            i += 1
if data.get("games"):
    for game in data["games"]:
        if game.get("visible"):
            listbox.insert(tk.END, game["display_name"])
            listbox.itemconfig(i, fg="blue")
            i += 1

button = tk.Button(window, text="Check For Updates", command=lambda: update_)
button.place(x=0, y=50)

label = tk.Label(window, text="Welcome!", font=("Arial", 25))
label.place(x=0, y=0)


label2 = tk.Label(window, text="Cloud Access Token Hidden Securely!")
label2.place(x=0, y=80)

label3 = tk.Label(window, text=data["os"][0]["version"])
label3.place(x=500, y=0)

listbox.place(x=0, y=100)

window.mainloop()