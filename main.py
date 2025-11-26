import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):  # ⬅️ AHORA RECIBE window Y text_edit
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")


def main():
    window = tk.Tk()
    # Creamos la ventana principal de la aplicación.
    window.title("Text Editor")
    # Le damos un título a la ventana (aparece arriba).
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    # Área de texto donde el usuario puede escribir.
    text_edit = tk.Text(window, font="Helvetica 18 bold")
    text_edit.grid(row=0, column=1, sticky="nsew")

    # Creamos un marco (Frame) al costado izquierdo de la ventana.
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    # Botón para guardar el archivo
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    # Botón para abrir un archivo existente
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()
main()
