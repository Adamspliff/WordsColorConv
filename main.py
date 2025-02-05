import tkinter as tk
import tkinter.ttk as ttk
#from tkinter import messagebox
import random

def get_numbers(text):
            
    
    hexa="0123456789ABCDEF"
    color = []
    n=0
    hexacolor="#"
    #rgb =()

    for i in text:
        i = i.upper()
        if i in hexa and n < 6:
            color.append(hexa.index(i))
            hexacolor += i
            n+=1
    
    if len(color) < 6:
        for i in range(0, 6 - len(color)):
            color.append(0)
            hexacolor += "0"
            n+=1
        else:
            pass

    r = 16 * color[0] + color[1] #r =int(hexa[0:2],16)
    g = 16 * color[2] + color[3]
    b = 16 * color[4] + color[5]

    rgb = f"({r},{g},{b})"

    return rgb, hexacolor



def clear():

    colors_entry.config(state="normal")
    colors_entry.delete(0,"end")
    colors_entry.config(state="readonly")
    text_entry.delete(0,"end")
    text_entry.config(background="white")

    colors_entry2.config(state="normal")
    colors_entry2.delete(0,"end")
    colors_entry2.config(state="readonly")
    text_entry2.delete(0,"end")
    text_entry2.config(background="white")

    colors_entry3.config(state="normal")
    colors_entry3.delete(0,"end")
    colors_entry3.config(state="readonly")
    text_entry3.delete(0,"end")
    text_entry3.config(background="white")

    header.config(background="#f1e1e1",text="Words into color")
    root.configure(background="#f1e1e1")
    text_label.configure(background="#f1e1e1")
    entry_label.configure(background="#f1e1e1")
    text_label2.configure(background="#f1e1e1")
    entry_label2.configure(background="#f1e1e1")
    text_label3.configure(background="#f1e1e1")
    entry_label3.configure(background="#f1e1e1")

    label.configure(background="#f1e1e1")
    label2.configure(background="#f1e1e1")




def get_entry_value():

    text = text_entry.get()
    text2 = text_entry2.get()
    text3 = text_entry3.get()

    if len(text) != 0:
        rgb, hexacolor = get_numbers(text)
        text_entry.config(background=hexacolor)
        colors_entry.config(state="normal")
        colors_entry.insert(0, rgb)
        colors_entry.config(state="readonly")

    if len(text2) != 0:
        rgb2, hexacolor2 = get_numbers(text2)
        text_entry2.config(background=hexacolor2)
        colors_entry2.config(state="normal")
        colors_entry2.insert(0, rgb2)
        colors_entry2.config(state="readonly")

    if len(text3) != 0:
        rgb3, hexacolor3 = get_numbers(text3)
        text_entry3.config(background=hexacolor3)
        colors_entry3.config(state="normal")
        colors_entry3.insert(0, rgb3)
        colors_entry3.config(state="readonly")



def action():

    header.config(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}",text="All the colors!")
    root.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")

    text_label.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
    entry_label.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")

    text_label2.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
    entry_label2.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")

    text_label3.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")
    entry_label3.configure(background=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}")

    label.configure(background=f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}")
    label2.configure(background=f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}")

    text_entry.config(background=f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}")
    text_entry2.config(background=f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}")
    text_entry3.config(background=f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}")


#-------------------Main Window
root = tk.Tk()
root.title("WordsColorConv")
root.geometry("900x1000")
root.resizable(True, True)
root.configure(background="#f1e1e1")
style = ttk.Style()
style.theme_use("default")


#-------------------Labels/Entries

header = ttk.Label(root, width=40, text="Words into color", font=("Lato",22),anchor="center",background="#f1e1e1")
header.grid(row=0,column=0, columnspan=2)

label = ttk.Label(root,width=106, anchor="center", background="#f1e1e1", font=("Lato",9))
label.grid(row=1,column=0, columnspan=2)

text_label = ttk.Label(root, width=40, text="Text 1:", font=("Lato",14), background="#f1e1e1")
text_label.grid(row=2,column=0)

text_entry = tk.Entry(root, width=40, font=("Lato",14))
text_entry.grid(row=3,column=0)

entry_label = ttk.Label(root, width=40, text="Colorcode 1:", font=("Lato",14), background="#f1e1e1")
entry_label.grid(row=2,column=1)

colors_entry = ttk.Entry(root, width=40, font=("Lato",14), state="readonly")
colors_entry.grid(row=3,column=1)

text_label2 = ttk.Label(root, width=40, text="Text 2:", font=("Lato",14), background="#f1e1e1")
text_label2.grid(row=4,column=0)

text_entry2 = tk.Entry(root, width=40,font=("Lato",14))
text_entry2.grid(row=5,column=0)

entry_label2 = ttk.Label(root, width=40, text="Colorcode 2:", font=("Lato",14), background="#f1e1e1")
entry_label2.grid(row=4,column=1)

colors_entry2 = ttk.Entry(root, width=40, font=("Lato",14), state="readonly")
colors_entry2.grid(row=5,column=1)

text_label3 = ttk.Label(root, width=40, text="Text 3:", font=("Lato",14), background="#f1e1e1")
text_label3.grid(row=6,column=0)

text_entry3 = tk.Entry(root, width=40,font=("Lato",14))
text_entry3.grid(row=7,column=0)

entry_label3 = ttk.Label(root, width=40, text="Colorcode 3:", font=("Lato",14), background="#f1e1e1")
entry_label3.grid(row=6, column=1)

colors_entry3 = ttk.Entry(root, width=40, font=("Lato",14), state="readonly")
colors_entry3.grid(row=7,column=1)

label2 = ttk.Label(root, width=106, text="How to: Please enter strings and they will be converted to colors!", anchor="center", background="#f1e1e1", font=("Lato", 9))
label2.grid(row=12, column=0, columnspan=2)

# ________________ Buttons

get_colors_button = ttk.Button(root, width=40, text="Colors", command=get_entry_value)
get_colors_button.grid(row=8,column=0,columnspan=2)

clear_button = ttk.Button(root, width=40, text="Clear", command=clear)
clear_button.grid(row=9,column=0, columnspan=2)

close_button = ttk.Button(root, width=40, text="Close",command=root.destroy)
close_button.grid(row=10,column=0, columnspan=2)

action_button = ttk.Button(root, width=40, text="Action!",command=action)
action_button.grid(row=11,column=0, columnspan=2)



root.mainloop()

