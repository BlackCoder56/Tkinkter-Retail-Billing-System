import os
import random
import smtplib
import tempfile
from tkinter import *
from tkinter import messagebox

# Creating new folder in case it doesn't exist
if not os.path.exists('Receipts'):
    os.mkdir('Receipts')

"""
CODE FOR FUNCTIONALITY PART
"""
bill_number = random.randint(100, 550)


# Receipt Function
def receipt():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Empty Field', 'Customer name and Contact Required')
    elif cosmetic_price_Entry.get() == 'Shs. 0' and grocery_price_Entry.get() == 'Shs. 0' and drink_price_Entry.get() == 'Shs. 0':
        messagebox.showerror('Empty Field', 'No Item is selected')
    elif cosmetic_tax_Entry.get() == 'Shs. 0.0' and grocery_tax_Entry.get() == 'Shs. 0.0' and drink_tax_Entry.get() == 'Shs. 0.0':
        messagebox.showerror('Empty Field', 'No Item is selected')
    elif cosmetic_price_Entry.get() == '' and grocery_price_Entry.get() == '' and drink_price_Entry.get() == '':
        messagebox.showerror('Empty Field', 'No Item is selected')
    elif cosmetic_tax_Entry.get() == '' and grocery_tax_Entry.get() == '' and drink_tax_Entry.get() == '':
        messagebox.showerror('Empty Field', 'No Item is selected')

    else:
        textArea.delete(1.0, END)
        textArea.insert(END, '_____________________________________')
        textArea.insert(END, '\n     ** Tax Invoice / Receipt **\n')
        textArea.insert(END, f'\nBill No: RCN{bill_number}')
        textArea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
        textArea.insert(END, f'\nCustomer Contact: {phoneEntry.get()}')
        textArea.insert(END, '\n=====================================')
        textArea.insert(END, ' \nProduct\t\tQTY\t\tTotal')
        textArea.insert(END, '\n=====================================')
        if bath_soap_value != 0:
            textArea.insert(END, f'\nBath Soap\t\t{bathsoapEntry.get()}\t\t{bath_soap_value}')
        if face_cream_value != 0:
            textArea.insert(END, f'\nFace Cream\t\t{facecreamEntry.get()}\t\t{int(face_cream_value)}')
        if face_wash_value != 0:
            textArea.insert(END, f'\nFace Wash\t\t{facewashEntry.get()}\t\t{int(face_wash_value)}')
        if hair_spray_value != 0:
            textArea.insert(END, f'\nHair Spray\t\t{hair_spray_Entry.get()}\t\t{int(hair_spray_value)}')
        if hair_gel_value != 0:
            textArea.insert(END, f'\nHair Gel\t\t{Hair_gel_Entry.get()}\t\t{int(hair_gel_value)}')
        if body_lotion_value != 0:
            textArea.insert(END, f'\nBody Lotion\t\t{body_lotion_Entry.get()}\t\t{int(body_lotion_value)}')
        if rice_value != 0:
            textArea.insert(END, f'\nRice\t\t{Rice_Entry.get()}\t\t{int(rice_value)}')
        if oil_value != 0:
            textArea.insert(END, f'\nOil    \t\t{Oil_Entry.get()}\t\t{int(oil_value)}')
        if avocado_value != 0:
            textArea.insert(END, f'\nAvocado\t\t{Avocado_Entry.get()}\t\t{int(avocado_value)}')
        if wheat_value != 0:
            textArea.insert(END, f'\nWheat\t\t{Wheat_Entry.get()}\t\t{int(wheat_value)}')
        if sugar_value != 0:
            textArea.insert(END, f'\nSugar\t\t{Sugar_Entry.get()}\t\t{int(sugar_value)}')
        if tea_value != 0:
            textArea.insert(END, f'\nTea    \t\t{Tea_Entry.get()}\t\t{int(tea_value)}')
        if bushera_value != 0:
            textArea.insert(END, f'\nBushera\t\t{Bushera_Entry.get()}\t\t{int(bushera_value)}')
        if pepsi_value != 0:
            textArea.insert(END, f'\nPepsi\t\t{Pepsi_Entry.get()}\t\t{int(pepsi_value)}')
        if sprite_value != 0:
            textArea.insert(END, f'\nSprite\t\t{Sprite_Entry.get()}\t\t{int(sprite_value)}')
        if drew_value != 0:
            textArea.insert(END, f'\nMtn Dew\t\t{Drew_Entry.get()}\t\t{int(drew_value)}')
        if fanta_value != 0:
            textArea.insert(END, f'\nFanta\t\t{fanta_Entry.get()}\t\t{int(fanta_value)}')
        if cock_value != 0:
            textArea.insert(END, f'\nCoca Cola\t\t{cock_Entry.get()}\t\t{int(cock_value)}')
        textArea.insert(END, '\n-------------------------------------')
        textArea.insert(END, f'\nNet Amount: \t{unit_total}')
        textArea.insert(END, f'\nTotal Tax:  \t{tax_total}')
        textArea.insert(END, f'\nTotal Bill: \t{grand_total}')
        textArea.insert(END, '\n_____________________________________')
        textArea.insert(END, '\n-------------------------------------')
        save_receipt()


