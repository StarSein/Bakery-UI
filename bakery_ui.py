from tkinter import ttk
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        mainframe = ttk.Frame(window, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

        self.num_sandwich = StringVar()
        sandwich_entry = ttk.Entry(mainframe, width=7, textvariable=self.num_sandwich)
        sandwich_entry.grid(column=2, row=1, sticky=(W, E))

        self.num_cake = StringVar()
        cake_entry = ttk.Entry(mainframe, width=7, textvariable=self.num_cake)
        cake_entry.grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="주문하기", command=self.send_order).grid(column=1, row=3, sticky=W)

        ttk.Label(mainframe, text="샌드위치 (5000원)").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="케이크 (20000원)").grid(column=1, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def send_order(self):
        try:
            val_sandwich = int(self.num_sandwich.get())
        except ValueError:
            val_sandwich = 0
        try:
            val_cake = int(self.num_cake.get())
        except ValueError:
            val_cake = 0

        order_text = ""
        if val_sandwich + val_cake:
            order_text += '{}: '.format(self.name)
            if val_sandwich > 0:
                order_text += '샌드위치 (5000원) %d개, ' % val_sandwich
            if val_cake > 0:
                order_text += '케이크 (20000원) %d개' % val_cake

        if order_text:
            self.bakeryView.add_order(order_text.rstrip(', '))


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
