"""!@package gui
    @brief A simple calculator with an user interface written in python using tkinter.

    @date April 2021
"""

from tkinter import * # pylint: disable=unused-wildcard-import, method-hidden
from mathLib import * # pylint: disable=unused-wildcard-import, method-hidden
from NumberSystems import DECTOBIN, BINTODEC
import subprocess
import os
import sys


##  slovnik pro vymenu znaku operaci za funkce
operand_dict = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '÷': 'DIV', '/': 'DIV', '^': 'POW', '√': 'ROOT', '!': 'FACT', 'abs': 'ABS', 'rand': 'RAND'}

##  string pro ulozeni posledniho zadavaneho cisla
in_number = ""

##  list pro ulozeni postupne sekvence zadanych cisel a operaci jako stringy
in_sequence = []

##  bool pro ulozeni, jestli je vypis vysledek
disp_result = False

##  bool pro ulozeni, jestli je binarni mod zadavani
binary = False

root = Tk()
root.configure(background='black')
root.title("Calculator")

#cyklus pre zmenu velkosti riadkov
for row_number in range(1, 8):
    Grid.rowconfigure(root, row_number, weight=1)

#cyklus pre zmenu velkosti stlpcov
for column_number in range(1, 4):
    Grid.columnconfigure(root, column_number, weight=1)

#obmedzenie zmensovania
root.wm_minsize(400, 500)

##  funkce pro vypsani zadanych cisel a operatoru
def print_disp():
    global binary, in_sequence, in_number
    entry.delete(0, END)
    if binary:
        for i in in_sequence:
            if i in operand_dict:
                entry.insert(END, i)
            elif not i.isnumeric() or "." in i:
                entry.delete(0, END)
                entry.insert(0, "ERROR")
                in_number = ""
                in_sequence.clear()
                return
            else:
                entry.insert(END, DECTOBIN(i))
        if not "." in in_number:
            entry.insert(END, DECTOBIN(in_number))
        else:
            in_number = ""
    else:
        entry.insert(0, ''.join(in_sequence))
        entry.insert(END, in_number)

##  funkcia pre vypisovanie cisel na vstupe
#   @param number zadane cislo
def button_number(number):
    global in_number, disp_result
    if entry.get() == "ERROR" or disp_result:
        entry.delete(0, END)
        in_number = ""
        disp_result = False
    if binary:
        tmp = DECTOBIN(str(in_number))
        tmp += str(number)
        in_number = BINTODEC(tmp)
    else:
        in_number += str(number)
    print_disp()

##  pridani nove operace, ulozi predchozi zadane cislo
#   @param operand zadany operand
def button_operand(operand):
    global in_number, disp_result
    if entry.get() == "ERROR":
        entry.delete(0, END)
    disp_result = False
    if len(in_number) == 0:
        if operand == '-':
            in_number = '-'
            entry.insert(END, in_number)
            return
        else:
            in_number = '0'

    if operand == '!' or operand == 'abs':
        in_number = operand_dict.get(operand) + '(' + in_number + ')'
    else:
        in_sequence.append(in_number)
        in_sequence.append(operand)
        in_number = ""

    print_disp()

##  funkcia pre vymazanie vstupu
def button_ce():
    global in_number, in_sequence
    entry.delete(0, END)
    in_number = ""
    in_sequence.clear()

##  smaze posledni zadane cislo nebo operaci
def button_del():
    global in_number, in_sequence
    if len(in_number) > 0:
        in_number = ""
    else:
        if len(in_sequence) > 0:
            in_sequence.pop()
    print_disp()

