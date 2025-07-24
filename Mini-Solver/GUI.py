import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Aerofoil_Generator import GenerateAerofoil

def InitialiseWindow():
    global ax, canvas

    root = tk.Tk()  # Create the main window
    root.title("NACA Airfoil Generator")  # Set window title
    root.geometry("800x500")  # Set window size

    global NACA_Num, AOA_Num

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

    label2 = tk.Label(frame, text="Angle of attack")
    label2.grid(row=1, column=0, padx=0)

    AOA_Num = tk.Entry(frame, text = "##")
    AOA_Num.grid(row=1, column=1, padx=0,pady=5)

    Button1 = tk.Button(frame, text= "Generate", command=lambda: GenerateAerofoil(NACA_Num.get(),AOA_Num.get(),ax,canvas))
    Button1.grid(row=2, column=1, padx=0)

    # Initialise Plot
    fig = Figure(figsize=(6, 3), dpi=100)
    ax  = fig.add_subplot(111)
    ax.set_title("Airfoil will appear here")
    ax.grid(False)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
    root.mainloop() # keeps window open and refreshed
