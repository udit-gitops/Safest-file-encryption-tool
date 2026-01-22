# Secure File Encryption Tool

This project is a desktop-based application developed to securely encrypt, decrypt, and edit files in an offline environment. The main aim of the project is to ensure that sensitive data remains protected on the local system without relying on internet connectivity or third-party services.
The application was developed during an internship at DRDO with a focus on secure file handling and controlled data access.



## Project Description

In many secure environments, especially defence and research setups, internet access is either restricted or completely unavailable. At the same time, sensitive files still need to be stored, modified, and protected from unauthorized access.

This project addresses that problem by providing a standalone desktop application that allows users to encrypt files using a password, decrypt them only when required, and securely edit encrypted files without permanently exposing the original data in plain text.

The tool works completely offline and gives the user full control over where files are stored and how they are accessed.



## Key Features

- File encryption and decryption using password-based security  
- Secure editing of encrypted files without saving plaintext permanently  
- Offline operation (no internet dependency)  
- User-defined output file location  
- Simple and easy-to-use graphical interface  
- Authentication check for incorrect passwords or tampered files  



## Technologies Used

- Python  
- Tkinter and ttkbootstrap (GUI)  
- AES encryption  
- PBKDF2 for key derivation  
- PyCryptodome library  
- PyInstaller for executable generation  



## How the Application Works

1. The user selects a file to encrypt or decrypt  
2. A passphrase is entered by the user  
3. The passphrase is converted into a secure encryption key using PBKDF2  
4. AES encryption is applied to the file data  
5. The encrypted or decrypted file is saved at the selected location  
6. For secure editing, the file is temporarily decrypted, edited, and re-encrypted automatically  



## Running the Project

### Using Python
```bash
python main.py
