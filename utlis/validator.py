import customtkinter
import tkinter as tk

def ONSeatBookingButton(self):
        headingLabel = customtkinter.CTkLabel(
            master=self.workingFrame,
            text="Seat Booking",
            width=520,  # Move width to constructor
            height=40,  # Move height to constructor
            corner_radius=10,
            fg_color="#00ADB5",  # Frame background color
            font=("Britannic Bold", 23, "bold"),  # Replace text_font with font
            text_color="#EEEEEE",  # Text color
        )
        nameLabel = customtkinter.CTkLabel(
            master=self.workingFrame,
            text="NAME:",
            text_color="#EEEEEE",
            font=("Calibri", 20, "underline", "bold"),
        )

        global nameEntryBox
        nameEntryBox = customtkinter.CTkEntry(
            master=self.workingFrame,
            width=400
        )
        
        cnicLabel = customtkinter.CTkLabel(
            master=self.workingFrame,
            text="CNIC:",
            text_color="#EEEEEE",
            font=("Calibri", 20, "underline", "bold"),
        )
        
        global cnicEntryBox
        cnicEntryBox = customtkinter.CTkEntry(
            master=self.workingFrame,
            width=300
        )

        phoneLabel = customtkinter.CTkLabel(
            master=self.workingFrame,
            text="Phone #",
            text_color="#EEEEEE",
            font=("Calibri", 20, "underline", "bold"),
        )
        global phoneEntryBox
        phoneEntryBox = customtkinter.CTkEntry(
            master=self.workingFrame,
            width=300
        )

        routeLabel = customtkinter.CTkLabel(
            master=self.workingFrame,
            text="Route:",
            text_color="#EEEEEE",
            font=("Calibri", 20, "underline", "bold"),
        )

        global routeOptionMenu
        routeOptionMenu = customtkinter.CTkOptionMenu(
            master=self.workingFrame,
            width= 250,
            fg_color="#219B9D",
            button_color="#397F83",
            button_hover_color="#80CCD5",
            text_color="#EEEEEE",
            dropdown_fg_color="#222831",
            dropdown_font=("Calibri", 16, "normal"),
            font= ("Calibri", 14, "normal"),
            values=["Route Selection","Narowal to Islamabad", "Narowal to Lahore", "Narowal to Sargodha", "Narowal to Mirpur"]
        )

        nextButton = customtkinter.CTkButton(
            master=self.workingFrame,
            width= 90,
            height=40,
            text="↪",
            fg_color="#00ADB5",
            hover_color="#80CCD5",
            text_color="#EEEEEE",
            font=("Calibri", 30, "bold"),
            command=self.OnUserInfoValidationButton
        )
        seatsLabel = customtkinter.CTkLabel(
            master=self.workingFrame,
            text="Number of Seats:",
            text_color="#EEEEEE",
            font=("Calibri", 20, "underline", "bold"),
        )

        global seatsEntryBox
        seatsEntryBox = customtkinter.CTkEntry(
            master=self.workingFrame,
            width=40
        )

        headingLabel.place(x=20, y=20)
        nameLabel.place(x=40, y=100)
        nameEntryBox.place(x=120, y=100)

        cnicLabel.place(x=40, y=140)
        cnicEntryBox.place(x=120, y=140)

        phoneLabel.place(x=40, y=180)
        phoneEntryBox.place(x=120, y=180)

        routeLabel.place(x=40, y=220)
        routeOptionMenu.place(x=122, y=222)

        seatsLabel.place(x=40, y=260)
        seatsEntryBox.place(x=200,y=260)

        nextButton.place(x=450, y=390)


