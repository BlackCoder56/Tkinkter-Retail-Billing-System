from heapq import merge
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
productsFrame.pack(pady=5,fill=X)

# Cosmetics
cosmeticsFrame = LabelFrame(productsFrame,text='Cosmetics',font=('times new roman', 15, 'bold'), fg='gold', bg='gray20', bd=8, relief=GROOVE)
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
body_lotion_Entry.grid(row=5, column=1, padx=30,pady=10)

# Groceries
GroceriesFrame = LabelFrame(productsFrame,text='Groceries',font=('times new roman', 15, 'bold'), fg='gold', bg='gray20', bd=8, relief=GROOVE)
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
Tea_Entry.grid(row=5, column=1, padx=30,pady=10)


# Drinks
Drinks_Label = LabelFrame(productsFrame,text='Drinks',font=('times new roman', 15, 'bold'), fg='gold', bg='gray20', bd=8, relief=GROOVE)
Drinks_Label.grid(row=0,column=2)

Bushera_Label = Label(Drinks_Label, text='Bushera', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Bushera_Label.grid(row=0, column=0, padx=8,pady=10,sticky='w')
Bushera_Entry = Entry(Drinks_Label, font=('arial', 15), width=10,bd=5)
Bushera_Entry.grid(row=0, column=1, padx=8,pady=10)

Pepsi_Label = Label(Drinks_Label, text='Pepsi', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Pepsi_Label.grid(row=1, column=0, padx=8,pady=10,sticky='w')
Pepsi_Entry = Entry(Drinks_Label, font=('arial', 15), width=10,bd=5)
Pepsi_Entry.grid(row=1, column=1, padx=8,pady=10)

Sprite_Label = Label(Drinks_Label, text='Sprite', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Sprite_Label.grid(row=2, column=0, padx=8,pady=10,sticky='w')
Sprite_Entry = Entry(Drinks_Label, font=('arial', 15), width=10,bd=5)
Sprite_Entry.grid(row=2, column=1, padx=8,pady=10)

Drew_Label = Label(Drinks_Label, text='Drew', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Drew_Label.grid(row=3, column=0, padx=8,pady=10,sticky='w')
Drew_Entry = Entry(Drinks_Label, font=('arial', 15), width=10,bd=5)
Drew_Entry.grid(row=3, column=1, padx=8,pady=10)

fanta_Label = Label(Drinks_Label, text='Fanta', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
fanta_Label.grid(row=4, column=0, padx=8,pady=10,sticky='w')
fanta_Entry = Entry(Drinks_Label, font=('arial', 15), width=10,bd=5)
fanta_Entry.grid(row=4, column=1, padx=8,pady=10)

cock_Label = Label(Drinks_Label, text='Coca Cola', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
cock_Label.grid(row=5, column=0, padx=8,pady=10,sticky='w')
cock_Entry = Entry(Drinks_Label, font=('arial', 15), width=10,bd=5)
cock_Entry.grid(row=5, column=1, padx=30,pady=10)

# Bill Area
bill_Frame = Frame(productsFrame, bd=8,relief=GROOVE)
bill_Frame.grid(row=0,column=3,padx=10)

bill_Label = Label(bill_Frame,text='Bill Area',font=('times new roman', 15, 'bold'), fg='white',bg='gray20' )
bill_Label.pack(fill=X)

# Scrollbar
Scrollbarr = Scrollbar(bill_Frame, orient=VERTICAL)
Scrollbarr.pack(side=RIGHT,fill=Y)
textArea = Text(bill_Frame,height=19,width=37,yscrollcommand=Scrollbarr.set)
textArea.pack()
Scrollbarr.config(command=textArea.yview)

# Bill Menu
bill_menu_Frame = LabelFrame(root,text='Bill Menu',font=('times new roman', 15, 'bold'), fg='gold', bg='gray20', bd=8, relief=GROOVE)
bill_menu_Frame.pack(fill=X)

# first column
cosmetic_price = Label(bill_menu_Frame, text='Cosmetic Price', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
cosmetic_price.grid(row=0, column=0, padx=8,pady=5,sticky='w')
cosmetic_price_Entry = Entry(bill_menu_Frame, font=('arial', 10), width=20,bd=5)
cosmetic_price_Entry.grid(row=0, column=1)

grocery_price = Label(bill_menu_Frame, text='Grocery Price', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
grocery_price.grid(row=1, column=0, padx=8,pady=5,sticky='w')
grocery_price_Entry = Entry(bill_menu_Frame, font=('arial', 10), width=20,bd=5)
grocery_price_Entry.grid(row=1, column=1)

drink_price = Label(bill_menu_Frame, text='Drink Price', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
drink_price.grid(row=2, column=0, padx=8,pady=5,sticky='w')
drink_price_Entry = Entry(bill_menu_Frame, font=('arial', 10), width=20,bd=5)
drink_price_Entry.grid(row=2, column=1)

# second column
cosmetic_tax = Label(bill_menu_Frame, text='Cosmetic Tax', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
cosmetic_tax.grid(row=0, column=2, padx=20,pady=5,sticky='w')
cosmetic_tax_Entry = Entry(bill_menu_Frame, font=('arial', 10), width=20,bd=5)
cosmetic_tax_Entry.grid(row=0, column=3)

grocery_tax = Label(bill_menu_Frame, text='Grocery Tax', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
grocery_tax.grid(row=1, column=2, padx=20,pady=5,sticky='w')
grocery_tax_Entry = Entry(bill_menu_Frame, font=('arial', 10), width=20,bd=5)
grocery_tax_Entry.grid(row=1, column=3)

drink_tax = Label(bill_menu_Frame, text='Drink Price', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
drink_tax.grid(row=2, column=2, padx=20,pady=5,sticky='w')
drink_tax_Entry = Entry(bill_menu_Frame, font=('arial', 10), width=20,bd=5)
drink_tax_Entry.grid(row=2, column=3)

# Button Section
button_Frame = Frame(bill_menu_Frame,bd=8,relief=GROOVE,bg='white')
button_Frame.grid(row=0,column=4,rowspan=3,padx=10)

total_btn = Button(button_Frame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=8,relief=GROOVE,width=6)
total_btn.grid(row=0,column=0,pady=10,padx=15)

bill_btn = Button(button_Frame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=8,relief=GROOVE,width=6)
bill_btn.grid(row=0,column=1,pady=10,padx=15)


email_btn = Button(button_Frame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=8,relief=GROOVE,width=6)
email_btn.grid(row=0,column=2,pady=10,padx=15)

print_btn = Button(button_Frame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=8,relief=GROOVE,width=6)
print_btn.grid(row=0,column=3,pady=10,padx=15)

Clear_btn = Button(button_Frame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=8,relief=GROOVE,width=6)
Clear_btn.grid(row=0,column=4,pady=10,padx=15)


root.mainloop()
=========
root.geometry('1270x684')
root.iconbitmap('ic\cart.ico')
# Title Label
headingLabel = Label(root, text='Retail Billing System',
                     font=('times new roman',30,'bold'),
                     bg='gray20',fg='gold',bd=10,relief=GROOVE)
headingLabel.pack(fill=X)

root.mainloop()
>>>>>>>>> Temporary merge  2
