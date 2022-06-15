from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import os

# Functions :

def save(event=None):
    f_name=ent1.get()
    l_name=ent2.get()
    ID    =ent3.get()
    NID   =ent4.get()
    bth_y =ent5.get()
    m_s   =ent6.get()
    n_ch  =ent7.get()
    o     =ent8.get()
    is_user=False
    info='{},{},{},{},{},{},{},{},{}\n'.format(f_name,l_name,ID,NID,bth_y,m_s,n_ch,o,res)
    f=open('info1.txt',mode='r')
    emp=f.readlines()
    f.close()
    for i in emp:
        temp=i.strip('\n')
        temp=temp.split(',')
        if temp[2]==ID:
            is_user=True
    
    if is_user==True:
        messagebox.showerror('خطا','شماره پرسنلی در بانک اطلاعات وجود دارد')
    else:
        emp=emp+[info]
        f=open('info1.txt',mode='w')
        f.writelines(emp)
        f.close()
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
        ent7.delete(0,END)
        ent8.delete(0,END)
        p_img['file']='acc.png'
        messagebox.showinfo('information','info saved')
        
def save_sal(event=None):
    s_d=[]
    sal_is=False
    ID =ents0.get()
    sal=ents10.get()
    ez =ents11.get()
    mam=ents12.get()
    mas=ents13.get()
    off=ents14.get()
    salary='{},{},{},{},{},{}\n'.format(ID,sal,ez,mam,mas,off)
    
    f=open('sal1.txt',mode='r')
    sal_data=f.readlines()
    f.close()
    
    for i in sal_data:
        temp=i.strip('\n')
        temp=temp.split(',')
        if temp[0]==ID:
            sal_is=True
            i=salary
        s_d=s_d+[i]
    if sal_is == False:
        s_d.append(salary)
    
    f=open('sal1.txt',mode='w')
    f.writelines(s_d)
    f.close()
    
    ents1['state']='normal'
    ents2['state']='normal'
    ents3['state']='normal'
    ents4['state']='normal'
    ents5['state']='normal'
    ents6['state']='normal'
    ents7['state']='normal'
    ents8['state']='normal'
    ents0.delete(0,END)
    ents1.delete(0,END)
    ents2.delete(0,END)
    ents3.delete(0,END)
    ents4.delete(0,END)
    ents5.delete(0,END)
    ents6.delete(0,END)
    ents7.delete(0,END)
    ents8.delete(0,END)
    ents10.delete(0,END)
    ents11.delete(0,END)
    ents12.delete(0,END)
    ents13.delete(0,END)
    ents14.delete(0,END)
    aks_s['file']='acc.png'
    ents0.focus_set()
    messagebox.showinfo('information','info saved')
        
    
def save_ed(event=None):
    Data=[]
    f_name_n=entw1.get()
    l_name_n=entw2.get()
    ID      =entw0.get()
    NID_n   =entw4.get()
    bth_y_n =entw5.get()
    m_s_n   =entw6.get()
    n_ch_n  =entw7.get()
    o_n     =entw8.get()
    aks_e['file']='acc.png'
    
    f=open('info1.txt',mode='r')
    data=f.readlines()
    f.close()
    for i in data:
        temp=i.strip('\n')
        temp=temp.split(',')
        if temp[2]==ID:
            temp[0]=f_name_n
            temp[1]=l_name_n
            temp[3]=NID_n
            temp[4]=bth_y_n
            temp[5]=m_s_n
            temp[6]=n_ch_n
            temp[7]=o_n

        
        info_n='{},{},{},{},{},{},{},{},{}\n'.format(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8])
        Data=Data+[info_n]
    f=open('info1.txt',mode='w')
    f.writelines(Data)
    f.close()
    entw0.delete(0,END)
    entw1.delete(0,END)
    entw2.delete(0,END)
    entw3['state']='normal'
    entw3.delete(0,END)
    entw3['state']='disabled'
    entw4.delete(0,END)
    entw5.delete(0,END)
    entw6.delete(0,END)
    entw7.delete(0,END)
    entw8.delete(0,END)
    entw0.focus_set()
    messagebox.showinfo('information','info saved')

    
