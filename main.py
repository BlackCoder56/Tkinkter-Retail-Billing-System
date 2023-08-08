from tkinter import *

root = Tk()
root.title("Retail Billing System ")
root.geometry('1270x684')
root.iconbitmap('ic\cart.ico')
# Title Label
headingLabel = Label(root, text='Retail Billing System',
                     font=('times new roman',30,'bold'),
                     bg='gray20',fg='gold',bd=10,relief=GROOVE)
headingLabel.pack(fill=X)

root.mainloop()