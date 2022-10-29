#Hacer un calculadora que haga operaciones simples.

from tkinter import *
import tkinter
window=Tk()
window.geometry("375x667")
window.title("Calculadora by Bruno Aguirre-Nancaro")

# una variable de texto para almacenar los datos introducidos en el campo de entrada.
txt=StringVar()
expression= ""
# Función para actualizar la expresión
# en el cuadro de entrada de texto
def click(num):

    # señalar la variable de expresión global
    global expression

    # concatenación de string
    expression = expression + str(num)

    # actualizar la expresión mediante el método set
    txt.set(expression)
# Función para evaluar la expresión final

def equal():
    # Se utiliza la sentencia try y except
    # para manejar los errores como el cero
    # error de división, etc.

    # Poner ese código dentro del bloque try
    # que puede generar el error
    try:
        # La función evalúa la expresión
        # y la función str convierte el resultado
        # en una string
        global expression
        # e1.delete(0,END)
        add = str(eval(expression))
        txt.set(add)
        # inicializar la variable de expresión
        # por string vacía
        expression = " "

        # si se genera un error entonces se maneja
        # por el bloque except
    except:
        expression.set("Error")
        expression=""
# definir una función borrar (clear)
def clr():
    # para borrar una entrada individual
    global expression
    length = len(txt.get())
    e1.delete(length - 1, 'end')


def clearAll():
    # para que se borre todo el texto
    global expression
    expression = ""
    txt.set("")


# creando marcos
frame1=Frame(window,width=390,height=600,bg="#005a96")
frame1.pack(side=TOP)
frame1.pack(fill = tkinter.Y,expand= True)
frame2=Frame(window,width=390,height=368,bg="#005a96")
frame2.pack(side=BOTTOM)
frame2.pack(fill = tkinter.Y,expand= True)

# crear una etiqueta
l1=Label(frame1,text="Casia - Marca ACME",bg="#005a96",font=("Roboto Condensed",20, 'bold'))
l2=Label(frame1,text="Hecho por Bruno Aguirre",bg="#005a96",font=("Arial Bold",10))
l1.pack(side=TOP,expand=YES)
l2.pack(side=TOP,expand=YES)
# crear un campo de entrada
e1=Entry(frame1,textvariable=txt,width=60,bd=10,font=("Roboto Condensed",42),
         fg="white",bg="#0070bc",relief=RIDGE,justify=RIGHT)
e1.pack(fill = tkinter.Y,expand= True)
e1.insert(0,"0")

# Añadir botones
# cuando el usuario presiona el botón, el comando o
# función afiliada a ese botón se ejecuta .
# Los atributos padx y pady añaden espacio extra horizontal y vertical a los widgets.
# Método place() de Python en Tkinter Permite establecer explícitamente la posición y el tamaño de una ventana, ya sea en términos absolutos, o relativos a otra ventana.
but1=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(7),text="7",font=("Roboto Condensed",16,'bold'))
but1.place(x=5,y=10)
but2=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(4),text="4",font=("Roboto Condensed",16,'bold'))
but2.place(x=5,y=81)

but3=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(1),text="1",font=("Roboto Condensed",16,'bold'))
but3.place(x=5,y=152)

but4=Button(frame2,padx=48,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(0),text="0",font=("Roboto Condensed",16,'bold'))
but4.place(x=5,y=223)

but5=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(8),text="8",font=("Roboto Condensed",16,'bold'))
but5.place(x=72,y=10)

but6=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(5),text="5",font=("Roboto Condensed",16,'bold'))
but6.place(x=72,y=81)

but7=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(2),text="2",font=("Roboto Condensed",16,'bold'))
but7.place(x=72,y=152)

but8=Button(frame2,padx=17,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click("."),text=".",font=("Roboto Condensed",16,'bold'))
but8.place(x=139,y=223)

but9=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
            command=lambda:click(9),text="9",font=("Roboto Condensed",16,'bold'))
but9.place(x=139,y=10)

but10=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
             command=lambda:click(6), text="6", font=("Roboto Condensed", 16,'bold'))
but10.place(x=139,y=81)

but11=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
             command=lambda:click(3),text="3",font=("Roboto Condensed",16,'bold'))
but11.place(x=139,y=152)

but12=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
             command=lambda:click("+"),text="+",font=("Roboto Condensed",16,'bold'))
but12.place(x=205,y=10)

but13=Button(frame2,padx=17,pady=14,bd=4,fg="white",bg='#008ceb',
             command=lambda:click("-"),text="-",font=("Roboto Condensed",16,'bold'))
but13.place(x=205,y=81)

but14=Button(frame2,padx=14,pady=14,bd=4,fg="white",bg='#008ceb',
             command=lambda:click("*"),text="x",font=("Roboto Condensed",16,'bold'))
but14.place(x=205,y=152)

but15=Button(frame2,padx=17,pady=14,bd=4,fg="white",bg='#008ceb',
             command=lambda:click("/"),text="/",font=("Roboto Condensed",16,'bold'))
but15.place(x=205,y=223)

but16=Button(frame2,padx=30,pady=84,bd=4,fg="white",bg='#136ca9',
             command=clr,text="<-",font=("Roboto Condensed",16,'bold'))
but16.place(x=270,y=10)

but17=Button(frame2,padx=168,pady=14,bd=4,fg="white",bg='#136ca9',
             command=equal,text="=",font=("Roboto Condensed",16,'bold'))
but17.place(x=5,y=294)

but18=Button(frame2,padx=25,pady=14,bd=4,fg="white",bg='#136ca9',
             command=clearAll,text="CE",font=("Roboto Condensed",16,'bold'))
but18.place(x=270,y=223)
# iniciar la GUI
window.mainloop()
