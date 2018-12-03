from Tkinter import *
import ttk
import seefire
import os


class Window(Frame):
    def __init__(self, master=None):
        is_sudo = os.getenv("SUDO_USER")
        if (is_sudo == None):
            print("Program must be run with sudo")
            exit()
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
        statusButton = Button(self, text="Status", command=self.status_window)
        statusButton.pack()
        eventsButton = Button(self, text="Events")

        # placing the button on my window
        rulesButton.place(x=0, y=0)
        statusButton.place(x=0, y=30)
        eventsButton.place(x=0, y=60)

    def rules_window(self):
        rule_win = Toplevel(root)
        scrollbar = Scrollbar(rule_win)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(rule_win)
        listbox.pack()
        rule_text = seefire.getRules()
        #rule_label = Label(rule_win, text=rule_text)
        #rule_label.place(x=0, y=0)
        #rule_label.pack
        listbox.insert(END, rule_text)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(commmand=listbox.yview)


    def status_window(self):
        status_win = Toplevel(root)
        tree = ttk.Treeview(status_win, columns=('Date', 'Status'))
        tree.heading('#0', text='Date')
        tree.heading('#1', text='Status')
        tree.place(x=0, y=0)
        tree.pack()
        treeview = tree
        seefire.getStatus(treeview)




root = Tk()

# size of the window
root.geometry("200x200")

app = Window(root)
root.mainloop()
