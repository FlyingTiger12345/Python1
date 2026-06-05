from tkinter import *
from datetime import datetime
import random


root = Tk()
root.title("reestaurant Managment System")
root.geometry('800x400')
root.configure(bg='beige')
frame1 = Frame(root,width = 500,height=300,relief =  SUNKEN ,  bg = 'beige',bd=4)
frame1.pack()
label1 = Label(frame1,font=("arial",18,'bold'), text = "Restaurant MAnagement System",bg="beige",fg = 'firebrick')

label1.grid(row = 1,column = 0,columnspan=4,padx=10,pady=10)

drink = StringVar()
pizza = StringVar()
burger = StringVar()
largeburger = StringVar()
fries = StringVar()




labeldrink= Label(frame1,text = "drinks",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labeldrink.grid(row = 3,column = 0,padx=10,pady=10)

entrydrink= Entry(frame1,textvariable = drink ,justify=RIGHT)
entrydrink.grid(row = 3,column=1,padx=10,pady=10)
entrydrink.insert(END,0)




labelpizza= Label(frame1,text = "Pizza",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labelpizza.grid(row = 4,column = 0,padx=10,pady=10)

entrypizza= Entry(frame1,textvariable = pizza ,justify=RIGHT)
entrypizza.grid(row = 4,column=1,padx=10,pady=10)
entrypizza.insert(END,0)



labelburger = Label(frame1,text = "Burger",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labelburger.grid(row = 5,column = 0,padx=10,pady=10)

entryburger= Entry(frame1,textvariable = burger ,justify=RIGHT)
entryburger.grid(row = 5,column=1,padx=10,pady=10)
entryburger.insert(END,0)






labellargerburger= Label(frame1,text = "LargeBurger",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labellargerburger.grid(row = 6,column = 0,padx=10,pady=10)

entrylargeburger= Entry(frame1,textvariable = largeburger ,justify=RIGHT)
entrylargeburger.grid(row = 6,column=1,padx=10,pady=10)
entrylargeburger.insert(END,0)


labelfries= Label(frame1,text = "fries",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labelfries.grid(row = 7,column = 0,padx=10,pady=10)

entryfries= Entry(frame1,textvariable = fries ,justify=RIGHT)
entryfries.grid(row = 7,column=1,padx=10,pady=10)
entryfries.insert(END,0)


labelorderno= Label(frame1,text = "orderno",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labelorderno.grid(row = 3,column = 2)
entryorderno= Entry(frame1)
entryorderno.grid(row = 3,column=3)

labelcost= Label(frame1,text = "Cost",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labelcost.grid(row = 4,column = 2)
entrycost= Entry(frame1)
entrycost.grid(row = 4,column=3)

labeltax= Label(frame1,text = "tax",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labeltax.grid(row = 5,column = 2)
entrytax= Entry(frame1)
entrytax.grid(row = 5,column=3)



labelservice= Label(frame1,text = "service",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labelservice.grid(row = 6,column = 2)
entryservice= Entry(frame1)
entryservice.grid(row = 6,column=3)


labeltotal= Label(frame1,text = "total",fg="firebrick",font=('Times,12,""bold'),bg="beige")
labeltotal.grid(row = 7,column = 2)
entrytotal= Entry(frame1)
entrytotal.grid(row = 7,column=3)




button1 = Button(frame1, text = "Price", fg = "beige", font= ('Times', 12, 'bold'), bg = "firebrick", padx=10 ,pady=10)
button1.grid(row=10, column = 0, padx=10, pady = 10)
button2 = Button(frame1, text = "Total", fg = "beige", font= ('Times', 12, 'bold'), bg = "firebrick", padx=10, pady=10)
button2.grid(row=10, column = 1, padx=10, pady = 10)
button3 = Button(frame1, text = "Reset", fg = "beige", font= ('Times', 12, 'bold'), bg ="firebrick", padx=10, pady=10)
button3.grid(row=10, column = 2,padx=10, pady = 10)
button4 = Button(frame1, text = "Exit", fg = "beige", font= ('Times', 12, 'bold'), bg = "firebrick", padx=10, pady=10)
button4.grid(row=10, column = 3,padx=10, pady = 10,)







root.mainloop()









