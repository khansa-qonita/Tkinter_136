import tkinter as tk
import tkinter.messagebox as msg

top=tk.Tk()
def helloCallBack(): 
    msg.showinfo ("Belajar GUI", "Assalamu'alaikum!")
CheckVar = tk.IntVar()
C=tk.Checkbutton(top, text="Gelar", variable= CheckVar, onvalue=1, offvalue=0, height=5, width=120)
C.pack()

L1=tk.Label(top, text=" Nama")
L1.pack(side=tk.LEFT)

E1=tk.Entry(top, bd=5)
E1.pack(side=tk.RIGHT)
                                   
w1=tk.Button(top, text= "Klik saya lagi!", command=helloCallBack)
w1.pack()

top.mainloop()

