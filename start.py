from tkinter import *

root = Tk()
root.title("Device Security Quiz")
root.geometry("600x600")
root.config(background="#fff292")

def clickStart():
    imageLabel.destroy()
    welcomeLabel.destroy()
    introLabel.destroy()
    startButton.destroy()

logo = PhotoImage(file="logo_brown.png")

imageLabel = Label(
    root,
    image=logo,
    background="#fff292"
)
imageLabel.pack()

welcomeLabel = Label(
    root,
    text="Welcome to\n" "Device Security Quiz",
    font =("Bahnschrift SemiBold", 26),
    fg="#000000",
    background="#fff292",
)
welcomeLabel.pack()

introLabel = Label(
    root,
    text="The fun way to practice your knowledge about\n malware and other malicious attacks\n inside your device",
    background="#ffffff",
    font=("Bahnschrift Light SemiCondensed", 18),
    bg="#fff292",
    fg="#3d261f",
    justify="center"
)
introLabel.pack(pady=20)

startButton = Button(
    root,
    text="GET STARTED!",
    fg="#ffffff",
    bg="#ea2a2a",
    activebackground="#ffbd59",
    font=("Bahnschrift Light Condensed", 20),
    relief=FLAT,
    padx=200,
)
startButton.config(command=clickStart)
startButton.pack()

root.mainloop()