def OnUserInfoValidationButton(self):
    busList = ['Bus Options']
    if not self.ValidateData():
        print("Validate Info!!!!")
        return
    self.ClearWorkingFrame()
    filteredSearch = DB_MANAGER.GetBusesForRoute(routeOptionMenu.get(), seatsEntryBox.get())
    for bus in filteredSearch:
        busList.append(str(bus[0]))

    print(busList)

    self.DisplayTreeView(filteredSearch)
    busMenuLabel = customtkinter.CTkLabel(
        master=workingFrame,
        text="Route:",
        text_color="#EEEEEE",
        font=("Calibri", 20, "underline", "bold"),
    )
    busOptionMenu = customtkinter.CTkOptionMenu(
        master=workingFrame,
        width= 100,
        fg_color="#219B9D",
        button_color="#397F83",
        button_hover_color="#80CCD5",
        text_color="#EEEEEE",
        dropdown_fg_color="#222831",
        dropdown_font=("Calibri", 16, "normal"),
        font= ("Calibri", 14, "normal"),
        values=busList
    )
    busOptionMenu.place(x=275, y=327)
    busMenuLabel.place(x=205, y=325)

    previousButton = customtkinter.CTkButton(
        master=workingFrame,
        width= 90,
        height=40,
        text="↩",
        fg_color="#00ADB5",
        hover_color="#80CCD5",
        text_color="#EEEEEE",
        font=("Calibri", 30, "bold"),
        #command=OnPreviousButton
    )
    previousButton.place(x=20, y=390)

    confirmationButton = customtkinter.CTkButton(
        master=workingFrame,
        width= 85,
        height=42,
        text="Confirm",
        fg_color="#00ADB5",
        hover_color="#80CCD5",
        text_color="#EEEEEE",
        font=("Calibri", 18, "normal"),
        #command=OnConfirmButton
    )
    confirmationButton.place(x=450, y=390)
    return

def ClearFrameTwo(self):
    self.nameLabel.place_forget()
    self.nameEntryBox.place_forget()
    self.cnicLabel.place_forget()
    self.cnicEntryBox.place_forget()
    self.phoneLabel.place_forget()
    self.phoneEntryBox.place_forget()
    self.routeLabel.place_forget()
    self.routeOptionMenu.place_forget()
    self.seatsEntryBox.place_forget()
    self.seatsLabel.place_forget()
    self.nextButton.place_forget()
    self.ticketInfoLabel.place_forget()
    self.invalidButton.place_forget()
    self.cancelLabel.place_forget()
    self.cancelEntryBox.place_forget()
    self.verifyCancelButton.place_forget()
    self.headingCancelLabel.place_forget()
    self.headingRefundLabel.place_forget() 
    self.refundLabel.place_forget()
    self.refundDateLabel.place_forget()
    self.refundEntryBox.place_forget()
    self.verifyRefundButton.place_forget()

def DisplayTreeView(self, filteredSearch):
    # Create a Style object
    style = ttk.Style()
    style.theme_use("clam")  # Use "clam" theme for better customization

    # Customize Treeview header
    style.configure(
        "Treeview.Heading",
        font=("Helvetica", 12, "bold"),
        background="lightblue",
        foreground="black",
        borderwidth=1,
    )

    # Customize Treeview rows
    style.configure(
        "Treeview",
        font=("Helvetica", 12),
        background="white",
        foreground="black",
        rowheight=25,
        fieldbackground="#393E46",
    )

    # Selected row styling
    style.map(
        "Treeview",
        background=[("selected", "#219B9D")],
        foreground=[("selected", "black")],
    )

    self.table.place(x=15, y=100, width=675)
    for col in self.columns:
        self.table.heading(col, text=col)
        self.table.column(col, width=100, anchor="center")

    for i, row in enumerate(filteredSearch):
        bg_color = "lightblue" if i % 2 == 0 else "white"
        self.table.insert("", "end", values=row, tags=("striped",))
        self.table.tag_configure("striped", background=bg_color)


def ValidateData(self):
    name = self.nameEntryBox.get()
    cnic = self.cnicEntryBox.get()
    phone = self.phoneEntryBox.get()
    seats = self.seatsEntryBox.get()
    route = self.routeOptionMenu.get()

    if self.validate_name(name) and self.validate_cnic(cnic) and self.validate_phone(phone) and self.validate_seats(seats) and route != "Route Selection":
        return True
    else:
        return False

def validate_name(name):
    if name.isalpha():
        return True
    messagebox.showerror("Validation Error", "Name must contain alphabets.")
    return False

def validate_cnic(cnic):
    if cnic.isdigit() and len(cnic) == 13:
        return True
    messagebox.showerror("Validation Error", "CNIC must be numeric and up to 13 digits.")
    return False

def validate_phone(phone):
    if phone.isdigit() and len(phone) == 11:
        return True
    messagebox.showerror("Validation Error", "Phone number must be numeric and up to 11 digits.")
    return False

def validate_seats(seats):
    if seats.isdigit() and 0 < int(seats) <= 50:
        return True
    messagebox.showerror("Validation Error", "Number of seats must be a numeric value between 1 and 50.")
    return False