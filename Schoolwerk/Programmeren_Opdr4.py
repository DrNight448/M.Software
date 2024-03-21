"""
    Marvin Bader
    Software development
    Opdracht 4: Een gui met Tkinter
"""
import tkinter as tk
window = tk.Tk()

    #Hier staat de introductie van de applicatie
label_a = tk.Label(text="Eerste GUI met Tkinter!")
label_a.pack()

    #hier kan iemand ze naam invoeren
entry_a = tk.Entry(fg="white", bg="blue", width=50,)
entry_a.insert(0, "Wa is juh naam a driller")
entry_a.pack()
frame_a = tk.Frame()

    #Hier kan iemand in typen
)
label_b = tk.Label(text="Hier onder kan je typen", fg="red", bg="gray",height=1, width=50,)
label_b.pack()
text_b = tk.Text(fg="orange", bg="black",height=4, width=50,)
text_b.pack()
frame_b = tk.Frame()

frame_a.pack()
frame_b.pack()

window.mainloop()
