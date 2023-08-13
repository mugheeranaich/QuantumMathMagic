from tkinter import *
import time

root = Tk()
root.geometry("342x490")
root.maxsize(width=342, height=490)
def click(event):
    global  scvalue

    text= event.widget.cget("text")
    if text == "OFF":
        scvalue.set("BY BY")
        enter.update()
        time.sleep(0.5)
        scvalue.set("")
        enter.update()
    elif text == 'AC':
        scvalue.set('0')
        enter.update()
        time.sleep(0.5)
        scvalue.set('')
    elif text == '=':
        try:
            value = eval(scvalue.get().replace('x','*').replace("÷",'/'))
            scvalue.set(value)
            enter.update()

        except:
            scvalue.set('Math ERROR')
            enter.update()
            time.sleep(1)
            scvalue.set('')
    elif text == 'DEL':
        scvalue.set(scvalue.get()[:-1])
        enter.update()


    else:
        scvalue.set(scvalue.get()+text)

        enter.xview_moveto(1)
        enter.update()


scvalue = StringVar()
scvalue.set("")
enter = Entry(root,textvar=scvalue ,bg='black',fg='white',font='Helvetica 40 bold')




enter.pack(ipadx=8,fill = X,pady=0)
charcoal_gray = "#505050"
frame1 = Frame(root, bg="black")
frame1.pack(side=LEFT,fill=X)
buttonc= Button(frame1, text="AC", bg="dark gray", fg="black", font='Helvetica 40')
buttonc.grid(row=0, column=0)
buttonc.bind("<Button-1>",click)
button_ = Button(frame1, text="DEL", bg="dark gray", fg="black", font='Helvetica 25',pady=15)
button_.grid(row=0, column=1)
button_.bind("<Button-1>", click)
button_ = Button(frame1, text="%", bg="dark gray", fg="black", font='Helvetica 40')
button_.grid(row=0, column=2)
button_.bind("<Button-1>", click)
button_ = Button(frame1, text="÷", bg="orange", fg="white", font='Helvetica 40 bold')
button_.grid(row=0, column=3)
button_.bind("<Button-1>", click)
charcoal_gray = "#505050"
button7 = Button(frame1,text="7",bg= charcoal_gray,fg="white",font='Helvetica 40 bold')
button7.grid(row=1,column=0)
button7.bind("<Button-1>", click)
button8 = Button(frame1, text="8", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button8.grid(row=1,column=1 )
button8.bind("<Button-1>", click)
button9 = Button(frame1, text="9", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button9.grid(row=1, column=2)
button9.bind("<Button-1>", click)
buttonx = Button(frame1, text="x", bg="orange", fg="white", font='Helvetica 40 bold')
buttonx.grid(row=1, column=3)
buttonx.bind("<Button-1>", click)

button4 = Button(frame1, text="4", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button4.grid(row=2, column=0)
button4.bind("<Button-1>", click)
button5 = Button(frame1, text="5", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button5.grid(row=2, column=1)
button5.bind("<Button-1>", click)
button6 = Button(frame1, text="6", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button6.grid(row=2, column=2)
button6.bind("<Button-1>", click)
button__ = Button(frame1, text="-", bg="orange", fg="white", font='Helvetica 40 bold',pady=5,padx=20)
button__.grid(row=2, column=3)
button__.bind("<Button-1>", click)

button1 = Button(frame1, text="1", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button1.grid(row=3, column=0,)
button1.bind("<Button-1>", click)
button2 = Button(frame1, text="2", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button2.grid(row=3, column=1)
button2.bind("<Button-1>", click)
button3 = Button(frame1, text="3", bg=charcoal_gray, fg="white",font='Helvetica 40 bold')
button3.grid(row=3, column=2)
button3.bind("<Button-1>", click)
button0001 = Button(frame1, text="+", bg="orange", fg="white", font='Helvetica 40 bold',pady=15)
button0001.grid(row=3, column=3)
button0001.bind("<Button-1>", click)
button0 = Button(frame1, text="0", bg=charcoal_gray, fg="white", font='Helvetica 40 bold')
button0.grid(row=4, column=0)
button0.bind("<Button-1>", click)
button0 = Button(frame1, text="00", bg=charcoal_gray, fg="white", font='Helvetica 35 bold')
button0.grid(row=4, column=1, )
button0.bind("<Button-1>", click)
button01 = Button(frame1, text=".", bg=charcoal_gray, fg="white", font='Helvetica 40 bold',padx=20)
button01.grid(row=4, column=2)
button01.bind("<Button-1>", click)
button001 = Button(frame1, text="=", bg="orange", fg="white", font='Helvetica 40 bold')
button001.grid(row=4, column=3)
button001.bind("<Button-1>", click)





root.mainloop()
