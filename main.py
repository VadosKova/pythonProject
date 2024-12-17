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
        result_label.config(text="Выберите валюту!")
        return

    rate = rates[currency]
    result = amount * rate
    result_label.config(text=f"{amount} ₴ = {result} {currency}")