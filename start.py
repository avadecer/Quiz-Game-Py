import tkinter as tk
from tkinter import *
import datetime
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
import tkinter.font as font

root = tk.Tk()
root.title("Device Security Quiz")
root.geometry("700x600")
root.config(background="#fff292")
root.resizable(False, False)


def center_window_on_screen():
    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def next_to_Q2():
    frame1.forget()
    frame2.pack(fill='both', expand=1)


def back_to_Q1():
    frame1.pack(fill='both', expand=1)
    frame2.forget()


def next_to_Q3():
    frame3.pack(fill='both', expand=1)
    frame2.forget()


def back_to_Q2():
    frame2.pack(fill='both', expand=1)
    frame3.forget()


def next_to_Q4():
    frame4.pack(fill='both', expand=1)
    frame3.forget()


def back_to_Q3():
    frame3.pack(fill='both', expand=1)
    frame4.forget()


def next_to_Q5():
    frame5.pack(fill='both', expand=1)
    frame4.forget()


def back_to_Q4():
    frame4.pack(fill='both', expand=1)
    frame5.forget()


def next_to_Q6():
    frame6.pack(fill='both', expand=1)
    frame5.forget()


def back_to_Q5():
    frame5.pack(fill='both', expand=1)
    frame6.forget()


def next_to_Q7():
    frame7.pack(fill='both', expand=1)
    frame6.forget()


def back_to_Q6():
    frame6.pack(fill='both', expand=1)
    frame7.forget()


def next_to_Q8():
    frame8.pack(fill='both', expand=1)
    frame7.forget()


def back_to_Q7():
    frame7.pack(fill='both', expand=1)
    frame8.forget()


def next_to_Q9():
    frame9.pack(fill='both', expand=1)
    frame8.forget()


def back_to_Q8():
    frame8.pack(fill='both', expand=1)
    frame9.forget()


def next_to_Q10():
    frame10.pack(fill='both', expand=1)
    frame9.forget()


def back_to_Q9():
    frame9.pack(fill='both', expand=1)
    frame10.forget()


def next_to_Q11():
    frame11.pack(fill='both', expand=1)
    frame10.forget()


def back_to_Q10():
    frame10.pack(fill='both', expand=1)
    frame11.forget()


def next_to_Q12():
    frame12.pack(fill='both', expand=1)
    frame11.forget()


def back_to_Q11():
    frame11.pack(fill='both', expand=1)
    frame12.forget()


def next_to_Q13():
    frame13.pack(fill='both', expand=1)
    frame12.forget()


def back_to_Q12():
    frame12.pack(fill='both', expand=1)
    frame13.forget()


def next_to_Q14():
    frame14.pack(fill='both', expand=1)
    frame13.forget()


def back_to_Q13():
    frame13.pack(fill='both', expand=1)
    frame14.forget()


def next_to_Q15():
    frame15.pack(fill='both', expand=1)
    frame14.forget()


def back_to_Q14():
    frame14.pack(fill='both', expand=1)
    frame15.forget()


def to_score():
    frame16.pack(fill='both', expand=1)
    frame15.forget()
    scoreboard()


width, height = 700, 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

frame1 = tk.Frame(root)
frame1.configure(bg='light yellow')

frame2 = tk.Frame(root)
frame2.configure(bg='light yellow')

frame3 = tk.Frame(root)
frame3.configure(bg='light yellow')

frame4 = tk.Frame(root)
frame4.configure(bg='light yellow')

frame5 = tk.Frame(root)
frame5.configure(bg='light yellow')

frame6 = tk.Frame(root)
frame6.configure(bg='light yellow')

frame7 = tk.Frame(root)
frame7.configure(bg='light yellow')

frame8 = tk.Frame(root)
frame8.configure(bg='light yellow')

frame9 = tk.Frame(root)
frame9.configure(bg='light yellow')

frame10 = tk.Frame(root)
frame10.configure(bg='light yellow')

frame11 = tk.Frame(root)
frame11.configure(bg='light yellow')

frame12 = tk.Frame(root)
frame12.configure(bg='light yellow')

frame13 = tk.Frame(root)
frame13.configure(bg='light yellow')

frame14 = tk.Frame(root)
frame14.configure(bg='light yellow')

