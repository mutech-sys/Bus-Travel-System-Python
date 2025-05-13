import customtkinter
from tkinter import messagebox

class EmployeeLoginWindow: # Create a class
    def __init__(self):
        self.LOGIN_WIN = customtkinter.CTk() # use self.LOGIN_WIN
        self.LOGIN_WIN.title("Login Page")
        self.LOGIN_WIN.geometry('600x320')
        self.LOGIN_WIN.resizable(False, False)
        self.LOGIN_WIN.configure(fg_color="#222831")
        self.LOGIN_WIN.grid_columnconfigure(0, weight=1)
        self.BOLD_FONT = customtkinter.CTkFont(family="Arial", size=18, weight="bold")
        self.USERNAME = "admin"
        self.USERPASS = "admin"
        self.authenticationApproved = False

    def displayWidget(self): # make this a method
        employee_verification_lbl = customtkinter.CTkLabel(
            self.LOGIN_WIN,
            text="Employee Verification",
            fg_color="#00ADB5",
            corner_radius=5,
            text_color="white",
            font=self.BOLD_FONT,
            pady=20,
            padx=70)

        employee_verification_lbl.grid(row=0, column=0, padx=70, pady=(25, 40), columnspan=2)

        emplyee_username_lbl = customtkinter.CTkLabel(
            self.LOGIN_WIN,
            text="Employee username",
            font=self.BOLD_FONT,
            text_color="white")

        emplyee_username_lbl.grid(row=2, column=0, padx=0, pady=(5, 5), sticky="s")

        self.employee_username_input = customtkinter.CTkEntry( # use self
            self.LOGIN_WIN,
            width=270)

        self.employee_username_input.grid(row=2, column=1, padx=(0, 50), pady=(0, 0), sticky="ew")

        employee_password_lbl = customtkinter.CTkLabel(
            self.LOGIN_WIN,
            text="Employee password",
            font=self.BOLD_FONT,
            text_color="white")

        employee_password_lbl.grid(row=3, column=0, padx=0, pady=(5, 5), sticky="ew")

        self.employee_password_input = customtkinter.CTkEntry( # use self
            self.LOGIN_WIN,
            width=270,
            show="*"
        )

        self.employee_password_input.grid(row=3, column=1, padx=(0, 50), pady=(20, 20), sticky="ew")

        okButton = customtkinter.CTkButton(
            self.LOGIN_WIN, 
            text="OK",
            font=self.BOLD_FONT,
            cursor="hand2",
            fg_color="#00ADB5",
            hover_color="#80CCD5",
            command=self.authenticateUser
            )

        okButton.grid(row=4, column=0, padx=20, pady=(10, 10), sticky="ew")

        cancelButton = customtkinter.CTkButton(
            self.LOGIN_WIN,
            text="Cancel", 
            cursor="hand2", 
            width=250, 
            font=self.BOLD_FONT, 
           command=self.LOGIN_WIN.destroy,
            fg_color="#00ADB5",
            hover_color="#80CCD5" )

        cancelButton.grid(row=4, column=1, padx=(0, 50), pady=(10, 10), sticky="ew")

    def authenticateUser(self):
        if (self.employee_username_input.get() == self.USERNAME) and (self.employee_password_input.get() == self.USERPASS): 
            self.authenticationApproved = True
            self.LOGIN_WIN.destroy()
            
        
        else:
            messagebox.showerror("Authentication Error","Wrong username or password !!! ")
            self.employee_username_input.delete(0, "end")
            self.employee_password_input.delete(0, "end")

    def returnAuthentication(self):
        return self.authenticationApproved


