from views.employee_login_win import *
from views.main_menu_win import *


login_win = EmployeeLoginWindow()
login_win.displayWidget()
login_win.LOGIN_WIN.mainloop()


if EmployeeLoginWindow.returnAuthentication(login_win) == True:
    main_win = MainWindow()
    main_win.createStartUpWidget()
    main_win.MAIN_WIN.mainloop()