def sch_sal(event=None): # Search in salary window
    ents1['state']='normal'
    ents2['state']='normal'
    ents3['state']='normal'
    ents4['state']='normal'
    ents5['state']='normal'
    ents6['state']='normal'
    ents7['state']='normal'
    ents8['state']='normal'
    
    ents1.delete(0,END)
    ents2.delete(0,END)
    ents3.delete(0,END)
    ents4.delete(0,END)
    ents5.delete(0,END)
    ents6.delete(0,END)
    ents7.delete(0,END)
    ents8.delete(0,END)
    aks_s['file']='acc.png'
    s=ents0.get()
    f=open('info1.txt',mode='r')
    data=f.readlines()
    f.close()
    for i in data:
        temp=i.strip('\n')
        temp=temp.split(',')
        if temp[2]==s:
            ents1.insert(0,temp[0])
            ents2.insert(0,temp[1])
            ents3.insert(0,temp[2])
            ents4.insert(0,temp[3])
            ents5.insert(0,temp[4])
            ents6.insert(0,temp[5])
            ents7.insert(0,temp[6])
            ents8.insert(0,temp[7])
            aks_s['file']=temp[8]
            ents1['state']='disabled' 
            ents2['state']='disabled' 
            ents3['state']='disabled' 
            ents4['state']='disabled' 
            ents5['state']='disabled' 
            ents6['state']='disabled' 
            ents7['state']='disabled' 
            ents8['state']='disabled' 
    ents10.focus_set()

def search(event=None):
    entw1.delete(0,END)
    entw2.delete(0,END)
    entw3['state']='normal'
    entw3.delete(0,END)
    entw4.delete(0,END)
    entw5.delete(0,END)
    entw6.delete(0,END)
    entw7.delete(0,END)
    entw8.delete(0,END)
    s=entw0.get()
    f=open('info1.txt',mode='r')
    data=f.readlines()
    f.close()
    for i in data:
        temp=i.strip('\n')
        temp=temp.split(',')
        if temp[2]==s:
            entw1.insert(0,temp[0])
            entw2.insert(0,temp[1])
            entw3.insert(0,temp[2])
            entw4.insert(0,temp[3])
            entw5.insert(0,temp[4])
            entw6.insert(0,temp[5])
            entw7.insert(0,temp[6])
            entw8.insert(0,temp[7])
            aks_e['file']=temp[8]
            entw3['state']='disabled'
            
            
