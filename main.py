import tkinter as tk
from PIL import ImageTk
import sqlite3

bg_colour = "#6495ed"

def clear_widgets(frame):
	for widget in frame.winfo_children():
		widget.destroy()

def load_frame1(): # Main Page
    for frame in (frame2,frame3,frame4):
        clear_widgets(frame)
    frame1.tkraise()
    frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file="extra/logo.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Button( #Button for Add Order
        frame1,
        text="Add new Order",
        bg = "#28393a",
        fg = "white",
        font = ("TkMenuFont", 14),
        cursor = "hand2",
        activebackground= "#badee2",
        activeforeground = "black",
        command = lambda:load_frame2()
            ).pack(pady = 10)

    tk.Button( # Button for Add Customer
        frame1,
        text="Add new Customer",
        bg = "#28393a",
        fg = "white",
        font = ("TkMenuFont", 14),
        cursor = "hand2",
        activebackground= "#badee2",
        activeforeground = "black",
        command = lambda:load_frame3()
            ).pack(pady = 10)

    tk.Button( # Button for Add Product
        frame1,
        text="Add new Product",
        bg = "#28393a",
        fg = "white",
        font = ("TkHeadingFont", 14),
        cursor = "hand2",
        activebackground= "#badee2",
        activeforeground = "black",
        command = lambda:load_frame4()
            ).pack(pady = 10)

