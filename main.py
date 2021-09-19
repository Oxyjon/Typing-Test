from tkinter import *

#init window
window = Tk()
window.title('Typing Test')

#used to store users typed characters                                                                                                                                                                                                                                                                                                                                                                       'As a result, Canada is a desirable place to live.
words_typed = []

#Functions
def start():
    #Update canvas text
    canvas.itemconfig(mytext, text="There are three reasons why Canada is one of the best countries in the world.\n"
            "First, Canada has an excellent health care system.\n"
            "All Canadians have access to medical services at a reasonable price.\n"
            "Second, Canada has a high standard of education.\n"
            "Students are taught by well-trained teachers and are encouraged to continue studying at university.\n"
            "Finally, Canada's cities are clean and efficiently managed.\n"
            "Canadian cities have many parks and lots of space for people to live.\n")
    canvas.update()
    # run the end command after 1 minute
    window.after(60000, end)

def end():
    #get text from input
    for word in text_input.get():
        words_typed.append(word)
    #Calulation for Words Per minute
    cpm = len(words_typed)
    wpm = cpm/5
    finished_text.config(text = f"Your CPM is {cpm} and your wpm is {wpm}")


#Buttons
start_btn = Button(text='Start', command=start)
start_btn.grid(column=0, row=3)

#Canvas
canvas = Canvas(width=600, height=600)
mytext = canvas.create_text(300,200,  text="Are you ready!? Press start")
canvas.grid(column=0, row=1,columnspan=2)

fin_btn = Button(text='Finished', command=end)
fin_btn.grid(column=1, row=3)
#Label
title_text = Label(text="Typing Speed Test")
title_text.grid(column=0, row=0,columnspan=2)

finished_text = Label(text='')
finished_text.grid(column=0, row=4,columnspan=2)
#Entry
text_input = Entry()
text_input.grid(column=0, row=2, columnspan=2)

window.mainloop()