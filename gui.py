import tkinter as tk 
from tkinter import filedialog
from tkinter import ttk


def browse_folder(selected_path):
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_path.config(text =folder_path)

    

 
def launch_gui():

    root = tk.Tk()
    root.geometry("800x500")
    root.title("DeClone")

    style = ttk.Style()
    style.theme_use('alt')  #clam,alt,default,classic

    label = ttk.Label(root,text="Choose a folder",font=("Arial",20))
    label.pack(padx=10,pady=10)
     
    input_frame = ttk.Frame(root)
    input_frame.pack(pady = 20)

    
    browse_button = ttk.Button(input_frame,text = "Browse", command = lambda:browse_folder(select_path)) #specify width and padding
    browse_button.pack(side= "left")

    select_path = ttk.Label(input_frame,width=50,text="No Folder Selected",anchor ="w")
    select_path.pack(side = "bottom",padx = 10)
    
    


    scan_frame = ttk.Frame(root)
    scan_frame.pack(pady = 10)

    scan_button = ttk.Button(scan_frame,text="Run Scan")
    scan_button.pack(side= "bottom")



    root.mainloop() 