def load_frame2(): # Add Order Page
    clear_widgets(frame1)
    frame2.tkraise()
    frame2.pack_propagate(False)

    tk.Label(
        frame2,
        text = 'Add Order',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 20)
        ).pack()

    tk.Label(
        frame2,
        text = 'Client',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    name = tk.Entry(
        frame2,
        bd = 5
        )
    name.pack()

    tk.Label(
        frame2,
        text = 'Details',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    details = tk.Text(
        frame2,
        width = 20,
        height = 10
        )
    details.pack()

    tk.Label(
        frame2,
        text = 'Date',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    date = tk.Entry(
        frame2,
        bd = 5
        )
    date.pack()

    tk.Button( #BACK Button
        frame2,
        text = 'BACK',
        font = ('TkHeadingFont', 16),
        bg = '#28393a',
        fg = 'white',
        cursor = 'hand2',
        activebackground = '#badee2',
        activeforeground = 'black',
        command = lambda:load_frame1()
        ).pack(side = tk.RIGHT)
    tk.Button( #Add to db Button
        frame2,
        text = 'ADD',
        font = ('TkHeadingFont', 16),
        bg = '#28393a',
        fg = 'white',
        cursor = 'hand2',
        activebackground = '#badee2',
        activeforeground = 'black',
        command = lambda:add_order(name.get(), details.get('1.0', 'end-1c'), date.get())
        ).pack(side = tk.RIGHT)

def add_order(name, details, date): # Adding the New Order in database
    connection = sqlite3.connect("extra/db.sqlite")
    cur = connection.cursor()

    cur.execute('SELECT Name, Price FROM Goods;')
    prices_list = cur.fetchall()

    cur.execute("SELECT * FROM Orders;")
    table_records = cur.fetchall()
    n = len(table_records)
    if n == 0:
    	id = 1
    else:
    	id = int(table_records[n - 1][0]) + 1

    cur.execute('''INSERT INTO Orders (ID, Client, Details, Date) VALUES (?, ?, ?, ?)''', (id, name, details, date))

    sum = 0.0
    for line in details.splitlines():
        req = line.split(' ')
        for product in prices_list:
            if product[0] == req[0]:
                try:
                    sum += int(req[1]) * int(product[1])
                except:
                    pass

    print(sum)

    connection.commit()

    connection.close()



def load_frame3(): # Add Customer Page
    clear_widgets(frame1)
    frame3.tkraise()
    frame3.pack_propagate(False)

    tk.Label(
        frame3,
        text = 'Add Customer',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 20)
        ).pack()

    tk.Label(
        frame3,
        text = 'Name',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    name = tk.Entry(
        frame3,
        bd = 5
        )
    name.pack()

    tk.Label(
        frame3,
        text = 'Address Line 1',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    add1 = tk.Entry(
        frame3,
        bd = 5
        )
    add1.pack()

    tk.Label(
        frame3,
        text = 'Address Line 2',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    add2 = tk.Entry(
        frame3,
        bd = 5
        )
    add2.pack()

    tk.Label(
        frame3,
        text = 'Tax Identification Number(ro: CUI)',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    cui = tk.Entry(
        frame3,
        bd = 5
        )
    cui.pack()

    tk.Label(
        frame3,
        text = 'Registration Number',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    number = tk.Entry(
        frame3,
        bd = 5
        )
    number.pack()

    tk.Button( #BACK Button
        frame3,
        text = 'BACK',
        font = ('TkHeadingFont', 16),
        bg = '#28393a',
        fg = 'white',
        cursor = 'hand2',
        activebackground = '#badee2',
        activeforeground = 'black',
        command = lambda:load_frame1()
        ).pack(side = tk.RIGHT)
    tk.Button( #Add to db Button
        frame3,
        text = 'ADD',
        font = ('TkHeadingFont', 16),
        bg = '#28393a',
        fg = 'white',
        cursor = 'hand2',
        activebackground = '#badee2',
        activeforeground = 'black',
        command = lambda:add_customer(name.get(), add1.get(), add2.get(), cui.get(), number.get())
        ).pack(side = tk.RIGHT)

def add_customer(name, add1, add2, cui, number): # Does the update on database for New Customer
    connection = sqlite3.connect("extra/db.sqlite")
    cur = connection.cursor()

    cur.execute("SELECT * FROM Customer;")
    table_records = cur.fetchall()
    n = len(table_records)
    if n == 0:
    	id = 1
    else:
    	id = int(table_records[n - 1][0]) + 1

    details = add1 + '\n' + add2 + '\n' + cui + '\n' + number

    cur.execute('''INSERT INTO Customer (ID, Name, Address) VALUES (?, ?, ?)''', (id, name, details))

    connection.commit()

    connection.close()


def load_frame4(): #Add Product Page
    clear_widgets(frame1)
    frame4.tkraise()
    frame4.pack_propagate(False)

    tk.Label(
        frame4,
        text = 'Add Product',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 20)
        ).pack()

    tk.Label(
        frame4,
        text = 'Code',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    code = tk.Entry(
        frame4,
        bd = 5
        )
    code.pack()

    tk.Label(
        frame4,
        text = 'Name',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    name = tk.Entry(
        frame4,
        bd = 5
        )
    name.pack()

    tk.Label(
        frame4,
        text = 'Price',
        bg = bg_colour,
        fg = 'white',
        font = ('TkHeadingFont', 14)
        ).pack()
    price = tk.Entry(
        frame4,
        bd = 5
        )
    price.pack()

    tk.Button( #BACK Button
        frame4,
        text = 'BACK',
        font = ('TkHeadingFont', 16),
        bg = '#28393a',
        fg = 'white',
        cursor = 'hand2',
        activebackground = '#badee2',
        activeforeground = 'black',
        command = lambda:load_frame1()
        ).pack(side = tk.RIGHT)
    tk.Button( #Add to db Button
        frame4,
        text = 'ADD',
        font = ('TkHeadingFont', 16),
        bg = '#28393a',
        fg = 'white',
        cursor = 'hand2',
        activebackground = '#badee2',
        activeforeground = 'black',
        command = lambda:add_product(code.get(), name.get(), int(price.get()))
        ).pack(side = tk.RIGHT)

def add_product(code, name, price): #Does the update on database for New Product

    # connect an sqlite database
    connection = sqlite3.connect("extra/db.sqlite")
    cur = connection.cursor()

    cur.execute("SELECT * FROM Goods;")
    table_records = cur.fetchall()
    n = len(table_records)
    if n == 0:
    	id = 1
    else:
    	id = int(table_records[n - 1][0]) + 1

    cur.execute('''INSERT INTO Goods (ID, Code, Name, Price) VALUES (?, ?, ?, ?)''', (id, code, name, price))

    connection.commit()

    connection.close()


root = tk.Tk() #Initializing the application
root.title('INVOPRO')
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour) # main page
frame2 = tk.Frame(root, bg=bg_colour) # add Order
frame3 = tk.Frame(root, bg=bg_colour) # add Customer
frame4 = tk.Frame(root, bg=bg_colour) # add Product

for frame in (frame1, frame2, frame3, frame4):
	frame.grid(row=0, column=0, sticky="nesw")

load_frame1() # opens the main page

root.mainloop()