##  po stisknuti = provede vypocet
def button_compute():
    global in_sequence, in_number, disp_result, binary
    entry.delete(0, END)
    in_sequence.append(in_number if len(in_number) > 0 else '0')
    eval_sequence = ""
    if len(in_sequence) == 1:
        eval_sequence = in_sequence[0]
    else:
        if in_sequence[1] == '√':
            eval_sequence = operand_dict.get(in_sequence[1]) + '(' + in_sequence[2] + ', ' + in_sequence[0] + ')'
        else:
            eval_sequence = operand_dict.get(in_sequence[1]) + '(' + in_sequence[0] + ', ' + in_sequence[2] + ')'
        for i in range(3, len(in_sequence), 2):
            if in_sequence[i] == '√':
                eval_sequence = operand_dict.get(in_sequence[i]) + '(' + in_sequence[i + 1] + ', ' + eval_sequence + ')'
            else:
                eval_sequence = operand_dict.get(in_sequence[i]) + '(' + eval_sequence + ', ' + in_sequence[i + 1] + ')'

    try:
        result = str(eval(eval_sequence))
        if binary:
            entry.insert(0, DECTOBIN(result))
        else:
            entry.insert(0, result)
        in_number = result
        disp_result = True
    except:
        entry.insert(0, 'ERROR')
        in_number = ""
    in_sequence.clear()

##  callback pro zpracovani zmacknuti klavesy
#   @param event zmacknuta klavesa
def key_event(event):
    if event.char.isnumeric() or event.char == '.':
        try:
            button_number(event.char)
        except:
            pass
    elif event.char in operand_dict:
        button_operand(event.char)
    elif event.keysym == "BackSpace":
        button_del()
    elif event.keysym == "Delete":
        button_ce()
    elif event.keysym == "Return":
        button_compute()

##  funkcia na otvorenie manualu
def open_manual():
    subprocess.Popen(["xdg-open " + get_path("res/manual.pdf")], shell=True)

##  funkcia na vypinanie a zapinanie tlacidiel pri pracovani s binarnou sustavou
def switch():
    global binary
    #vypnutie nepotrebnych tlacidiel
    if not binary:
        button_7["state"] = "disabled"
        button_8["state"] = "disabled"
        button_9["state"] = "disabled"
        button_4["state"] = "disabled"
        button_5["state"] = "disabled"
        button_6["state"] = "disabled"
        button_2["state"] = "disabled"
        button_3["state"] = "disabled"
        button_dot["state"] = "disabled"
        binary = True

    #zapnutie vsetkych tlacidiel
    else:
        button_7["state"] = "normal"
        button_8["state"] = "normal"
        button_9["state"] = "normal"
        button_4["state"] = "normal"
        button_5["state"] = "normal"
        button_6["state"] = "normal"
        button_2["state"] = "normal"
        button_3["state"] = "normal"
        button_dot["state"] = "normal"
        binary = False

    print_disp()

##  funkce pro vraceni spravne cesty res souboru
#   @param relative relativni cesta k souboru
#   @return absolutni cesta k souboru
def get_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath("."), relative)

#vstupne pole
entry = Entry(root, width=8, borderwidth=10, font=('Helvetica', 40), fg='white', bg='#6F00D2', takefocus = 0)
entry.grid(row=0, column=0, columnspan=4, ipadx=120, ipady=40, sticky=W+E)


#prvy riadok
button_random_num = Button(root, text='random number', font=('Helvetica', 20), fg='white', padx=26, pady=20, bg='#8600FF', command=lambda: button_operand('rand'))
button_CE = Button(root, text='CE', font=('Helvetica', 20), fg='white', padx=39, pady=20, bg='#8600FF', command=button_ce)
button_delete= Button(root, text='delete', font=('Helvetica', 20), fg='white', padx=24, pady=20, bg='#8600FF', command=button_del)

#stlacanie tlacidiel v prvom riadku
button_random_num.grid(row=1, column=0, columnspan=2, sticky=W+E)
button_CE.grid(row=1, column=2, sticky=W+E)
button_delete.grid(row=1, column=3, sticky=W+E)


#druhy riadok
button_bin_to_dec = Button(root, text='BIN -> DEC', font=('Helvetica', 20), fg='white', padx=51, pady=20, bg='#921AFF', command=switch)
button_factorial = Button(root, text='!', font=('Helvetica', 20), fg='white', padx=54, pady=20, bg='#921AFF', command=lambda: button_operand('!'))
button_manual = Button(root, text='manual', font=('Helvetica', 20), fg='white', padx=16, pady=20, bg='#921AFF', command=open_manual)

#stlacanie tlacidiel v druhom riadku
button_bin_to_dec.grid(row=2, column=0, columnspan=2, sticky=W+E)
button_factorial.grid(row=2, column=2, sticky=W+E)
button_manual.grid(row=2, column=3, sticky=W+E)