def sch_f(event=None):
    entf2['state']='normal'
    entf3['state']='normal'
    entf4['state']='normal'
    entf5['state']='normal'
    entf6['state']='normal'
    entf7['state']='normal'
    entf8['state']='normal'
    entf9['state']='normal'
    entf10['state']='normal'
    entf11['state']='normal'
    entf12['state']='normal'
    entf13['state']='normal'
    entf14['state']='normal'
    entf15['state']='normal'
    entf16['state']='normal'
    
    entf2.delete(0,END)
    entf3.delete(0,END)
    entf4.delete(0,END)
    entf5.delete(0,END)
    entf6.delete(0,END)
    entf7.delete(0,END)
    entf8.delete(0,END)
    entf9.delete(0,END)
    entf10.delete(0,END)
    entf11.delete(0,END)
    entf12.delete(0,END)
    entf13.delete(0,END)
    entf14.delete(0,END)
    entf15.delete(0,END)
    entf16.delete(0,END)
    aks_f['file']='acc.png'
    
    s=entf1.get()
    
    f=open('info1.txt',mode='r')
    data=f.readlines()
    f.close()
    a=open('sal1.txt',mode='r')
    salary=a.readlines()
    a.close()
    for i in data:
        temp=i.strip('\n')
        temp=temp.split(',')
        if temp[2]==s:
            entf2.insert(0,temp[0])
            entf3.insert(0,temp[1])
            entf4.insert(0,temp[2])
            entf5.insert(0,temp[3])
            entf6.insert(0,temp[7])
            aks_f['file']=temp[8]
            
    for i in salary:
        sal=i.strip('\n')
        sal=sal.split(',')
        if sal[0]==s:
            
            hogh=int(sal[1])
            hogh_f='{:,}'.format(hogh)
            entf7.insert(0,hogh_f)
            
            ezafe=int(sal[2])
            ezafe_f='{:,}'.format(ezafe)
            entf8.insert(0,ezafe_f)
            
            mask=int(sal[3])
            mask_f='{:,}'.format(mask)
            entf9.insert(0,mask_f)
            
            ma=int(sal[4])
            ma_f='{:,}'.format(ma)
            entf10.insert(0,ma_f)
            
            mor=int(sal[5])
            mor_f='{:,}'.format(mor)
            entf11.insert(0,mor_f)
            
            bime=500000
            bime_f='{:,}'.format(bime)
            entf12.insert(0,bime_f)
            
            maliat=int(sal[1])*0.09
            maliat_f='{:,}'.format(maliat)
            entf13.insert(0,maliat_f)
            
            jam=int(sal[1])+int(sal[2])+int(sal[3])+int(sal[4])
            jam_f='{:,}'.format(jam)
            entf14.insert(0,jam_f)
            
            kosorat=int(sal[5])+bime+maliat
            kosorat_f='{:,}'.format(kosorat)
            entf15.insert(0,kosorat_f)
            
            khales=jam-kosorat
            khales_f='{:,}'.format(khales)
            entf16.insert(0,khales_f)

    
    entf2['state']='disabled'
    entf3['state']='disabled'
    entf4['state']='disabled'
    entf5['state']='disabled'
    entf6['state']='disabled'
    entf7['state']='disabled'
    entf8['state']='disabled'
    entf9['state']='disabled'
    entf10['state']='disabled'
    entf11['state']='disabled'
    entf12['state']='disabled'
    entf13['state']='disabled'
    entf14['state']='disabled'
    entf15['state']='disabled'
    entf16['state']='disabled'
    
    
    
def new_info():
    win1.state('normal')
    win1.lift(win)
    
def op_fsh():
    win4.state('normal')
    win4.lift(win)
    
def op_sch(event=None):
    win2.state('normal')
    win2.lift(win)
    
def op_sal(event=None):
    win3.state('normal')
    win3.lift(win)

def op_img():
    global res
    filetypes=[('png image','png'),('jpg image','jpg')]
    res=filedialog.askopenfilename(title='personal image',filetypes=filetypes,initialdir=os.getcwd())
    p_img['file']=res
    
    
def op_main(event=None):
    user_pass=[]
    admin=False
    user=ent_u.get()
    password =ent_p.get()
    f=open('admin.txt',mode='r')
    userpass=f.readlines()
    f.close()
    for i in userpass:
        up=i.strip('\n')
        up=up.split(',')
        user_pass.append(up)
    for i in user_pass:
        if user==i[0] and password==i[1]:
            admin=True
    if admin==True:
        win.state('normal')
        win.lift(root)
        root.state('iconic')
    else:
        messagebox.showerror('Wrong entries','Username or password is wrong')
    
    
def f_we2(event=None):
    entw2.focus_set()
    
def f_we3(event=None):
    entw3.focus_set()
    
def f_we4(event=None):
    entw4.focus_set()

def f_we5(event=None):
    entw5.focus_set()
    
def f_we6(event=None):
    entw6.focus_set()

def f_we7(event=None):
    entw7.focus_set()

def f_we8(event=None):
    entw8.focus_set()
    
def f_e2(event=None):
    ent2.focus_set()
    
def f_e3(event=None):
    ent3.focus_set()
    
def f_e4(event=None):
    ent4.focus_set()

def f_e5(event=None):
    ent5.focus_set()
    
def f_e6(event=None):
    ent6.focus_set()

def f_e7(event=None):
    ent7.focus_set()

def f_e8(event=None):
    ent8.focus_set()
    
def f_s11(event=None):
    ents11.focus_set()

def f_s12(event=None):
    ents12.focus_set()

def f_s13(event=None):
    ents13.focus_set()

def f_s14(event=None):
    ents14.focus_set()


def f_p(event=None):
    ent_p.focus_set()

