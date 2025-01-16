from tkinter import *
from tkinter.constants import DISABLED
import random
import datetime

operator = ''
food_price = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_price = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_price = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_button(character):
    global operator
    operator = operator + character
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)


def delete_all():
    global operator
    operator = ''
    calculator_display.delete(0, END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.delete(0, result)
    operator = ''

def review_check():
    x= 0
    for b in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state= NORMAL)
            if food_box[x].get() == '0':
                food_box[x].delete(0, END)
            food_box[x].focus
        else:
            food_box[x].config(state= DISABLED)
            food_text[x].set('0')
        x += 1

    x = 0
    for b in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=NORMAL)
            if drink_box[x].get() == '0':
                drink_box[x].delete(0, END)
            drink_box[x].focus
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1
    x = 0
    for b in dessert_box:
        if dessert_variables[x].get() == 1:
            dessert_box[x].config(state=NORMAL)
            if dessert_box[x].get() == '0':
                dessert_box[x].delete(0, END)
            dessert_box[x].focus
        else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1

def total_calculation():
    food_subtotal = 0
    p= 0
    for unit in food_text:
        food_subtotal= food_subtotal + (float(unit.get()) * food_price[p])
        p +=1
    print(food_subtotal)

    drink_subtotal = 0
    p = 0
    for unit in drink_text:
        drink_subtotal = drink_subtotal + (float(unit.get()) * drink_price[p])
        p += 1
    print(drink_subtotal)

    dessert_subtotal = 0
    p = 0
    for unit in dessert_text:
        dessert_subtotal = dessert_subtotal + (float(unit.get()) * dessert_price[p])
        p += 1
    print(dessert_subtotal)

    my_subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    my_taxes = my_subtotal * 0.11
    my_total = my_subtotal + my_taxes

    food_cost_var.set(f'${round(food_subtotal, 2)}')
    drink_cost_var.set(f'${round(drink_subtotal, 2)}')
    dessert_cost_var.set(f'${round(dessert_subtotal, 2)}')
    subtotal_cost_var.set(f'${round(my_subtotal, 2)}')
    taxes_cost_var.set(f'${round(my_taxes, 2)}')
    total_cost_var.set(f'${round(my_total, 2)}')

def create_invoice():
    invoice_text.delete(1.0, END)
    invoice_number = f'N# - {random.randint(1000, 9999)}'
    my_date = datetime.datetime.now()
    invoice_date = f'{my_date.month}/{my_date.day}/{my_date.year} - {my_date.hour}: {my_date.minute}'
    invoice_text.insert(END,f'Information: \t{invoice_number}\t\t{invoice_date}\n')
    invoice_text.insert(END, f'*'*47+ '\n')
    invoice_text.insert(END,f'items\t\tQuality\titems cost\n')
    invoice_text.insert(END, f'-'*54 + '\n')

    x = 0
    for f in food_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{food_list[x]}\t\t{f.get()}\t'
                                     f'${int(f.get()) * food_price[x]}\n')
        x += 1

    x = 0
    for d in drink_text:
        if d.get() != '0':
            invoice_text.insert(END, f'{drink_list[x]}\t\t{d.get()}\t'
                                     f'${int(d.get()) * drink_price[x]}\n')
        x += 1

    x= 0
    for e in dessert_text:
        if e.get() != '0':
            invoice_text.insert(END, f'{dessert_list[x]}\t\t{e.get()}\t'
                                     f'${int(e.get()) * dessert_price[x]}\n')
        x += 1

    

#Initialize TKinter
application = Tk()

#Window size
application.geometry("1020x630+0+0")

#Prevent Maximizing
application.resizable(False, False)

#Window Title
application.title("My Restaurent - Invoicing System")

#Background color
application.config(bg = "blue")

#Top Panel
top_panel = Frame(application, bd = 10, relief = RAISED)
top_panel.pack(side = TOP)

#Title Tag
title_tag = Label(top_panel, text = "Invoicing System", fg = "azure4", font=("Dosis", 40), bg = "burlywood", width = 27)
title_tag.grid(row = 0, column = 0)

#Left Panel
left_panel = Frame(application, bd = 1, relief= FLAT)
left_panel.pack(side = LEFT)

