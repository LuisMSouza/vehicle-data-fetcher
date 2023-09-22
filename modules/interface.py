from modules.getFiles import getFiles
from modules.readFiles import readFiles
from modules.createFile import createDoc, createDocNotaries
from modules.readNotaries import findNotaries

import customtkinter
import os
import modules.constants as constants


class Application:
    def __init__(self, master=None):
        self.frame = customtkinter.CTkFrame(master)
        self.vehicles_data = {}
        self.notaries_data = {}
        self.frame.pack(pady=5, padx=60, fill="both", expand=True)
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
        self.main_label.pack(pady=10)

        self.button_download = customtkinter.CTkButton(
            master=self.frame,
            text=constants.DOWNLOAD_FILES,
            command=self.donwload_files,
            fg_color="#2BB339",
            hover_color="#1A7623",
            width=280,
        )
        self.button_download.pack(pady=10)

        self.button_extract_vehicle = customtkinter.CTkButton(
            master=self.frame,
            text=constants.EXTRACT_FILE_VEHICLE,
            command=self.extract_vehicle,
            fg_color="#2BB339",
            hover_color="#1A7623",
            width=280,
        )
        self.button_extract_vehicle.pack(pady=10)

        self.button_extract_notaries = customtkinter.CTkButton(
            master=self.frame,
            text=constants.EXTRACT_FILE_REGISTRY,
            command=self.extract_notaries,
            fg_color="#2BB339",
            hover_color="#1A7623",
            width=280,
        )
        self.button_extract_notaries.pack(pady=10)

        self.button_create_pdf_vehicles = customtkinter.CTkButton(
            master=self.frame,
            text=constants.CREATE_FILE_VEHICLE,
            command=self.create_pdf_vehicles,
            fg_color="#2BB339",
            hover_color="#1A7623",
            width=280,
        )
        self.button_create_pdf_vehicles.pack(pady=10)

        self.button_create_pdf_notaries = customtkinter.CTkButton(
            master=self.frame,
            text=constants.CREATE_FILE_REGISTRY,
            command=self.create_pdf_notaries,
            fg_color="#2BB339",
            hover_color="#1A7623",
            width=280,
        )
        self.button_create_pdf_notaries.pack(pady=10)

    def extract_notaries(self):
        """Extrair dados de cartórios"""
        self.main_label.configure(text=constants.EXTRACT_NOTARIES_DATA)

        if not os.path.exists("tmp"):
            self.main_label.configure(text=constants.FILES_NOT_FOUND)
            return

        files = os.listdir("tmp")

        if len(files) == 0:
            self.main_label.configure(text=constants.FILES_NOT_FOUND)

        self.notaries_data = findNotaries()
        self.main_label.configure(text=constants.EXTRACT_NOTARIES_SUCCESS)

    def create_pdf_vehicles(self):
        """Criar PDF de dados de veículos"""
        self.main_label.configure(text=constants.CREATING_VEHICLE_PDF)
        if len(self.vehicles_data) == 0:
            self.main_label.configure(text=constants.NO_VEHICLES_DATA)
            return

        createDoc(self.vehicles_data)
        self.main_label.configure(text=constants.PDF_VEHICLE_SUCCESS)

    def create_pdf_notaries(self):
        """Criar PDF de dados de cartórios"""
        self.main_label.configure(text=constants.CREATING_REGISTRY_PDF)
        if len(self.notaries_data) == 0:
            self.main_label.configure(text=constants.NO_NOTARIES_DATA)
            return

        createDocNotaries(self.notaries_data)
        self.main_label.configure(text=constants.PDF_REGISTRY_SUCCESS)

    def donwload_files(self):
        """Donwload the pdf files"""
        self.main_label.configure(text=constants.DOWNLOADING_FILES)
        donwload_files = getFiles(constants.WEBSITE_URL)
        if donwload_files:
            self.main_label.configure(text=constants.DOWNLOAD_SUCCESS)

    def extract_vehicle(self):
        """Extract vehicles data from pdf files"""
        self.main_label.configure(text=constants.EXTRACT_VEHICLE_DATA)

        if not os.path.exists("tmp"):
            self.main_label.configure(text=constants.FILES_NOT_FOUND)
            return

        files = os.listdir("tmp")

        if len(files) == 0:
            self.main_label.configure(text=constants.FILES_NOT_FOUND)

        self.vehicles_data = readFiles()
        self.main_label.configure(text=constants.EXTRACT_VEHICLES_SUCCESS)


root = customtkinter.CTk()
root.title(constants.APP_TITLE)
root.iconbitmap(constants.APP_ICON_PATH)
root.geometry(constants.APP_DIMENSION)
Application(root)
root.mainloop()
