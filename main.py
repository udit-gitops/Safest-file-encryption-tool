from ui import HomeScreen
import ttkbootstrap as ttk

if __name__ == '__main__':
    app = ttk.Window(themename="morph")
    app.title("Encrypted File Utility")
    app.geometry("600x400")
    HomeScreen(app)
    app.mainloop()