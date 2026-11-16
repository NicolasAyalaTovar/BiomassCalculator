"""Biomass Calculator: desktop GUI for estimating insect biomass.

Implements the length-weight relationship of Rogers et al. (1976), later
applied by Stork & Blackburn (1993):

    biomass = n * (0.0305 * l ** 2.62)

where ``n`` is the abundance (number of individuals), ``l`` is the body
length in millimetres and the result is the dry biomass in milligrams.
"""

import tkinter as tk
from tkinter import messagebox, ttk

COEFFICIENT = 0.0305
EXPONENT = 2.62
FONT = ("Times New Roman", 12)

INFO_TEXT = (
    "This tool applies the biomass formula proposed by Rogers et al. (1976), "
    "later used by Stork and Blackburn (1993). It links the number of insects "
    "to their body length:\n\nb = n · (0.0305 · l^2.62)\n\n"
    "where n = abundance, l = body length (mm) and b = dry biomass (mg)."
)

REFERENCES_TEXT = (
    "References:\n"
    "• Rogers, L., Hinds, L. & Buschbom, R. (1976). A general weight vs length "
    "relationship for insects. Ann. Entomol. Soc. Am. 69: 387-389.\n"
    "• Stork, N. E. & Blackburn, T. M. (1993). Abundance, body size and biomass "
    "of arthropods in tropical forest. Oikos 67: 483-489."
)


def compute_biomass(abundance: int, length_mm: float) -> float:
    """Return the estimated dry biomass (mg) for ``abundance`` insects of ``length_mm``."""
    if abundance < 0 or length_mm <= 0:
        raise ValueError("Abundance must be >= 0 and length must be > 0.")
    return abundance * COEFFICIENT * length_mm ** EXPONENT


def is_integer(text: str) -> bool:
    """Tk validation callback: allow only digits (or an empty field)."""
    return text.isdigit() or text == ""


class BiomassApp:
    def __init__(self, root: tk.Tk) -> None:
        root.title("Biomass Calculator")
        root.resizable(False, False)

        style = ttk.Style()
        for widget in ("TLabel", "TEntry", "TButton"):
            style.configure(widget, font=FONT)

        frame = ttk.Frame(root, padding=20)
        frame.grid(row=0, column=0, sticky="nsew")

        tk.Label(frame, text=INFO_TEXT, wraplength=500, font=FONT,
                 justify="center").grid(row=0, column=0, columnspan=2, pady=5)

        validate_int = (root.register(is_integer), "%P")
        ttk.Label(frame, text="Abundance (n):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.abundance_entry = ttk.Entry(frame, width=25, validate="key",
                                         validatecommand=validate_int, font=FONT)
        self.abundance_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Body length in millimetres (l):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.size_entry = ttk.Entry(frame, width=25, font=FONT)
        self.size_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Button(frame, text="Calculate Biomass",
                   command=self.calculate).grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(frame, text="Biomass: ")
        self.result_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        tk.Label(frame, text=REFERENCES_TEXT, wraplength=500, font=FONT,
                 justify="left").grid(row=5, column=0, columnspan=2, sticky="w", padx=5, pady=10)

        root.bind("<Return>", lambda _event: self.calculate())

    def calculate(self) -> None:
        try:
            abundance = int(self.abundance_entry.get())
            length = float(self.size_entry.get().replace(",", "."))
            result = compute_biomass(abundance, length)
        except ValueError:
            messagebox.showerror(
                "Invalid input",
                "Please enter a whole number for abundance and a positive number for size.")
            return
        self.result_label.config(text=f"Biomass: {result:.2f} mg (dry weight)")


def main() -> None:
    root = tk.Tk()
    BiomassApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
