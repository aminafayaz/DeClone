import tkinter as tk 

def launch_gui():
    root = tk.Tk()

    root.geometry("800x500")
    root.title("DeClone")

    label = tk.Label(root,text="Choose a folder",font=("Arial",20))
    label.pack(padx=10,pady=10)
    root.mainloop() #calls the main loop of tkinterr