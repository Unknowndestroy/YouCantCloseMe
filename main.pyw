import tkinter as tk
from tkinter import ttk
import locale

def get_system_language():
    lang = locale.getdefaultlocale()[0]
    if lang and lang.startswith("tr"):
        return "TR"
    else:
        return "EN"


sys_lang = get_system_language()
if sys_lang == "TR":
    title_text = "Kapatılamaz Pencere"
    tab_main_name = "Ana"
    tab_tutorial_name = "Öğretici"
else:
    title_text = "Non-closable GUI"
    tab_main_name = "Main"
    tab_tutorial_name = "Tutorial"

root = tk.Tk()
root.title(title_text)
root.geometry("600x400")

root.protocol("WM_DELETE_WINDOW", lambda: None)


notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")


frame_main = tk.Frame(notebook)
notebook.add(frame_main, text=tab_main_name)

frame_tutorial = tk.Frame(notebook)
notebook.add(frame_tutorial, text=tab_tutorial_name)




lang_var = tk.StringVar(value=get_system_language())

def update_message():
    lang = lang_var.get()
    if lang == "EN":
        message = "You Cant Close Me! 🫵🤣"
    elif lang == "TR":
        message = "Beni Kapatamazsın! 🫵🤣"
    else: 
        sys_lang = get_system_language()
        if sys_lang == "TR":
            message = "Beni Kapatamazsın! 🫵🤣"
        else:
            message = "You Cant Close Me! 🫵🤣"
    label_message.config(text=message)


frame_lang = tk.Frame(frame_main)
frame_lang.pack(pady=10)
for text, val in [("EN", "EN"), ("TR", "TR"), ("SYSTEM", "SYSTEM")]:
    rb = tk.Radiobutton(frame_lang, text=text, variable=lang_var, value=val, command=update_message)
    rb.pack(side="left", padx=5)


label_message = tk.Label(frame_main, text="", font=("Helvetica", 24))
label_message.pack(expand=True)
update_message()


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
color_index = 0

def update_bg():
    global color_index
    current_color = colors[color_index]
    frame_main.config(bg=current_color)
    label_message.config(bg=current_color)
    frame_lang.config(bg=current_color)
    color_index = (color_index + 1) % len(colors)
    root.after(100, update_bg)  

update_bg()



tutorial_lang_var = tk.StringVar(value=get_system_language())

def update_tutorial():
    lang = tutorial_lang_var.get()
    if lang == "EN":
        text = (
            "Tutorial: Non-closable GUI Code (EN)\n\n"
            "1. The window's close event is overridden using:\n"
            '   root.protocol("WM_DELETE_WINDOW", lambda: None)\n'
            "   which disables the X button.\n\n"
            "2. A rainbow effect is created by updating the background color\n"
            "   periodically using the after() method.\n\n"
            "3. Two tabs are implemented using the Notebook widget."
        )
    elif lang == "TR":
        text = (
            "Tutorial: Kapatılamayan GUI Kodu (TR)\n\n"
            "1. Pencerenin kapatma olayı, şu şekilde geçersiz kılınır:\n"
            '   root.protocol("WM_DELETE_WINDOW", lambda: None)\n'
            "   bu da X butonunu etkisiz hale getirir.\n\n"
            "2. Arka plan rengi, after() metodu ile düzenli aralıklarla değiştirilerek\n"
            "   gökkuşağı efekti oluşturulur.\n\n"
            "3. Notebook widget ile iki sekme oluşturulur."
        )
    else:  
        sys_lang = get_system_language()
        if sys_lang == "TR":
            text = (
                "Tutorial: Kapatılamayan GUI Kodu (Sistem)\n\n"
                "1. Pencerenin kapatma olayı, şu şekilde geçersiz kılınır:\n"
                '   root.protocol("WM_DELETE_WINDOW", lambda: None)\n'
                "   bu da X butonunu etkisiz hale getirir.\n\n"
                "2. Arka plan rengi, after() metodu ile düzenli aralıklarla değiştirilerek\n"
                "   gökkuşağı efekti oluşturulur.\n\n"
                "3. Notebook widget ile iki sekme oluşturulur."
            )
        else:
            text = (
                "Tutorial: Non-closable GUI Code (System)\n\n"
                "1. The window's close event is overridden using:\n"
                '   root.protocol("WM_DELETE_WINDOW", lambda: None)\n'
                "   which disables the X button.\n\n"
                "2. A rainbow effect is created by updating the background color\n"
                "   periodically using the after() method.\n\n"
                "3. Two tabs are implemented using the Notebook widget."
            )
    tutorial_text.delete("1.0", tk.END)
    tutorial_text.insert(tk.END, text)


frame_tutorial_lang = tk.Frame(frame_tutorial)
frame_tutorial_lang.pack(pady=10)
for text, val in [("EN", "EN"), ("TR", "TR"), ("SYSTEM", "SYSTEM")]:
    rb = tk.Radiobutton(frame_tutorial_lang, text=text, variable=tutorial_lang_var, value=val, command=update_tutorial)
    rb.pack(side="left", padx=5)

tutorial_text = tk.Text(frame_tutorial, wrap="word")
tutorial_text.pack(expand=True, fill="both")
update_tutorial()

root.mainloop()
