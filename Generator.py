import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def main():
    InitialiseWindow()
    

def InitialiseWindow():
    global ax, canvas

    root = tk.Tk()  # Create the main window
    root.title("NACA Airfoil Generator")  # Set window title
    root.geometry("800x500")  # Set window size

    global NACA_Num

    # Add title
    label = tk.Label(root, text = "Welcome to the NACA Airfoil Generator!")
    label.pack(pady=20)

    #Create Frame
    frame = tk.Frame(root)
    frame.pack(anchor='n', padx = 10, expand=True)

    # NACA Info
    label1 = tk.Label(frame, text="Naca Code")
    label1.grid(row=0, column=0, padx=0)

    NACA_Num = tk.Entry(frame, text = "####")
    NACA_Num.grid(row=0, column=1, padx=0)

    Button1 = tk.Button(frame, text= "Generate", command=lambda: GenerateAerofoil(NACA_Num.get()))
    Button1.grid(row=0, column=2, padx=0)

    # Initialise Plot
    fig = Figure(figsize=(6, 3), dpi=100)
    ax  = fig.add_subplot(111)
    ax.set_title("Airfoil will appear here")
    #ax.set_xlim(0, 1.5); ax.set_ylim(-0.75, 0.75)
    ax.grid(False)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
    root.mainloop() # keeps window open and refreshed

def GenerateAerofoil(naca_code: str):

    ax.clear()
    ax.set_title(f"NACA {naca_code} ")
    
    
    
    canvas.draw()
    


main()