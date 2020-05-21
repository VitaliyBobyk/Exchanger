from tkinter import *
from tkinter import ttk
import requests

root = Tk()
root.resizable(width=False, height=False)
root.geometry('290x300')
root.title('Hello!')
root['bg'] = 'white'

PAGE = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()


class Data:
    def currency(self):
        try:
            want_combo_value = combobox_want.get()
            ent_float = float(ent_string.get())
            for i in PAGE:
                if want_combo_value == i['ccy']:
                    sale = float(i['sale'])
                    result_string.set('You should pay: ' + str(ent_float * sale) + ' HRN')
        except ValueError:
            result_string.set('Something went wrong!')


r = Data()
ent_string = StringVar()
result_string = StringVar()

want = Label(root, text='I want to buy:')
want.place(x=0, y=5)
combobox_want = ttk.Combobox(root, width=14, values=[
                                "USD",
                                "EUR",
                                "RUR",
                                "BTC"], state='readonly')
combobox_want.place(x=140, y=35)
combobox_want.current(0)
ent = Entry(root, width=14, bg='white', textvariable=ent_string)
ent.place(x=0, y=35)
result = Entry(root, text='You should pay: ', width=30, bg='white', textvariable=result_string)
result.place(x=4, y=80)
res = Button(root, width=15, text='Calculate', command=lambda: r.currency())
res.place(x=70, y=120)

root.mainloop()
