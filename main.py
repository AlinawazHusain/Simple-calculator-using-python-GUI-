from tkinter import *
ans=""
def press(n):
	global ans
	ans = ans + str(n)
	label.config(text=ans)
def total(m,ans):
	t=str(eval(ans))
	label.config(text=t)

def setNew():
	global ans
	ans=''
	label.config(text=("answer"))


window=Tk()
window.title("Simple calculator")
window.config(bg='azure4')
label=Label(window,text="Answer",bg='antiquewhite3',fg='black',height=2,width=50)
label.pack(side="top")
frame=Frame(window)
frame.pack()

button1=Button(frame,text=9,height=5,width=10,bg='orange',fg='black',command=lambda :press(9))
button2=Button(frame,text=8,height=5,width=10,bg='orange',fg='black',command=lambda: press(8))
button3=Button(frame,text=7,height=5,width=10,bg='orange',fg='black',command=lambda: press(7))
button4=Button(frame,text='+',height=5,width=10,bg='orange',fg='black',command=lambda: press('+'))
button5=Button(frame,text=6,height=5,width=10,bg='orange',fg='black',command=lambda: press(6))
button6=Button(frame,text=5,height=5,width=10,bg='orange',fg='black',command=lambda: press(5))
button7=Button(frame,text=4,height=5,width=10,bg='orange',fg='black',command=lambda: press(4))
button8=Button(frame,text='-',height=5,width=10,bg='orange',fg='black',command=lambda: press('-'))
button9=Button(frame,text=3,height=5,width=10,bg='orange',fg='black',command=lambda: press(3))
button10=Button(frame,text=2,height=5,width=10,bg='orange',fg='black',command=lambda: press(2))
button11=Button(frame,text=1,height=5,width=10,bg='orange',fg='black',command=lambda: press(1))
button12=Button(frame,text='x',height=5,width=10,bg='orange',fg='black',command=lambda: press('*'))
button13=Button(frame,text='.',height=5,width=10,bg='orange',fg='black',command=lambda: press('.'))
button14=Button(frame,text=0,height=5,width=10,bg='orange',fg='black',command=lambda: press(0))
button15=Button(frame,text='=',height=5,width=10,bg='orange',fg='black',command=lambda:total('=',ans))
button16=Button(frame,text='/',height=5,width=10,bg='orange',fg='black',command=lambda: press('/'))



button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)
button4.grid(row=1,column=4)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=2,column=3)
button8.grid(row=2,column=4)
button9.grid(row=3,column=1)
button10.grid(row=3,column=2)
button11.grid(row=3,column=3)
button12.grid(row=3,column=4)
button13.grid(row=4,column=1)
button14.grid(row=4,column=2)
button15.grid(row=4,column=3)
button16.grid(row=4,column=4)

frame2=Frame(window)
frame2.pack(side="bottom")
reset=Button(frame2,text="RESET",height=5, width=50,bg='green', fg='white',command=lambda: setNew())
reset.pack()



window.mainloop()
