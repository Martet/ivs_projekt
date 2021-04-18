from tkinter import *
from mathLib import *

#slovnik pro vymenu znaku operaci za funkce
operand_dict = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '÷': 'DIV', '^': 'POW', '√': 'ROOT'}

#string pro ulozeni posledniho zadavaneho cisla
in_number = ""
#list pro ulozeni postupne sekvence zadanych cisel a operaci jako stringy
in_sequence = []
#bool pro ulozeni, jestli je vypis vysledek
disp_result = False

root = Tk()
root. configure(background='black')
root.title("Calculator")

#funkcia pre vypisovanie cisel na vstupe
def button_number(number):
    global in_number, disp_result
    if entry.get() == "ERROR" or disp_result:
        entry.delete(0, END)
        in_number = ""
        disp_result = False
    entry.insert(END, str(number))
    in_number += str(number)

#pridani nove operace, ulozi predchozi zadane cislo
def button_operand(operand):
    global in_number, disp_result
    if entry.get() == "ERROR":
        entry.delete(0, END)
    disp_result = False
    entry.insert(END, operand)
    in_sequence.append(in_number if len(in_number) > 0 else '0')
    in_sequence.append(operand)
    in_number = ""

#funkcia pre vymazanie vstupu
def button_CE():
    global in_number, in_sequence
    entry.delete(0, END)
    in_number = ""
    in_sequence.clear()

#smaze posledni zadane cislo nebo operaci
def button_delete():
    global in_number, in_sequence
    if len(in_number) > 0:
        in_number = ""
    else:
        if len(in_sequence) > 0:
            in_sequence.pop()
    entry.delete(0, END)
    entry.insert(0, ''.join(in_sequence))

#po stisknuti = provede vypocet
def button_compute():
    global in_sequence, in_number, disp_result
    entry.delete(0, END)
    in_sequence.append(in_number if len(in_number) > 0 else '0')
    eval_sequence = ""
    if len(in_sequence) == 1:
        eval_sequence = in_sequence[0]
    else:
        eval_sequence = operand_dict.get(in_sequence[1]) + '(' + in_sequence[0] + ', ' + in_sequence[2] + ')'
        for i in range(3, len(in_sequence), 2):
            eval_sequence = operand_dict.get(in_sequence[i]) + '(' + eval_sequence + ', ' + in_sequence[i + 1] + ')'

    try:
        result = str(eval(eval_sequence))
        entry.insert(0, result)
        in_number = result
        disp_result = True
    except:
        entry.insert(0, 'ERROR')
        in_number = ""
    in_sequence.clear()

#vstupne pole
entry = Entry(root, width=8, borderwidth=10, font=('Helvetica', 80), fg='white', bg='#6F00D2')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#prvy riadok
button_random_num = Button(root, text='random number', font=('Helvetica', 20), fg='white', padx=26.5, pady=20, bg='#8600FF')
button_CE = Button(root, text='CE', font=('Helvetica', 20), fg='white', padx=39, pady=20, bg='#8600FF', command=button_CE)
button_delete= Button(root, text='delete', font=('Helvetica', 20), fg='white', padx=24, pady=20, bg='#8600FF', command=button_delete)

#stlacanie tlacidiel v prvom riadku
button_random_num.grid(row=1, column=0, columnspan=2)
button_CE.grid(row=1, column=2)
button_delete.grid(row=1, column=3)


#druhy riadok
button_abs = Button(root, text='|abs|', font=('Helvetica', 20), fg='white', padx=29, pady=20, bg='#921AFF')
button_square = Button(root, text='x^n', font=('Helvetica', 20), fg='white', padx=37, pady=20, bg='#921AFF', command=lambda: button_operand('^'))
button_sqrt = Button(root, text='√', font=('Helvetica', 20), fg='white', padx=52, pady=20, bg='#921AFF', command=lambda: button_operand('√'))
button_divise = Button(root, text='÷', font=('Helvetica', 20), fg='white', padx=53, pady=20, bg='#921AFF', command=lambda: button_operand('÷'))

#stlacanie tlacidiel v druhom riadku
button_abs.grid(row=2, column=0)
button_square.grid(row=2, column=1)
button_sqrt.grid(row=2, column=2)
button_divise.grid(row=2, column=3)


#treti riadok
button_7 = Button(root, text='7', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#9F35FF', command=lambda: button_number(7))
button_8 = Button(root, text='8', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#9F35FF', command=lambda: button_number(8))
button_9 = Button(root, text='9', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#9F35FF', command=lambda: button_number(9))
button_multiply = Button(root, text='x', font=('Helvetica', 20), fg='white', padx=54, pady=20, bg='#9F35FF', command=lambda: button_operand('*'))

#stlacanie tlacidiel v tretom riadku
button_7.grid(row=3 , column=0)
button_8.grid(row=3 , column=1)
button_9.grid(row=3 , column=2)
button_multiply.grid(row=3, column=3)


#stvrty riadok
button_4 = Button(root, text='4', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#B15BFF', command=lambda: button_number(4))
button_5 = Button(root, text='5', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#B15BFF', command=lambda: button_number(5))
button_6 = Button(root, text='6', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#B15BFF', command=lambda: button_number(6))
button_substract = Button(root, text='-', font=('Helvetica', 20), fg='white', padx=56, pady=20, bg='#B15BFF', command=lambda: button_operand('-'))

#stlacanie tlacidiel v stvrtom riadku
button_4.grid(row=4 , column=0)
button_5.grid(row=4 , column=1)
button_6.grid(row=4 , column=2)
button_substract.grid(row=4, column=3)


#piaty riadok
button_1 = Button(root, text='1', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#BE77FF', command=lambda: button_number(1))
button_2 = Button(root, text='2', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#BE77FF', command=lambda: button_number(2))
button_3 = Button(root, text='3', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#BE77FF', command=lambda: button_number(3))
button_add = Button(root, text='+', font=('Helvetica', 20), fg='white', padx=53, pady=20, bg='#BE77FF', command=lambda: button_operand('+'))

#stlacanie tlacidiel v piatom riadku
button_1.grid(row=5 , column=0)
button_2.grid(row=5 , column=1)
button_3.grid(row=5 , column=2)
button_add.grid(row=5, column=3)


#siesty-posledny riadok
button_0 = Button(root, text='0', font=('Helvetica', 20), fg='white', padx=50, pady=20, bg='#CA8EFF', command=lambda: button_number(0))
button_dot = Button(root, text='.', font=('Helvetica', 20), fg='white', padx=54, pady=20, bg='#CA8EFF', command=lambda: button_number('.'))
button_equal = Button(root, text='=', font=('Helvetica', 20), fg='white', padx=117, pady=20, bg='#CA8EFF', command=button_compute)

#stlacanie tlacidiel v siestom-poslednom riadku
button_0.grid(row=6, column=1)
button_dot.grid(row=6, column=0)
button_equal.grid(row=6, column=2, columnspan=2)


root.mainloop()



