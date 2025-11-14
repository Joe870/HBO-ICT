import tkinter as tk
from tkinter import ttk, messagebox

# --------------------------
# BASISVENSTER
# --------------------------
root = tk.Tk()
root.title("Biker Verhuur Applicatie")

window_width = 700
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# --------------------------
# NOTEBOOK (TABS)
# --------------------------
tabControl = ttk.Notebook(root)
tab_verhuur = ttk.Frame(tabControl)
tab_reizen = ttk.Frame(tabControl)
tab_service = ttk.Frame(tabControl)
tab_faq = ttk.Frame(tabControl)

tabControl.add(tab_verhuur, text="Fietsen huren")
tabControl.add(tab_reizen, text="Reizen")
tabControl.add(tab_service, text="Service")
tabControl.add(tab_faq, text="FAQ")
tabControl.pack(expand=1, fill="both")

# --------------------------
# TAB 1 – Fietsen huren
# --------------------------
verhuur_data = []  # hier “slaan we op” wat de gebruiker invoert

def huur_fiets():
    naam = entry_naam.get()
    aantal = entry_aantal.get()
    soort = fiets_type.get()

    if not naam or not aantal:
        messagebox.showwarning("Fout", "Vul alle velden in!")
        return
    
    record = {"naam": naam, "aantal": aantal, "soort": soort}
    verhuur_data.append(record)

    messagebox.showinfo("Succes", f"{naam} heeft {aantal} {soort}-fiets(en) gehuurd.")
    entry_naam.delete(0, tk.END)
    entry_aantal.delete(0, tk.END)

label_naam = tk.Label(tab_verhuur, text="Naam klant:")
label_naam.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_naam = tk.Entry(tab_verhuur, width=30)
entry_naam.grid(row=0, column=1, padx=10, pady=10)

label_aantal = tk.Label(tab_verhuur, text="Aantal fietsen:")
label_aantal.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_aantal = tk.Entry(tab_verhuur, width=30)
entry_aantal.grid(row=1, column=1, padx=10, pady=10)

label_type = ttk.Label(tab_verhuur, text='Selecteer fiets soort:').grid(row=2, column=0, padx=10, pady=10, sticky="w")

fiets_type = tk.StringVar()
fiets_soort = ttk.Combobox(tab_verhuur, width = 27, textvariable=fiets_type)
fiets_soort['values'] = ('Vrouwen standaard', 'Vrouwen elektrisch', 'mannen  standaard', 'mannen elektrisch')
fiets_soort.grid(row=2, column=1, padx=10, pady=10)

btn_huur = tk.Button(tab_verhuur, text="Bevestig huur", command=huur_fiets, bg="#4CAF50", fg="white")
btn_huur.grid(row=3, column=1, pady=15)

# --------------------------
# TAB 2 – Reizen boeken
# --------------------------
label_reis = tk.Label(tab_reizen, text="Kies type reis:")
label_reis.pack(pady=10)

reis_type = tk.StringVar(value="Basic")
ttk.Radiobutton(tab_reizen, text="Basic (campings)", variable=reis_type, value="Basic").pack()
ttk.Radiobutton(tab_reizen, text="Luxe (hotels)", variable=reis_type, value="Luxe").pack()

btn_reis = tk.Button(tab_reizen, text="Boek reis", command=lambda: messagebox.showinfo("Reis geboekt", f"Je hebt een {reis_type.get()} reis geboekt!"))
btn_reis.pack(pady=20)

# --------------------------
# TAB 3 – Service aanvragen
# --------------------------
label_service = tk.Label(tab_service, text="Service bij pech of slecht weer")
label_service.pack(pady=10)

btn_service = tk.Button(tab_service, text="Service aanvragen", command=lambda: messagebox.showinfo("Service", "Serviceverzoek is verzonden!"))
btn_service.pack(pady=10)

# --------------------------
# TAB 4 – FAQ
# --------------------------
faq_text = """Veelgestelde vragen:

1. Hoe kan ik een fiets huren?
   → Ga naar het tabblad 'Fietsen huren' en vul het formulier in.

2. Kan ik accessoires huren?
   → Ja, dat kan in combinatie met een fiets.

3. Hoe werkt de verzekering?
   → U kunt een link openen naar onze verzekeringspartner (nog te integreren).
"""

faq_label = tk.Label(tab_faq, text=faq_text, justify="left")
faq_label.pack(padx=20, pady=20, anchor="w")

# --------------------------
# START
# --------------------------
root.mainloop()