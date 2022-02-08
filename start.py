import tkinter as tk
from tkinter import *
import random

root = tk.Tk()
root.title("Device Security Quiz")
root.geometry("600x600")
root.config(background="#fff292")

questions = [
    "Below are steps in scanning antivirus. \nRearrange them in the correct sequence. \n\n a. Scan the selected file \n b. Choose an antivirus program \n c. Wait While the program is scanning and the result is produced \n d. Select the file that need to be scanned",
    "How often should antivirus software be updated \n(the best way to protect computers?",
    "The #1 thing you can do to avoid malware is: ",
    "In the address portion of a website, what prefix \nindicates your communications are being encrypted during transit.",
    "How does identity theft cause problems for online users?",
    "What wouldn't you do if you know your computer is \nsuspect by malware?",
    "The mouse on your computer screen starts to move around \non its own and click on things on your desktop. What do you do?",
    "It is a type of malicious software that disguises itself \nas a legitimate file or program"
]

answers = [["d-b-a-c",
            "b-d-a-c",
            "a-c-b-d",
            "c-a-d-b"],
           ["Monthly",
            "Every 3 months",
            "Annually",
            "Never"],
           ["Install antivirus software and keep it updated",
            "Don't open email attachments'",
            "Don't download anything from the web'",
            "Be friendly always"],
           ["Http://",
            "Https://",
            "Ftp://",
            "Tcp://"],
           ["Steals social security",
            "Locates where you live and all information",
            "Steals bank information",
            "All of the above"],
           ["Stop doing any online activity that requires your username, \npassword, and other personal information.",
            "Keep shopping, banking, using every account about online activity",
            "Try to use anti-virus and anti-spyware software, \nand a firewall to defend the malware",
            "Try to call a professional help"],
           ["Disconnect your computer from the network",
            "Unplug your mouse",
            "Turn your computer off",
            "Don’t do anything"],
           ["Trojan Horse",
            "Worms",
            "Spyware",
            "Ransomware"]]

cor_answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]
user_answer = []

indexes=[]
def gen():
    global indexes
    while (len(indexes) < 8):
        x = random.randint(0, 7)
        if x in indexes:
            continue
        else:
            indexes.append(x)


ques = 1

def calc():
    global indexes,user_answer,cor_answers
    x = 0
    for i in indexes:
        if user_answer[x] == cor_answers[i]:
            cor_lbl = Label(
                root,
                text="Correct",
                font=("Consolas", 16),
                width=200,
                justify="center",
                background="green",
            )
            cor_lbl.pack()
        else:
            wro_lbl = Label(
                root,
                text="Incorrect",
                font=("Consolas", 16),
                width=200,
                justify="center",
                background="red",
            )
            wro_lbl.pack()


def selected():
    global radiovar, user_answer, cor_answers
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 8:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers[indexes[ques]][0]
        r2['text'] = answers[indexes[ques]][1]
        r3['text'] = answers[indexes[ques]][2]
        r4['text'] = answers[indexes[ques]][3]
        ques += 1
    else:
        pass


def startquiz():

    gen()

    global lblQuestion, r1, r2, r3, r4

    greeting = tk.Label(text="Device Security Quiz",
                        foreground="#E3170A",
                        background="#FCF6B1",
                        width=70,
                        font=("Consolas", 20)
                        )
    greeting.pack(pady=(0, 50))

    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        foreground="#ffffff",
        background="#E03616",
        font=("Consolas", 12),
        justify="center",
        wraplength=650
    )
    lblQuestion.pack(pady=(0,50))

    global radiovar
    radiovar = StringVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers[indexes[0]][0],
        font=("Consolas", 11),
        bg="#FCF6B1",
        value=0,
        variable=radiovar,
        command=selected
    )
    r1.pack(pady=(0, 20))

    r2 = Radiobutton(
        root,
        text=answers[indexes[0]][1],
        font=("Consolas", 11),
        bg="#FCF6B1",
        value=1,
        variable=radiovar,
        command=selected
    )
    r2.pack(pady=(0, 20))

    r3 = Radiobutton(
        root,
        text=answers[indexes[0]][2],
        font=("Consolas", 11),
        bg="#FCF6B1",
        value=2,
        variable=radiovar,
        command=selected
    )
    r3.pack(pady=(0, 20))

    r4 = Radiobutton(
        root,
        text=answers[indexes[0]][3],
        font=("Consolas", 11),
        bg="#FCF6B1",
        value=3,
        variable=radiovar,
        command=selected
    )
    r4.pack(pady=(0, 20))


def clickStart():
    imageLabel.destroy()
    welcomeLabel.destroy()
    introLabel.destroy()
    startButton.destroy()
    startquiz()

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