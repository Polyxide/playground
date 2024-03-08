from tkinter import *

from tkinter import ttk

def funk(*args):

    min_bet = int(m_bet.get())
    total = int(t_total.get())
    bet = min_bet
    counter = 0
    summary = 1

    while total > summary:

            summary += bet
            bet *= 2
            counter += 1

    chance_to_loose = 0.5135

    for x in range(counter - 1):
        chance_to_loose *= 0.5135

    chance = (1 - chance_to_loose) * 100
    c_chance = '{:.2f}'.format(chance)

    answer.set(f'You will win with {c_chance}% chance, taking {counter} steps')


root = Tk()
root.title("Roulette")

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, E, W, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


ttk.Label(mainframe, text='Enter your total money:').grid(column=1, row=1)


t_total = StringVar()
total_entry = ttk.Entry(mainframe, width=10, textvariable=t_total)
total_entry.grid(column=1, row=2)


ttk.Label(mainframe, text='Enter desirable win:').grid(column=3, row=1)


m_bet = StringVar()
min_bet_entry = ttk.Entry(mainframe, width=10, textvariable=m_bet)
min_bet_entry.grid(column=3, row=2)


answer = StringVar()
ttk.Label(mainframe, textvariable=answer).grid(column=1, row=3)


ttk.Button(mainframe, text='calculate', command=funk).grid(column=3, row=3, sticky=(S, E))


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", funk)
root.mainloop()