import customtkinter
#import DB_MANAGER
from tkinter import messagebox
from datetime import datetime
import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self):
        self.MAIN_WIN = customtkinter.CTk()      # Creating a Main Menu Window
        self.MAIN_WIN.geometry("800x550")        # Set Dimensions
        self.MAIN_WIN.title("Bus Seat Booking and Ticket Management")        # Set Title
        self.MAIN_WIN.resizable(False, False)        # Disable Resizing
        self.MAIN_WIN.configure(fg_color="#222831")      # Set background color of the main window
        #MAIN_WIN.iconbitmap("Icons/bus_icon.ico")
        customtkinter.set_appearance_mode("System")      # Setting the default theme of the Window
        customtkinter.set_default_color_theme("blue") 

    def createStartUpWidget(self):
        topLabelHeading = customtkinter.CTkLabel(
        master=self.MAIN_WIN,
        text="Bus Seat Booking and Ticket Management",
        width=780,  # Move width to constructor
        height=40,  # Move height to constructor
        fg_color="#00ADB5",  # Frame background color
        corner_radius=10,
        font=("Britannic Bold", 23, "bold"),  # Replace text_font with font
        text_color="#EEEEEE"  # Text color
    )
        global sideBarFrame
    # Create a frame for the buttons (Frame 1)
        sideBarFrame = customtkinter.CTkFrame(
            master=self.MAIN_WIN,
            width=200,
            height=460,  # Adjusted height for new window geometry
            corner_radius=10,
            fg_color="#393E46"  # Frame background color
        )
        # Create buttons in Frame 1
        bookButton = customtkinter.CTkButton(
            master=sideBarFrame,
            text="Book Seat",
            width=160,  # Move width to constructor
            height=40,  # Move height to constructor
            command=self.ONSeatBookingButton,
            fg_color="#00ADB5",  # Button color
            hover_color="#80CCD5",  # Slightly lighter hover color
            text_color="#EEEEEE",  # Text color
            font=("Calibri", 18, "normal")
        )

        cancelButton = customtkinter.CTkButton(
            master=sideBarFrame,
            text="Cancel Ticket",
            width=160,
            height=40,
            fg_color="#00ADB5",  # Button color
            hover_color="#80CCD5",
            text_color="#EEEEEE",
            font=("Calibri", 18, "normal"),
            #command=OnCancelTicketButton
        )

        refundedTicketsButton = customtkinter.CTkButton(
            master=sideBarFrame,
            text="Refunded Tickets",
            width=160,
            height=40,
            fg_color="#00ADB5",  # Button color
            hover_color="#80CCD5",
            text_color="#EEEEEE",
            font=("Calibri", 18, "normal"),
            #command=OnRefundTicketButton
        )

        logoutButton = customtkinter.CTkButton(
            master=sideBarFrame,
            text="Log Out",
            width=160,
            height=40,
            fg_color="#00ADB5",
            hover_color="#80CCD5",
            text_color="#EEEEEE",
            font=("Calibri", 18, "normal"),
            #command=OnLogOutButton
        )
        global workingFrame
        # Create a frame for functionality display (Frame 2)
        workingFrame = customtkinter.CTkFrame(
            master=self.MAIN_WIN,
            width=560,
            height=460,  # Adjusted height for new window geometry
            corner_radius=10,
            fg_color="#393E46"
        )

        topLabelHeading.place(x=10, y=10)
        sideBarFrame.place(x=10, y=60)
        bookButton.place(x=20, y=20)
        cancelButton.place(x=20, y=80)
        refundedTicketsButton.place(x=20, y=140)
        logoutButton.place(x=20, y=400)
        workingFrame.place(x=230, y=60)

    

   