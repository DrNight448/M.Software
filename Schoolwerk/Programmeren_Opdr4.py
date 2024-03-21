"""
    Marvin Bader
    Software development
    Opdracht 4: Een gui met Tkinter
"""
import tkinter as tk
window = tk.Tk()

    #Hier staat de introductie van de applicatie
label = tk.Label(text="Eerste GUI met Tkinter!")
label.pack()

    #hier kan iemand ze naam invoeren
entry = tk.Entry(fg="white", bg="blue", width=50,)
entry.insert(0, "Wa is juh naam a driller")
entry.pack()

    #Hier kan iemand in typen
label = tk.Label(text="Hier onder kan je typen", fg="red", bg="gray",height=1, width=50,)
label.pack()
text_box = tk.Text(fg="orange", bg="black",height=4, width=50,)
text_box.pack()
window.mainloop()