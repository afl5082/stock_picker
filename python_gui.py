#https://www.youtube.com/watch?v=Zw6M-BnAPP0
import stock_data as sd
from tkinter import *
from tkinter.ttk import *
from tkcalendar import *
import sys, os
from ttkthemes import themed_tk as tk
import locale

locale.setlocale(locale.LC_ALL, '')

def growth_chart():
    #place growth chart here on button click
    #https://www.youtube.com/watch?v=Zw6M-BnAPP0


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def stock_calc():
    global e
    global user_pick
    user_pick = e.get()
    return


def grab_date():

    global purchase_date
    cal_label.config(text=cal.get_date())

    purchase_date = cal.get_date()


def hypo_growth():

    global my_label_try

    if purchase_date != "" and user_pick != "":

        #removes stock recc text box
        if my_label_try != "":
            my_label_try.destroy()

        text_wid.destroy()

        stock_list = sd.stock_growth(user_pick, purchase_date)

        purchase_price = stock_list[0]
        today_price = stock_list[1]

        units_bought = 10000 / float(purchase_price)
        growth = round((units_bought * float(today_price)) - 10000, 0)

        #output to GUI
        my_label = Label(root, text=int(growth))
        my_label.grid(row=4, column=1)

        return

    else:

        my_label_try = Label(root,
                             text="Please Type a Stock and Pick a Date First")
        my_label_try.grid(row=5, column=1)


symbols = {
    'TSLA': 'Tesla',
    'ZM': 'Zoom',
    'SE': 'Sea Limited',
    'NIO': 'NIO Limited',
    'MRNA': 'Moderna, Inc.'
}

root = Tk()
#root = tk.ThemedTk()
#root.get_themes()
#root.set_theme("adapta")

root.title("Stock Pick")
logo = PhotoImage(file=resource_path('datat_logo.png'))
root.iconphoto(False, logo)
#root.configure(background='grey')

e = Entry(root, width=35)
#, borderwidth=5
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.focus_set()

style = Style()
style.configure('TButton',
                font=('calibri', 12),
                foreground='black',
                background='black',
                borderwidth=1)

#https://stackoverflow.com/questions/27347981/how-to-change-the-color-of-ttk-button
stock_rec_dict = sd.stock_recs()

user_pick = ""
purchase_date = ""
my_label_try = ""

#i = 2

text_wid = Text(root, height=7, width=25)
text_wid.grid(row=4, column=1)
text_wid.configure(font=('calibri', 14))

for key, value in stock_rec_dict.items():

    currency_format = locale.currency(value[1], grouping=True)

    text_wid.insert(
        END,
        str(value[0]) + ": " + str(currency_format).replace('.00', ''))
    text_wid.insert(END, '\n')
    #stockrec_label = Label(root, text=value[1])
    #stockrec_label.grid(row=i, column=1)

cal = Calendar(root, selectmode="day", year=2020, month=1, day=1)
cal.grid(row=4, column=4)

button_1 = Button(root, text="Enter", command=stock_calc)
#padx=10, pady=5,
button_1.grid(row=2, column=1)

button_2 = Button(root, text="Enter Purchase Date", command=grab_date)
button_2.grid(row=2, column=4)

cal_label = Label(root, text="")
cal_label.grid(row=0, column=4)

button_3 = Button(root,
                  text="Calculate Hypothetical Growth",
                  command=hypo_growth)
button_3.grid(row=6, column=1)

root.mainloop()