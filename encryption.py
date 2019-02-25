# Import necessary packages
from cryptography.fernet import Fernet
from tkinter import Tk, Label, LabelFrame, Button, Entry, IntVar, END, W, E, Frame
import tkinter

# Initialize seed and fernet object for encryption
global sec
sec = 'f51M4ZGQzPtdWP6zO9twyftG1hfLs50FRcJcIvwKv1Q='
sec = bytes(sec.encode('utf-8'))
f = Fernet(sec) #type: <cryptography.fernet.Fernet object>
    
# Encrypt plaintext string to ciphertext string
def encrypt(thisString):
    encryptedString = f.encrypt(bytes(thisString.encode('utf-8')))
    encryptedString = str(encryptedString).encode('utf-8')
    return encryptedString #type = <class 'string'>

# Decrypt ciphertext string to plaintext string
def decrypt(encryptedString):
    encryptedBytes = bytes(encryptedString.encode('utf-8'))
    decryptedBytes = f.decrypt(encryptedBytes)
    decryptedString = str(decryptedBytes).encode('utf-8')
    return decryptedString #type = <class 'string'>

# Open log.txt, read plaintext contents and overwrite with
# equivalent ciphertext
def e():
    log_file = open("log.txt","r")
    decrypted_log_contents = log_file.read()
    log_file.close()
    open("log.txt", "w").close()
    encrypted_log_contents = encrypt(decrypted_log_contents)
    log_file = open("log.txt","w")
    log_file.write(encrypted_log_contents)
    log_file.close()

    # Erase existing output message and replace with new
    global output_message
    output_message.pack_forget()
    output_message = Label(output_area, text="Successfully encrypted file")
    output_message.pack()

# Open log.txt, read ciphertext contents and overwrite with
# equivalent ciphertext
def d():
    log_file = open("log.txt","r")
    encrypted_log_contents = log_file.read()
    log_file.close()
    open("log.txt","w").close()
    decrypted_log_contents = decrypt(encrypted_log_contents)
    log_file = open("log.txt","w")
    log_file.write(decrypted_log_contents)
    log_file.close()

    # Erase existing output message and replace with new
    global output_message
    output_message.pack_forget()
    output_message = Label(output_area, text="Successfully decrypted file")
    output_message.pack()
    
# Tk function to close the program window
def close_window():
    top.destroy()

# Main script to initialize program window and
# it's interactive elements and labels

global top
global output_area
global output_message

if __name__=='__main__':
    top = tkinter.Tk()
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
    output_area = LabelFrame(top, width=200, height=100)
    output_area.pack()
    output_message = Label(output_area, text="Ready")
    output_message.pack()
    top.geometry('400x300')
    top.title("File Encrypter")
    top.mainloop()
