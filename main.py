from tkinter import *
import requests


root = Tk()
root.title("Password and username Verification")
root.geometry("500x500")
root.config(bg='#8dc63f')

# API
url = "http://api.exchangeratesapi.io/v1/latest?access_key=fab4bca97cc9094b963030c6064ed5c2"

req = requests.get(url)

result = req.json()
print(result)
rates = result['rates'].keys()


# function
def convertor():

    amount = float(amount_entry.get())

    new_amnt = amount * result['rates'][lst.get(ACTIVE)]  # converting currency

    answer['text'] = new_amnt


frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)
# Labels
l1_convertor = Label(root, text="Converting US Currency TO OTHERS", bg="#666666", fg="white", font=("bold", 12))
l1_convertor.place(x=80, y=20)

amount = Label(root, text="Amount:", bg="#666666", fg="white", font=("bold", 12),)
amount.place(x=20, y=80)

# Entry
amount_entry = Entry(root)
amount_entry.place(x=175, y=80)

# Label
crrncy1 = Label(root, text="To Currency:", bg="#666666", fg="white", font=("bold", 12))
crrncy1.place(x=20, y=225)

# function
lst = Listbox(root, width=20)
for i in rates:
    lst.insert(END, str(i))
lst.place(x=175, y=150)

# button
btn = Button(root, text="Convertor", bg='#8dc63f', command=convertor, borderwidth=10)
btn.place(x=200, y=350)

# Label
answer = Label(root, font=('bold', 12), width=20)
answer.place(x=150, y=400)

root.mainloop()
