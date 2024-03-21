"""
    Marvin Bader
    Software development
    Opdracht 4: Een gui met Tkinter
"""
import tkinter as tk
window = tk.Tk()
label = tk.Label(text="Eerste GUI met Tkinter!")
label.pack()




entry = tk.Entry(fg="white", bg="blue", width=50)
entry.pack()

entry.insert(0, "Wa is juh naam a driller")

window.mainloop()