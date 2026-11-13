import sys
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import Encoder.encoder as e 
from PIL import Image

window = tk.Tk()
window.title("Encoder")
window.resizable(False, False)
window.configure(bg="#000000")
window.geometry("600x700")

title = tk.Label(window,
                text="Encode Your Secrets",
                font=("Impact" , 25),
                fg="#FFFFFF", 
                bg="#000000",
                pady=15,
                anchor="center",
                justify="center"
                )
title.pack()

caution = tk.Label(window,
                text="With this application you can simply encode your messages into a picture",
                
                font=("Arial" , 12),
                fg="#FFFFFF", 
                bg="#000000",
                pady=5,
                anchor="center",
                justify="center",
                )
caution2 = tk.Label(window,
                text="Notice: Given key should be remembered for decoding",
                
                font=("Arial" , 13 , "bold"),
                fg="#FFFFFF", 
                bg="#000000",
                pady=5,
                anchor="center",
                justify="center",
                )

caution.pack()
caution2.pack()
path_label = None
path = None
flag = True
error = None
pages = []

def next_page(page_number):
    for page in pages:
        page.pack_forget()
    pages[page_number].pack()


#page1
page1 = tk.Frame(window , bg = "#000000")



def select_file():
    global path_label
    if path_label is not None:
        path_label.destroy()
        
    file_path = filedialog.askopenfilename(
        title="Select your image",
        
        filetypes=[("Image files" , "*.png *.jpg")]
    )
    if not file_path:
         return
    global img
    img = Image.open(file_path).convert("RGBA")
    path_label = tk.Label(page1,
        text = file_path,
        bg = "#000000",
        fg = "#7d7d7d",
        pady=10,
        font = ("Arial" , 10 , "bold"),
        
    )
    path_label.pack()
    global path
    path = file_path
    next_b()
    
file_button = tk.Button(page1,
                        text="Select your picture",
                        pady= 3,
                        bg="#ffffff",
                        fg="#000000",
                        command=select_file
                        )
page1.pack(anchor="w" , padx=20)
file_button.pack(side="left")


def next_b():
    global flag
    if flag == False:
        return None
    tk.Button(page1,
                        text="Next",
                        bg="#ffffff",
                        fg="#000000",
                        pady= 2 ,
                        command=lambda: next_page(1)
                    ).pack(anchor= "s" , side="bottom")
    flag = False
page2 = tk.Frame(window , bg = "#000000")
label = tk.Label(page2 ,
                      bg= "black" ,
                      fg= "white" ,
                      font=("Arial" , 10 , "bold"),
                      text= "Enter your message:",
                      anchor="w"
                          )
label2 = tk.Label(page2 ,
                      bg= "black" ,
                      fg= "white" ,
                      font=("Arial" , 10 , "bold"),
                      text= "Enter your key:",
                      anchor="w"
                          )
text_box = tk.Text(
     page2,
      bg= "#000000",
      fg= "#ffffff",
      width=70,
      height=10
        )
key_box = tk.Entry(
      page2,
      bg= "#000000",
      fg= "#ffffff",
      width=50,
        )
def code_get():
    code = text_box.get("1.0" , "end-1c")
    try:
        key = int(key_box.get())
    except:
        global error
        if error is not None:
            error.destroy()
        error = tk.Label(window , text="key should be a number!")
        error.pack()
        next_page(1)
        key_box.delete(0 , tk.END)
        return 0

        
    clen = len(code)
    global img
    e.encoder(code , clen , key , img)
    img.save("Encoded.png")
page2.pack()
label.pack()
text_box.pack()
label2.pack()
key_box.pack()
def code():
    
    if code_get() != 0:
        next_page(2)
tk.Button(page2,
                        text="Next",
                        bg="#ffffff",
                        fg="#000000",
                        pady= 2 ,
                        command=code
                        ).pack(anchor= "s" , side="bottom")

page3 = tk.Frame(window , bg = "#000000")
page3.pack()
tk.Label(page3 , text="your image saved\nEncoded.png" ,
            font=("Impact" , 25)).pack(anchor="center")


pages = [page1 , page2 , page3]
next_page(0)
window.mainloop()