def sp(event=None):
    ent_p['show']=''

def dsp(event=None):
    ent_p['show']='*'
    
def wth1(event=None):
    win1.state('withdrawn')

def wth2(event=None):
    entw0.delete(0,END)
    entw1.delete(0,END)
    entw2.delete(0,END)
    entw3['state']='normal'
    entw3.delete(0,END)
    entw4.delete(0,END)
    entw5.delete(0,END)
    entw6.delete(0,END)
    entw7.delete(0,END)
    entw8.delete(0,END)
    aks_e['file']='acc.png'
    win2.state('withdrawn')
    
def wth3(event=None):
    win3.state('withdrawn')

def wth4(event=None):
    win4.state('withdrawn')
    
# Login window :________________________________________________________________________________________________

root = Tk()

root.geometry('270x105+600+400')
root.title('صفحه ورود')
root.iconbitmap(True, 'add.ico')
root.state('normal')
root.lift()

frm_up = Frame(root)
frm_up.pack(expand=TRUE,fill=BOTH)

lbl_u=Label(frm_up,text=': نام کاربري',relief='flat',anchor=E,width=15)
lbl_u.place(x=150,y=5)
    
ent_u=Entry(frm_up,relief='groove',justify=RIGHT)
ent_u.place(x=50,y=5)
ent_u.focus_set()
ent_u.bind('<Return>',f_p)
    

lbl_p=Label(frm_up,text=': رمز عبور',relief='flat',anchor=E,width=15)
lbl_p.place(x=150,y=40)
    
ent_p=Entry(frm_up,relief='groove',show='*',justify=RIGHT)
ent_p.place(x=50,y=40)
ent_p.bind('<Return>',op_main)


eye=PhotoImage(file='1.png')
lbl_s=Label(frm_up,image=eye,relief='flat')
lbl_s.place(x=5,y=40)
lbl_s.bind('<Button-1>',sp)
lbl_s.bind('<Leave>',dsp)


btn_l= Button(frm_up,text='ورود',command=op_main,width=10)
btn_l.place(x=80,y=70)   

# Main window :___________________________________________________________________________________________________

win = Toplevel()
win.state('withdrawn')
win.geometry('1170x630+150+50')
win.resizable(False,False)
win.title('حسابداری')

frm_1 = Frame(win)
frm_1.pack(expand=TRUE,fill=BOTH)

bg_img=PhotoImage(file='ac3.png')
lbl_1=Label(frm_1,image=bg_img)
lbl_1.place(x=0,y=0)

btn_1=Button(frm_1,text='ثبت اطلاعات جدید',width=15,bg='#F0F8FF',command=new_info)
btn_1.place(x=135,y=60)

btn_2=Button(frm_1,text='ویرایش اطلاعات',bg='#F0F8FF',width=15 ,command=op_sch  )
btn_2.place(x=135,y=110)
    
btn_3=Button(frm_1,text='محاسبه حقوق',bg='#F0F8FF',width=15,   command=op_sal  )
btn_3.place(x=135,y=160)

btn_4=Button(frm_1,text='مشاهده فیش حقوقی',bg='#F0F8FF',width=15,command=op_fsh )
btn_4.place(x=135,y=210)

    
    
    
# Information window :___________________________________________________________________________________________

win1 = Toplevel()

win1.geometry('250x350+600+200')
win1.state('withdrawn')
win1.title('اطلاعات')

frm = Frame(win1)
frm.pack(expand=TRUE,fill=BOTH)

lbl1=Label(frm,text=': نام',relief='flat',anchor=E,width=15)
lbl1.place(x=120,y=5)

ent1=Entry(frm,relief='groove',justify=RIGHT)
ent1.place(x=10,y=5)
ent1.focus_set()
ent1.bind('<Return>',f_e2)


lbl2=Label(frm,text=': نام خانوادگی',relief='flat',anchor=E,width=15)
lbl2.place(x=120,y=35)

ent2=Entry(frm,relief='groove',justify=RIGHT)
ent2.place(x=10,y=35)
ent2.bind('<Return>',f_e3)

