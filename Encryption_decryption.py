import base64
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Function to encrypt the text
def encrypt_text():
    password = code.get()
    if password == "1234":
        # Retrieve the message from the input text box
        message = text1.get(1.0, END).strip()
        if message:
            # Encode the message to ASCII and then encode it using base64
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt_text = base64_bytes.decode("ascii")

            # Create a new window for displaying the encrypted text
            screen1 = Toplevel(screen)
            screen1.title("Encryption")
            screen1.geometry("420x300")
            screen1.configure(bg="black")

            # Function to save the encrypted text to a file
            def save_encrypted():
                file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
                if file_path:
                    try:
                        with open(file_path, "w") as file:
                            file.write(encrypt_text)
                        messagebox.showinfo("Save Successful", "Encrypted text saved successfully.")
                    except Exception as e:
                        messagebox.showerror("Save Error", str(e))

            # Label for displaying the encrypted text
            Label(screen1, text="Text Encrypted", font="ariel 21 bold").place(x=10, y=10)
            text2 = Text(screen1, font="28", bd=4, wrap=WORD)
            text2.place(x=10, y=70, width=390, height=160)
            text2.insert(END, encrypt_text)

            # Button to save the encrypted text
            Button(screen1, text="Save Encrypted Text", font="ariel 15 bold", fg="green", command=save_encrypted).place(x=80, y=240, width=250)
        else:
            messagebox.showerror("ERROR", "Please enter text for encryption")
    elif password == "":
        messagebox.showerror("ERROR", "Please Enter Secret Key")
    elif password != "1234":
        messagebox.showerror("Oops", "Invalid Secret Key")

# Function to decrypt the text
def decrypt_text():
    password = code.get()
    if password == "1234":
        # Retrieve the message from the input text box
        message = text1.get(1.0, END).strip()
        if message:
            # Decode the message using base64 and then decode it from ASCII
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt_text = base64_bytes.decode("ascii")

            # Create a new window for displaying the decrypted text
            screen2 = Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("420x300")
            screen2.configure(bg="black")

            # Function to save the decrypted text to a file
            def save_decrypted():
                file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
                if file_path:
                    try:
                        with open(file_path, "w") as file:
                            file.write(decrypt_text)
                        messagebox.showinfo("Save Successful", "Decrypted text saved successfully.")
                    except Exception as e:
                        messagebox.showerror("Save Error", str(e))

            # Label for displaying the decrypted text
            Label(screen2, text="Text Decrypted", font="ariel 21 bold").place(x=10, y=10)
            text2 = Text(screen2, font="28", bd=4, wrap=WORD)
            text2.place(x=10, y=70, width=390, height=160)
            text2.insert(END, decrypt_text)

            # Button to save the decrypted text
            Button(screen2, text="Save Decrypted Text", font="ariel 15 bold", fg="green", command=save_decrypted).place(x=80, y=240, width=250)
        else:
            messagebox.showerror("ERROR", "Please enter text for decryption")
    elif password == "":
        messagebox.showerror("ERROR", "Please Enter Secret Key")
    elif password != "1234":
        messagebox.showerror("Oops", "Invalid Secret Key")

# Function to choose a file and load its content into the input text box
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                text1.delete(1.0, END)
                text1.insert(END, file.read())
        except Exception as e:
            messagebox.showerror("File Error", str(e))

# Function to reset the input text box and secret key
def reset():
    text1.delete(1.0, END)
    code.set("")

# Function to toggle the visibility of the secret key
def toggle_key_visibility():
    if show_key.get():
        key_entry.config(show="")
    else:
        key_entry.config(show="*")

# Create the main window
screen = Tk()
screen.geometry("420x420")
screen.title("Encryption and Decryption")
screen.configure(bg="black")

# Label for "Enter Text"
Label(screen, text="Enter Text", font="Ariel 20 bold", bg="white").place(x=10, y=15)
# Input text box for entering the text
text1 = Text(screen, font="15")
text1.place(x=10, y=55, width=400, height=100)

# Label for "Enter Secret Key"
Label(screen, text="Enter Secret Key", font="Ariel 15 bold").place(x=130, y=160)

# Checkbutton for toggling the visibility of the secret key
show_key = BooleanVar()
show_key_checkbutton = Checkbutton(screen, text="Show Key", variable=show_key, command=toggle_key_visibility)
show_key_checkbutton.place(x=290, y=205)

# Entry field for entering the secret key
code = StringVar()
key_entry = Entry(textvariable=code, bd=5, font="5", show="*")
key_entry.place(x=50, y=200)

# Buttons
Button(screen, text="Encrypt Text", font="ariel 20 bold", fg="Red", command=encrypt_text).place(x=15, y=280, width=190)
Button(screen, text="Decrypt Text", font="ariel 20 bold", fg="Red", command=decrypt_text).place(x=220, y=280, width=190)
Button(screen, text="Choose File", font="ariel 8 bold", fg="green", command=choose_file).place(x=160, y=20, width=100)
Button(screen, text="Reset", font="ariel 15 bold", fg="blue", command=reset).place(x=160, y=370, width=100)

mainloop()
