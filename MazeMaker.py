from tkinter import Tk, PhotoImage

from src.Presentation.AppMediator import AppMediator

if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')

    photo = PhotoImage(file="./res/logo.png")
    root.iconphoto(False, photo)

    app = AppMediator(root)
    app.display()
    app.tick()

    root.mainloop()