lbl3=Label(frm,text=': شماره پرسنلی',relief='flat',anchor=E,width=15)
lbl3.place(x=120,y=65)

ent3=Entry(frm,relief='groove',justify=RIGHT)
ent3.place(x=10,y=65)
ent3.bind('<Return>',f_e4)

lbl4=Label(frm,text=': کد ملی',relief='flat',anchor=E,width=15)
lbl4.place(x=120,y=95)

ent4=Entry(frm,relief='groove',justify=RIGHT)
ent4.place(x=10,y=95)
ent4.bind('<Return>',f_e5)

lbl5=Label(frm,text=': تاریخ تولد',relief='flat',anchor=E,width=15)
lbl5.place(x=120,y=125)


ent5=Entry(frm,relief='groove',justify=RIGHT)
ent5.place(x=10,y=125)
ent5.bind('<Return>',f_e6)

lbl6=Label(frm,text=': وضعیت تاهل',relief='flat',anchor=E,width=15)
lbl6.place(x=120,y=155)


ent6=Entry(frm,relief='groove',justify=RIGHT)
ent6.place(x=10,y=155)
ent6.bind('<Return>',f_e7)

lbl7=Label(frm,text=': تعداد فرزند',relief='flat',anchor=E,width=15)
lbl7.place(x=120,y=185)


ent7=Entry(frm,relief='groove',justify=RIGHT)
ent7.place(x=10,y=185)
ent7.bind('<Return>',f_e8)

lbl8=Label(frm,text=': سمت',relief='flat',anchor=E,width=15)
lbl8.place(x=120,y=215)

ent8=Entry(frm,relief='groove',justify=RIGHT)
ent8.place(x=10,y=215)
ent8.bind('<Return>',save)



p_img=PhotoImage(file='acc.png')
lbl4=Label(frm,image=p_img)
lbl4.place(x=10,y=240)

btn1= Button(frm,text='عکس پرسنلی',command=op_img)
btn1.place(x=150,y=250)

btn2= Button(frm,text='ثبت اطلاعات',command=save)
btn2.place(x=150,y=300)

btn2= Button(frm,text='خروج',command=wth1)
btn2.place(x=10,y=300)


# Editing window :_________________________________________________________________________________________________

win2 =Toplevel(win)
win2.geometry('250x400+600+200')
win2.title('ویرایش اطلاعات')
win2.state('withdrawn')


frm3 = Frame(win2)
frm3.pack(expand=TRUE,fill=BOTH)

# Search parts :

lblw0=Label(frm3,text=': شماره پرسنلی',relief='flat',width=15,anchor=E)
lblw0.place(x=120,y=5)

entw0=Entry(frm3,relief='groove',justify=RIGHT)
entw0.place(x=10,y=5)
entw0.focus_set()
entw0.bind('<Return>',search)

btnw0=Button(frm3,text='جستجو',command=search,anchor=E)
btnw0.place(x=120,y=35)

# Results of search :

lblw1=Label(frm3,text=': نام',relief='flat',anchor=E,width=15)
lblw1.place(x=120,y=65)

entw1=Entry(frm3,relief='groove',justify=RIGHT)
entw1.place(x=10,y=65)
entw1.bind('<Return>',f_we2)


lblw2=Label(frm3,text=': نام خانوادگی',relief='flat',anchor=E,width=15)
lblw2.place(x=120,y=95)

entw2=Entry(frm3,relief='groove',justify=RIGHT)
entw2.place(x=10,y=95)
entw2.bind('<Return>',f_we3)

lblw3=Label(frm3,text=': شماره پرسنلی',relief='flat',anchor=E,width=15)
lblw3.place(x=120,y=125)

entw3=Entry(frm3,relief='groove',justify=RIGHT)
entw3.place(x=10,y=125)
entw3.bind('<Return>',f_we4)

lblw4=Label(frm3,text=': کد ملی',relief='flat',anchor=E,width=15)
lblw4.place(x=120,y=155)

entw4=Entry(frm3,relief='groove',justify=RIGHT)
entw4.place(x=10,y=155)
entw4.bind('<Return>',f_we5)

