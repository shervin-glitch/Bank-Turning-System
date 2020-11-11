from tkinter import *
from datetime import datetime

root=Tk()

def press(label):
    global counter , counter_list
    if counter_list:
        co[label]['textvariable'].set(counter_list.pop(0))

def get_date():
    dt=datetime.now()
    return dt.strftime("%d/%b/%Y")

def get_time():
    dt=datetime.now()
    return dt.strftime("%H:%M:%S")

def get_number():
    global counter,counter_list
    counter+=1
    counter_list.append(counter)
    co['date']['textvariable'].set("Date : {}".format(get_date()))
    co['time']['textvariable'].set("Time : {}".format(get_time()))
    co['counter']['textvariable'].set('Your Turn : {}'.format(counter))
    co['waiting']['textvariable'].set("waiting : {}".format(len(counter_list)))

counter=0
counter_list=list()

co={
    'turn':{
        'text':'Get a Number',
        'height':5,
        'width':20,
        'font':('Courier' , 13),
        'bg':'#27ae60',
        'padx':5
    },
    'cancel':{
        'text':'Exit',
        'height':5,
        'width':20,
        'font':('Courier' , 13),
        'bg':"#d8334a"
    },
    'op1':{
        'text':'Operator-1',
        'bg':'#ff793f',
        'width':13,
        'height':5
    },
    'op2':{
        'text':'Operator-2',
        'bg':'#ff793f',
        'width':13,
        'height':5
    },
    'op3':{
        'text':'Operator-3',
        'bg':'#ff793f',
        'width':13,
        'height':5
    },
    'lop1':{
        'textvariable':IntVar(),
        'width':5,
        'height':2,
        'font':("Times",20,'bold'),
        'bg':'#8cba98',
        'borderwidth':3,
        'relief':'sunken'
    },
    'lop2':{
        'textvariable':IntVar(),
        'width':5,
        'height':2,
        'font':("Times" , 20 , 'bold'),
        'bg':'#8cba98',
        'borderwidth':3,
        'relief':'sunken'
    },
    'lop3':{
        'textvariable':IntVar(),
        'width':5,
        'height':2,
        'font':("Times" , 20 , 'bold'),
        'bg':'#8cba98',
        'borderwidth':3,
        'relief':'sunken'
    },
    'date':{
        'textvariable':StringVar(),
        'font':("Courier" , 15 , 'bold'),
        'bg':'#d9fffe',
        'relief':'raised'
    },
    'time':{
        'textvariable':StringVar(),
        'font':("Courier" , 15 , 'bold'),
        'bg':'#d9fffe',
        'relief':'raised'
    },
    'counter':{
        'textvariable':StringVar(),
        'height':3,
        'font':("Courier" , 15 , 'bold'),
        'bg':'#d9fffe',
        'relief':'raised'
    },
    'waiting':{
        'textvariable':StringVar(),
        'font':("Courier" , 15 , 'bold'),
        'bg':'#d9fffe',
        'relief': "raised"
    },
}

root.title("Bank")
root.geometry("240x300")
root.resizable(0 , 0)
root.config(background = "LightBlue")

Button(root
       , command = get_number
       , cnf = co['turn'])\
    .grid(
    row = 0
    , column = 0
    , padx = 13
    , pady = 13)
Button(root
       , command= root.destroy
       , cnf = co['cancel'])\
    .grid(
    row = 1
    , column = 0
    , padx = 13
    , sticky = E+W)

operator=Toplevel()
operator.geometry('380x193')
operator.title("Bank Turning")
operator.config(background = "#f8c291")
operator.resizable(0 , 0)

Button(operator
       , command = lambda :press('lop1')
       , cnf = co['op1'])\
    .grid(
    row = 0
    , column = 0
    , padx = 13
    , pady = 13)
Label(operator
      , co['lop1'])\
    .grid(
    row = 1
    , column = 0)

Button(operator
       , command = lambda :press('lop2')
       , cnf = co['op2'])\
    .grid(
    row = 0
    , column = 1
    , padx = 13
    , pady = 13)
Label(operator
      , co['lop2'])\
    .grid(
    row = 1
    , column = 1)

Button(operator
       , command = lambda :press('lop3')
       , cnf = co['op3'])\
    .grid(
    row = 0
    , column = 2
    , padx = 13
    , pady = 13)
Label(operator
      , co['lop3'])\
    .grid(
    row = 1
    , column = 2)

customer = Toplevel()
customer.title("Customer Window")
customer.geometry('250x300')
customer.resizable(0 , 0)
customer.config(background = '#d9fffe')

Label(customer
      , cnf = co['counter'])\
    .grid(
    row = 0
    , column = 0
    , sticky = N+E+W+S)
Label(customer
      , cnf = co['waiting'])\
    .grid(
    row = 1
    , column = 0
    , sticky = N+E+W+S)
Label(customer
      , cnf = co['date'])\
    .grid(
    row = 2
    , column = 0
    , sticky = N+E+W+S)
Label(customer
      , cnf = co['time'])\
    .grid(
    row = 3
    , column = 0
    , sticky = N+E+W+S)

root.mainloop()