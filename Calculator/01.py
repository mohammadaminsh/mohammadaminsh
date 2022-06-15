from math    import *
from tkinter import *
import tkinter.messagebox



# Functions :


def key_event(*args):
    if ent.get() == '0':
        ent.delete(0, END)
        
def btn_1():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'1')


def btn_2():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'2')
    
def btn_3():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'3')


def btn_4():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'4')

def btn_5():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'5')

def btn_6():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'6')

def btn_7():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'7')

def btn_8():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'8')

def btn_9():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'9')

def btn_0():
    if ent.get()=='0':
        ent.delete(0,END)
    pos=len(ent.get())
    ent.insert(pos,'0')


def btn_p():
    pos=len(ent.get())
    ent.insert(pos,'+')

def btn_m():
    pos=len(ent.get())
    ent.insert(pos,'-')

def btn_t():
    pos=len(ent.get())
    ent.insert(pos,'*')
    
def btn_d():
    pos=len(ent.get())
    ent.insert(pos,'/')
    
    
def btn_c():
    ent.delete(0,END)
    ent.insert(0,'0')
    
    
def btn_sin():
    try:
        ans=float(ent.get())
        if switch is True:
            ans=sin(radians(ans))
        else:
            ans=sin(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
        
def btn_cos():
    try:
        ans=float(ent.get())
        if switch is True:
            ans=cos(radians(ans))
        else:
            ans=cos(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
        
def btn_tan():
    try:
        ans=float(ent.get())
        if switch is True:
            ans=tan(radians(ans))
        else:
            ans=tan(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
        
def btn_asin():
    try:
        ans=float(ent.get())
        if switch is True:
            ans=degrees(asin(ans))
        else:
            ans=asin(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
def btn_acos():
    try:
        ans=float(ent.get())
        if switch is True:
            ans=degrees(acos(ans))
        else:
            ans=acos(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
        
def btn_atan():
    try:
        ans=float(ent.get())
        if switch is True:
            ans=degrees(atan(ans))
        else:
            ans=atan(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
        
def btn_pow():
    pos=len(ent.get())
    ent.insert(pos,'**')
    
def btn_lg():
    try:
        ans=float(ent.get())
        ans=log10(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
def btn_ln():
    try:
        ans=float(ent.get())
        ans=log(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
def btn_fac():
    try:
        ans=float(ent.get())
        ans=factorial(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
def btn_sqrt():
    try:
        ans=float(ent.get())
        ans=sqrt(ans)
        ent.delete(0,END)
        ent.insert(0,str(ans))
    except :
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")   
    
def btn_dot():
    pos=len(ent.get())
    ent.insert(pos,'.')
    
def btn_pi():
    if ent.get() == '0':
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, str(pi))
    
def btn_e():
    if ent.get() == '0':
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, str(e))
    
def btn_p1():
    pos = len(ent.get())
    ent.insert(pos, '(')

def btn_p2():
    pos = len(ent.get())
    ent.insert(pos, ')')
    
def btn_del():
    pos = len(ent.get())
    disp =ent.get()
    ent.delete(0, END)
    ent.insert(0, disp[0:pos-1])
        
def btn_d_r():
    global switch
    if switch is None:
        switch = True
        btn_rad['text'] = 'Deg'
    else:
        switch = None
        btn_rad['text'] = 'Rad'
        
def btn_eq(*args):
    try:
        ans = ent.get()
        ans = eval(ans)
        ent.delete(0, END)
        ent.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    
# Creating the window :
win = Tk()

win.title('scientific calculator by shenabi')
win.geometry('550x400+150+150')
win.attributes('-topmost',1)

switch=None # For rad/deg

# Operators and numbers Frames :

frm1 = Frame(win)
frm2 = Frame(win)
frm3 = Frame(win)
frm4 = Frame(win)

# Entry frame :

frm_ent=Frame(win)

# Setting the frames :

frm_ent.pack(expand=TRUE,fill=BOTH)
frm1.pack(expand=TRUE,fill=BOTH)
frm2.pack(expand=TRUE,fill=BOTH)
frm3.pack(expand=TRUE,fill=BOTH)
frm4.pack(expand=TRUE,fill=BOTH)

# Enabling the entry box :

ent = Entry (frm_ent,justify=RIGHT,bg="#abbab1",bd=0,font=('tahoma',20),relief='groove')
ent.focus_set()
ent.pack(side=LEFT,expand=TRUE,fill=BOTH)
ent.bind("<Return>", btn_eq)
ent.bind("<Escape>", btn_c)
ent.bind("<Key-1>", key_event)
ent.bind("<Key-2>", key_event)
ent.bind("<Key-3>", key_event)
ent.bind("<Key-4>", key_event)
ent.bind("<Key-5>", key_event)
ent.bind("<Key-6>", key_event)
ent.bind("<Key-7>", key_event)
ent.bind("<Key-8>", key_event)
ent.bind("<Key-9>", key_event)
ent.bind("<Key-0>", key_event)
ent.bind("<Key-.>", key_event)
ent.insert(0,'0')


# 1st line of operators & numbers :

btn_ln = Button(frm1,text='Ln',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_ln)
btn_ln.pack(side=LEFT,expand=TRUE,fill=BOTH)


btn_log = Button(frm1,text='Log',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_lg)
btn_log.pack(side=LEFT,expand=TRUE,fill=BOTH)


btn_sin = Button(frm1,text='sin',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_sin)
btn_sin.pack(side=LEFT,expand=TRUE,fill=BOTH)


btn_cos = Button(frm1,text='cos',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_cos)
btn_cos.pack(side=LEFT,expand=TRUE,fill=BOTH)


btn_tan = Button(frm1,text='tan',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_tan)
btn_tan.pack(side=LEFT,expand=TRUE,fill=BOTH)



btn_fact = Button(frm1,text='n!',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,padx=5,pady=5,command=btn_fac)
btn_fact.pack(side=LEFT,expand=TRUE,fill=BOTH)


btn_pi = Button(frm1,text='π',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,padx=5,pady=5,command=btn_pi)
btn_pi.pack(side=LEFT,expand=TRUE,fill=BOTH)

# 2nd line of operators & numbers :

btn_e = Button(frm2,text='e',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_e)
btn_e.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_sqrt = Button(frm2,text='√x',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_sqrt)
btn_sqrt.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_rsin = Button(frm2,text='sin-1',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_asin)
btn_rsin.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_rcos = Button(frm2,text='cos-1',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_acos)
btn_rcos.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_rtan = Button(frm2,text='tan-1',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_atan)
btn_rtan.pack(side=LEFT,expand=TRUE,fill=BOTH)


btn_xy = Button(frm2,text='x^y',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_pow)
btn_xy.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_rad = Button(frm2,text='rad',font='segoe 12',width=7,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_d_r)
btn_rad.pack(side=LEFT,expand=TRUE,fill=BOTH)

# 3rd line of operators & numbers :

btn_1 = Button(frm3,text='1',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_1)
btn_1.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_2 = Button(frm3,text='2',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_2)
btn_2.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_3 = Button(frm3,text='3',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_3)
btn_3.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_4 = Button(frm3,text='4',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_4)
btn_4.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_5 = Button(frm3,text='5',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_5)
btn_5.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_dot = Button(frm3,text='.',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_dot)
btn_dot.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_bs = Button(frm3,text='⌫',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_del)
btn_bs.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_c = Button(frm3,text='c',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_c)
btn_c.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_p1 = Button(frm3,text='(',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_p1)
btn_p1.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_p2 = Button(frm3,text=')',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_p2)
btn_p2.pack(side=LEFT,expand=TRUE,fill=BOTH)


# 4th line of operators & numbers :

btn_6 = Button(frm4,text='6',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_6)
btn_6.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_7 = Button(frm4,text='7',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_7)
btn_7.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_8 = Button(frm4,text='8',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_8)
btn_8.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_9 = Button(frm4,text='9',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_9)
btn_9.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_0 = Button(frm4,text='0',font='segoe 13',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_0)
btn_0.pack(side=LEFT,expand=TRUE,fill=BOTH)


btn_eq = Button(frm4,text='=',font='segoe 12',width=5,bg='#FF7D40',fg='white',bd=0,relief=GROOVE,command=btn_eq)
btn_eq.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_d = Button(frm4,text='/',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_d)
btn_d.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_t = Button(frm4,text='*',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_t)
btn_t.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_p = Button(frm4,text='+',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_p)
btn_p.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn_m = Button(frm4,text='-',font='segoe 12',width=5,bg='#333333',fg='white',bd=0,relief=GROOVE,command=btn_m)
btn_m.pack(side=LEFT,expand=TRUE,fill=BOTH)


win.mainloop()