lblw5=Label(frm3,text=': تاریخ تولد',relief='flat',anchor=E,width=15)
lblw5.place(x=120,y=185)


entw5=Entry(frm3,relief='groove',justify=RIGHT)
entw5.place(x=10,y=185)
entw5.bind('<Return>',f_we6)

lblw6=Label(frm3,text=': وضعیت تاهل',relief='flat',anchor=E,width=15)
lblw6.place(x=120,y=215)


entw6=Entry(frm3,relief='groove',justify=RIGHT)
entw6.place(x=10,y=215)
entw6.bind('<Return>',f_we7)

lblw7=Label(frm3,text=': تعداد فرزند',relief='flat',anchor=E,width=15)
lblw7.place(x=120,y=245)


entw7=Entry(frm3,relief='groove',justify=RIGHT)
entw7.place(x=10,y=245)
entw7.bind('<Return>',f_we8)

lblw8=Label(frm3,text=': سمت',relief='flat',anchor=E,width=15)
lblw8.place(x=120,y=275)

entw8=Entry(frm3,relief='groove',justify=RIGHT)
entw8.place(x=10,y=275)
entw8.bind('<Return>',save_ed)

aks_e=PhotoImage(file='acc.png')
lblw9=Label(frm3,image=aks_e,relief='flat',anchor=E)
lblw9.place(x=80,y=305)

btnw1=Button(frm3,text='ثبت تغییرات',command=save_ed,anchor=E)
btnw1.place(x=120,y=355)

btnw2=Button(frm3,text='خروج',command=wth2,anchor=E)
btnw2.place(x=10,y=355)


# Salary window :========================================================================================================

win3 =Toplevel(win)
win3.geometry('500x360+500+150')
win3.title('اطلاعات حقوقی ')
win3.state('withdrawn')

frm2 =Frame(win3)
frm2.pack(expand=TRUE,fill=BOTH)

# Personal information :

lbls0=Label(frm2,text=': شماره پرسنلی',relief='flat',width=15,anchor=E)
lbls0.place(x=370,y=5)

ents0=Entry(frm2,relief='groove',justify=RIGHT)
ents0.place(x=260,y=5)
ents0.focus_set()
ents0.bind('<Return>',sch_sal)

btns0=Button(frm2,text='جستجو',command=sch_sal,anchor=E)
btns0.place(x=370,y=35)


lbls1=Label(frm2,text=': نام',relief='flat',anchor=E,width=15)
lbls1.place(x=370,y=65)

ents1=Entry(frm2,relief='groove',justify=RIGHT)
ents1.place(x=260,y=65)
ents1.bind('<Return>',f_we2)


lbls2=Label(frm2,text=': نام خانوادگی',relief='flat',anchor=E,width=15)
lbls2.place(x=370,y=95)

ents2=Entry(frm2,relief='groove',justify=RIGHT)
ents2.place(x=260,y=95)
ents2.bind('<Return>',f_we3)

lbls3=Label(frm2,text=': شماره پرسنلی',relief='flat',anchor=E,width=15)
lbls3.place(x=370,y=125)

ents3=Entry(frm2,relief='groove',justify=RIGHT)
ents3.place(x=260,y=125)
ents3.bind('<Return>',f_we4)

lbls4=Label(frm2,text=': کد ملی',relief='flat',anchor=E,width=15)
lbls4.place(x=370,y=155)

ents4=Entry(frm2,relief='groove',justify=RIGHT)
ents4.place(x=260,y=155)
ents4.bind('<Return>',f_we5)

lbls5=Label(frm2,text=': تاریخ تولد',relief='flat',anchor=E,width=15)
lbls5.place(x=370,y=185)


ents5=Entry(frm2,relief='groove',justify=RIGHT)
ents5.place(x=260,y=185)
ents5.bind('<Return>',f_we6)

lbls6=Label(frm2,text=': وضعیت تاهل',relief='flat',anchor=E,width=15)
lbls6.place(x=370,y=215)


ents6=Entry(frm2,relief='groove',justify=RIGHT)
ents6.place(x=260,y=215)
ents6.bind('<Return>',f_we7)