# Funtion for Saving the Receipt
def save_receipt():
    global bill_number
    bill_no = f'RCN{bill_number}'
    result = messagebox.askyesno('Confirm', 'Do you want to safe the receipt?')
    if result:
        content = textArea.get(1.0, END)
        receipt_file = open(f'Receipts/ {bill_no}.txt', 'w')
        receipt_file.write(content)
        receipt_file.close()
        messagebox.showinfo("Success", f"Receipt {bill_no} has been saved successfully")
        bill_number = random.randint(100, 550)


def send_email():
    def sending_message():
        try:
            if sender_email_input.get() == '' or password_input.get() == '':
                messagebox.showerror('Error', 'Sender details missing!!..', parent=root1)
            elif customer_email_input.get() == '':
                messagebox.showerror('Error', 'Customer email address missing!!..', parent=root1)
            elif message_box_input.get(1.0, END) == '\n':
                messagebox.showerror('Error', 'Bill details missing!!..', parent=root1)
            else:
                message_object = smtplib.SMTP('smtp.gmail.com', 587)
                message_object.starttls()
                message_object.login(sender_email_input.get(), password_input.get())
                message_object.sendmail(sender_email_input.get(), customer_email_input.get(),
                                        message_box_input.get(1.0, END))
                message_object.quit()
                messagebox.showinfo('Success', f'Receipt has been successfully sent to {customer_email_input.get()}')
                root1.destroy()

        except:
            messagebox.showerror('External error', 'Something went wrong, try again please!', parent=root1)

    if textArea.get(1.0, END) == '\n':
        messagebox.showerror("Error", "No Bill to send")
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('Sending Receipt to email')
        root1.config(bg='gray10')
        root1.resizable(False, False)
        # UI design
        sender_frame = LabelFrame(root1, text="Sender's Details", font=('arial', 18, 'bold'), fg='gold', bg='gray10')
        sender_frame.grid(row=0, column=0, padx=5, pady=5)

        sender_email = Label(sender_frame, text='Email', font=('arial', 15, 'bold'), fg='white', bg='gray10')
        sender_email.grid(row=0, column=0, pady=10, padx=8, sticky='w')

        sender_email_input = Entry(sender_frame, font=('arial', 15, 'bold'), fg='black')
        sender_email_input.grid(row=0, column=1, padx=8)

        password = Label(sender_frame, text='Password', font=('arial', 15, 'bold'), fg='white', bg='gray10', )
        password.grid(row=1, column=0, pady=10, padx=8)

        password_input = Entry(sender_frame, font=('arial', 15, 'bold'), fg='black')
        password_input.grid(row=1, column=1)

        customer_frame = LabelFrame(root1, text="Customer's Details", font=('arial', 18, 'bold'), fg='gold',
                                    bg='gray10')
        customer_frame.grid(row=1, column=0, padx=5, pady=5)

        customer_email = Label(customer_frame, text='Email', font=('arial', 15, 'bold'), fg='white', bg='gray10')
        customer_email.grid(row=0, column=0, pady=10, padx=8, sticky='w')

        customer_email_input = Entry(customer_frame, font=('arial', 15, 'bold'), fg='black')
        customer_email_input.grid(row=0, column=1, padx=8)

        message_box = Label(customer_frame, text='Receipt:', font=('arial', 15, 'bold'), fg='white', bg='gray10')
        message_box.grid(row=1, column=0, pady=10, padx=8, sticky='w')

        # scroll = Scrollbar(customer_frame, orient=VERTICAL)
        # scroll.pack(side=RIGHT, fill=Y)
        message_box_input = Text(customer_frame, font=('arial', 15), fg='black', width=30, height=10)
        message_box_input.grid(row=2, column=0, columnspan=2)
        # scroll.config(command=message_box_input.yview)

        # adding data from receipt area to be sent
        message_box_input.delete(1.0, END)
        message_box_input.insert(END,
                                 textArea.get(1.0, END).replace('=', '').replace('-', '').replace('_', '').replace(
                                     '\t\t\t',
                                     '\t'))

        _frame = LabelFrame(root1, font=('arial', 18, 'bold'), fg='gold', bg='gray10')
        _frame.grid(row=2, column=0, pady=2)
        send_receipt_btn = Button(_frame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='blue', width=18,
                                  command=sending_message)
        send_receipt_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=60)

        root1.mainloop()


