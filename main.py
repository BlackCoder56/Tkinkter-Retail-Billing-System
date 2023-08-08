from tkinter import *

root = Tk()
root.title("Retail Billing System ")
root.geometry('1270x684+-3+-4')
root.iconbitmap('ic\cart.ico')
# Title Label
headingLabel = Label(root, text='Retail Billing System',
                     font=('times new roman', 30, 'bold'),
                     bg='gray20', fg='gold', bd=10, relief=RIDGE)
headingLabel.pack(fill=X, pady=8)
"""
Customer Details Frame
"""
customer_Details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), fg='gold',
                                    bg='gray20', bd=8, relief=GROOVE)
customer_Details_frame.pack(fill=X)

nameLabel = Label(customer_Details_frame, text='Name', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
nameLabel.grid(row=0, column=0, padx=20, pady=2)

nameEntry = Entry(customer_Details_frame, font=('arial', 15), width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_Details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), fg='white',
                   bg='gray20')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_Details_frame, font=('arial', 15), width=18)
phoneEntry.grid(row=0, column=3, padx=8)

bill_numberLabel = Label(customer_Details_frame, text='Bill Number', font=('times new roman', 15, 'bold'), fg='white',
                         bg='gray20')
bill_numberLabel.grid(row=0, column=4, padx=20, pady=2)

bill_numberEntry = Entry(customer_Details_frame, font=('arial', 15), width=18)
bill_numberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_Details_frame, text="SEARCH", font=('arial', 12, 'bold'), bd=7, width=10)
searchButton.grid(row=0, column=6, padx=20, pady=8)

"""
Product Frames
"""
productsFrame = Frame(root)
productsFrame.pack(pady=5)

# Cosmetics
cosmeticsFrame = LabelFrame(productsFrame,text='Cosmetics',font=('times new roman', 15, 'bold'), fg='gold',
                                    bg='gray20', bd=8, relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
bathsoapLabel.grid(row=0, column=0, padx=8,pady=10,sticky='w')
bathsoapEntry = Entry(cosmeticsFrame, font=('arial', 15), width=10,bd=5)
bathsoapEntry.grid(row=0, column=1, padx=8,pady=10)

facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
facecreamLabel.grid(row=1, column=0, padx=8,pady=10,sticky='w')
facecreamEntry = Entry(cosmeticsFrame, font=('arial', 15), width=10,bd=5)
facecreamEntry.grid(row=1, column=1, padx=8,pady=10)

facewashLabel = Label(cosmeticsFrame, text='Face wash', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
facewashLabel.grid(row=2, column=0, padx=8,pady=10,sticky='w')
facewashEntry = Entry(cosmeticsFrame, font=('arial', 15), width=10,bd=5)
facewashEntry.grid(row=2, column=1, padx=8,pady=10)

hair_spray_Label = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
hair_spray_Label.grid(row=3, column=0, padx=8,pady=10,sticky='w')
hair_spray_Entry = Entry(cosmeticsFrame, font=('arial', 15), width=10,bd=5)
hair_spray_Entry.grid(row=3, column=1, padx=8,pady=10)

Hair_gel_Label = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Hair_gel_Label.grid(row=4, column=0, padx=8,pady=10,sticky='w')
Hair_gel_Entry = Entry(cosmeticsFrame, font=('arial', 15), width=10,bd=5)
Hair_gel_Entry.grid(row=4, column=1, padx=8,pady=10)

body_lotion_Label = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
body_lotion_Label.grid(row=5, column=0, padx=8,pady=10,sticky='w')
body_lotion_Entry = Entry(cosmeticsFrame, font=('arial', 15), width=10,bd=5)
body_lotion_Entry.grid(row=5, column=1, padx=8,pady=10)

# Groceries
GroceriesFrame = LabelFrame(productsFrame,text='Groceries',font=('times new roman', 15, 'bold'), fg='gold',
                                    bg='gray20', bd=8, relief=GROOVE)
GroceriesFrame.grid(row=0,column=1)

Rice_Label = Label(GroceriesFrame, text='Rice', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Rice_Label.grid(row=0, column=0, padx=8,pady=10,sticky='w')
Rice_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10,bd=5)
Rice_Entry.grid(row=0, column=1, padx=8,pady=10)

Oil_Label = Label(GroceriesFrame, text='Oil', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Oil_Label.grid(row=1, column=0, padx=8,pady=10,sticky='w')
Oil_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10,bd=5)
Oil_Entry.grid(row=1, column=1, padx=8,pady=10)

Avocado_Label = Label(GroceriesFrame, text='Avocado', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Avocado_Label.grid(row=2, column=0, padx=8,pady=10,sticky='w')
Avocado_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10,bd=5)
Avocado_Entry.grid(row=2, column=1, padx=8,pady=10)

Wheat_Label = Label(GroceriesFrame, text='Wheat', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Wheat_Label.grid(row=3, column=0, padx=8,pady=10,sticky='w')
Wheat_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10,bd=5)
Wheat_Entry.grid(row=3, column=1, padx=8,pady=10)

Sugar_Label = Label(GroceriesFrame, text='Sugar', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Sugar_Label.grid(row=4, column=0, padx=8,pady=10,sticky='w')
Sugar_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10,bd=5)
Sugar_Entry.grid(row=4, column=1, padx=8,pady=10)

Tea_Label = Label(GroceriesFrame, text='Tea', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Tea_Label.grid(row=5, column=0, padx=8,pady=10,sticky='w')
Tea_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10,bd=5)
Tea_Entry.grid(row=5, column=1, padx=8,pady=10)

root.mainloop()
