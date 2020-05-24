import tkinter
from tkinter import messagebox
def sumuj():
    try:
        val_a = int(a_entry.get())
        val_b = int(b_entry.get())
        suma = val_a + val_b
        wynik.configure(text=suma)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")


root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Zmienna a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="Zmienna b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

wynik_labl = tkinter.Label(master=root, text="Wynik:")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()


submit = tkinter.Button(master=root, text="Policz", command=sumuj)
submit.pack()


root.mainloop()

print("Po mainloop")