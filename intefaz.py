from tkinter import *
import os

raiz = Tk()
raiz.title("Calculadora")
raiz.geometry("400x600")
raiz.resizable(False, False)

# En esta pantalla se escribiran los numeros.
pantalla = Label(raiz, bg = "black", width = 50, height = 4, bd = 5, relief = "flat").place(relx = 0.5, rely = 0, anchor = N)

# Aqui estaran los botones de la calculadora.
botones = Label(raiz, bg = "gray", width = 50, height = 35, bd = 5, relief = "flat").place(relx = 0.5, rely = 1, anchor = S)

btnporcentaje = Button(botones, text = "%", bg = "black", fg = "white", width = 8, height = 3, bd = 5, relief = "groove")
btnporcentaje.place(x = 30, y = 70)

btnCE = Button(botones, text = "CE", bg = "black", fg = "white", width = 8, height = 3, bd = 5, relief = "groove")
btnCE.place(x = 120, y = 70)

btnC = Button(botones, text = "C", bg = "black", fg = "white", width = 8, height = 3, bd = 5, relief = "groove")
btnC.place(x = 210, y = 70)

btnBorrar = Button(botones, text = "<<", bg = "black", fg = "white", width = 8, height = 3, bd = 5, relief = "groove")
btnBorrar.place(x = 300, y = 70)

btn1EntreX = Button(botones, text = "1\u2044x", bg = "black", fg = "white", width = 8, height = 3, bd = 5, relief = "groove")
btn1EntreX.place(x = 30, y = 140)

btnXSquare = Button(botones, text="x\u00B2", bg="black", fg="white", width=8, height=3, bd=5, relief="groove")
btnXSquare.place(x = 120, y = 140)

btnRaiz = Button(botones, text = "\u221A", bg="black", fg="white", width=8, height=3, bd=5, relief="groove")
btnRaiz.place(x = 210, y = 140)

btnDivisor = Button(botones, text = "/", bg="black", fg="white", width=8, height=3, bd=5, relief="groove")
btnDivisor.place(x = 300, y = 140)

raiz.mainloop()