# calculadora cientifica
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk

window = Tk()
window.title("CALCULADORA FINANCIERA")
window.geometry("600x300")

w = Text(window)
w.place(x="10", y="10", width=232, height=35)
w.insert(INSERT, "0")


def valor_presente():
    tasa = float(r.get()) / 100

    if str(scrollbar1.get()) == "Anual":

        if str(scrollbar2.get()) == "Anual":
            tasa = tasa

        elif str(scrollbar2.get()) == "Semestral":
            tasa = (tasa + 1) ** (0.5) - 1

        elif str(scrollbar2.get()) == "Trimestral":
            tasa = (tasa + 1) ** (0.25) - 1

        elif str(scrollbar2.get()) == "Mensual":
            tasa = (tasa + 1) ** (1 / 12) - 1

        elif str(scrollbar2.get()) == "Ninguna":
            tasa = tasa

    elif str(scrollbar1.get()) == "Mensual":

        if str(scrollbar2.get()) == "Anual":
            tasa = (tasa + 1) ** 12 - 1

        elif str(scrollbar2.get()) == "Semestral":
            tasa = (tasa + 1) ** (6) - 1

        elif str(scrollbar2.get()) == "Trimestral":
            tasa = (tasa + 1) ** (3) - 1

        elif str(scrollbar2.get()) == "Mensual":
            tasa = tasa

        elif str(scrollbar2.get()) == "Ninguna":
            tasa = tasa

    elif str(scrollbar1.get()) == "Otra":
        tasa = tasa

    numerador = 1 - (1 + tasa) ** (-1 * float(pagos.get()))
    pagas = float(premio.get())
    answer = pagas * (numerador / tasa)

    if str(scrollbar3.get()) == "No ajustar":

        if str(pagos.get()) == "inf":

            ans = float(premio.get()) / tasa

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

        else:

            print(round(answer, 3))

            ans = round(answer, 3)

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(ans))

    elif str(scrollbar3.get()) == "Adelante" and str(pagos.get()) != "inf":

        if str(scrollbar1.get()) == "Anual":

            latasa = (float(r.get()) / 100 + 1) ** (1 / 12) - 1
            ans = ((round(answer, 3)) * ((1 + latasa) ** float(elajuste.get())))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

        elif str(scrollbar1.get()) == "Mensual":

            latasa = float(r.get()) / 100
            ans = ((round(answer, 3)) * ((1 + latasa) ** float(elajuste.get())))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

    elif str(scrollbar3.get()) == "Atras" and str(pagos.get()) != "inf":

        if str(scrollbar1.get()) == "Anual":

            latasa = (float(r.get()) / 100 + 1) ** (1 / 12) - 1
            ans = ((round(answer, 3)) / ((1 + latasa) ** float(elajuste.get())))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

        elif str(scrollbar1.get()) == "Mensual":

            latasa = float(r.get()) / 100
            ans = ((round(answer, 3)) / ((1 + latasa) ** float(elajuste.get())))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))



    elif str(scrollbar3.get()) == "Adelante" and str(pagos.get()) == "inf":

        if str(scrollbar1.get()) == "Anual":
            latasa = (float(r.get()) / 100 + 1) ** (1 / 12) - 1
            ans = float(premio.get()) / tasa * ((1 + latasa) ** float(elajuste.get()))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

        elif str(scrollbar1.get()) == "Mensual":
            latasa = float(r.get()) / 100
            ans = float(premio.get()) / tasa * ((1 + latasa) ** float(elajuste.get()))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))


    elif str(scrollbar3.get()) == "Atras" and str(pagos.get()) == "inf":

        if str(scrollbar1.get()) == "Anual":
            latasa = (float(r.get()) / 100 + 1) ** (1 / 12) - 1
            ans = (float(premio.get()) / tasa) / ((1 + latasa) ** float(elajuste.get()))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

        elif str(scrollbar1.get()) == "Mensual":
            latasa = float(r.get()) / 100
            ans = (float(premio.get()) / tasa) / ((1 + latasa) ** float(elajuste.get()))

            print(round(ans, 3))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))


