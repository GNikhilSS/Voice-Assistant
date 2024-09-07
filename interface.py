from tkinter import*
from PIL import Image, ImageTk

import Speech_to_text
import action

def ask():
    user = Speech_to_text.speech_to_text()
    bot = action.action(user)
    text.insert(END, 'User-->' + user + '\n')
    if bot != None:
        text.insert(END, 'Bot-->' + str(bot) + '\n')
    if bot == "Take care":
        root.destroy()    

def send():
    user = entry.get()
    bot = action.action(user)
    text.insert(END, 'User-->' + user + '\n')
    if bot != None:
        text.insert(END, 'Bot-->' + str(bot) + '\n')
    if bot == "Take care":
        root.destroy()

def delete():
    text.delete("1.0", "end")

 
root = Tk() 
root.title("Assistant")
root.geometry("580x750")
root.resizable(False, False)
root.config(bg="#010D26")


frame = LabelFrame(root, padx=100, pady=15, borderwidth=3, relief="raised")
frame.config(bg="#252524")
frame.grid(row=0, column=0, padx=63, pady=20)


text_label = Label(frame, text="ASSISTANT", font=("comic Sans ms", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

image = ImageTk.PhotoImage(Image.open("img/assitant.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)
 

text = Text(root, font=("courier 10 bold"), bg="#ff00ff")
text.grid(row=2, column=0)
text.place(x=100, y=405, width=375, height=100)

entry = Entry(root, justify=CENTER)
entry.place(x=108, y=520, width=350, height=30)


B1 = Button(root, text="ASK", bg="#00ffff", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
B1.place(x=70, y=575)

B2 = Button(root, text="SEND", bg="#00ffff", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
B2.place(x=225, y=575)

B3 = Button(root, text="DELETE", bg="#00ffff", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
B3.place(x=400, y=575)


root.mainloop() 