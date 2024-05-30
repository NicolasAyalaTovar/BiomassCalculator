import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk,font 
from tkinter import messagebox

def is_integer(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False

# Function
def calculate_biomass():
    try:
        n = int(abundance_entry.get())  
        l = float(size_entry.get())
        r1 = l**2.62
        r2 = 0.0305 * r1
        result = n * r2
        result_label.config(text=f"Biomass: {result:.2f}")  
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for abundance and size.")

#Interface
root = tk.Tk()
root.title("Biomass Calculator")
vcmd = (root.register(is_integer),'%P')

style = ttk.Style()
style.configure("TLabel", font=('Times New Roman', 12))
style.configure("TEntry", font=('Times New Roman', 12))
style.configure("TButton", font=('Times New Roman', 12))

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

info_text = ("This script is designed so you can use the formula for calculating biomass proposed "
            "by Rogers et al, 1976, which was later used by Stork and Blackburn in their study. "
            "The formula links the number of insects to their size (length) and is as follows: "
            "b = n (0.0305*l^2.62) where n = Abundance and l = Size")
info_label = tk.Label(frame, text=info_text, wraplength=500, font=('Times New Roman', 12), justify='center')
info_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)

abundance_label = ttk.Label(frame, text="Abundance (n):")
abundance_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
abundance_entry = ttk.Entry(frame, width=25, validate='key', validatecommand=vcmd, font=('Times New Roman', 12))
abundance_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

size_label = ttk.Label(frame, text="Size in centimeters (l):")
size_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
size_entry = ttk.Entry(frame, width=25, font=('Times New Roman', 12))
size_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate Biomass", command=calculate_biomass, style="TButton")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="Biomass: ")
result_label.grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)

references_text = ("References:\n"
                "- Rogers, L., Hinds, L. y Buschbom, R. (1976) A general weight vs length relationships for insects. Ann. Entomol.Soc.Am. 69: 387-389.\n"
                "- Stork, N. E. y Blackburn, T. M. (1993). Abundance, body size and biomass of arthropods in tropical forest. Oikos 67: 483-489.")
references_label = tk.Label(frame, text=references_text, wraplength=500, font=('Times New Roman', 12), justify='left')
references_label.grid(row=5, column=0, columnspan=2, sticky=tk.W, padx=5, pady=10)

root.mainloop()