lbls7=Label(frm2,text=': تعداد فرزند',relief='flat',anchor=E,width=15)
lbls7.place(x=370,y=245)


ents7=Entry(frm2,relief='groove',justify=RIGHT)
ents7.place(x=260,y=245)
ents7.bind('<Return>',f_we8)

lbls8=Label(frm2,text=': سمت',relief='flat',anchor=E,width=15)
lbls8.place(x=370,y=275)

ents8=Entry(frm2,relief='groove',justify=RIGHT)
ents8.place(x=260,y=275)

aks_s=PhotoImage(file='acc.png')
lbls9=Label(frm2,image=aks_s,relief='flat',anchor=E)
lbls9.place(x=300,y=305)

# Salary calc :

lbls9=Label(frm2,text=': درآمدها',font='bold',relief='flat',anchor=E,width=15)
lbls9.place(x=40,y=5)

lbls10=Label(frm2,text=': حقوق پایه',relief='flat',anchor=E,width=15)
lbls10.place(x=120,y=35)

ents10=Entry(frm2,relief='groove',justify=RIGHT)
ents10.place(x=10,y=35)
ents10.bind('<Return>',f_s11)

lbls10=Label(frm2,text=': اضافه کاری',relief='flat',anchor=E,width=15)
lbls10.place(x=120,y=65)

ents11=Entry(frm2,relief='groove',justify=RIGHT)
ents11.place(x=10,y=65)
ents11.bind('<Return>',f_s12)

lbls11=Label(frm2,text=': حق مسکن',relief='flat',anchor=E,width=15)
lbls11.place(x=120,y=95)

ents12=Entry(frm2,relief='groove',justify=RIGHT)
ents12.place(x=10,y=95)
ents12.bind('<Return>',f_s13)

lbls11=Label(frm2,text=': حق ماموریت',relief='flat',anchor=E,width=15)
lbls11.place(x=120,y=125)

ents13=Entry(frm2,relief='groove',justify=RIGHT)
ents13.place(x=10,y=125)
ents13.bind('<Return>',f_s14)

lbls12=Label(frm2,text=': کسورات',font='bold',relief='flat',anchor=E,width=15)
lbls12.place(x=40,y=155)

lbls13=Label(frm2,text=': مرخصی ',relief='flat',anchor=E,width=15)
lbls13.place(x=120,y=185)

ents14=Entry(frm2,relief='groove',justify=RIGHT)
ents14.place(x=10,y=185)
ents14.bind('<Return>',save_sal)

btns1=Button(frm2,text='ثبت اطلاعات',command=save_sal,anchor=E)
btns1.place(x=40,y=215)

btns2=Button(frm2,text='خروج',command=wth3,anchor=E)
btns2.place(x=40,y=250)

# Salary check :==========================================================================================================

win4=Toplevel(win)
win4.geometry('1000x280+250+200')
win4.title('فیش حقوقی')
win4.state('withdrawn')

frm4=Frame(win4)
frm4.pack(expand=TRUE,fill=BOTH)


lblf1=Label(frm4,text=': کد پرسنلی',relief='flat',anchor=E,width=15)
lblf1.place(x=850,y=5)

entf1=Entry(frm4,relief='groove',justify=RIGHT)
entf1.place(x=750,y=5)
entf1.focus_set()
entf1.bind('<Return>',sch_f)

btnf1=Button(frm4,text='جست و جو',command=sch_f,anchor=E)
btnf1.place(x=780,y=40)

lblf2=Label(frm4,text=': نام',relief='flat',anchor=E,width=15)
lblf2.place(x=850,y=75)

entf2=Entry(frm4,relief='groove',justify=RIGHT)
entf2.place(x=750,y=75)

lblf3=Label(frm4,text=': نام خانوادگی',relief='flat',anchor=E,width=15)
lblf3.place(x=850,y=105)

entf3=Entry(frm4,relief='groove',justify=RIGHT)
entf3.place(x=750,y=105)

lblf4=Label(frm4,text=': کد پرسنلی',relief='flat',anchor=E,width=15)
lblf4.place(x=850,y=135)

