import tkinter as tk 
from tkinter import filedialog
from tkinter import ttk
from duplicate_finder import scan_for_duplicates
from send2trash import send2trash
from tkinter import messagebox
import os



def browse_folder(label_widget):
    folder_path = filedialog.askdirectory()
    if folder_path:
        label_widget.config(text =folder_path)



def run_scan_and_display(folder_path, tree_widget):
    for item in tree_widget.get_children():
        tree_widget.delete(item)  

    duplicates = scan_for_duplicates(folder_path)

    if not duplicates:
        tree_widget.insert("", "end", text="No duplicate files found.")
        return

    for idx, (hash_, files) in enumerate(duplicates.items(), 1):
        group_id = tree_widget.insert("", "end", text=f"Group {idx} (hash: {hash_[:8]}...)")

        for file_info in files:
            size_kb = round(file_info["size"]/1024,2)

            tree_widget.insert(group_id, "end", text="", values=(file_info["path"],f"{size_kb} KB"))

def delete_selected_files(tree_widget):
    selected_items = tree_widget.selection()

    if not selected_items:
        messagebox.showinfo("No selection", "Please select files to delete.")
        return

    confirm = messagebox.askyesno("Confirm Delete", "Move selected files to Trash?")
    if not confirm:
        return

    for item in selected_items:
        raw_path = tree_widget.item(item, "values")[0]
        file_path = os.path.normpath(raw_path) 
        try:
            send2trash(file_path)
            tree_widget.delete(item)
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete {file_path}:\n{e}")

 
def launch_gui():

    root = tk.Tk()
    root.geometry("800x500")
    root.title("DeClone")

    style = ttk.Style()
    style.theme_use('alt')  #clam,alt,default,classic

    label = ttk.Label(root,text="Choose a folder",font=("Arial",10))
    label.pack(padx=10,pady=10)

    #input frame 
    input_frame = ttk.Frame(root)
    input_frame.pack(pady = 20)

    browse_button = ttk.Button(input_frame,text = "Browse", command = lambda:browse_folder(select_path_label)) #specify width and padding
    browse_button.pack(side= "left")

    select_path_label = ttk.Label(input_frame,width=50,text="No Folder Selected",anchor ="w")
    select_path_label.pack(side = "bottom",padx = 10)


    # scan frame
    scan_frame = ttk.Frame(root)
    scan_frame.pack(pady = 10)

    scan_button = ttk.Button(scan_frame,text="Run Scan",command =lambda:run_scan_and_display(select_path_label.cget("text"),tree))
    scan_button.pack(side= "bottom")

    

    # Treeview for displaying results
    columns = ("Path","Size")
    tree = ttk.Treeview(root, columns=columns, show="tree")
    tree.heading("#0", text="Duplicate Groups")
    tree.heading("Path", text="File Path")
    tree.heading("Size", text="Size (KB)")
    tree.pack(padx=10, pady=10, fill="both", expand=True)


    delete_button = ttk.Button(root, text="Move Selected to Trash", command=lambda: delete_selected_files(tree))
    delete_button.pack(pady=10)

    root.mainloop() 
