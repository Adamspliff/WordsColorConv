import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import random

def getNumbers(text):
            
    
    hex=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    color = []
    n=0
    hexcolor="#"
    #rgb =()

    for i in text:
        i = i.upper()
        if i in hex and n < 6:
            color.append(hex.index(i))
            hexcolor += i
            n+=1
    
    if len(color) < 6:
        for i in range(0, 6 - len(color)):
            color.append(0)
            hexcolor += "0"
            n+=1
        else:
            pass

    r = 16 * color[0] + color[1] #r =int(hex[0:2],16)
    g = 16 * color[2] + color[3]
    b = 16 * color[4] + color[5]

    rgb = (f"({r},{g},{b})")

    return rgb, hexcolor
        

        

def main():


    def clear():

        colors_entry.delete(0,"end")
        text_entry.delete(0,"end")
        text_entry.config(background="white")
        
        colors_entry2.delete(0,"end")
        text_entry2.delete(0,"end")
        text_entry2.config(background="white")

        colors_entry3.delete(0,"end")
        text_entry3.delete(0,"end")
        text_entry3.config(background="white")

        header.config(background="#f1e1e1",text="Words into color")
        root.configure(background="#F0F0F0")
        text_label.configure(background="#f1e1e1")
        entry_label.configure(background="#f1e1e1")
        text_label2.configure(background="#f1e1e1")
        entry_label2.configure(background="#f1e1e1")
        text_label3.configure(background="#f1e1e1")
        entry_label3.configure(background="#f1e1e1")
    

        
    def get_entry_value():

        text = text_entry.get()
        text2 = text_entry2.get()
        text3 = text_entry3.get()

        rgb,hexcolor = getNumbers(text)
        rgb2,hexcolor2 = getNumbers(text2)
        rgb3,hexcolor3 = getNumbers(text3)

        text_entry.config(background=hexcolor)
        text_entry2.config(background=hexcolor2)
        text_entry3.config(background=hexcolor3)

        colors_entry.insert(0,rgb)
        colors_entry2.insert(0,rgb2)
        colors_entry3.insert(0,rgb3)
    
    def action():

        header.config(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}",text="All the colors!")
        root.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
        text_label.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
        entry_label.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
        text_label2.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
        entry_label2.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
        text_label3.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
        entry_label3.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
    
    
    root = tk.Tk()
    root.title("WordsColorConv")
    root.geometry("400x600")
    root.resizable(True, True)
    root.configure(background="#f1e1e1")
    style = ttk.Style()
    style.theme_use("default")
    
    header = ttk.Label(root, width=40, text="Words into color:", font=("Lato",14))
    header.pack()

    text_label = ttk.Label(root, width=40, text="Text 1:", font=("Lato",14))
    text_label.pack()

    text_entry = tk.Entry(root, width=40, font=("Lato",14))
    text_entry.pack()
    
    entry_label = ttk.Label(root, width=40, text="Colorcode 1:", font=("Lato",14))
    entry_label.pack()

    colors_entry = ttk.Entry(root, width=40, font=("Lato",14))
    colors_entry.pack()

    text_label2 = ttk.Label(root, width=40, text="Text 2:", font=("Lato",14))
    text_label2.pack()

    text_entry2 = tk.Entry(root, width=40,font=("Lato",14))
    text_entry2.pack()
    
    entry_label2 = ttk.Label(root, width=40, text="Colorcode 2:", font=("Lato",14))
    entry_label2.pack()
    
    colors_entry2 = ttk.Entry(root, width=40, font=("Lato",14))
    colors_entry2.pack()

    text_label3 = ttk.Label(root, width=40, text="Text 3:", font=("Lato",14))
    text_label3.pack()

    text_entry3 = tk.Entry(root, width=40,font=("Lato",14))
    text_entry3.pack()

    entry_label3 = ttk.Label(root, width=40, text="Colorcode 3:", font=("Lato",14))
    entry_label3.pack()
    
    colors_entry3 = ttk.Entry(root, width=40, font=("Lato",14))
    colors_entry3.pack()
    

    getColors_button = ttk.Button(root, width=40, text="Colors", command=get_entry_value)
    getColors_button.pack()

    clear_button = ttk.Button(root, width=40, text="Clear", command=clear)
    clear_button.pack()

    close_button = ttk.Button(root, width=40, text="Close",command=root.destroy)
    close_button.pack()

    action_button = ttk.Button(root, width=40, text="Action!",command=action)
    action_button.pack()


    root.mainloop()

if __name__ == "__main__":
    main()