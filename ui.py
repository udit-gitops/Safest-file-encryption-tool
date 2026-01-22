import tkinter as tk
from tkinter import filedialog, messagebox, Text  # Text comes from tkinter

from ttkbootstrap.widgets import Frame, Button, Label, Entry
from encryption_utils import encrypt_file, decrypt_file, overwrite_encrypted_file



class HomeScreen(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill='both', expand=True)

        Label(self, text="Encrypted File Utility", font=("Poppins Semibold", 20)).pack(pady=20)

        Button(self, text="Encrypt File", command=self.encrypt).pack(pady=10)
        Button(self, text="Decrypt File", command=self.decrypt).pack(pady=10)
        Button(self, text="Secure Edit", command=self.secure_edit).pack(pady=10)

    def get_password(self):
        pw_window = tk.Toplevel(self)
        pw_window.title("Enter Password")
        Label(pw_window, text="Password:").pack(pady=5)
        pw_entry = Entry(pw_window, show="*")
        pw_entry.pack(pady=5)

        def submit():
            self.password = pw_entry.get()
            pw_window.destroy()

        Button(pw_window, text="Submit", command=submit).pack(pady=10)
        self.wait_window(pw_window)
        return getattr(self, 'password', None)

    def encrypt(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            password = self.get_password()
            if password:
                save_path = filedialog.asksaveasfilename(defaultextension=".enc")
                if save_path:
                    encrypt_file(file_path, save_path, password)
                    messagebox.showinfo("Done", f"Encrypted and saved to:\n{save_path}")

    def decrypt(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            password = self.get_password()
            if password:
                save_path = filedialog.asksaveasfilename(defaultextension=".dec")
                if save_path:
                    try:
                        decrypt_file(file_path, save_path, password)
                        messagebox.showinfo("Done", f"Decrypted and saved to:\n{save_path}")
                    except ValueError as e:
                        messagebox.showerror("Error", str(e))

    def secure_edit(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            password = self.get_password()
            if password:
                try:
                    decrypted_content = decrypt_file(file_path, None, password, return_data=True)
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
                    return

                edit_window = tk.Toplevel(self)
                edit_window.title("Secure Edit")
                text_box = Text(edit_window, wrap='word')
                text_box.pack(fill='both', expand=True)
                text_box.insert('1.0', decrypted_content)

                def save_changes():
                    updated_content = text_box.get('1.0', 'end-1c')
                    overwrite_encrypted_file(file_path, updated_content, password)
                    messagebox.showinfo("Saved", "Changes saved and re-encrypted successfully.")
                    edit_window.destroy()

                Button(edit_window, text="Save Changes", command=save_changes).pack(pady=5)
