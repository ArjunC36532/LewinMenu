import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *


class Menu:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('1000x200')

        self.setupItems()
        self.setupQuantities()
        self.setupSauces()

        self.itemsFrame.grid(column=0, row=0)
        self.quantitiesFrame.grid(column=1, row=0)
        self.saucesFrame.grid(column=2, row=0)

        self.main_window.mainloop()

    def setupItems(self):
        self.itemsFrame = Frame(self.main_window, padx=50)
        self.itemsLabel = Label(self.itemsFrame, text="Items", pady=2.5)
        self.chickenLabel = Label(self.itemsFrame, text="Chicken Sandwichs($5.00):", pady=2.5)
        self.fingersLabel = Label(self.itemsFrame, text="Chicken Fingers($4.00):", pady=2.5)
        self.orderButton = Button(self.itemsFrame, text="Place Order", pady=2.5, command = self.calculateTotal)
        self.totalLabel = Label(self.itemsFrame, text="Total:", pady=2.5)

        self.itemsLabel.grid(column=0, row=0)
        self.chickenLabel.grid(column=0, row=1)
        self.fingersLabel.grid(column=0, row=2)
        self.orderButton.grid(column=0, row=3)
        self.totalLabel.grid(column=0, row=4)

    def setupQuantities(self):
        self.quantitiesFrame = Frame(self.main_window, padx = 100)

        self.quantitiesLabel = Label(self.quantitiesFrame, text="Quantity", pady=2.5)
        self.chickenEntry = tkinter.Text(self.quantitiesFrame, pady=2.5, width=3, height=0.5)
        self.fingersEntry = tkinter.Text(self.quantitiesFrame, pady=2.5, width=3, height=0.5)
        self.quitButton = tkinter.Button(self.quantitiesFrame, text="Quit", pady=2.5, command = self.quit)

        self.totalCost = tkinter.StringVar()
        self.totalCost.set("$0.00")

        self.totalCostLabel = tkinter.Label(self.quantitiesFrame, textvariable=self.totalCost, pady=2.5)

        self.quantitiesLabel.grid(column=0, row=0)
        self.chickenEntry.grid(column=0, row=1)
        self.fingersEntry.grid(column=0, row=2)
        self.quitButton.grid(column=0, row=3)
        self.totalCostLabel.grid(column=0, row=4)

    def setupSauces(self):
        self.saucesFrame = Frame(self.main_window)

        self.saucesLabel = Label(self.saucesFrame, text = "Sauces $0.50")
        self.arjunSauce = Label(self.saucesFrame, text = "Arjun Sauce")
        self.bbqSauce = Label(self.saucesFrame, text = "BBQ Sauce")
        self.hotHotHotSauce = Label(self.saucesFrame, text = "HOTHOTHOTHOT Sauce")
        self.regularSauce = Label(self.saucesFrame, text = "Regular Sauce")

        self.arjunSauceChecked = IntVar()
        self.bbqSauceChecked = IntVar()
        self.hothothotSauceChecked = IntVar()
        self.regularSauceChecked = IntVar()


        self.arjunSauceCheckBox = Checkbutton(self.saucesFrame, variable= self.arjunSauceChecked)
        self.bbqSauceCheckBox = Checkbutton(self.saucesFrame, variable = self.bbqSauceChecked)
        self.hotHotHotSauceCheckBox = Checkbutton(self.saucesFrame, variable = self.hothothotSauceChecked)
        self.regularSauceCheckBox = Checkbutton(self.saucesFrame, variable = self.regularSauceChecked)

        self.saucesLabel.grid(row = 0, column = 0)
        self.arjunSauceCheckBox.grid(row = 1, column = 0)
        self.bbqSauceCheckBox.grid(row = 2, column = 0)
        self.hotHotHotSauceCheckBox.grid(row = 3, column = 0)
        self.regularSauceCheckBox.grid(row = 4, column = 0)

        self.arjunSauce.grid(row = 1, column = 1)
        self.bbqSauce.grid(row = 2, column = 1)
        self.hotHotHotSauce.grid(row = 3, column = 1)
        self.regularSauce.grid(row = 4, column = 1)

    def calculateTotal(self):
      print("Hello world")



    def quit(self):
        self.main_window.quit()












menu = Menu()
