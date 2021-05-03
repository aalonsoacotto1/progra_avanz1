import tkinter as tk 

def click(event):
	print(str(entry.get()))
	entry.delete(0, tk.END)
	cont = contador['text']
	cont = int(cont) + 1
	contador['text'] = str(cont)
	if cont >= 5:
		ventana.destroy()

def enter(event):
	print(str(entry.get()))
	entry.delete(0, tk.END)
	cont = contador['text']
	cont = int(cont) + 1
	contador['text'] = str(cont)
	if cont >= 5:
		ventana.destroy()

ventana = tk.Tk()

contador = tk.Label(text="0")
contador.pack()
instruccion = tk.Label(text="Ingresa tu nombre:")
entry = tk.Entry()
instruccion.pack()
entry.pack()
boton = tk.Button(text="Enviar!")
boton.bind("<Button-1>", click)
ventana.bind("<Return>", enter)
#boton.pack()

ventana.mainloop()

# INVESTIGAR:

# HTML5 
	# HTML
	# CSS
	# JS