#Cost Panel
cost_panel = Frame(left_panel, bd = 1, relief= FLAT, bg= 'azure4', padx= 50)
cost_panel.pack(side = BOTTOM)

#Food Panel
food_panel = LabelFrame(left_panel, text = "Food", font = ("Dosis", 19, "bold"), bd =1 , relief= FLAT, fg = "azure4")
food_panel.pack(side = LEFT)

#Drink Panel
drink_panel = LabelFrame(left_panel, text = "Drink", font = ("Dosis", 19, "bold"), bd =1 , relief= FLAT, fg = "azure4")
drink_panel.pack(side = LEFT)
#Dessert Panel
dessert_panel = LabelFrame(left_panel, text = "Dessert", font = ("Dosis", 19, "bold"), bd =1 , relief= FLAT, fg = "azure4")
dessert_panel.pack(side = LEFT)

#RIght Panel
right_panel = Frame(application, bd = 1, relief= FLAT)
right_panel.pack(side = RIGHT)

#Calculator Panel
calculator_panel = Frame(right_panel, bd = 1, relief = FLAT, bg = "burlywood")
calculator_panel.pack()

#Invoice Panel
invoice_panel = Frame(right_panel, bd = 1, relief = FLAT, bg = "burlywood")
invoice_panel.pack()

#Calculator Panel
buttons_panel = Frame(right_panel, bd = 1, relief = FLAT, bg = "burlywood")
buttons_panel.pack()

#Product lists
food_list = ["Chicken", "Lamb", "Salmon", "Hake", "Kebab", "Pizza1", "Pizza2", "Pizza3"]
drink_list = ["Lemonade", "Soda", "Juice", "Cola", "Wine1", "Wine2", "Beer1", "Beer2"]
dessert_list = ["Ice-Cream", "Fruit", "Brownies", "Pudding", "Cheesecake", "Cake1", "Cake2", "Cake3"]

#Create food items
food_variables = []
food_box = []
food_text = []

counter = 0
for food in food_list:
    food_variables.append(" ")
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text = food.title(),
                       font = ("Dosis,", 19, "bold"),
                       onvalue=1,
                       offvalue=0,
                       variable = food_variables[counter],
                       command = review_check)
    food.grid(row = counter,
              column = 0,
              sticky = W)

    food_box.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_box[counter]= Entry(food_panel,
                             font=('Dosis', 18, 'bold'),
                             bd= 1,
                             width = 6,
                             state = DISABLED,
                             textvariable= food_text[counter])
    food_box[counter].grid(row = counter,
                           column = 1,
                           )

    counter += 1

#Create drink items
drink_variables = []
drink_box = []
drink_text = []

counter = 0
for drink in drink_list:
    drink_variables.append(" ")
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel,
                        text = drink.title(),
                        font = ("Dosis,", 19, "bold"),
                        onvalue=1,
                        offvalue=0,
                        variable = drink_variables[counter],
                        command = review_check)
    drink.grid(row = counter,
               column = 0,
               sticky = W)
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter] = Entry(drink_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=drink_text[counter])
    drink_box[counter].grid(row=counter,
                           column=1,
                           )
    counter += 1

#Create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []

counter = 0
for dessert in dessert_list:
    dessert_variables.append(" ")
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text = dessert.title(),
                          font = ("Dosis,", 19, "bold"),
                          onvalue=1, offvalue=0,
                          variable = dessert_variables[counter],
                          command= review_check)
    dessert.grid(row = counter,
                 column = 0,
                 sticky = W)
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter] = Entry(dessert_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=dessert_text[counter])
    dessert_box[counter].grid(row=counter,
                           column=1,
                           )

    counter += 1

#variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_cost_var = StringVar()
taxes_cost_var = StringVar()
total_cost_var = StringVar()

#cost and labels and input fields

