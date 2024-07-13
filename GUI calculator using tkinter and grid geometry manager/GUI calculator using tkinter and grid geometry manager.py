from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)
def clear():
    result_label.config(text='')
def get_operator(op):
    global first_number,operator
    first_number=int(result_label['text'])
    operator=op
    result_label.config(text='')
def get_result():
    global first_number,second_number,operator
    
    second_number=int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number-second_number))
    elif operator == '*':
        result_label.config(text=str(round(first_number*second_number,3)))
    else:
        if second_number==0:
            result_label.config(text="Can't divide by zero")
        else:
            result_label.config(text=str(round(first_number/second_number,3)))
        
        
        
win=Tk()
win.title('Calculator')
win.geometry('325x500')
win.resizable(0,0) #basically x-direction me bhi 0 movement
#and y- direcgtion mein bhi 0 moment ; resizable(x,y)
#In other words, you can't change the size of calculator
#window by just dragging the GUI edges or or by clicking 
#at the maximize button.
win.configure(background='black')
win.iconbitmap('calc.ico')
#Till now, we learn how to make application using pack 
#geometry manager today we will use grid geometry manager.

#geometry manager is responsible where to place the UI 
#elements on the GUI screen.
result_label=Label(win,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))

btn7=Button(win,text='7',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8=Button(win,text='8',bg='#00a65a',fg='white',width=6,height=3, command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9=Button(win,text='9',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_add=Button(win,text='+',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))

btn4=Button(win,text='4',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5=Button(win,text='5',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6=Button(win,text='6',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_sub=Button(win,text='-',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))

btn1=Button(win,text='1',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2=Button(win,text='2',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3=Button(win,text='3',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_mul=Button(win,text='x',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))

btn_equal=Button(win,text='=',bg='#00a65a',fg='white',width=6,height=3,command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',14))

btn_clr=Button(win,text='C',bg='#00a65a',fg='white',width=6,height=3,command=clear)
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('verdana',14))

btn0=Button(win,text='0',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btn_div=Button(win,text='/',bg='#00a65a',fg='white',width=6,height=3,command=lambda:get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))

win.mainloop()
