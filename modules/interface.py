from modules.getFiles import getFiles
import customtkinter
import os
import modules.constants as constants


class Application:
    def __init__(self, master=None):
        self.frame = customtkinter.CTkFrame(master)
        self.frame.pack(pady=10, padx=60, fill="both", expand=True)
        self.appearance = customtkinter.set_appearance_mode("dark")
        self.colortheme = customtkinter.set_default_color_theme("dark-blue")
        self.main_label = customtkinter.CTkLabel(
            master=self.frame,
            text="",
            width=280,
            height=80,
            font=("Poppins", 12),
            fg_color="#1e2227",
            corner_radius=5,
            justify="center",
        )
        self.main_label.pack(pady=50)
        self.button_download = customtkinter.CTkButton(
            master=self.frame,
            text=constants.DOWNLOAD_FILES,
            command=self.donwload_files,
            fg_color="#2BB339",
            hover_color="#1A7623",
            width=280,
        ).pack(pady=10)
        self.button_extract = customtkinter.CTkButton(
            master=self.frame,
            text=constants.CREATE_FILE,
            command=self.extract_files,
            fg_color="#2BB339",
            hover_color="#1A7623",
            width=280,
        ).pack(pady=10)
        self.button_close = customtkinter.CTkButton(
            master=self.frame,
            text=constants.CLOSE,
            command=self.close,
            fg_color="#D51F1F",
            hover_color="#991717",
            width=280,
        ).pack(pady=10)

    def donwload_files(self):
        """Donwload the pdf files"""
        self.main_label.configure(text=constants.DOWNLOADING_FILES)
        donwload_files = getFiles(constants.WEBSITE_URL)
        if donwload_files:
            self.main_label.configure(text=constants.DOWNLOAD_SUCCESS)

    def extract_files(self):
        """Extract data from pdf files"""
        files = os.listdir("tmp")
        if len(files) == 0:
            self.main_label.configure(
                text=constants.FILES_NOT_FOUND
            )
    def close(self):
        """Close the app"""
        exit()


root = customtkinter.CTk()
root.geometry("500x350")
Application(root)
root.mainloop()
