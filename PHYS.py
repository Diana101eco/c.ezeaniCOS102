import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        Q_microC = float(entry_charge.get())
        V = float(entry_voltage.get())

        Q = Q_microC * 1e-6
        C = Q / V
        E = 0.5 * C * V**2
        C_microF = C * 1e6

        result = f"Capacitance: {C_microF:.3f} μF\nEnergy Stored: {E:.3f} J"
        messagebox.showinfo("Results", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

app = tk.Tk()
app.title("Capacitor Calculator")

tk.Label(app, text="Charge (μC):").grid(row=0, column=0, padx=10, pady=5)
entry_charge = tk.Entry(app)

entry_charge.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Voltage (V):").grid(row=1, column=0, padx=10, pady=5)
entry_voltage = tk.Entry(app)
entry_voltage.grid(row=1, column=1, padx=10, pady=5)

tk.Button(app, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()
