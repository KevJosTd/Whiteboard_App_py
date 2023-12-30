import tkinter as tk
from tkinter.colorchooser import askcolor

# Define una función llamada named start_drawing que recibe como parametro un evento (event)
# In GUI programming, events are actions that trigger specific functions when they happen
def start_drawing(event):
    #global variables
    #lobal variables are accessible from anywhere in the code and can be modified within functions
    global is_drawing, prev_x, prev_y

    #This variable is typically used to indicate whether a drawing action is in progress. 
    # By setting it to True, the function signals that a drawing action has started.
    is_drawing = True

    #This line captures the current coordinates of the mouse cursor when the start_drawing function is called.
    # It assigns the x and y coordinates of the mouse cursor at that moment to the prev_x and prev_y variables.
    # These variables are used to track the starting point of the drawing action.
    prev_x = event.x
    prev_y = event.y

def draw (event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x = event.x
        current_y = event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill = drawing_color, width = line_width, capstyle = tk.ROUND, smooth = True)
        prev_x = current_x
        prev_y = current_y

def stop_drawing(event):
    global is_drawing
    is_drawing = False

def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color

def change_background_color(canvas):
    color = askcolor()[1]
    if color:
        canvas.config(bg = color)

def change_line_width(value):
    global line_width
    line_width = int(value)


######## Crear Ventana 
# Crea la ventana principal de la aplicación
root = tk.Tk()
# Establece el titulo de la ventada de la aplicación
root.title("Whiteboard App")
# Crea un lienzo de dibujo dentro de la ventana principal. El lienzo es un área rectangular y se inicia con el color blanco
canvas = tk.Canvas(root, bg= "black")
#Configura el lienzo para llenar el espacio horizontal y vertical y permite que el lienzo se expanda y ocupe toda la ventana
canvas.pack(fill = "both", expand = True)
#El usuario está dibujando o no
is_drawing = False
#Especifica el color que vas a usar para dibujar en el lienzo
drawing_color = "white"
#Especifica el ancho de las líneas para dibujar
line_width = 2
#Establece el tamaño inicial de la aplicación en pixeles (ancho x alto)
root.geometry("800x600")

####### Construir barra de navegación y controles
# Crear un frame para contener los botones en la misma línea
controls_frame = tk.Frame(root)
#Contiene los controles en la parte superior llenando el espacio horizontal
controls_frame.pack(side = "top", fill = "x")

#Crear dos botones y asignarles posiciones fijas en la pantalla
bg_color_button = tk.Button(controls_frame, text = "Change Background Color", command = lambda: change_background_color(canvas))
color_button = tk.Button(controls_frame, text = "Change Line Color", command = change_pen_color)
clear_button = tk.Button(controls_frame, text = "Clear", command = lambda: canvas.delete("all"))

#Asignamos la posición y el tamaño de los botones
bg_color_button.pack(side = "left", padx= 5, pady = 5)
color_button.pack(side = "left", padx = 5, pady = 5)
clear_button.pack(side = "left", padx= 5, pady = 5)

####### Crear un control deslizante para la función ancho de línea
#Crea un label con la etiqueta Line Width
line_width_label = tk.Label(controls_frame, text = "Line Width")
#Asigna la posición y el tamaño del label
line_width_label.pack(side = "left", padx = 5, pady = 5)
#Crea un control deslizante horizontal que permite elegir el ancho de línea. Valor mínimo de 1 y maximo de 10
line_width_slider = tk.Scale(controls_frame, from_ = 1, to = 10, orient = "horizontal", command = lambda val: change_line_width(val))
#Establece la posición inicial del control deslizante
line_width_slider.set(line_width)
#Asigna la posición y el tamaño del control deslizante
line_width_slider.pack(side = "left", padx = 5, pady = 5)

####### Conectar las funciones con el GUI
#Cuando el botón izquierdo del mouse es oprimido desencadena la función start_drawing
canvas.bind("<Button-1>", start_drawing)
#Mientras se mantiene presionada el botón izquierdo del mouse y se mueve el mouse sobre el lienzo,
# se desencadena la función draw
canvas.bind("<B1-Motion>", draw)
#Cuando se suelta el botón izquierdo del mouse, se activa la función stop_drawing
canvas.bind("<ButtonRelease-1>", stop_drawing)
#Inicia el bucle principal de la aplicación, permitiendole responder a las interacciónes y eventos del usuario
root.mainloop()
