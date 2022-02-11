import tkinter as tk
from tkinter import *
import datetime
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
import tkinter.font as font

root = tk.Tk()
root.title("Device Security Quiz")
root.geometry("600x600")
root.config(background="#fff292")

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

width, height = 900, 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

frame1 = tk.Frame(root)
frame1.configure(bg='light yellow')

frame2 = tk.Frame(root)
frame2.configure(bg='light yellow')

frame3 = tk.Frame(root)
frame3.configure(bg='light yellow')

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

font_large = font.Font(family='Georgia', size='15', weight='bold')
font_small = font.Font(family='Georgia', size='12')

def q1Rigth():
    tk.Label(frame1, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q1Wrong():
    tk.Label(frame1, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q2Rigth():
    tk.Label(frame2, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q2Wrong():
    tk.Label(frame2, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q3Rigth():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q3Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q10Rigth():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q10Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q11Rigth():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q11Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q12Rigth():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q12Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q13Rigth():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q13Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q14Rigth():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q14Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)
def q15Rigth():
    tk.Label(frame3, text='  Correct  ', font=font_large, background='red', fg='white').place(x=380, y=400)
def q15Wrong():
    tk.Label(frame3, text='Incorrect', font=font_large, background='red', fg='white').place(x=380, y=400)



def startquiz():

    question1 = tk.Label(frame1, text='Below are steps in scanning antivirus.'
                                      ' Rearrange them in the correct sequence. \n\n a. Scan the selected file \n '
                                      'b. Choose an antivirus program \n c. Wait While the program is scanning and the'
                                      'result is produced \n d. Select the file that need to be scanned',
                         font=font_large, bg='light yellow')
    q1A = tk.Button(frame1, text='A. d-b-a-c', font=font_large, bg='#FCF6B1', command=q1Wrong)
    q1B = tk.Button(frame1, text='B. b-d-a-c', font=font_large, bg='#FCF6B1', command=q1Rigth)
    q1C = tk.Button(frame1, text='C. a-c-b-d', font=font_large, bg='#FCF6B1', command=q1Wrong)
    q1D = tk.Button(frame1, text='D. c-a-d-b', font=font_large, bg='#FCF6B1', command=q1Wrong)

    question1.pack(pady=20)
    q1A.place(x=200, y=200)
    q1B.place(x=200, y=300)
    q1C.place(x=550, y=200)
    q1D.place(x=550, y=300)

    btnNextQ2 = tk.Button(frame1, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q2)

    btnNextQ2.place(x=750, y=400)

    question2 = tk.Label(frame2,
                         text='How often should antivirus software be updated (the best way to protect computers)?',
                         font=font_large, bg='light yellow')

    q2A = tk.Button(frame2, text='A. Monthly', font=font_large, bg='#FCF6B1', command=q2Rigth)
    q2B = tk.Button(frame2, text='B. Every 3 months', font=font_large, bg='#FCF6B1', command=q2Wrong)
    q2C = tk.Button(frame2, text='C. Annually', font=font_large, bg='#FCF6B1', command=q2Wrong)
    q2D = tk.Button(frame2, text='D. Never', font=font_large, bg='#FCF6B1', command=q2Wrong)

    question2.pack(pady=20)
    q2A.place(x=200, y=100)
    q2B.place(x=200, y=200)
    q2C.place(x=550, y=100)
    q2D.place(x=550, y=200)

    btnBackQ1 = tk.Button(frame2, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q1)
    btnBackQ1.place(x=100, y=400)

    question3 = tk.Label(frame3, text='The #1 thing you can do to avoid malware is:', font=font_large,
                         bg='light yellow')
    q3A = tk.Button(frame3, text='A. Install antivirus software and keep it updated', font=font_large, bg='#FCF6B1',
                    command=q3Rigth)
    q3B = tk.Button(frame3, text='B. Do not open email attachments', font=font_large, bg='#FCF6B1', command=q3Wrong)
    q3C = tk.Button(frame3, text='C. Do not download anything from the web.', font=font_large, bg='#FCF6B1',
                    command=q3Wrong)
    q3D = tk.Button(frame3, text='D. Be friendly always', font=font_large, bg='#FCF6B1', command=q3Wrong)

    question3.pack(pady=20)
    q3A.pack(pady=20)
    q3B.pack(pady=20)
    q3C.pack(pady=20)
    q3D.pack(pady=20)

    btnNextQ3 = tk.Button(frame2, text='NEXT', font=font_small, bg='#FCF6B1', command=next_to_Q3)
    btnNextQ3.place(x=750, y=400)

    btnBackQ2 = tk.Button(frame3, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q2)
    btnBackQ2.place(x=100, y=400)

    question15 = tk.Label(frame15, text='How can you tell if a website encrypts its traffic?', font=font_large,
                         bg='light yellow')
    q15A = tk.Button(frame15, text='A. Google it', font=font_large, bg='#FCF6B1',
                    command=q15Wrong)
    q15B = tk.Button(frame15, text='B. Look for the lock symbol in a URL', font=font_large, bg='#FCF6B1', command=q15Rigth)
    q15C = tk.Button(frame15, text='C. All websites encrypt their traffic', font=font_large, bg='#FCF6B1',
                    command=q15Wrong)
    q15D = tk.Button(frame15, text='D. Encrypted sites take longer to load', font=font_large, bg='#FCF6B1', command=q15Wrong)

    question15.pack(pady=20)
    q15A.pack(pady=20)
    q15B.pack(pady=20)
    q15C.pack(pady=20)
    q15D.pack(pady=20)

    btnBackQ14 = tk.Button(frame15, font=font_small, text='BACK', bg='#FCF6B1', command=back_to_Q2)
    btnBackQ14.place(x=100, y=400)

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
frame1.pack(fill='both', expand=1)

root.mainloop()
