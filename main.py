import json
import customtkinter as ctk
from CTkListbox import CTkListbox
import os
import sys
from enum import auto
import subprocess

class UpdateState():
    IDLE = auto()

class AppDescription(ctk.CTkToplevel):
    def __init__(self, root, params):
        super().__init__(root)
        self.title("Details")
        self.params = params

        self.info_label = ctk.CTkLabel(
            self,
            text = self.params["appname"]
        )
        self.info_label.pack(pady = 5)
        self.desc_box = ctk.CTkLabel(
            self,
            text = self.params["desc"],
            wraplength = 280
        )
        self.desc_box.configure(state="disabled")
        self.desc_box.pack()
        self.run_file_button = ctk.CTkButton(
            self,
            text = "Run File",
            command = self.run_file
        )
        self.run_file_button.pack(pady = 5)

        self.geometry("300x300")

    def run_file(self):
        print(self.params["path"])
        subprocess.Popen([self.params["path"]])
        self.destroy()

class ToolBoxClient(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ToolBox")

        self.info_label = ctk.CTkLabel(
            self,
            font = ("Arial", 20)
        )
        self.info_label.pack(padx=5, anchor=ctk.NW)
        self.update_btn = ctk.CTkButton(self)
        self.update_btn.pack(pady=5)
        self.update_state_tran(UpdateState.IDLE)
        
        self.load_data()

        self.uninstall_btn = ctk.CTkButton(
                    self,
                    text = "Uninstall App",
                    fg_color = "red",
                    hover_color = "orange",
                    command = self.uninstall
                )
        
        self.app_box = CTkListbox(
            self,
            width = 370,
            height = 250,
            text_color = "blue",
            hover_color = "green",
            highlight_color = "yellow",
            command = self.open_desc
        )
        self.app_box.pack(padx=5, pady=5)
        self.uninstall_btn.pack()
        self.init_app_box()

        self.geometry("400x380")

    def init_app_box(self):
        if self.data.get("os"):
            for software in self.data["os"]:
                if software.get("visible"):
                    self.app_box.insert(ctk.END, software["display_name"])
        if self.data.get("apps"):
            for game in self.data["apps"]:
                if game.get("visible"):
                    self.app_box.insert(ctk.END, game["display_name"])

    def load_data(self):
        if hasattr(sys, 'frozen'):
            self.BASE_DIR = os.path.dirname(sys.executable)
        else:
            self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.MYDATA_DIR = os.path.join(self.BASE_DIR, "os_d//mydata.json")

        self.BASE_DIR = os.path.normpath(self.BASE_DIR)
        self.MYDATA_DIR = os.path.normpath(self.MYDATA_DIR)

        with open(self.MYDATA_DIR, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

        self.env_file = self.data["os"][1]

    def update_state_tran(self, state: UpdateState):
        match state:
            case UpdateState.IDLE:
                self.info_label.configure(text="Welcome!")
                self.update_btn.configure(text="Check For Updates", command=self.check_for_updates)

    def check_for_updates(self):
        self.info_label.configure(text="Sorry! Updates Not Supported.")

    def open_desc(self, current):
        finding = True
        for app in self.data["apps"]:
            if app["display_name"] == current:
                params = {
                    "appname": app["display_name"],
                    "path": os.path.normpath(os.path.join(self.BASE_DIR, "apps", app["file"])),
                    "desc": app["desc"]
                    }
                self.latest_desc = AppDescription(self, params)
                finding = False
        if finding:
            for soft in self.data["os"]:
                        if soft["display_name"] == current:
                            params = {
                                        "appname": soft["display_name"],
                                        "path": os.path.join(self.BASE_DIR, "os_d", soft["file"]),
                                        "desc": soft["desc"]
                                }
                            self.latest_desc = AppDescription(self, params)
                            finding = False

    def uninstall(self):
        for path, name, file in os.walk():
            if file[:5] == "unins":
                subprocess.Popen([path])
                self.destroy()

if __name__ == "__main__":
    app = ToolBoxClient()
    app.mainloop()
    