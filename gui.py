from Tkinter import *
import seefire


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("SeeFire")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        rulesButton = Button(self, text="Rules", command=self.rules_window)
        rulesButton.pack()
        statusButton = Button(self, text="Status")
        eventsButton = Button(self, text="Events")

        # placing the button on my window
        rulesButton.place(x=0, y=0)
        statusButton.place(x=0, y=30)
        eventsButton.place(x=0, y=60)

    def rules_window(self):
        ruleWin = Toplevel(root)
        ruleText = seefire.getRules()
        display = Label(ruleWin, text=ruleText)
        display.place(x=0, y=0)
        display.pack




root = Tk()

# size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()