#treti riadok
button_abs = Button(root, text='|abs|', font=('Helvetica', 20), fg='white', padx=29, pady=20, bg='#9F35FF', command=lambda: button_operand('abs'))
button_square = Button(root, text='x^n', font=('Helvetica', 20), fg='white', padx=37, pady=20, bg='#9F35FF', command=lambda: button_operand('^'))
button_sqrt = Button(root, text='√', font=('Helvetica', 20), fg='white', padx=52, pady=20, bg='#9F35FF', command=lambda: button_operand('√'))
button_divise = Button(root, text='÷', font=('Helvetica', 20), fg='white', padx=52, pady=20, bg='#9F35FF', command=lambda: button_operand('÷'))

#stlacanie tlacidiel v tretom riadku
button_abs.grid(row=3, column=0, sticky=W+E)
button_square.grid(row=3, column=1, sticky=W+E)
button_sqrt.grid(row=3, column=2, sticky=W+E)
button_divise.grid(row=3, column=3, sticky=W+E)


#stvrty riadok
button_7 = Button(root, text='7', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#B15BFF', command=lambda: button_number(7))
button_8 = Button(root, text='8', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#B15BFF', command=lambda: button_number(8))
button_9 = Button(root, text='9', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#B15BFF', command=lambda: button_number(9))
button_multiply = Button(root, text='*', font=('Helvetica', 20), fg='white', padx=55, pady=20, bg='#B15BFF', command=lambda: button_operand('*'))

#stlacanie tlacidiel v stvrtom riadku
button_7.grid(row=4 , column=0, sticky=W+E)
button_8.grid(row=4 , column=1, sticky=W+E)
button_9.grid(row=4 , column=2, sticky=W+E)
button_multiply.grid(row=4, column=3, sticky=W+E)


#piaty riadok
button_4 = Button(root, text='4', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#BE77FF', command=lambda: button_number(4))
button_5 = Button(root, text='5', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#BE77FF', command=lambda: button_number(5))
button_6 = Button(root, text='6', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#BE77FF', command=lambda: button_number(6))
button_substract = Button(root, text='-', font=('Helvetica', 20), fg='white', padx=56, pady=20, bg='#BE77FF', command=lambda: button_operand('-'))

#stlacanie tlacidiel v piatom riadku
button_4.grid(row=5 , column=0, sticky=W+E)
button_5.grid(row=5 , column=1, sticky=W+E)
button_6.grid(row=5 , column=2, sticky=W+E)
button_substract.grid(row=5, column=3, sticky=W+E)


#siesty riadok
button_1 = Button(root, text='1', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#CA8EFF', command=lambda: button_number(1))
button_2 = Button(root, text='2', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#CA8EFF', command=lambda: button_number(2))
button_3 = Button(root, text='3', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#CA8EFF', command=lambda: button_number(3))
button_add = Button(root, text='+', font=('Helvetica', 20), fg='white', padx=52, pady=20, bg='#CA8EFF', command=lambda: button_operand('+'))

#stlacanie tlacidiel v siestom riadku
button_1.grid(row=6 , column=0, sticky=W+E)
button_2.grid(row=6 , column=1, sticky=W+E)
button_3.grid(row=6 , column=2, sticky=W+E)
button_add.grid(row=6, column=3, sticky=W+E)


#siedmy-posledny riadok
button_0 = Button(root, text='0', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#d3a4ff', command=lambda: button_number(0))
button_dot = Button(root, text='.', font=('Helvetica', 20), fg='white', padx=54, pady=20, bg='#d3a4ff', command=lambda: button_number('.'))
button_equal = Button(root, text='=', font=('Helvetica', 20), fg='white', padx=115, pady=20, bg='#d3a4ff', command=button_compute)

#stlacanie tlacidiel v siedmom-poslednom riadku
button_0.grid(row=7, column=1, sticky=W+E)
button_dot.grid(row=7, column=0, sticky=W+E)
button_equal.grid(row=7, column=2, columnspan=2, sticky=W+E)

root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=get_path('res/logo.png')))
root.bind("<Key>", key_event)
root.mainloop()