def con_g():
    #La tasa de crecimiento g no se ajusta (la que pongas en el cuadro es la que se usara).
    tasa = float(r.get()) / 100
    tasa_ajuste = 0

    if str(scrollbar1.get()) == "Anual":
        #La tasa de ajuste es siempre mensual
        tasa_ajuste = (1 + tasa) ** (1 / 12) - 1

        if str(scrollbar2.get()) == "Anual":
            tasa = tasa

        elif str(scrollbar2.get()) == "Semestral":
            tasa = (tasa + 1) ** (0.5) - 1

        elif str(scrollbar2.get()) == "Trimestral":
            tasa = (tasa + 1) ** (0.25) - 1

        elif str(scrollbar2.get()) == "Mensual":
            tasa = (tasa + 1) ** (1 / 12) - 1

        elif str(scrollbar2.get()) == "Ninguna":
            tasa = tasa

    elif str(scrollbar1.get()) == "Mensual":
        tasa_ajuste = tasa

        if str(scrollbar2.get()) == "Anual":
            tasa = (tasa + 1) ** 12 - 1

        elif str(scrollbar2.get()) == "Semestral":
            tasa = (tasa + 1) ** (6) - 1

        elif str(scrollbar2.get()) == "Trimestral":
            tasa = (tasa + 1) ** (3) - 1

        elif str(scrollbar2.get()) == "Mensual":
            tasa = tasa

        elif str(scrollbar2.get()) == "Ninguna":
            tasa = tasa

    elif str(scrollbar1.get()) == "Otra":
        tasa = tasa

    tasag = float(grow.get()) / 100

    the_ans = (float(premio.get()) / (tasa - tasag)) * (1 - ((1 + tasag) / (1 + tasa)) ** (float(pagos.get())))
    inf_ans = float(premio.get()) / (tasa - tasag)

    if str(pagos.get()) == "inf":

        if str(scrollbar3.get()) == "No ajustar":

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(inf_ans, 3)))

        elif str(scrollbar3.get()) == "Adelante":

            def_ans = inf_ans * (1 + tasa_ajuste) ** (float(elajuste.get()))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(def_ans, 3)))

        elif str(scrollbar3.get()) == "Atras":

            def_ans = inf_ans * (1 / (1 + tasa_ajuste)) ** (float(elajuste.get()))


    elif str(pagos.get()) != "inf":

        if str(scrollbar3.get()) == "No ajustar":

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(the_ans, 3)))

        elif str(scrollbar3.get()) == "Adelante":

            def_ans = the_ans * (1 + tasa_ajuste) ** (float(elajuste.get()))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(def_ans, 3)))

        elif str(scrollbar3.get()) == "Atras":

            def_ans = the_ans * (1 / (1 + tasa_ajuste)) ** (float(elajuste.get()))

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(def_ans, 3)))


def inflacion():
    inflacion = (float(dato2.get()) / float(dato1.get()) - 1) * 100

    w = Text(window)
    w.place(x="10", y="10", width=232, height=35)
    w.insert(INSERT, str(round(inflacion, 3)) + "%")


def get_cuotas():

    tasa = float(r.get()) / 100
    tasa_ajuste = 0

    if str(scrollbar1.get()) == "Anual":
        tasa_ajuste = (1 + tasa)**(1/12) - 1

        if str(scrollbar2.get()) == "Anual":
            tasa = tasa

        elif str(scrollbar2.get()) == "Semestral":
            tasa = (tasa + 1) ** (0.5) - 1

        elif str(scrollbar2.get()) == "Trimestral":
            tasa = (tasa + 1) ** (0.25) - 1

        elif str(scrollbar2.get()) == "Mensual":
            tasa = (tasa + 1) ** (1 / 12) - 1

        elif str(scrollbar2.get()) == "Ninguna":
            tasa = tasa

    elif str(scrollbar1.get()) == "Mensual":
        tasa_ajuste = tasa

        if str(scrollbar2.get()) == "Anual":
            tasa = (tasa + 1) ** 12 - 1

        elif str(scrollbar2.get()) == "Semestral":
            tasa = (tasa + 1) ** (6) - 1

        elif str(scrollbar2.get()) == "Trimestral":
            tasa = (tasa + 1) ** (3) - 1

        elif str(scrollbar2.get()) == "Mensual":
            tasa = tasa

        elif str(scrollbar2.get()) == "Ninguna":
            tasa = tasa

    elif str(scrollbar1.get()) == "Otra":
        tasa = tasa

    numerador = 1 - (1 + tasa)**(-1*float(pagos.get()))
    the_ans = float(vp_entry.get())/(numerador/tasa)
    inf_ans = float(vp_entry.get())*tasa


    if str(pagos.get()) == "inf":

        if str(scrollbar3.get()) == "No ajustar":

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(inf_ans, 3)))

        elif str(scrollbar3.get()) == "Adelante":

            ans = inf_ans/((1 + tasa_ajuste)**(float(elajuste.get())))
            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

        elif str(scrollbar3.get()) == "Atras":
            
            ans = inf_ans*((1 + tasa_ajuste)**(float(elajuste.get())))
            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))


    elif str(pagos.get()) != "inf":

        if str(scrollbar3.get()) == "No ajustar":

            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(the_ans, 3)))

        elif str(scrollbar3.get()) == "Adelante":

            ans = the_ans/((1 + tasa_ajuste)**(float(elajuste.get())))
            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))

        elif str(scrollbar3.get()) == "Atras":

            ans = the_ans*((1 + tasa_ajuste)**(float(elajuste.get())))
            w = Text(window)
            w.place(x="10", y="10", width=232, height=35)
            w.insert(INSERT, str(round(ans, 3)))
            

            

