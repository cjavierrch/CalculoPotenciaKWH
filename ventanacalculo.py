#calculo consumo electrico

import tkinter
ventana2=tkinter.Tk()
ventana2.title("Consumo Electrico - Grupo 4")
ventana2.geometry("500x250")

#declaracion de variables
potencia=0
cantidad=0
horasuso=0
diasuso=0
#evaluacion consumo mes
valorkwh=0
potenciatotal=0
consumowh=0
consumokvh=0
consumomes=0
#la tarifa mensual esta fijada segun limites consumo mes
tarifamensual=0


def btnsalir():
    #cierra la ventana
    ventana2.destroy()

def btnlimpiar():
    #borra el contenido de los cuadros de texto
    crdtx21.delete(0,"end")
    crdtx22.delete(0,"end")
    crdtx23.delete(0,"end")
    crdtx24.delete(0,"end")
    crdtxt212.delete(0,"end")
    crdtxt213.delete(0,"end")
    crdtxt214.delete(0,"end")
    crdtxt215.delete(0,"end")
    crdtxt216.delete(0,"end")
 


#INGRESO DE VALORES
etiq21=tkinter.Label(ventana2, text="Ingrese Potencia Electrodomestico: ")
etiq21.pack()
etiq21.place(x=20,y=20)
crdtx21=tkinter.Entry(ventana2)
crdtx21.pack()
crdtx21.place(x=220, y=20)
etiq22=tkinter.Label(ventana2, text="Ingrese Cantidad: ")
etiq22.pack()
etiq22.place(x=20, y=45)
etiq23=tkinter.Label(ventana2, text="Ingrese Horas de Uso: ")
etiq23.pack()
etiq23.place(x=20, y=70)
etiq24=tkinter.Label(ventana2, text="Ingrese Dias de Uso: ")
etiq24.pack()
etiq24.place(x=20, y=90)
crdtx22=tkinter.Entry(ventana2)
crdtx22.pack()
crdtx22.place(x=220, y=45)
crdtx23=tkinter.Entry(ventana2)
crdtx23.pack()
crdtx23.place(x=220, y=70)
crdtx24=tkinter.Entry(ventana2)
crdtx24.pack()
crdtx24.place(x=220, y=95)

etiq26=tkinter.Label(ventana2, text=f"Potencia Total (W): ")
etiq26.pack()
etiq26.place(x=20,y=120)
etiq27=tkinter.Label(ventana2, text=f"Consumo Diario (Wh): ")
etiq27.pack()
etiq27.place(x=20, y=145)
etiq28=tkinter.Label(ventana2, text=f"Consumo Kilovatio Hora (kWh): ")
etiq28.pack()
etiq28.place(x=20, y=170)
etiq29=tkinter.Label(ventana2, text=f"Consumo Mensual (kWh): ")
etiq29.pack()
etiq29.place(x=20, y=195)
etiq210=tkinter.Label(ventana2, text=f"Tarifa Mensual (kWh) $: ")
etiq210.pack()
etiq210.place(x=20,y=220)

crdtxt212=tkinter.Entry(ventana2)
crdtxt212.pack()
crdtxt212.place(x=220,y=120)
crdtxt213=tkinter.Entry(ventana2)
crdtxt213.pack()
crdtxt213.place(x=220, y=145)
crdtxt214=tkinter.Entry(ventana2)
crdtxt214.pack()
crdtxt214.place(x=220, y=170)
crdtxt215=tkinter.Entry(ventana2)
crdtxt215.pack()
crdtxt215.place(x=220, y=195)
crdtxt216=tkinter.Entry(ventana2)
crdtxt216.pack()
crdtxt216.place(x=220,y=220)


#INICIO CALCULO VALORES y PRESENTACION

def btncalcular():
    #global potencia
    #global cantidad
    #global horasuso
    #global diasuso
    #global valorkwh

    potencia=float(crdtx21.get())
    cantidad=float(crdtx22.get())
    horasuso=float(crdtx23.get())
    diasuso=float(crdtx24.get())
    
    potenciatotal=potencia*cantidad
    consumowh=round((potenciatotal*horasuso),2)
    consumokvh=round((consumowh/1000),2)
    consumomes=round((consumokvh*diasuso),2)
    #la tarifa mensual esta fijada por $0,09
    
    tarifamensual=round((consumomes*valorkwh),2)
    
    crdtxt212.insert(0,f"{potenciatotal}")
    crdtxt213.insert(0,f"{consumowh}")
    crdtxt214.insert(0,f"{consumokvh} ")
    crdtxt215.insert(0,f"{consumomes}")
    crdtxt216.insert(0,f"{tarifamensual} ")
    

#botones de comando para la ventana
btn21=tkinter.Button(ventana2,  text="CALCULAR", command=btncalcular)
btn21.pack()
btn21.place(x=380,y=60, height=30,width=75)

btn22=tkinter.Button(ventana2,  text="LIMPIAR", command=btnlimpiar)
btn22.pack()
btn22.place(x=380,y=100,height=30,width=75)
    
btn23=tkinter.Button(ventana2,  text="SALIR", command=btnsalir)
btn23.pack()
btn23.place(x=380,y=140,height=30,width=75)
    





ventana2.mainloop()
