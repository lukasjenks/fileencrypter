from cryptography.fernet import Fernet
from tkinter import Tk, Label, LabelFrame, Button, Entry, IntVar, END, W, E, Frame
import tkinter
        
global sec
sec = 'f51M4ZGQzPtdWP6zO9twyftG1hfLs50FRcJcIvwKv1Q='
sec = bytes(sec.encode('utf-8'))
f = Fernet(sec) #type: <cryptography.fernet.Fernet object>

#String -> String
def encrypt(thisString):
    encryptedString = f.encrypt(bytes(thisString.encode('utf-8')))
    encryptedString = str(encryptedString).encode('utf-8')
    return encryptedString #type = <class 'string'>

#String -> String
def decrypt(encryptedString):
    encryptedBytes = bytes(encryptedString.encode('utf-8'))
    decryptedBytes = f.decrypt(encryptedBytes)
    decryptedString = str(decryptedBytes).encode('utf-8')
    return decryptedString #type = <class 'string'>

def e():
    log_file = open("log.txt","r")
    decrypted_log_contents = log_file.read()
    log_file.close()
    open("log.txt", "w").close()
    encrypted_log_contents = encrypt(decrypted_log_contents)
    log_file = open("log.txt","w")
    log_file.write(encrypted_log_contents)
    log_file.close()
    
def d():
    log_file = open("log.txt","r")
    encrypted_log_contents = log_file.read()
    log_file.close()
    open("log.txt","w").close()
    decrypted_log_contents = decrypt(encrypted_log_contents)
    log_file = open("log.txt","w")
    log_file.write(decrypted_log_contents)
    log_file.close()

def close_window():
    top.destroy()
    
top = tkinter.Tk()
#Code to add widgets will go here...
labelframe = LabelFrame(top, width=600, height=600, text="ENCRYPTION MODULE 1.0")
labelframe.pack()
left = Label(labelframe, text="Use the buttons below to encrypt/decrypt log")
left.pack()
encrypt_button = Button(top,text="Encrypt",command=e)
encrypt_button.pack()
decrypt_button = Button(top,text="Decrypt",command=d)
decrypt_button.pack()
quit_button = Button(top,text="Quit",command=close_window)
quit_button.pack()
top.geometry('300x200')
top.title("Lukas' Encryption Module")
top.mainloop()
