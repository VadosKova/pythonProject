#Задание 1

from tkinter import *
from tkinter import ttk

rates = { "USD": 0.027, "EUR": 0.025, "PLN": 0.12, "GBP": 0.022 }

def convert():
    num = entry.get()

    if not num.isdigit() or float(num) <= 0:
        result_label.config(text="Должно быть положительное число")
        return

    amount = float(num)
    currency = currency_combobox.get()

    if currency == "Выберите валюту":
        result_label.config(text="Выберите валюту")
        return

    rate = rates[currency]
    result = amount * rate
    result_label.config(text=f"{amount} ₴ = {result} {currency}")


root = Tk()
root.geometry("300x300")
root.title("Курс валют")

Label(root, text="Сумма в гривне:").pack()

entry = Entry(root)
entry.pack()

currency_combobox = ttk.Combobox(root, values=["Выберите валюту", "USD", "EUR", "PLN", "GBP"])
currency_combobox.set("Выберите валюту")
currency_combobox.pack()

convert_btn = Button(root, text="Convert", command=convert)
convert_btn.pack(pady=10)

result_label = Label(root, text="Результат: ")
result_label.pack()


root.mainloop()