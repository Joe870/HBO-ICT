import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# --------------------------
# databse gegevens
# --------------------------
# db_config = {
#     'user': 'user',
#     'password' : 'password',
#     'host' : 'db',
#     'database' : 'mydatabase',
#     'port' : 3306
# }

# try: 
#     cnx = mysql.connector.connect(db_config)

#     cursor = cnx.cursor()
#     cursor.execute("SELECT 1")
#     result = cursor.fetchone()
#     print(f"Connection succesful! Query result: {result}")

#     cursor.close()
#     cnx.close()
# except mysql.connector.Error as err:
#     print(f"Error connecting to MySQLL {err}")

# if __name__ == "__main__":
#     pass
# --------------------------
# BASISVENSTER
# --------------------------
master = tk.Tk()
master.title("Biker Verhuur Applicatie")

window_width = 700
window_height = 500
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
master.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# --------------------------
# NOTEBOOK (TABS)
# --------------------------
tabControl = ttk.Notebook(master)
tab_verhuur = ttk.Frame(tabControl)
tab_accesoires = ttk.Frame(tabControl)
tab_reizen = ttk.Frame(tabControl)
tab_service = ttk.Frame(tabControl)
tab_faq = ttk.Frame(tabControl)
tab_contact = ttk.Frame(tabControl)

tabControl.add(tab_verhuur, text="Fietsen huren")
tabControl.add(tab_accesoires, text="accesoires huren")
tabControl.add(tab_reizen, text="Reizen")
tabControl.add(tab_service, text="Service")
tabControl.add(tab_faq, text="FAQ")
tabControl.add(tab_contact, text="Contact")
tabControl.pack(expand=1, fill="both")


# --------------------------
# TAB 1 – Fietsen huren
# --------------------------
verhuur_data = []  # hier “slaan we op” wat de gebruiker invoert

def huur_fiets():
   naam = entry_fiets_naam.get()
   aantal = entry_fiets_aantal.get()
   soort = fiets_type.get()

   if not naam or not aantal:
      messagebox.showwarning("Fout", "Vul alle velden in!")
      return
         
   record = {"naam": naam, "aantal": aantal, "soort": soort}
   verhuur_data.append(record)

   messagebox.showinfo("Succes", f"{naam} heeft {aantal} {soort}-fiets(en) gehuurd.")
   entry_fiets_naam.delete(0, tk.END)
   entry_fiets_aantal.delete(0, tk.END)

label_fiets_naam = tk.Label(tab_verhuur, text="Naam klant:")
label_fiets_naam.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_fiets_naam = tk.Entry(tab_verhuur, width=30)
entry_fiets_naam.grid(row=0, column=1, padx=10, pady=10)

label_fiets_aantal = tk.Label(tab_verhuur, text="Aantal fietsen:")
label_fiets_aantal.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_fiets_aantal = tk.Entry(tab_verhuur, width=30)
entry_fiets_aantal.grid(row=1, column=1, padx=10, pady=10)

label_fiets_type = ttk.Label(tab_verhuur, text='Selecteer fiets soort:').grid(row=2, column=0, padx=10, pady=10, sticky="w")

fiets_type = tk.StringVar()
fiets_soort = ttk.Combobox(tab_verhuur, width = 27, textvariable=fiets_type)
fiets_soort['values'] = ('Vrouwen standaard', 'Vrouwen elektrisch', 'mannen  standaard', 'mannen elektrisch')
fiets_soort.grid(row=2, column=1, padx=10, pady=10)

btn_huur_fiets = tk.Button(tab_verhuur, text="Bevestig huur", command=huur_fiets, bg="#4CAF50", fg="white")
btn_huur_fiets.grid(row=3, column=1, pady=15)

# --------------------------
# tab 2 accesoires huren
# --------------------------
def huur_accesoires():
   naam = entry_accessoires_naam.get()
   aantal = entry_accessoires_aantal.get()
   soort = accessoires_soort.get()

   if not naam or not aantal:
      messagebox.showwarning("Fout", "Vul alle velden in!")
      return
   
   if naam in verhuur_data:
      record = {"naam": naam, "aantal": aantal, "soort": soort}
      verhuur_data.append(record)

      messagebox.showinfo("Succes", f"{naam} heeft {aantal} {soort}-accessoires gehuurd.")
      entry_fiets_naam.delete(0, tk.END)
      entry_fiets_aantal.delete(0, tk.END)

label_accessoires_naam = tk.Label(tab_accesoires, text="Klant naam:")
label_accessoires_naam.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_accessoires_naam = tk.Entry(tab_accesoires, width=30)
entry_accessoires_naam.grid(row=0, column=1, padx=10, pady=10)

label_accessoires_aantal = tk.Label(tab_accesoires, text="Aantal accessoires:")
label_accessoires_aantal.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_accessoires_aantal = tk.Entry(tab_accesoires, width=30)
entry_accessoires_aantal.grid(row=1, column=1, padx=10, pady=10)

label_accesoires_type = ttk.Label(tab_accesoires, text='Selecteer accesoire soort:').grid(row=2, column=0, padx=10, pady=10, sticky="w")

accessoires_type = tk.StringVar()
accessoires_soort = ttk.Combobox(tab_accesoires, width = 27, textvariable=accessoires_type)
accessoires_soort['values'] = ('Fietstas', 'Fietshelm', 'Kinderzitje')
accessoires_soort.grid(row=2, column=1, padx=10, pady=10)

btn_accessoires_huur = tk.Button(tab_accesoires, text="Bevestig huur", bg="#4CAF50", fg="white")
btn_accessoires_huur.grid(row=3, column=1, pady=15)


# --------------------------
# TAB 3 – Reizen boeken
# --------------------------
label_reis = tk.Label(tab_reizen, text="Kies type reis:")
label_reis.pack(pady=10)

reis_type = tk.StringVar(value="Basic")
ttk.Radiobutton(tab_reizen, text="Basic (campings)", variable=reis_type, value="Basic").pack()
ttk.Radiobutton(tab_reizen, text="Luxe (hotels)", variable=reis_type, value="Luxe").pack()

btn_reis = tk.Button(tab_reizen, text="Boek reis", command=lambda: messagebox.showinfo("Reis geboekt", f"Je hebt een {reis_type.get()} reis geboekt!"))
btn_reis.pack(pady=20)

# --------------------------
# TAB 4 – Service aanvragen
# --------------------------
label_service = tk.Label(tab_service, text="Service bij pech of slecht weer")
label_service.pack(pady=10)

btn_service = tk.Button(tab_service, text="Service aanvragen", command=lambda: messagebox.showinfo("Service", "Serviceverzoek is verzonden!"))
btn_service.pack(pady=10)

# --------------------------
# TAB 5 – FAQ
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
# TAB 5 – Contact
# --------------------------
contact_text = """Veelgestelde vragen:

telefoonnummer : 123456787
E-mailadres : example@outlook.com
"""

contact_label = tk.Label(tab_contact, text=contact_text, justify="left")
contact_label.pack(padx=20, pady=20, anchor="w")
# --------------------------
# START
# --------------------------
master.mainloop()
print(verhuur_data)