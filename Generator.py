import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np



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
    ax.grid(False)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
    root.mainloop() # keeps window open and refreshed

def GenerateAerofoil(naca_code: str):
    
    naca_code_strip = naca_code.strip()
    if len(naca_code_strip) != 4 or not naca_code_strip.isdigit():

        tk.messagebox.showerror("Invalid NACA code","Please enter exactly 4 numeric digits, e.g. 2412")
        return
    
    else:
        
        m = int(naca_code_strip[0])/100
        p = int(naca_code_strip[1])/10
        t = int(naca_code_strip[2:4])/100
        print(m,p,t)

        x = np.linspace(0, 1, 100)
        yc = np.where( x < p , m/p**2*(2*p*x - x**2),  m/(1-p)**2*((1-2*p) + 2*p*x - x**2))
        dyc_dx = np.where(  x < p, (2*m / p**2) * (p - x), (2*m / (1-p)**2) * (p - x))
        
        yt = (t/0.2)*(0.2969*np.sqrt(x) - 0.1260*x - 0.3516*x**2 + 0.2843*x**3 - 0.1015*x**4)
    
        X_U = x - yt * np.sin(np.arctan(dyc_dx)) ; X_L = x + yt * np.sin(np.arctan(dyc_dx))  
        Y_U = yc + yt * np.cos(np.arctan(dyc_dx)) ; Y_L = yc - yt * np.cos(np.arctan(dyc_dx))

        ax.clear()
        ax.set_title(f"NACA {naca_code} ")
        ax.set_xlim(-0.5, 1.5); ax.set_ylim(-0.5, 0.5)

        ax.plot(x, yc)
        ax.plot(X_U, Y_U, 'b-')
        ax.plot(X_L, Y_L, 'b-')
        
        canvas.draw()
    
    
    


main()