from tkinter import *
import math
win=Tk()
win.geometry('600x600')
win.title('smart calculator')
win.resizable(width=False,height=False)
win.config(bg='cyan')

def power(a,b):
    return math.pow(a,b)

def log(a,b):
    return math.log(a,b) #b is base of log

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def mod(a,b):
    return a%b

def Lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1
    # return math.lcm(a,b)

def Hcf(a,b):
    h = a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1
     # return ( (a*b) / (math.lcm(a,b)) )


operations={'ADD':add,'ADDITION':add,'SUM':add,
            'SUB':sub,'SUBSTRACTION':sub,'MINUS':sub,
            'DIVISION':div,'DIV':div,'DIVIDE':div,
            'MULTIPLICATION':mul,'MULTIPLY':mul,'INTO':mul,'MUL':mul,
            'MODULOUS':mod,'MOD':mod,'REMAINDER':mod,
            'LCM':Lcm,'HCF':Hcf,
            'POWER':power,'POW':power,
            'LOG':log,'LOGARITHM':log}

def extract_number(text):
    l=[]
    for n in text.split(' '):
        try:
            l.append(float(n))
        except ValueError:
            pass
    return l


def calculate():
    word=Urtext.get()
    for text in word.split(' '):
        if text.upper() in operations.keys():
            try:
                l=extract_number(word)
                result=operations[text.upper()](l[0],l[1])
                lb.delete(0,END)
                lb.insert(END,result)
            except:
                lb.delete(0,END)
                lb.insert(END,'something went wrong please try again')
            finally:
                break
        elif text.upper() not in operations.keys():
                lb.delete(0,END)
                lb.insert(END,'something went wrong please try again')



l=Label(win,width=40,height=3,relief='raised',text='HEY, I AM SMART CALCULATOR',font='arial 10 bold',fg='red')
l.place(x=150,y=30)
l=Label(win,width=30,height=3,relief='raised',text='MY NAME IS SHIRO',font='arial 10',bg='white')
l.place(x=180,y=100)
l=Label(win,width=30,height=3,relief='raised',text='what can i help you? \n (+ , - , * , / , % , log , lcm , hcf , power)',font='arial 10',bg='white')
l.place(x=180,y=300)

Urtext=StringVar()
e=Entry(win,width=50,font='arial 13',fg='green',textvariable=Urtext)
e.place(x=90,y=370)

b=Button(win,command=calculate,text='Calculate this',padx=5,pady=3,bg='violet')
b.place(x=250,y=400)

lb=Listbox(win,width=50,height=5,fg='red')
lb.place(x=150,y=440)

win.mainloop()