# ESTA ES LA PARTE DEL VALOR PRESENTE

# tasa interes
r = Entry(window)
r.pack(side=LEFT)
r.place(x="115", y="72")

bot = Button(window, text="Tasa interes")
bot.place(x="10", y="70", width=90, height=25)

# Ajuste tasa
bot2 = Button(window, text="Ajustar tasa a:")
bot2.place(x="10", y="102", width=90, height=24)

# VALOR CUOTAS
premio = Entry(window)
premio.place(x="115", y="134")

bot3 = Button(window, text="Valor cuotas")
bot3.place(x="10", y="133", width=90, height=24)

# NUMERO PAGOS
pagos = Entry(window)
pagos.place(x="115", y="167")

bot4 = Button(window, text="N° Pagos")
bot4.place(x="10", y="165", width=90, height=24)

# BARRAS DE SELECCION
scrollbar1 = Spinbox(window, values=("Anual", "Mensual", "Otra"))
scrollbar1.place(x="250", y="72", width=90)

scrollbar2 = Spinbox(window, values=("Anual", "Semestral", "Trimestral", "Mensual", "Ninguna"))
scrollbar2.place(x="115", y="103", width=125)

# CON O SIN CRECIMIENTO
bot6 = Button(window, text="Crecimiento (tasa)")
bot6.place(x="10", y="200", width=117)

grow = Entry(window)
grow.place(x="130", y="202", width=111)

botg = Button(window, text="VP con g", command=con_g)
botg.place(x="155", y="260", height=35, width=91)

# AJUSTE PERIODOS EN MESES
bot5 = Button(window, text="Ajuste (N° meses)")
bot5.place(x="10", y="230", width=117)

elajuste = Entry(window)
elajuste.place(x="130", y="232", width=111)

scrollbar3 = Spinbox(window, values=("Adelante", "Atras", "No ajustar"))
scrollbar3.place(x="250", y="232", width=90)

# BOTON DE EJECUCION
valorpresente = Button(window, text="Valor presente", command=valor_presente)
valorpresente.place(x="10", y="260", width=140, height=35)

# INFLACION

dato1 = Entry(window)
dato1.place(x="355", y="230", width=110)

dato2 = Entry(window)
dato2.place(x="475", y="230", width=110)

bot.ipc1 = Button(window, text="IPC 1")
bot.ipc1.place(x="355", y="200", width=110)

bot.ipc2 = Button(window, text="IPC 2")
bot.ipc2.place(x="475", y="200", width=110)

bot_inflacion = Button(window, text="Inflacion", command=inflacion)
bot_inflacion.place(x="355", y="260", height=35, width=230)


#Valor de las cuotas a partir de el VP

bot_cuotas = Button(window, text = "Valor Cuotas", command = get_cuotas)
bot_cuotas.place(x = "250", y = "260", height = 35, width = 95)

Vp = Button(window, text = "VP cuotas (total)")
Vp.place(x = "355", y = "70", height = 25, width = 230)

vp_entry = Entry(window)
vp_entry.place(x = "355", y = "100", width = 230)


window.mainloop()
