from tkinter import *

root = Tk()
root.title("Retail Billing System ")
root.geometry('1270x684')
root.iconbitmap('ic\cart.ico')
# Title Label
headingLabel = Label(root, text='Retail Billing System',
                     font=('times new roman',30,'bold'),
                     bg='gray20',fg='gold',bd=10,relief=RIDGE)
headingLabel.pack(fill=X,pady=10)
"""
Customer Details Frame
"""
customer_Details_frame = LabelFrame(root,text='Customer Details',font=('times new roman', 15,'bold'),fg='gold',bg='gray20',bd=8,relief=GROOVE)
customer_Details_frame.pack(fill=X)

nameLabel = Label(customer_Details_frame, text='Name',font=('times new roman',15,'bold'),fg='white',bg='gray20')
nameLabel.grid(row=0, column=0,padx=20,pady=2)

nameEntry = Entry(customer_Details_frame, font=('arial',15),width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel = Label(customer_Details_frame, text='Phone Number',font=('times new roman',15,'bold'),fg='white',bg='gray20')
phoneLabel.grid(row=0, column=2,padx=20,pady=2)

phoneEntry = Entry(customer_Details_frame, font=('arial',15),width=18)
phoneEntry.grid(row=0,column=3,padx=8)

bill_numberLabel = Label(customer_Details_frame, text='Bill Number',font=('times new roman',15,'bold'),fg='white',bg='gray20')
bill_numberLabel.grid(row=0, column=4,padx=20,pady=2)

bill_numberEntry = Entry(customer_Details_frame, font=('arial',15),width=18)
bill_numberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_Details_frame, text="SEARCH",font=('arial',12,'bold'),bd=7, width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)

"""
Body Frames
"""


root.mainloop()