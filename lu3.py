import tkinter as tk

master = tk.Tk()
master.title("Bike verhuur")

def input1():
    print("ik ben in functie input1")
    input_entry1.delete(1, tk.END)  # Remove current text in entry

window_width = 500
window_height = 200

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

master.iconbitmap('./Logo/bike.ico')

top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief="groove")

input_label1 = tk.Label(top_frame, text="Hoeveelheid fietsen")
input_entry1 = tk.Entry(top_frame, width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input1)

top_frame.pack(side=tk.TOP)
line.pack(pady=10) 
bottom_frame.pack(side=tk.BOTTOM)

input_label1.grid(row=0, column=0, padx=10, pady=5, sticky='w')
input_entry1.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
browse1.grid(row=0, column=3, padx=10, pady=5)

master.mainloop()