frame15 = tk.Frame(root)
frame15.configure(bg='light yellow')

frame16 = tk.Frame(root)
frame16.configure(bg='light yellow')

font_large = font.Font(family='Georgia', size='15', weight='bold')
font_small = font.Font(family='Georgia', size='12')


def q1Right():
    tk.Label(frame1, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q1Wrong():
    tk.Label(frame1, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q2Right():
    tk.Label(frame2, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q2Wrong():
    tk.Label(frame2, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q3Right():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q3Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q4Right():
    tk.Label(frame4, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q4Wrong():
    tk.Label(frame4, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q5Right():
    tk.Label(frame5, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q5Wrong():
    tk.Label(frame5, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q6Right():
    tk.Label(frame6, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q6Wrong():
    tk.Label(frame6, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q7Right():
    tk.Label(frame7, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q7Wrong():
    tk.Label(frame7, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q8Right():
    tk.Label(frame8, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q8Wrong():
    tk.Label(frame8, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q9Right():
    tk.Label(frame9, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q9Wrong():
    tk.Label(frame9, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q10Right():
    tk.Label(frame10, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q10Wrong():
    tk.Label(frame10, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q11Right():
    tk.Label(frame11, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q11Wrong():
    tk.Label(frame11, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q12Right():
    tk.Label(frame12, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q12Wrong():
    tk.Label(frame12, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q13Right():
    tk.Label(frame13, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q13Wrong():
    tk.Label(frame13, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q14Right():
    tk.Label(frame14, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q14Wrong():
    tk.Label(frame14, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


def q15Right():
    tk.Label(frame15, text='  Correct  ', font=font_large, background='#228B22', fg='white').place(x=300, y=500)


def q15Wrong():
    tk.Label(frame15, text='Incorrect', font=font_large, background='red', fg='white').place(x=300, y=500)


root.counter = 0


def correct_button_clicked():
    root.counter += 1


def scoreboard():
    lblhead = Label(root, text="Let's see how much you've got!", bg="#8B0000",
                    fg="#ffffff", width=80, font=("Lucida Calligraphy Italic", 30))
    lblhead.place(x=350, y=50, anchor="n")

    score = Label(text="Your Score\n" + str(root.counter) + " / 15", font=("Aharoni", 30))
    score.place(x=250, y=150)

    if root.counter >= 11:
        lblpass = Label(root, text="Great job!", bg="#A0522D",
                        fg="#ffffff", width=20, font=("Impact", 30))
        lblpass.place(x=350, y=400, anchor="s")

    else:
        lblfail = Label(root, text="Nice try!", bg="#A0522D",
                        fg="#ffffff", width=20, font=("Impact", 30))
        lblfail.place(x=350, y=400, anchor="s")

    tryagain = Button(text="TRY AGAIN", font=font_large)
    tryagain.place(x=690, y=500, anchor="se")

    def proginfo():
        prog = Label(root,
                     text="People behind the program:\n \n Ann Vergie Adecer\nPatricia Andy Aquino\nMa. Carmela Bolante\nJonalee Lorie Naife\n Angelique Grace Quiñones",
                     font=font_small, justify=LEFT)
        prog.place(x=20, y=450)

    info = Button(root, text="INFO", font=font_large, command=proginfo)
    info.place(x=690, y=570, anchor="se")


def startquiz():
    question1 = tk.Label(frame1, text='Below are steps in scanning antivirus.'
                                      ' \nRearrange them in the correct sequence. \n\n a. Scan the selected file \n '
                                      'b. Choose an antivirus program \n c. Wait While the program is scanning and the'
                                      'result is produced \n d. Select the file that need to be scanned',
                         font=font_large, bg='light yellow')

    def q1():
        q1A['state'] = tk.DISABLED
        q1B['state'] = tk.DISABLED
        q1C['state'] = tk.DISABLED
        q1D['state'] = tk.DISABLED

    q1A = tk.Button(frame1, text='A. d-b-a-c', font=font_large, bg='#FCF6B1', command=lambda: [q1Wrong(), q1()])
    q1B = tk.Button(frame1, text='B. b-d-a-c', font=font_large, bg='#FCF6B1',
                    command=lambda: [q1Right(), correct_button_clicked(), q1()])
    q1C = tk.Button(frame1, text='C. a-c-b-d', font=font_large, bg='#FCF6B1', command=lambda: [q1Wrong(), q1()])
    q1D = tk.Button(frame1, text='D. c-a-d-b', font=font_large, bg='#FCF6B1', command=lambda: [q1Wrong(), q1()])

    question1.pack(pady=20)
    q1A.place(x=120, y=250)
    q1B.place(x=120, y=350)
    q1C.place(x=470, y=250)
    q1D.place(x=470, y=350)

    btnNextQ2 = tk.Button(frame1, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q2)

    btnNextQ2.place(x=600, y=500)

    question2 = tk.Label(frame2,
                         text='How often should antivirus software be \nupdated (the best way to protect computers)?',
                         font=font_large, bg='light yellow')

    def q2():
        q2A['state'] = tk.DISABLED
        q2B['state'] = tk.DISABLED
        q2C['state'] = tk.DISABLED
        q2D['state'] = tk.DISABLED

    q2A = tk.Button(frame2, text='A. Monthly', font=font_large, bg='#FCF6B1',
                    command=lambda: [q2Right(), correct_button_clicked(), q2()])
    q2B = tk.Button(frame2, text='B. Every 3 months', font=font_large, bg='#FCF6B1', command=lambda: [q2Wrong(), q2()])
    q2C = tk.Button(frame2, text='C. Annually', font=font_large, bg='#FCF6B1', command=lambda: [q2Wrong(), q2()])
    q2D = tk.Button(frame2, text='D. Never', font=font_large, bg='#FCF6B1', command=lambda: [q2Wrong(), q2()])

    question2.pack(pady=20)
    q2A.place(x=120, y=150)
    q2B.place(x=120, y=250)
    q2C.place(x=470, y=150)
    q2D.place(x=470, y=250)

    btnBackQ1 = tk.Button(frame2, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q1)
    btnBackQ1.place(x=50, y=500)
    question3 = tk.Label(frame3, text='The #1 thing you can do to avoid malware is:', font=font_large,
                         bg='light yellow')

    def q3():
        q3A['state'] = tk.DISABLED
        q3B['state'] = tk.DISABLED
        q3C['state'] = tk.DISABLED
        q3D['state'] = tk.DISABLED

    q3A = tk.Button(frame3, text='A. Install antivirus software and keep it updated', font=font_large, bg='#FCF6B1',
                    command=lambda: [q3Right(), correct_button_clicked(), q3()])
    q3B = tk.Button(frame3, text='B. Do not open email attachments', font=font_large, bg='#FCF6B1',
                    command=lambda: [q3Wrong(), q3()])
    q3C = tk.Button(frame3, text='C. Do not download anything from the web.', font=font_large, bg='#FCF6B1',
                    command=lambda: [q3Wrong(), q3()])
    q3D = tk.Button(frame3, text='D. Be friendly always', font=font_large, bg='#FCF6B1',
                    command=lambda: [q3Wrong(), q3()])

    question3.pack(pady=20)
    q3A.pack(pady=20)
    q3B.pack(pady=20)
    q3C.pack(pady=20)
    q3D.pack(pady=20)

    btnNextQ3 = tk.Button(frame2, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q3)
    btnNextQ3.place(x=600, y=500)

    btnBackQ2 = tk.Button(frame3, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q2)
    btnBackQ2.place(x=50, y=500)

    question4 = tk.Label(frame4,
                         text='In the address portion of a website, what prefix indicates your \ncommunications are being encrypted during transit',
                         font=font_large, bg='light yellow')

    def q4():
        q4A['state'] = tk.DISABLED
        q4B['state'] = tk.DISABLED
        q4C['state'] = tk.DISABLED
        q4D['state'] = tk.DISABLED

    q4A = tk.Button(frame4, text='A. Http://', font=font_large, bg='#FCF6B1', command=lambda: [q4Wrong(), q4()])
    q4B = tk.Button(frame4, text='B. Https://', font=font_large, bg='#FCF6B1',
                    command=lambda: [q4Right(), correct_button_clicked(), q4()])
    q4C = tk.Button(frame4, text='C. Ftp://', font=font_large, bg='#FCF6B1', command=lambda: [q4Wrong(), q4()])
    q4D = tk.Button(frame4, text='D. Tcp://', font=font_large, bg='#FCF6B1', command=lambda: [q4Wrong(), q4()])

    question4.pack(pady=20)
    q4A.place(x=120, y=150)
    q4B.place(x=120, y=250)
    q4C.place(x=470, y=150)
    q4D.place(x=470, y=250)

    btnNextQ4 = tk.Button(frame3, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q4)
    btnNextQ4.place(x=600, y=500)

    btnBackQ3 = tk.Button(frame4, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q3)
    btnBackQ3.place(x=50, y=500)

    question5 = tk.Label(frame5, text='How does identity theft cause problems for online users?', font=font_large,
                         bg='light yellow')

    def q5():
        q5A['state'] = tk.DISABLED
        q5B['state'] = tk.DISABLED
        q5C['state'] = tk.DISABLED
        q5D['state'] = tk.DISABLED

    q5A = tk.Button(frame5, text='A. Steals social security', font=font_large, bg='#FCF6B1',
                    command=lambda: [q5Wrong(), q5()])
    q5B = tk.Button(frame5, text='B. Locates where you live and all information', font=font_large, bg='#FCF6B1',
                    command=lambda: [q5Wrong(), q5()])
    q5C = tk.Button(frame5, text='C. Steals bank information', font=font_large, bg='#FCF6B1',
                    command=lambda: [q5Wrong(), q5()])
    q5D = tk.Button(frame5, text='D. All of the above', font=font_large, bg='#FCF6B1',
                    command=lambda: [q5Right(), correct_button_clicked(), q5()])

    question5.pack(pady=20)
    q5A.pack(pady=20)
    q5B.pack(pady=20)
    q5C.pack(pady=20)
    q5D.pack(pady=20)

    btnNextQ5 = tk.Button(frame4, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q5)
    btnNextQ5.place(x=600, y=500)

    btnBackQ4 = tk.Button(frame5, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q4)
    btnBackQ4.place(x=50, y=500)

    question6 = tk.Label(frame6, text='What would you not do if you know your computer \nis suspect by malware?',
                         font=font_large, bg='light yellow')

    def q6():
        q6A['state'] = tk.DISABLED
        q6B['state'] = tk.DISABLED
        q6C['state'] = tk.DISABLED
        q6D['state'] = tk.DISABLED

    q6A = tk.Button(frame6,
                    text='A. Stop doing any online activity that requires your \nusername, password, and other personal information.',
                    font=font_large, bg='#FCF6B1', command=lambda: [q6Wrong(), q6()])
    q6B = tk.Button(frame6, text='B. Keep shopping, banking, using every account \nabout online activity.',
                    font=font_large, bg='#FCF6B1', command=lambda: [q6Right(), correct_button_clicked(), q6()])
    q6C = tk.Button(frame6,
                    text='C.Try to use anti-virus and anti-spyware software, \nand a firewall to defend the malware',
                    font=font_large, bg='#FCF6B1', command=lambda: [q6Wrong(), q6()])
    q6D = tk.Button(frame6, text='D. Try to call a professional help', font=font_large, bg='#FCF6B1',
                    command=lambda: [q6Wrong(), q6()])

    question6.pack(pady=20)
    q6A.pack(pady=20)
    q6B.pack(pady=20)
    q6C.pack(pady=20)
    q6D.pack(pady=20)

    btnNextQ6 = tk.Button(frame5, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q6)
    btnNextQ6.place(x=600, y=500)

    btnBackQ5 = tk.Button(frame6, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q5)
    btnBackQ5.place(x=50, y=500)

    def q7():
        q7A['state'] = tk.DISABLED
        q7B['state'] = tk.DISABLED
        q7C['state'] = tk.DISABLED
        q7D['state'] = tk.DISABLED

    question7 = tk.Label(frame7,
                         text='The mouse on your computer screen starts to move \naround on its own and click on things on \nyour desktop. What do you do?',
                         font=font_large, bg='light yellow')
    q7A = tk.Button(frame7, text='A. Disconnect your computer from the network', font=font_large, bg='#FCF6B1',
                    command=lambda: [q7Right(), correct_button_clicked(), q7()])
    q7B = tk.Button(frame7, text='B. Unplug your mouse', font=font_large, bg='#FCF6B1',
                    command=lambda: [q7Wrong(), q7()])
    q7C = tk.Button(frame7, text='C. Turn your computer off', font=font_large, bg='#FCF6B1',
                    command=lambda: [q7Wrong(), q7()])
    q7D = tk.Button(frame7, text='D. Don’t do anything', font=font_large, bg='#FCF6B1',
                    command=lambda: [q7Wrong(), q7()])

    question7.pack(pady=20)
    q7A.pack(pady=20)
    q7B.pack(pady=20)
    q7C.pack(pady=20)
    q7D.pack(pady=20)

    btnNextQ7 = tk.Button(frame6, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q7)
    btnNextQ7.place(x=600, y=500)

    btnBackQ6 = tk.Button(frame7, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q6)
    btnBackQ6.place(x=50, y=500)

    question8 = tk.Label(frame8,
                         text='It is a type of malicious software that disguises \nitself as a legitimate file or program',
                         font=font_large, bg='light yellow')

    def q8():
        q8A['state'] = tk.DISABLED
        q8B['state'] = tk.DISABLED
        q8C['state'] = tk.DISABLED
        q8D['state'] = tk.DISABLED

    q8A = tk.Button(frame8, text='A. Trojan Horse', font=font_large, bg='#FCF6B1',
                    command=lambda: [q8Right(), correct_button_clicked(), q8()])
    q8B = tk.Button(frame8, text='B. Worms', font=font_large, bg='#FCF6B1', command=lambda: [q8Wrong(), q8()])
    q8C = tk.Button(frame8, text='C. Spyware', font=font_large, bg='#FCF6B1', command=lambda: [q8Wrong(), q8()])
    q8D = tk.Button(frame8, text='D. Ransomware', font=font_large, bg='#FCF6B1', command=lambda: [q8Wrong(), q8()])

    question8.pack(pady=20)
    q8A.place(x=80, y=180)
    q8B.place(x=80, y=280)
    q8C.place(x=430, y=180)
    q8D.place(x=430, y=280)

    btnNextQ8 = tk.Button(frame7, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q8)
    btnNextQ8.place(x=600, y=500)

    btnBackQ7 = tk.Button(frame8, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q7)
    btnBackQ7.place(x=50, y=500)

    question9 = tk.Label(frame9,
                         text='It is a type of malware that restricts access to your \nown files. Often, payment is required \nfor the access to be returned',
                         font=font_large, bg='light yellow')

    def q9():
        q9A['state'] = tk.DISABLED
        q9B['state'] = tk.DISABLED
        q9C['state'] = tk.DISABLED
        q9D['state'] = tk.DISABLED

    q9A = tk.Button(frame9, text='A. Trojan Horse', font=font_large, bg='#FCF6B1', command=lambda: [q9Wrong(), q9()])
    q9B = tk.Button(frame9, text='B. Worms', font=font_large, bg='#FCF6B1', command=lambda: [q9Wrong(), q9()])
    q9C = tk.Button(frame9, text='C. Spyware', font=font_large, bg='#FCF6B1', command=lambda: [q9Wrong(), q9()])
    q9D = tk.Button(frame9, text='D. Ransomware', font=font_large, bg='#FCF6B1',
                    command=lambda: [q9Right(), correct_button_clicked(), q9()])

    question9.pack(pady=20)
    q9A.place(x=80, y=180)
    q9B.place(x=80, y=280)
    q9C.place(x=430, y=180)
    q9D.place(x=430, y=280)

    btnNextQ9 = tk.Button(frame8, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q9)
    btnNextQ9.place(x=600, y=500)

    btnBackQ8 = tk.Button(frame9, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q8)
    btnBackQ8.place(x=50, y=500)

    question10 = tk.Label(frame10, text='Which of the following is an example of a “phishing” attack?', font=font_large,
                          bg='light yellow')

    def q10():
        q10A['state'] = tk.DISABLED
        q10B['state'] = tk.DISABLED
        q10C['state'] = tk.DISABLED
        q10D['state'] = tk.DISABLED

    q10A = tk.Button(frame10,
                     text='A. Sending someone an email that contains a malicious link \nthat is disguised to look like '
                          'an email from \nsomeone the person knows',
                     font=font_small, bg='#FCF6B1', command=lambda: [q10Wrong(), q10()])
    q10B = tk.Button(frame10,
                     text='B. Creating a fake website that looks nearly identical \nto a real website in order to trick users \ninto entering their login information',
                     font=font_small, bg='#FCF6B1', command=lambda: [q10Wrong(), q10()])
    q10C = tk.Button(frame10,
                     text='C. Sending someone a text message that contains a \nmalicious link that is disguised to look like a notification '
                          '\nthat the person has won a contest',
                     font=font_small, bg='#FCF6B1', command=lambda: [q10Wrong(), q10()])
    q10D = tk.Button(frame10, text='D. All of the above', font=font_small, bg='#FCF6B1',
                     command=lambda: [q10Right(), correct_button_clicked(), q10()])

    question10.pack(pady=20)
    q10A.pack(pady=15)
    q10B.pack(pady=15)
    q10C.pack(pady=15)
    q10D.pack(pady=15)

    btnNextQ10 = tk.Button(frame9, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q10)
    btnNextQ10.place(x=600, y=500)

    btnBackQ10 = tk.Button(frame10, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q9)
    btnBackQ10.place(x=50, y=500)

    question11 = tk.Label(frame11, text='Which of the following four passwords is the most secure?', font=font_large,
                          bg='light yellow')

    def q11():
        q11A['state'] = tk.DISABLED
        q11B['state'] = tk.DISABLED
        q11C['state'] = tk.DISABLED
        q11D['state'] = tk.DISABLED

    q11A = tk.Button(frame11, text='A. WTh!5Z', font=font_large, bg='#FCF6B1',
                     command=lambda: [q11Right(), correct_button_clicked(), q11()])
    q11B = tk.Button(frame11, text='B. 123456', font=font_large, bg='#FCF6B1', command=lambda: [q11Wrong(), q11()])
    q11C = tk.Button(frame11, text='C. into*48', font=font_large, bg='#FCF6B1', command=lambda: [q11Wrong(), q11()])
    q11D = tk.Button(frame11, text='D. Ball123', font=font_large, bg='#FCF6B1', command=lambda: [q11Wrong(), q11()])

    question11.pack(pady=20)
    q11A.place(x=120, y=150)
    q11B.place(x=120, y=250)
    q11C.place(x=470, y=150)
    q11D.place(x=470, y=250)

    btnNextQ11 = tk.Button(frame10, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q11)
    btnNextQ11.place(x=600, y=500)

    btnBackQ11 = tk.Button(frame11, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q10)
    btnBackQ11.place(x=50, y=500)

    question12 = tk.Label(frame12, text='What kind of cybersecurity risks can be minimized by '
                                        '\nusing a Virtual Private Network (VPN)?',
                          font=font_large, bg='light yellow')

    def q12():
        q12A['state'] = tk.DISABLED
        q12B['state'] = tk.DISABLED
        q12C['state'] = tk.DISABLED
        q12D['state'] = tk.DISABLED

    q12A = tk.Button(frame12, text='A. Use of insecure Wi-Fi networks', font=font_large, bg='#FCF6B1',
                     command=lambda: [q12Right(), correct_button_clicked(), q12()])
    q12B = tk.Button(frame12, text='B. De-anonymization by network operators', font=font_large, bg='#FCF6B1',
                     command=lambda: [q12Wrong(), q12()])
    q12C = tk.Button(frame12, text='C. Key-logging', font=font_large, bg='#FCF6B1', command=lambda: [q12Wrong(), q12()])
    q12D = tk.Button(frame12, text='D. Phishing attacks', font=font_large, bg='#FCF6B1',
                     command=lambda: [q12Wrong(), q12()])

    question12.pack(pady=20)
    q12A.pack(pady=20)
    q12B.pack(pady=20)
    q12C.pack(pady=20)
    q12D.pack(pady=20)

    btnNextQ12 = tk.Button(frame11, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q12)
    btnNextQ12.place(x=600, y=500)

    btnBackQ11 = tk.Button(frame12, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q11)
    btnBackQ11.place(x=50, y=500)

    question13 = tk.Label(frame13,
                          text='On most home computers, how often should you update \nyour operating system and security software?',
                          font=font_large, bg='light yellow')

    def q13():
        q13A['state'] = tk.DISABLED
        q13B['state'] = tk.DISABLED
        q13C['state'] = tk.DISABLED
        q13D['state'] = tk.DISABLED

    q13A = tk.Button(frame13, text='A. Monthly', font=font_large, bg='#FCF6B1',
                     command=lambda: [q13Right(), correct_button_clicked(), q13()])
    q13B = tk.Button(frame13, text='B. You do not need to update your system', font=font_large, bg='#FCF6B1',
                     command=lambda: [q13Wrong(), q13()])
    q13C = tk.Button(frame13, text='C. Three times a week', font=font_large, bg='#FCF6B1',
                     command=lambda: [q13Wrong(), q13()])
    q13D = tk.Button(frame13, text='D. At least once a week', font=font_large, bg='#FCF6B1',
                     command=lambda: [q13Wrong(), q13()])

    question13.pack(pady=20)
    q13A.pack(pady=20)
    q13B.pack(pady=20)
    q13C.pack(pady=20)
    q13D.pack(pady=20)

    btnNextQ13 = tk.Button(frame12, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q13)
    btnNextQ13.place(x=600, y=500)

    btnBackQ12 = tk.Button(frame13, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q12)
    btnBackQ12.place(x=50, y=500)

    question14 = tk.Label(frame14,
                          text=' It is a malicious software that replicate themselves \nover and over to deplete system resources',
                          font=font_large, bg='light yellow')

    def q14():
        q14A['state'] = tk.DISABLED
        q14B['state'] = tk.DISABLED
        q14C['state'] = tk.DISABLED
        q14D['state'] = tk.DISABLED

    q14A = tk.Button(frame14, text='A. Trojan Horse', font=font_large, bg='#FCF6B1', command=lambda: [q14Wrong, q14()])
    q14B = tk.Button(frame14, text='B. Worms', font=font_large, bg='#FCF6B1',
                     command=lambda: [q14Right(), correct_button_clicked(), q14()])
    q14C = tk.Button(frame14, text='C. Spyware', font=font_large, bg='#FCF6B1', command=lambda: [q14Wrong, q14()])
    q14D = tk.Button(frame14, text='D. Ransomware', font=font_large, bg='#FCF6B1', command=lambda: [q14Wrong, q14()])

    question14.pack(pady=20)
    q14A.place(x=80, y=180)
    q14B.place(x=80, y=280)
    q14C.place(x=430, y=180)
    q14D.place(x=430, y=280)

    btnNextQ14 = tk.Button(frame13, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q14)
    btnNextQ14.place(x=600, y=500)

    btnBackQ13 = tk.Button(frame14, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q13)
    btnBackQ13.place(x=50, y=500)

    question15 = tk.Label(frame15, text=' How can you tell if a website encrypts its traffic?', font=font_large,
                          bg='light yellow')

    def q15():
        q15A['state'] = tk.DISABLED
        q15B['state'] = tk.DISABLED
        q15C['state'] = tk.DISABLED
        q15D['state'] = tk.DISABLED

    q15A = tk.Button(frame15, text='A. Google it', font=font_large, bg='#FCF6B1',
                     command=lambda: [q15Wrong(), to_score(), q15()])
    q15B = tk.Button(frame15, text='B. Look for the lock symbol in a URL', font=font_large, bg='#FCF6B1',
                     command=lambda: [q15Right(), correct_button_clicked(), to_score()])
    q15C = tk.Button(frame15, text='C. All websites encrypt their traffic', font=font_large, bg='#FCF6B1',
                     command=lambda: [q15Wrong(), to_score(), q15()])
    q15D = tk.Button(frame15, text='D. Encrypted sites take longer to load', font=font_large, bg='#FCF6B1',
                     command=lambda: [q15Wrong(), to_score(), q15()])

    question15.pack(pady=20)
    q15A.pack(pady=20)
    q15B.pack(pady=20)
    q15C.pack(pady=20)
    q15D.pack(pady=20)

    btnNextQ15 = tk.Button(frame14, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q15)
    btnNextQ15.place(x=600, y=500)

    btnBackQ14 = tk.Button(frame15, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q14)
    btnBackQ14.place(x=50, y=500)


def videoplayer():
    videoLabel = Label(
        root,
        text="Instructions: Click 'Load' to import the mp4 file. \nThen click 'Play' to learn the topic about Device Security. \nClick 'Start Quiz' to proceed.",
        font=("Bahnschrift Light SemiCondensed", 18),
        bg="#fff292",
        fg="#3d261f",
        justify="center")
    videoLabel.pack(pady=5)

    def update_duration(event):
        """ updates the duration after finding the duration """
        end_time["text"] = str(datetime.timedelta(seconds=vid_player.duration()))
        progress_slider["to"] = vid_player.duration()

    def update_scale(event):
        """ updates the scale value """
        progress_slider.set(vid_player.current_duration())

    def load_video():
        """ loads the video """
        file_path = filedialog.askopenfilename()

        if file_path:
            vid_player.load(file_path)

            progress_slider.config(to=0, from_=0)
            progress_slider.set(0)
            play_pause_Btn["text"] = "Play"

    def seek(value):
        """ used to seek a specific timeframe """
        vid_player.seek(int(value))

    def skip(value: int):
        """ skip seconds """
        vid_player.skip_sec(value)
        progress_slider.set(progress_slider.get() + value)

    def play_pause():
        """ pauses and plays """
        if vid_player.is_paused():
            vid_player.play()
            play_pause_Btn["text"] = "Pause"

        else:
            vid_player.pause()
            play_pause_Btn["text"] = "Play"

    def video_ended(event):
        """ handle video ended """
        progress_slider.set(progress_slider["to"])
        play_pause_Btn["text"] = "Play"

    def clickQuiz():
        videoLabel.destroy()
        vid_player.destroy()
        load_Btn.destroy()
        play_pause_Btn.destroy()
        rewind_5sec.destroy()
        skip_plus_5sec.destroy()
        start_time.destroy()
        end_time.destroy()
        progress_slider.destroy()
        start_quizBtn.destroy()
        startquiz()

    load_Btn = Button(
        root,
        text="LOAD",
        fg="#3d261f",
        bg="#ffbd59",
        activebackground="#ea2a2a",
        activeforeground="#ffffff",
        font=("Bahnschrift Light Condensed", 12),
        relief=FLAT,
        padx=50,
        command=load_video)
    load_Btn.pack()

    vid_player = TkinterVideo(scaled=True, pre_load=False, master=root)
    vid_player.pack(expand=True, fill="both")

    play_pause_Btn = Button(
        root,
        text="PLAY",
        fg="#3d261f",
        bg="#ffbd59",
        activebackground="#ea2a2a",
        activeforeground="#ffffff",
        font=("Bahnschrift Light Condensed", 12),
        relief=FLAT,
        padx=50,
        command=play_pause)
    play_pause_Btn.pack()

    rewind_5sec = Button(root, text="Rewind -5 sec", command=lambda: skip(-5))
    rewind_5sec.pack(side="left")

    start_time = Label(root, text=str(datetime.timedelta(seconds=0)))
    start_time.pack(side="left")

    progress_slider = Scale(root, from_=0, to=0, orient="horizontal", command=seek)
    progress_slider.pack(side="left", fill="x", expand=True)

    end_time = Label(root, text=str(datetime.timedelta(seconds=0)))
    end_time.pack(side="left")

    vid_player.bind("<<Duration>>", update_duration)
    vid_player.bind("<<SecondChanged>>", update_scale)
    vid_player.bind("<<Ended>>", video_ended)

    skip_plus_5sec = Button(root, text="Skip +5 sec", command=lambda: skip(5))
    skip_plus_5sec.pack(side="left")

    start_quizBtn = Button(
        root,
        text="START QUIZ >>",
        fg="#ffffff",
        bg="#ea2a2a",
        activebackground="#ffbd59",
        font=("Bahnschrift Light Condensed", 20),
        relief=FLAT,
        command=clickQuiz)
    start_quizBtn.pack(side=RIGHT)


def clickStart():
    imageLabel.destroy()
    welcomeLabel.destroy()
    introLabel.destroy()
    startButton.destroy()
    videoplayer()


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
    font=("Bahnschrift SemiBold", 26),
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
frame1.pack(fill='both', expand=1)

root.mainloop()
