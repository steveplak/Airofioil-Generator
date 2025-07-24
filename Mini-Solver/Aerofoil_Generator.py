import tkinter as tk
import numpy as np
from matplotlib.transforms import Affine2D


def GenerateAerofoil(naca_code: str, AOA_Num: str,ax,canvas):
    
    naca_code_strip = naca_code.strip()
    AOA_Num_strip = AOA_Num.strip()

    if not AOA_Num_strip.isdigit() or 0 > int(AOA_Num_strip) or int(AOA_Num_strip) > 90 :
        tk.messagebox.showerror("Invalid Angle of Atack","Please enter a number between 0 and 90")
        return
    
    if len(naca_code_strip) != 4 or not naca_code_strip.isdigit():

        tk.messagebox.showerror("Invalid NACA code","Please enter exactly 4 numeric digits, e.g. 2412")
        return
        
    else:
        
        m = int(naca_code_strip[0])/100
        p = int(naca_code_strip[1])/10
        t = int(naca_code_strip[2:4])/100
        print(m,p,t)

        #calculate acording to equations from paper: https://web.stanford.edu/~cantwell/AA200_Course_Material/The%20NACA%20airfoil%20series.pdf
        x = np.linspace(0, 1, 100)
        yc = np.where( x < p , m/p**2*(2*p*x - x**2),  m/(1-p)**2*((1-2*p) + 2*p*x - x**2))
        dyc_dx = np.where(  x < p, (2*m / p**2) * (p - x), (2*m / (1-p)**2) * (p - x))
        
        yt = (t/0.2)*(0.2969*np.sqrt(x) - 0.1260*x - 0.3516*x**2 + 0.2843*x**3 - 0.1015*x**4)
    
        X_U = x - yt * np.sin(np.arctan(dyc_dx)) ; X_L = x + yt * np.sin(np.arctan(dyc_dx))
        Y_U = yc + yt * np.cos(np.arctan(dyc_dx)) ; Y_L = yc - yt * np.cos(np.arctan(dyc_dx))


        # account for angle
        angle = - int(AOA_Num_strip)
        rot = Affine2D().rotate_deg_around(0, 0, angle) + ax.transData
        
        ax.clear()
        ax.set_title(f"NACA {naca_code} ")
        ax.set_xlim(-1.5, 2); ax.set_ylim(-1.5, 1.5)

        ax.plot(x, yc, transform=rot)
        ax.plot(X_U, Y_U, 'b-', transform=rot)
        ax.plot(X_L, Y_L, 'b-', transform=rot)
        
        canvas.draw()