import tkinter as tk
# Importamos la librería Tkinter con el alias "tk"
# Tkinter es la librería estándar de Python para hacer interfaces gráficas.


def main():
    window = tk.Tk()
    # Creamos la ventana principal de la aplicación.
    # Tk() es la raíz de toda app de escritorio con Tkinter.

    window.title("Text Editor")
    # Le damos un título a la ventana (aparece arriba).

    # Configuramos el tamaño mínimo de las filas y columnas del grid.
    window.rowconfigure(0, minsize=400)
    # Esto dice: la fila 0 debe tener mínimo 400px de alto.

    window.columnconfigure(1, minsize=500)
    # Esto dice: la columna 1 debe tener mínimo 500px de ancho.
    # (La columna 0 será para el panel de botones)

    # Creamos un marco (Frame) al costado izquierdo de la ventana.
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    # relief=tk.RAISED → le da un borde "elevado"
    # bd=2 → ancho del borde

    frame.grid(row=0, column=0, sticky="ns")
    # Colocamos el marco en la cuadrícula:
    # row=0, column=0 → esquina superior izquierda
    # sticky="ns" → estira el frame verticalmente ("north-south")

    # Área de texto donde el usuario puede escribir.
    text_edit = tk.Text(window, font="Helvetica 18 bold")
    # tk.Text es un widget para texto multilinea.
    # Le damos una fuente más grande para que sea más cómodo.

    text_edit.grid(row=0, column=1, sticky="nsew")
    # Lo colocamos en la columna 1, ocupando la parte derecha.
    # sticky="nsew" → se estira en todas las direcciones.
    # (Esto hace que el área de texto crezca con la ventana)

    # Botón para guardar el archivo (todavía sin funcionalidad real)
    save_button = tk.Button(frame, text="Save")

    # Botón para abrir un archivo existente
    open_button = tk.Button(frame, text="Open")

    # Colocamos los botones dentro del frame (panel izquierdo)
    save_button.grid(row=0, column=0, padx=5, pady=5)
    # padx/pady → margen alrededor del botón

    open_button.grid(row=1, column=0, padx=5, pady=5)
    # Cada botón va en una fila distinta

    # Inicio del loop principal de la ventana.
    window.mainloop()
    # Aquí Tkinter queda "escuchando":
    # clics, teclas, eventos, redimensionado, etc.


main()
# Ejecutamos la función principal que crea y abre la interfaz