def print_receipt():
    if textArea.get(1.0, END) == '\n':
        messagebox.showerror('Empty Bill area', "Receipt area is empty!!")
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textArea.get(1.0, END))
        os.startfile(file, 'print')


# total  function
def total():
    global bath_soap_value, face_cream_value, face_wash_value, hair_spray_value, hair_gel_value, body_lotion_value
    global rice_value, oil_value, avocado_value, wheat_value, sugar_value, tea_value
    global bushera_value, pepsi_value, sprite_value, drew_value, fanta_value, cock_value
    global unit_total, tax_total, grand_total

    # Cosmetics Total and Taxes
    cosmetic_price_Entry.delete(0, END)
    cosmetic_tax_Entry.delete(0, END)
    bath_soap_value = int(bathsoapEntry.get()) * 3400
    face_cream_value = int(facecreamEntry.get()) * 4400
    face_wash_value = int(facewashEntry.get()) * 4000
    hair_spray_value = int(hair_spray_Entry.get()) * 3400
    hair_gel_value = int(Hair_gel_Entry.get()) * 3900
    body_lotion_value = int(body_lotion_Entry.get()) * 5100

    cosmetic_total = (
            bath_soap_value + face_cream_value + face_wash_value + hair_spray_value + hair_gel_value + body_lotion_value)

    cosmetic_price_Entry.insert(0, f"Shs. {cosmetic_total}")
    cosmetics_tax_value = (cosmetic_total * 0.15)/100
    cosmetic_tax_Entry.insert(0, f"Shs. {cosmetics_tax_value}")

    # Groceries Total and Taxes
    grocery_price_Entry.delete(0, END)
    grocery_tax_Entry.delete(0, END)
    rice_value = int(Rice_Entry.get()) * 5000
    oil_value = int(Oil_Entry.get()) * 5600
    avocado_value = int(Avocado_Entry.get()) * 4000
    wheat_value = int(Wheat_Entry.get()) * 7000
    sugar_value = int(Sugar_Entry.get()) * 6080
    tea_value = int(Tea_Entry.get()) * 2000

    groceries_total = (rice_value + oil_value + avocado_value + wheat_value + sugar_value + tea_value)
    grocery_price_Entry.insert(0, f"Shs. {groceries_total}")
    groceries_tax_value = float(groceries_total * 0.2) /100
    grocery_tax_Entry.insert(0, f"Shs. {groceries_tax_value}")

    # Drinks Total and Taxes
    drink_price_Entry.delete(0, END)
    drink_tax_Entry.delete(0, END)
    bushera_value = int(Bushera_Entry.get()) * 4800
    pepsi_value = int(Pepsi_Entry.get()) * 2000
    sprite_value = int(Sprite_Entry.get()) * 2000
    drew_value = int(Drew_Entry.get()) * 1500
    fanta_value = int(fanta_Entry.get()) * 2000
    cock_value = int(cock_Entry.get()) * 2000

    drinks_total = (bushera_value + pepsi_value + sprite_value + drew_value + fanta_value + cock_value)
    drink_price_Entry.insert(0, f"Shs. {drinks_total}")
    drinks_tax_value = float(drinks_total * 0.2) / 100
    drink_tax_Entry.insert(0, f"Shs. {drinks_tax_value}")

    unit_total = (cosmetic_total + groceries_total + drinks_total)
    tax_total = (cosmetics_tax_value + groceries_tax_value + drinks_tax_value)
    grand_total = (unit_total + tax_total)


