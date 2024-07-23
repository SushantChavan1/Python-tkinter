from tkinter import *

class Calculator:
    def __init__(self):
        self.root = Tk()
        
        #Creating the frame
        self.frame = Frame(self.root, width=600, height=400)
        self.frame.pack(padx=10, pady=10)
        
        #Creating the Lables
        label = Label(self.frame, text="This is a simple calculator",font=("Arial",20))
        lblnum1=Label(self.frame, text="Enter the 1 Num",font=("Arial",10))
        lblnum2=Label(self.frame, text="Enter the 2 Num",font=("Arial",10))
        res=Label(self.frame, text="Result",font=("Arial",10))

        #Creating the input boxes
        en1=Entry(self.frame)
        en2=Entry(self.frame)
        re=Entry(self.frame)

        #Creating buttons
        b1=Button(self.frame,text="Add",command=lambda:cal("+"))
        b2=Button(self.frame,text="Sub",command=lambda:cal("-"))
        b3=Button(self.frame,text="Multi",command=lambda:cal("*"))
        b4=Button(self.frame,text="Div",command=lambda:cal("/"))


        #Fixing into the frame by using the grid system
        label.grid(row=0,column=0)
        lblnum1.grid(row=1,column=0)
        en1.grid(row=1,column=1,columnspan=3)
        lblnum2.grid(row=2,column=0)
        en2.grid(row=2,column=1,columnspan=3)
        res.grid(row=3,column=0)
        re.grid(row=3,column=1,columnspan=3)
        b1.grid(row=5,column=0)
        b2.grid(row=5,column=1)
        b3.grid(row=5,column=2)
        b4.grid(row=5,column=3)

        #Assigning Events
        def cal(str):
            num1=int(en1.get())
            num2=int(en2.get())
            if(str=="+"):
                re.insert(END,num1+num2)
            elif(str=="-"):
                re.insert(END,num1-num2)
            elif(str=="*"):
                re.insert(END,num1*num2)
            else:
                re.insert(END,num1/num2)

        self.root.mainloop()

ob = Calculator()

