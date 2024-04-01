import tkinter
from tkinter import ttk
from tkinter import *


class Menu:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('800x200')

        self.setupItems()
        self.setupQuantities()

        self.main_window.mainloop()

    def setupItems(self):
        self.itemsFrame = Frame(self.main_window, padx=50)
        self.itemsLabel = Label(self.itemsFrame, text="Items", pady=2.5)
        self.chickenLabel = Label(self.itemsFrame, text="Chicken Sandwichs($5.00):", pady=2.5)
        self.fingersLabel = Label(self.itemsFrame, text="Chicken Fingers($4.00):", pady=2.5)
        self.orderButton = Button(self.itemsFrame, text="Place Order", pady=2.5)
        self.totalLabel = Label(self.itemsFrame, text="Total:", pady=2.5)

        self.itemsLabel.grid(column=0, row=0)
        self.chickenLabel.grid(column=0, row=1)
        self.fingersLabel.grid(column=0, row=2)
        self.orderButton.grid(column=0, row=3)
        self.totalLabel.grid(column=0, row=4)

        self.itemsFrame.grid(column=0, row=0)

    def setupQuantities(self):
        self.quantitiesFrame = Frame(self.main_window)

        self.quantitiesLabel = Label(self.quantitiesFrame, text="Quantity", pady=2.5)
        self.chickenEntry = tkinter.Text(self.quantitiesFrame, pady=2.5, width=3, height=0.5)
        self.fingersEntry = tkinter.Text(self.quantitiesFrame, pady=2.5, width=3, height=0.5)
        self.quitButton = tkinter.Button(self.quantitiesFrame, text="Quit", pady=2.5)

        self.totalCost = tkinter.StringVar()
        self.totalCost.set("$0.00")

        self.totalCostLabel = tkinter.Label(self.quantitiesFrame, textvariable=self.totalCost, pady=2.5)

        self.quantitiesLabel.grid(column=0, row=0)
        self.chickenEntry.grid(column=0, row=1)
        self.fingersEntry.grid(column=0, row=2)
        self.quitButton.grid(column=0, row=3)
        self.totalCostLabel.grid(column=0, row=4)

        self.quantitiesFrame.grid(column=1, row=0)

    def setupSauces(self):
        self.saucesFrame = Frame(self.main_window)

        self.saucesLabel = Label(self.saucesFrame, text = "Sauces $0.50")
        self.




menu = Menu()
