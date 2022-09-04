from tkinter import *
from tkinter import messagebox
import random
import time


# username= project
# password=123
# ======================function for login==================
def TheLogin():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("", "Please fill in the spaces, blank spaces are not entertained.")
    elif (uname == "project" and password == "123"):
        messagebox.showinfo("", "Login Success!")
        login.destroy()
    else:
        messagebox.showinfo("", "Incorrect Username and Password")


login = Tk()
login.title("Login")
login.geometry("400x400")
login['bg'] = 'wheat'
global e1
global e2

Label(login, text="Username", bg="wheat").place(x=10, y=10)
Label(login, text="Password", bg="wheat").place(x=10, y=40)

e1 = Entry(login)
e1.place(x=140, y=10)

e2 = Entry(login)
e2.place(x=140, y=40)
e2.config(show="*")

Button(login, fg="white", font=('candara', 12, 'bold'), command=TheLogin, text="Login", bg="sienna3", height=3,
       width=13).place(x=10, y=100)
login.mainloop()

root = Tk()
root.geometry("1020x720+0+0")
root.title("BILLING SYSTEM")
root['bg'] = 'wheat'
Label(root, bg="wheat", text='Laiba Khalid (20-CS-74)\n ').pack(side=TOP, pady=10)

Tops = Frame(root, bg="wheat", width=1600, height=100, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, bg="wheat", width=1500, height=1000, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, bg="wheat", width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

root.resizable(True, True)

# ===========the time================
localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, bg="wheat", font=('Britannic Bold', 30, 'bold'), text="BILLING SYSTEM", fg="Black", anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, bg="wheat", font=('Bahnschrift SemiBold', 20,), text=localtime, fg="steel blue", anchor=W)
lblinfo.grid(row=1, column=0)
lblinfo = Label(Tops, bg="wheat", font=('Bahnschrift SemiBold', 20, 'bold'),
                text="Please enter the amount of products in each box", fg="sienna", anchor='w')
lblinfo.grid(row=2, column=0)


def Ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)
    cof = float(Fries.get())
    colfries = float(Largefries.get())
    cob = float(Burger.get())
    cofi = float(Filet.get())
    cochee = float(Cheese_burger.get())
    codr = float(Drinks.get())
    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costoffilet = cofi * 50
    costofcheeseburger = cochee * 30
    costofdrinks = codr * 35
    costofmeal = "Rs.", str(
        '%.2f' % (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax = ((costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) * 0.33)
    Totalcost = (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)
    Ser_Charge = (
                (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) / 99)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()


def reset():
    name.set("")
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


# ---------------------------------------------------------------------------------------
name = StringVar()
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

lblname = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Customer Name", fg="brown", anchor='w')
lblname.grid(row=0, column=0)
txtname = Entry(f1, font=('Bahnschrift', 16, 'bold'), textvariable=name, bd=6, insertwidth=6, justify='right')
txtname.grid(row=0, column=1)

lblreference = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Order No.", fg="brown", anchor='w')
lblreference.grid(row=1, column=0)
txtreference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=6, insertwidth=6, justify='right')
txtreference.grid(row=1, column=1)

lblDrinks = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Drinks", fg="sienna", anchor='w')
lblDrinks.grid(row=2, column=0)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="tan",
                  justify='right')
txtDrinks.grid(row=2, column=1)

lblfries = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text=" French Fries ", fg="sienna", anchor='w')
lblfries.grid(row=3, column=0)
txtfries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="tan",
                 justify='right')
txtfries.grid(row=3, column=1)

lblLargefries = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Pizza ", fg="sienna", anchor='w')
lblLargefries.grid(row=4, column=0)
txtLargefries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Largefries, bd=6, insertwidth=4,
                      bg="tan", justify='right')
txtLargefries.grid(row=4, column=1)

lblburger = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Burger ", fg="sienna", anchor='w')
lblburger.grid(row=5, column=0)
txtburger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="tan",
                  justify='right')
txtburger.grid(row=5, column=1)

lblFilet = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Pasta ", fg="sienna", anchor='w')
lblFilet.grid(row=6, column=0)
txtFilet = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="tan",
                 justify='right')
txtFilet.grid(row=6, column=1)

lblCheese_burger = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Cheese burger", fg="sienna",
                         anchor='w')
lblCheese_burger.grid(row=7, column=0)
txtCheese_burger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4,
                         bg="tan", justify='right')
txtCheese_burger.grid(row=7, column=1)

# --------------------------------------------------------------------------------------

lblcost = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Cost", fg="black", anchor='w')
lblcost.grid(row=2, column=2)
txtcost = Entry(f1, font=('arial', 16, 'bold'), textvariable=cost, insertwidth=4, bg="white", justify='right')
txtcost.grid(row=2, column=3)

lblService_Charge = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Service Charge", fg="black",
                          bd=10, anchor='w')
lblService_Charge.grid(row=3, column=2)
txtService_Charge = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, insertwidth=4,
                          bg="white", justify='right')
txtService_Charge.grid(row=3, column=3)

lblTax = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Tax", fg="black", anchor='w')
lblTax.grid(row=4, column=2)
txtTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, insertwidth=4, bg="white", justify='right')
txtTax.grid(row=4, column=3)

lblSubtotal = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="Subtotal", fg="black", anchor='w')
lblSubtotal.grid(row=5, column=2)
txtSubtotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Subtotal, insertwidth=4, bg="white",
                    justify='right')
txtSubtotal.grid(row=5, column=3)

lblTotal = Label(f1, bg="wheat", font=('Bahnschrift', 16, 'bold'), text="TOTAL", fg="maroon", anchor='w')
lblTotal.grid(row=6, column=2)
txtTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, insertwidth=4, bg="wheat4", justify='right')
txtTotal.grid(row=6, column=3)

# -----------------------------------------buttons------------------------------------------

# calculate button
btnTotal = Button(f1, padx=16, pady=8, fg="white", font=('Bahnschrift', 16, 'bold'), width=10, text="CALCULATE",
                  bg="sienna3", command=Ref)
btnTotal.grid(row=15, column=1)
# reset button
btnreset = Button(f1, padx=16, pady=8, fg="white", font=('Bahnschrift', 16, 'bold'), width=10, text="RESET",
                  bg="sienna3", command=reset)
btnreset.grid(row=15, column=2)
# exit button
btnexit = Button(f1, padx=16, pady=8, fg="white", font=('Bahnschrift', 16, 'bold'), width=10, text="EXIT", bg="firebrick",
                 command=qexit)
btnexit.grid(row=15, column=3)


# price list window
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    roo['bg'] = 'wheat'
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="ITEMS", fg="black", bg="wheat", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="___", fg="white", bg="wheat", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="PRICE", fg="black", bg="wheat", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="French Fries", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="Pizza ", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="Burger ", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="Pasta ", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="Cheese Burger", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('Bahnschrift', 15, 'bold'), text="Drinks", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="sienna", bg="wheat", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()


# -----------------------------------------buttons------------------------------------------
# price list button
btnprice = Button(f1, padx=16, pady=8, fg="white", font=('Bahnschrift', 16, 'bold'), width=10, text="PRICE LIST",bg="sienna3", command=price)
btnprice.grid(row=14, column=0)
root.mainloop()