entf4=Entry(frm4,relief='groove',justify=RIGHT)
entf4.place(x=750,y=135)

lblf5=Label(frm4,text=': کد ملی',relief='flat',anchor=E,width=15)
lblf5.place(x=850,y=165)

entf5=Entry(frm4,relief='groove',justify=RIGHT)
entf5.place(x=750,y=165)

lblf6=Label(frm4,text=': سمت',relief='flat',anchor=E,width=15)
lblf6.place(x=850,y=195)

entf6=Entry(frm4,relief='groove',justify=RIGHT)
entf6.place(x=750,y=195)

# Label 1 :----------

lfrm1=LabelFrame(frm4,text='حقوق و مزایا',width=270,height=150,font='bold')
lfrm1.place(x=400,y=5)

lblf7=Label(lfrm1,text=': حقوق پایه',relief='flat',anchor=E,width=15)
lblf7.place(x=120,y=5)

entf7=Entry(lfrm1,relief='groove',justify=RIGHT)
entf7.place(x=10,y=5)

lblf8=Label(lfrm1,text=': اضافه کاری',relief='flat',anchor=E,width=15)
lblf8.place(x=120,y=35)

entf8=Entry(lfrm1,relief='groove',justify=RIGHT)
entf8.place(x=10,y=35)

lblf9=Label(lfrm1,text=': حق مسکن',relief='flat',anchor=E,width=15)
lblf9.place(x=120,y=65)

entf9=Entry(lfrm1,relief='groove',justify=RIGHT)
entf9.place(x=10,y=65)

lblf10=Label(lfrm1,text=': حق ماموریت',relief='flat',anchor=E,width=15)
lblf10.place(x=120,y=95)

entf10=Entry(lfrm1,relief='groove',justify=RIGHT)
entf10.place(x=10,y=95)

# Label 2 :-----------


lfrm2=LabelFrame(frm4,text='کسورات',width=270,height=150,font='bold')
lfrm2.place(x=100,y=5)


lblf11=Label(lfrm2,text=': مرخصی',relief='flat',anchor=E,width=15)
lblf11.place(x=110,y=5)

entf11=Entry(lfrm2,relief='groove',justify=RIGHT)
entf11.place(x=10,y=5)

lblf12=Label(lfrm2,text=': حق بیمه',relief='flat',anchor=E,width=15)
lblf12.place(x=110,y=35)

entf12=Entry(lfrm2,relief='groove',justify=RIGHT)
entf12.place(x=10,y=35)

lblf13=Label(lfrm2,text=': مالیات ',relief='flat',anchor=E,width=15)
lblf13.place(x=110,y=65)

entf13=Entry(lfrm2,relief='groove',justify=RIGHT)
entf13.place(x=10,y=65)

# Bottom of the page :


lblf14=Label(frm4,text=': جمع مزایا',relief='flat',anchor=E,width=15)
lblf14.place(x=530,y=195)

entf14=Entry(frm4,relief='groove',justify=RIGHT)
entf14.place(x=430,y=195)

lblf15=Label(frm4,text=': جمع کسورات',relief='flat',anchor=E,width=15)
lblf15.place(x=230,y=195)

entf15=Entry(frm4,relief='groove',justify=RIGHT)
entf15.place(x=130,y=195)

##lblf16=Label(frm4,text=': خالص دریافتی',relief='flat',anchor=E,width=15)
##lblf16.place(x=150,y=195)
##
##entf16=Entry(frm4,relief='groove',justify=RIGHT)
##entf16.place(x=50,y=195)

lblf16=Label(frm4,text=': خالص دریافتی',relief='flat',anchor=E,width=15)
lblf16.place(x=400,y=240)

entf16=Entry(frm4,relief='groove',justify=RIGHT)
entf16.place(x=300,y=240)


btnf2=Button(frm4,text='خروج',command=wth4,anchor=E)
btnf2.place(x=50,y=240)

aks_f=PhotoImage(file='acc.png')
lblf18=Label(frm4,image=aks_f,relief='flat',anchor=E)
lblf18.place(x=10,y=10)


root.mainloop()