food_cost_label = Label(cost_panel,
                        text= 'Food cost',
                        font= ('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
food_cost_label.grid(row=0,column=0)
food_cost_text = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd= 1,
                       width = 10,
                       state='readonly',
                       textvariable=food_cost_var)
food_cost_text.grid(row=0,column=1, padx= 41)

drink_cost_label = Label(cost_panel,
                        text= 'drink cost',
                        font= ('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
drink_cost_label.grid(row=1,column=0)
drink_cost_text = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd= 1,
                       width = 10,
                       state='readonly',
                       textvariable=drink_cost_var)
drink_cost_text.grid(row=1,column=1, padx= 41)

dessert_cost_label = Label(cost_panel,
                        text= 'dessert cost',
                        font= ('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
dessert_cost_label.grid(row=2,column=0)
dessert_cost_text = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd= 1,
                       width = 10,
                       state='readonly',
                       textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2,column=1, padx= 41)


subtotal_cost_label = Label(cost_panel,
                        text= 'subtotal cost',
                        font= ('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
subtotal_cost_label.grid(row=0,column=2)
subtotal_cost_text = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd= 1,
                       width = 10,
                       state='readonly',
                       textvariable=subtotal_cost_var)
subtotal_cost_text.grid(row=0,column=3, padx= 41)

taxes_cost_label = Label(cost_panel,
                        text= 'taxes ',
                        font= ('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
taxes_cost_label.grid(row=1,column=2)
taxes_cost_text = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd= 1,
                       width = 10,
                       state='readonly',
                       textvariable= taxes_cost_var)
taxes_cost_text.grid(row=1,column=3, padx = 41)


total_cost_label = Label(cost_panel,
                        text= 'total ',
                        font= ('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
total_cost_label.grid(row=2,column=2)
total_cost_text = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd= 1,
                       width = 10,
                       state='readonly',
                       textvariable= total_cost_var)
total_cost_text.grid(row=2,column=3, padx= 41)

#buttons
buttons = ['total', 'invoice', 'save', 'reset']
created_buttons= []
column = 0
for button in buttons:
    button = Button(buttons_panel,
                    text = button.title(),
                    font = ('Dosis', 10,'bold'),
                    fg= 'white',
                    bg ='azure4',
                    bd = 1,
                    width = 9)
    created_buttons.append(button)
    button.grid(row=0,
                column= column)
    column += 1

created_buttons[0].config(command= total_calculation)
created_buttons[1].config(command= create_invoice)

#invoice area
invoice_text= Text(invoice_panel,
                   font= ('Dosis', 10,'bold'),
                   bd=1,
                   width= 42,
                   height= 10)
invoice_text.grid(row=0,
                  column=0)

#calculator
calculator_display = Entry(calculator_panel,
                           font= ('Dosis', 10,'bold'),
                           width = 32,
                           bd=1)
calculator_display.grid(row=0, column=0, columnspan=4)
calculator_buttons= ['7','8','9','+',
                     '4','5','6','-',
                     '1','2','3','x',
                     'CE','Delete','0','/']

stored_buttons = []
my_row = 1
my_column = 0
for button in calculator_buttons:
    button= Button(calculator_panel,
                   text=button.title(),
                   font=('Dosis', 10,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    stored_buttons.append(button)
    button.grid(row=my_row,
                column= my_column)
    if my_column==3:
        my_row+=1
    my_column +=1
    if my_column == 4:
        my_column = 0
stored_buttons[0].config(command=lambda: click_button('7'))
stored_buttons[1].config(command=lambda: click_button('8'))
stored_buttons[2].config(command=lambda: click_button('9'))
stored_buttons[3].config(command=lambda: click_button('+'))
stored_buttons[4].config(command=lambda: click_button('4'))
stored_buttons[5].config(command=lambda: click_button('5'))
stored_buttons[6].config(command=lambda: click_button('6'))
stored_buttons[7].config(command=lambda: click_button('-'))
stored_buttons[8].config(command=lambda: click_button('1'))
stored_buttons[9].config(command=lambda: click_button('2'))
stored_buttons[10].config(command=lambda: click_button('3'))
stored_buttons[11].config(command=lambda: click_button('*'))
stored_buttons[12].config(command=get_result)
stored_buttons[13].config(command=delete_all)
stored_buttons[14].config(command=lambda: click_button('0'))
stored_buttons[15].config(command=lambda: click_button('/'))













#Prevent window from closing
application.mainloop()