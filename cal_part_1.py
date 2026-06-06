from tkinter import *
import ast
root=Tk()
pos=0
#adding text to the particular entry field
def get_number(num):
    global pos
    display.insert(pos,num)
    pos+=len(str(num))

#clear all button code
def clear_all():
    display.delete(0,END)

#backspace button
def undo():
    entire_expression1=display.get()
    if len(entire_expression1):
        new_string=entire_expression1[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"")

# eqaul to button functional
def calculate():
    entire_expression=display.get()
    try:
        node = ast.parse(entire_expression,mode="eval")
        result=eval(compile(node,'<string>','eval'))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
   
#above function replacement
"""def get_number(num):
    display.insert(END, str(num))"""

#input field
display=Entry(root)
display.grid(row=1,columnspan=6) #row 1 is this

#part 2
#opertations
#creating first operations buttons
operations1=["+","-","*","/","*3.14","%","(","**"]
counter1=0
for i in range(2,4):
    for j in range(0,4):
        button_text=operations1[counter1]
        button1=Button(root,text=operations1[counter1],width=4,height=2,command=lambda text1=button_text:get_number(text1))
        button1.grid(row=i,column=j)
        counter1+=1

#creating buttons numbers
numbers=[1,2,3,4,5,6,7,8,9]
counter2=0
for x in range(4,7):
    for y in range(3):
        button_text=numbers[counter2] # we are paasing button_text to get_number function
        button2=Button(root,text=button_text,width=4,height=2,command=lambda text1=button_text:get_number(text1))
        button2.grid(row=x,column=y)
        counter2+=1
# for button 0 below button 8
button1=Button(root,text="0",width=4,height=2,command=lambda :get_number("0"))
button1.grid(row=7,column=1)

#creating operations2
counter3=0
operations2=[")","**2","1/x"]
for k in range(4,7):
    for l in range(3,4):
        button_text=operations2[counter3]
        button3=Button(root,text=operations2[counter3],width=4,height=2,command=lambda text1=button_text:get_number(text1))
        button3.grid(row=k,column=l)
        counter3+=1

#creating operations3
counter4=0
operations3=["."]
for m in range(7,8):
    for n in range(0,1):
        if(n==1):
            continue
        button_text=operations3[counter4]
        button4=Button(root,text=operations3[counter4],width=4,height=2,command=lambda text1=button_text:get_number(text1))
        button4.grid(row=m,column=n)
        counter4+=1

#creating all clear and equal to button
Button(root,text="AC",width=4,height=2,command=clear_all).grid(row=7,column=2)
Button(root,text="=",width=4,height=2,command=calculate).grid(row=7,column=3)
#backspace button
Button(root,text="<-",width=4,height=2,command=undo).grid(row=2,column=4)
root.mainloop()