# Clear or refresh
def clear():
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)

    bathsoapEntry.delete(0, END)
    bathsoapEntry.insert(0, "0")
    facecreamEntry.delete(0, END)
    facecreamEntry.insert(0, "0")
    facewashEntry.delete(0, END)
    facewashEntry.insert(0, "0")
    hair_spray_Entry.delete(0, END)
    hair_spray_Entry.insert(0, "0")
    Hair_gel_Entry.delete(0, END)
    Hair_gel_Entry.insert(0, "0")
    body_lotion_Entry.delete(0, END)
    body_lotion_Entry.insert(0, "0")
    Rice_Entry.delete(0, END)
    Rice_Entry.insert(0, "0")
    Oil_Entry.delete(0, END)
    Oil_Entry.insert(0, "0")
    Avocado_Entry.delete(0, END)
    Avocado_Entry.insert(0, "0")
    Wheat_Entry.delete(0, END)
    Wheat_Entry.insert(0, "0")
    Sugar_Entry.delete(0, END)
    Sugar_Entry.insert(0, "0")
    Tea_Entry.delete(0, END)
    Tea_Entry.insert(0, "0")
    Bushera_Entry.delete(0, END)
    Bushera_Entry.insert(0, "0")
    Pepsi_Entry.delete(0, END)
    Pepsi_Entry.insert(0, "0")
    Sprite_Entry.delete(0, END)
    Sprite_Entry.insert(0, "0")
    Drew_Entry.delete(0, END)
    Drew_Entry.insert(0, "0")
    fanta_Entry.delete(0, END)
    fanta_Entry.insert(0, "0")
    cock_Entry.delete(0, END)
    cock_Entry.insert(0, "0")

    cosmetic_price_Entry.delete(0, END)
    cosmetic_tax_Entry.delete(0, END)

    grocery_price_Entry.delete(0, END)
    grocery_tax_Entry.delete(0, END)

    drink_price_Entry.delete(0, END)
    drink_tax_Entry.delete(0, END)

    textArea.delete(1.0, END)

    nameEntry.focus()


"""
CODE FOR THE UI DESIGN
"""

root = Tk()
root.title("Retail Billing System ")

root.geometry('1270x684+-3+-4')
root.iconbitmap('ic\cart.ico')
# Title Label
headingLabel = Label(root, text='Suzanna Shop Billing System',
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
nameEntry.focus()
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
productsFrame.pack(pady=5, fill=X)

# Cosmetics
cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), fg='gold',
                            bg='gray20', bd=8, relief=GROOVE)
cosmeticsFrame.grid(row=0, column=0)

bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
bathsoapLabel.grid(row=0, column=0, padx=8, pady=10, sticky='w')
bathsoapEntry = Entry(cosmeticsFrame, font=('arial', 15), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, padx=8, pady=10)
bathsoapEntry.insert(0, "0")

facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
facecreamLabel.grid(row=1, column=0, padx=8, pady=10, sticky='w')
facecreamEntry = Entry(cosmeticsFrame, font=('arial', 15), width=10, bd=5)
facecreamEntry.grid(row=1, column=1, padx=8, pady=10)
facecreamEntry.insert(0, "0")

facewashLabel = Label(cosmeticsFrame, text='Face wash', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
facewashLabel.grid(row=2, column=0, padx=8, pady=10, sticky='w')
facewashEntry = Entry(cosmeticsFrame, font=('arial', 15), width=10, bd=5)
facewashEntry.grid(row=2, column=1, padx=8, pady=10)
facewashEntry.insert(0, "0")

hair_spray_Label = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), fg='white',
                         bg='gray20')
hair_spray_Label.grid(row=3, column=0, padx=8, pady=10, sticky='w')
hair_spray_Entry = Entry(cosmeticsFrame, font=('arial', 15), width=10, bd=5)
hair_spray_Entry.grid(row=3, column=1, padx=8, pady=10)
hair_spray_Entry.insert(0, "0")

Hair_gel_Label = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Hair_gel_Label.grid(row=4, column=0, padx=8, pady=10, sticky='w')
Hair_gel_Entry = Entry(cosmeticsFrame, font=('arial', 15), width=10, bd=5)
Hair_gel_Entry.grid(row=4, column=1, padx=8, pady=10)
Hair_gel_Entry.insert(0, "0")

body_lotion_Label = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), fg='white',
                          bg='gray20')
body_lotion_Label.grid(row=5, column=0, padx=8, pady=10, sticky='w')
body_lotion_Entry = Entry(cosmeticsFrame, font=('arial', 15), width=10, bd=5)
body_lotion_Entry.grid(row=5, column=1, padx=30, pady=10)
body_lotion_Entry.insert(0, "0")

# Groceries
GroceriesFrame = LabelFrame(productsFrame, text='Groceries', font=('times new roman', 15, 'bold'), fg='gold',
                            bg='gray20', bd=8, relief=GROOVE)
GroceriesFrame.grid(row=0, column=1)

Rice_Label = Label(GroceriesFrame, text='Rice', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Rice_Label.grid(row=0, column=0, padx=8, pady=10, sticky='w')
Rice_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10, bd=5)
Rice_Entry.grid(row=0, column=1, padx=8, pady=10)
Rice_Entry.insert(0, "0")

Oil_Label = Label(GroceriesFrame, text='Oil', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Oil_Label.grid(row=1, column=0, padx=8, pady=10, sticky='w')
Oil_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10, bd=5)
Oil_Entry.grid(row=1, column=1, padx=8, pady=10)
Oil_Entry.insert(0, "0")

Avocado_Label = Label(GroceriesFrame, text='Avocado', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Avocado_Label.grid(row=2, column=0, padx=8, pady=10, sticky='w')
Avocado_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10, bd=5)
Avocado_Entry.grid(row=2, column=1, padx=8, pady=10)
Avocado_Entry.insert(0, "0")

Wheat_Label = Label(GroceriesFrame, text='Wheat', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Wheat_Label.grid(row=3, column=0, padx=8, pady=10, sticky='w')
Wheat_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10, bd=5)
Wheat_Entry.grid(row=3, column=1, padx=8, pady=10)
Wheat_Entry.insert(0, "0")

Sugar_Label = Label(GroceriesFrame, text='Sugar', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Sugar_Label.grid(row=4, column=0, padx=8, pady=10, sticky='w')
Sugar_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10, bd=5)
Sugar_Entry.grid(row=4, column=1, padx=8, pady=10)
Sugar_Entry.insert(0, "0")

