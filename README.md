# Encryption_Decryption_GUI
The provided code is a simple encryption and decryption application using the Tkinter library in Python. It allows the user to encrypt and decrypt text using a secret key. Here's a breakdown of how the code works:

The necessary modules are imported: base64 for encoding and decoding text, and the Tkinter modules for creating the graphical user interface.

Two functions are defined: encrypt_text() and decrypt_text(). These functions handle the encryption and decryption processes, respectively.

In the encrypt_text() function:

The user's input password is checked. If it matches the expected password ("1234"), the encryption process continues.
The input text is retrieved from the text1 widget and stripped of leading and trailing whitespace.
The input text is encoded as ASCII and then base64 encoded using the base64.b64encode() function.
The encrypted text is displayed in a new window (screen1) and can be saved to a file using the save_encrypted() function.
In the decrypt_text() function:

The user's input password is checked. If it matches the expected password ("1234"), the decryption process continues.
The input text is retrieved from the text1 widget and stripped of leading and trailing whitespace.
The input text is base64 decoded using the base64.b64decode() function and then decoded as ASCII.
The decrypted text is displayed in a new window (screen2) and can be saved to a file using the save_decrypted() function.
The choose_file() function is responsible for opening a file dialog and allowing the user to select a text file. The contents of the selected file are then displayed in the text1 widget for further encryption or decryption.

The reset() function clears the text1 widget and the secret key entry field (key_entry).

The toggle_key_visibility() function toggles the visibility of the secret key entry field based on the state of the "Show Key" check button.

The Tkinter window is created (screen) with the necessary labels, text fields, buttons, and check buttons.

The main event loop is started with mainloop(), which allows the user to interact with the application.
