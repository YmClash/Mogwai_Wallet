import customtkinter
import sys


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("MogLogin")

def run():
    print("run")

def exit():
    print("exit")
    sys.exit()

frame = cous




# run_batton= customtkinter.CTkButton(app,text="RUN",command =run())
# run_batton.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
#
# exit_button = customtkinter.CTkButton(app,text="EXIT",command = exit())
#
#
#
# run_batton.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)



app.mainloop()

