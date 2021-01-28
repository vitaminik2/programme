from tkinter import *
 
clicks = 0
 
 
def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
 
root = Tk()

root.geometry("300x250")
 
btn = Button(text="клик",background="blue",foreground="lime",  
             padx="3100", pady="1000", font="1000", command=click_button)
btn.pack()
 
root.mainloop()
 