Tea_Label = Label(GroceriesFrame, text='Tea', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Tea_Label.grid(row=5, column=0, padx=8, pady=10, sticky='w')
Tea_Entry = Entry(GroceriesFrame, font=('arial', 15), width=10, bd=5)
Tea_Entry.grid(row=5, column=1, padx=30, pady=10)
Tea_Entry.insert(0, "0")

# Drinks
Drinks_Label = LabelFrame(productsFrame, text='Drinks', font=('times new roman', 15, 'bold'), fg='gold', bg='gray20',
                          bd=8, relief=GROOVE)
Drinks_Label.grid(row=0, column=2)

Bushera_Label = Label(Drinks_Label, text='Bushera', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Bushera_Label.grid(row=0, column=0, padx=8, pady=10, sticky='w')
Bushera_Entry = Entry(Drinks_Label, font=('arial', 15), width=10, bd=5)
Bushera_Entry.grid(row=0, column=1, padx=8, pady=10)
Bushera_Entry.insert(0, "0")

Pepsi_Label = Label(Drinks_Label, text='Pepsi', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Pepsi_Label.grid(row=1, column=0, padx=8, pady=10, sticky='w')
Pepsi_Entry = Entry(Drinks_Label, font=('arial', 15), width=10, bd=5)
Pepsi_Entry.grid(row=1, column=1, padx=8, pady=10)
Pepsi_Entry.insert(0, "0")

Sprite_Label = Label(Drinks_Label, text='Sprite', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Sprite_Label.grid(row=2, column=0, padx=8, pady=10, sticky='w')
Sprite_Entry = Entry(Drinks_Label, font=('arial', 15), width=10, bd=5)
Sprite_Entry.grid(row=2, column=1, padx=8, pady=10)
Sprite_Entry.insert(0, "0")

Drew_Label = Label(Drinks_Label, text='Drew', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
Drew_Label.grid(row=3, column=0, padx=8, pady=10, sticky='w')
Drew_Entry = Entry(Drinks_Label, font=('arial', 15), width=10, bd=5)
Drew_Entry.grid(row=3, column=1, padx=8, pady=10)
Drew_Entry.insert(0, "0")

fanta_Label = Label(Drinks_Label, text='Fanta', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
fanta_Label.grid(row=4, column=0, padx=8, pady=10, sticky='w')
fanta_Entry = Entry(Drinks_Label, font=('arial', 15), width=10, bd=5)
fanta_Entry.grid(row=4, column=1, padx=8, pady=10)
fanta_Entry.insert(0, "0")

cock_Label = Label(Drinks_Label, text='Coca Cola', font=('times new roman', 15, 'bold'), fg='white', bg='gray20')
cock_Label.grid(row=5, column=0, padx=8, pady=10, sticky='w')
cock_Entry = Entry(Drinks_Label, font=('arial', 15), width=10, bd=5)
cock_Entry.grid(row=5, column=1, padx=30, pady=10)
cock_Entry.insert(0, "0")

# Bill Area
bill_Frame = Frame(productsFrame, bd=8, relief=GROOVE)
bill_Frame.grid(row=0, column=3, padx=10)

bill_Label = Label(bill_Frame, text='**  Receipt Area  **', font=('times new roman', 15, 'bold'), fg='white',
                   bg='gray20')
bill_Label.pack(fill=X)

# Scrollbar
Scrollbarr = Scrollbar(bill_Frame, orient=VERTICAL)
Scrollbarr.pack(side=RIGHT, fill=Y)
textArea = Text(bill_Frame, height=19, width=37, yscrollcommand=Scrollbarr.set)
textArea.pack()
Scrollbarr.config(command=textArea.yview)

# Bill Menu
bill_menu_Frame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), fg='gold', bg='gray20', bd=8,
                             relief=GROOVE)
bill_menu_Frame.pack(fill=X)

# first column
cosmetic_price = Label(bill_menu_Frame, text='Cosmetic Price', font=('times new roman', 12, 'bold'), fg='white',
                       bg='gray20')
cosmetic_price.grid(row=0, column=0, padx=8, pady=5, sticky='w')
cosmetic_price_Entry = Entry(bill_menu_Frame, font=('arial', 10, 'bold'), width=20, bd=5)
cosmetic_price_Entry.grid(row=0, column=1)

grocery_price = Label(bill_menu_Frame, text='Grocery Price', font=('times new roman', 12, 'bold'), fg='white',
                      bg='gray20')
grocery_price.grid(row=1, column=0, padx=8, pady=5, sticky='w')
grocery_price_Entry = Entry(bill_menu_Frame, font=('arial', 10, 'bold'), width=20, bd=5)
grocery_price_Entry.grid(row=1, column=1)

drink_price = Label(bill_menu_Frame, text='Drink Price', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
drink_price.grid(row=2, column=0, padx=8, pady=5, sticky='w')
drink_price_Entry = Entry(bill_menu_Frame, font=('arial', 10, 'bold'), width=20, bd=5)
drink_price_Entry.grid(row=2, column=1)

# second column
cosmetic_tax = Label(bill_menu_Frame, text='Cosmetic Tax', font=('times new roman', 12, 'bold'), fg='white',
                     bg='gray20')
cosmetic_tax.grid(row=0, column=2, padx=20, pady=5, sticky='w')
cosmetic_tax_Entry = Entry(bill_menu_Frame, font=('arial', 10, 'bold'), fg='blue', width=20, bd=5)
cosmetic_tax_Entry.grid(row=0, column=3)

grocery_tax = Label(bill_menu_Frame, text='Grocery Tax', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
grocery_tax.grid(row=1, column=2, padx=20, pady=5, sticky='w')
grocery_tax_Entry = Entry(bill_menu_Frame, font=('arial', 10, 'bold'), fg='blue', width=20, bd=5)
grocery_tax_Entry.grid(row=1, column=3)

drink_tax = Label(bill_menu_Frame, text='Drink Price', font=('times new roman', 12, 'bold'), fg='white', bg='gray20')
drink_tax.grid(row=2, column=2, padx=20, pady=5, sticky='w')
drink_tax_Entry = Entry(bill_menu_Frame, font=('arial', 10, 'bold'), fg='blue', width=20, bd=5)
drink_tax_Entry.grid(row=2, column=3)

# Button Section
button_Frame = Frame(bill_menu_Frame, bd=8, relief=GROOVE, bg='white')
button_Frame.grid(row=0, column=4, rowspan=3, padx=10)

total_btn = Button(button_Frame, text='Total', font=('arial', 16, 'bold'), bg='green', command=total, fg='white', bd=8,
                   relief=GROOVE,
                   width=6)
total_btn.grid(row=0, column=0, pady=10, padx=15)

bill_btn = Button(button_Frame, text='Bill', font=('arial', 16, 'bold'), bg='blue', fg='white', bd=8, relief=GROOVE,
                  width=6, command=receipt)
bill_btn.grid(row=0, column=1, pady=10, padx=15)

email_btn = Button(button_Frame, text='Email', font=('arial', 16, 'bold'), bg='blue', fg='white', bd=8, relief=GROOVE,
                   width=6, command=send_email)
email_btn.grid(row=0, column=2, pady=10, padx=15)

print_btn = Button(button_Frame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=8, relief=GROOVE,
                   width=6, command=print_receipt)
print_btn.grid(row=0, column=3, pady=10, padx=15)

Clear_btn = Button(button_Frame, text='Clear', font=('arial', 16, 'bold'), bg='red', fg='white', bd=8, relief=GROOVE,
                   width=6, command=clear)
Clear_btn.grid(row=0, column=4, pady=10, padx=15)

root.mainloop()
# =========
root.geometry('1270x684')
root.iconbitmap('ic\cart.ico')
# Title Label
headingLabel = Label(root, text='Retail Billing System',
                     font=('times new roman', 30, 'bold'),
                     bg='gray20', fg='gold', bd=10, relief=GROOVE)
headingLabel.pack(fill=X)

root.mainloop()
# >>>>>>>>> Temporary merge  2
