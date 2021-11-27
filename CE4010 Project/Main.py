import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from rc4_encryption import *
from display_csvfile import *
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Create canvas
HEIGHT = 600
WIDTH = 500
bgcolor = '#80c1ff'
frames_width = 0.75
frames_positionx = 0.5
top_frame_height = 0.2
top_frame_positiony = 0.02
middle_frame_height = top_frame_height 
middle1_frame_positiony = top_frame_height
middle2_frame_positiony = top_frame_height + top_frame_positiony + middle_frame_height
bottom_frame_height = 0.3
bottom_frame_positiony = top_frame_height + 2*top_frame_positiony + 2*middle_frame_height

root = tk.Tk()
root.title("Attack on WEP with ARC4 encryption")
root.resizable(0, 0)                      #to lock the window to the default size 

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#Create top frame
top_frame = tk.Frame(root)
top_frame.place(relx = frames_positionx, rely = top_frame_positiony, relwidth = frames_width, relheight = top_frame_height, anchor = 'n')

#Create middle1 blue frame
middle_frame1 = tk.Frame(root,bg = bgcolor,bd=10)
middle_frame1.place(relx = frames_positionx, rely = middle1_frame_positiony, relwidth = frames_width, relheight = middle_frame_height, anchor = 'n')

#Create middle2 blue frame
middle_frame2 = tk.Frame(root,bg = bgcolor,bd=10)
middle_frame2.place(relx = frames_positionx, rely = middle2_frame_positiony, relwidth = frames_width, relheight = middle_frame_height, anchor = 'n')

#Create bottom blue frame
lower_frame = tk.Frame(root, bg = bgcolor,bd=15)
lower_frame.place(relx = frames_positionx, rely = bottom_frame_positiony, relwidth = frames_width, relheight = bottom_frame_height, anchor = 'n')

####------------------------------------------------------------------------------------------------------------------------------------------------------------
## Top Frame: User Input
buttons_font = ('courier', 14, "bold")
buttons_height = 1
buttons_width = 15

#global variables
WEP_key = ""
plain_text = ""
enc_plainText = ""

#obtaining key for RC4 and key retrieval algorithm
tk.Label(top_frame, text="Input key (Hex and multiple of 2 chars): ").grid(row=0)

e1 = tk.Entry(top_frame,width = 20)
e1.grid(row=0, column=1)

def get_key():
    global WEP_key
    key = e1.get()
    
    if(len(key)%2 == 0):
        try:
            i=0
            while i < len(key):
            #retrieve each byte of keys(2 characters) and convert to int
                keyByte = int(key[i] + key[i+1], 16)
                i += 2
            WEP_key = key
            Result['text'] = "Key entered!"
            Result['font'] = buttons_font
        except:
            Result['text'] = "Key is supposed to be\n in Hexadecimal"
            Result['font'] = buttons_font
    else:
        Result['text'] = "Please choose an appropriate \nlength for the key"
        Result['font'] = buttons_font
    return key

    
tk.Button(top_frame, 
          text='Enter', command = get_key).grid(row=0, column=50,
                                    sticky=tk.W, 
                                    pady=4)

#obtaining plaintext for RC4 algorithm
tk.Label(top_frame, text="Input plaintext for RC4 encryption:").grid(row=1)

e12 = tk.Entry(top_frame,width = 20)
e12.grid(row=1, column=1)

def get_plain_text():
    global plain_text
    text = e12.get()
    plain_text = text
    Result['text'] = "Plaintext entered!"
    Result['font'] = buttons_font

tk.Button(top_frame, 
          text='Enter', command = get_plain_text).grid(row=1, column=50,
                                    sticky=tk.W, 
                                    pady=4)

####------------------------------------------------------------------------------------------------------------------------------------------------------------
## Middle Frame1: RC4 Implementation Buttons
tk.Label(middle_frame1, text="RC4 Implementation").grid(row=0)
def encrypt():
    global WEP_key, plain_text, enc_plainText
    if(WEP_key!="" and plain_text != ""):
        enc_plainText = rc4_encrypt(WEP_key, plain_text)
        Result['text'] = "Ciphertext is " + enc_plainText
    elif (WEP_key==""):
        Result['text'] = "Key is empty"
        Result['font'] = buttons_font
    elif (plain_text==""):
        Result['text'] = "Plaintext is empty"
        Result['font'] = buttons_font

def decrypt():
    global WEP_key, plain_text, enc_plainText
    if(WEP_key!="" and enc_plainText != ""):
        text = rc4_decrypt(WEP_key, enc_plainText)
        if(plain_text==text):
            Result['text'] = "Decrypted plaintext is: " + text + "\n Decryption is successful!"
        else:
            Result['text'] = "Decrypted plaintext is: " + text + "\n Decryption is unsuccessful!\n Something went wrong."     
    elif (WEP_key==""):
        Result['text'] = "Key is empty"
        Result['font'] = buttons_font
    elif (enc_plainText==""):
        Result['text'] = "Plaintext is not encrypted yet"
        Result['font'] = buttons_font
        
button = tk.Button(middle_frame1,text ='Encrypt',font = buttons_font, height = buttons_height, width = buttons_width, relief=tk.RAISED,command=encrypt)
button.place(relx=0,rely=0.5,relwidth = 0.5,relheight = 0.5)
button = tk.Button(middle_frame1,text ='Decrypt',font = buttons_font, height = buttons_height, width = buttons_width, relief=tk.RAISED,command=decrypt)
button.place(relx=0.5,rely=0.5,relwidth = 0.5,relheight = 0.5)


####------------------------------------------------------------------------------------------------------------------------------------------------------------
## Middle Frame2: WEP Packet Generation and Key Retrieval Buttons
tk.Label(middle_frame2, text="WEP Packet Generation and Key Retrieval").grid(row=0)
def generate():
    if(WEP_key!=""):
        generate_key_packets(WEP_key)
        display_csvfile()
        Result['text'] = "Packets simulated!"
        Result['font'] = buttons_font
    else:
        Result['text'] = "Key is empty"
        Result['font'] = buttons_font
    
def retrieve():
    try:
        open("WEPOutputSim.csv")
        Result['text'] = "Retrieved key: " + retrieve_key()
        Result['font'] = buttons_font
    except:
        Result['text'] = "There is no packets\n to work with!"
        Result['font'] = buttons_font

button = tk.Button(middle_frame2,text ='Generate',font = buttons_font, height = buttons_height, width = buttons_width, relief=tk.RAISED,command=generate)
button.place(relx=0,rely=0.5,relwidth = 0.5,relheight = 0.5)
button = tk.Button(middle_frame2,text ='Retrieve Key',font = buttons_font, height = buttons_height, width = buttons_width, relief=tk.RAISED,command=retrieve)
button.place(relx=0.5,rely=0.5,relwidth = 0.5,relheight = 0.5)

####------------------------------------------------------------------------------------------------------------------------------------------------------------
##Bottom Frame: Display text

Result = tk.Label(lower_frame)
Result.place(relx=0,relwidth = 1,relheight = 1)

root.mainloop()
