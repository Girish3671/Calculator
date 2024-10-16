
from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.geometry("570x600")
root.resizable(False,False)
root.configure(bg='#17161b')
equation=""
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
def show(value):
    global equation
    # if value=="7" and value=="6" and value=="5" and value=="4" and value=="3" and value=="2" and value=="1" and value=="0" and value=="8" and value=="9":
    #     equation+=int(value)
    equation+=value
    label_result.config(text=equation)
def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="Andha hai kya  ❤️de "
            equation=""
    label_result.config(text=result)
def clear_last():
    global equation
    equation=equation[:-1]
    label_result.config(text=equation)

label_result=Label(root,height=2,width=25,text=" ",font=("arial",30))
label_result.pack()
button1=Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#3697f5",fg="black",command=lambda : clear()).place(x=10,y=100)
button1=Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda : show('/')).place(x=150,y=100)
button1=Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda : show('%')).place(x=290,y=100)
button1=Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show('*')).place(x=430,y=100)

button1=Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda : show("7")).place(x=10,y=200)
button1=Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("8")).place(x=150,y=200)
button1=Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("9")).place(x=290,y=200)
button1=Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("-")).place(x=430,y=200)

button1=Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("4")).place(x=10,y=300)
button1=Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("5")).place(x=150,y=300)
button1=Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("6")).place(x=290,y=300)
button1=Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("+")).place(x=430,y=300)

button1=Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("3")).place(x=10,y=400)
button1=Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("2")).place(x=150,y=400)
button1=Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("1")).place(x=290,y=400)
button1=Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show("0")).place(x=10,y=500)

button1=Button(root,text="back",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :clear_last()).place(x=430,y=400)
button1=Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="#2a2d36",fg="white",command=lambda :show(".")).place(x=290,y=500)
button1=Button(root,text="=",width=5,height=1,font=("arial",30,"bold"),relief="raised",bd=1,bg="orange",fg="white",command=lambda :calculate()).place(x=430,y=500)
root.mainloop()