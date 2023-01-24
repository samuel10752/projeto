from tkinter import*

root = Tk()

fr1 = Frame(root, background='black')
fr2 = Frame(root, background='red')

lb1_fr1 = Label(fr1, text='Label no Frame 1', font='28')
lb2_fr2 = Label(fr2, text='label no frame 2',font='28')

bt1_fr1 = Button(fr1,text='Bt no frame 1', font='28')
bt1_fr2 = Button(fr2,text='Bt no frame 2', font='28')

fr1.pack()
fr2.pack()

lb1_fr1.grid(row=0, column=0)
bt1_fr1.grid(row=1, column=1)
lb2_fr2.grid(row=0, column=0)
bt1_fr2.grid(row=1, column=1)

root.mainloop()