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
        eventsButton = Button(self, text="Events", command=self.events_window)

        # placing the button on my window
        rulesButton.place(x=0, y=0)
        statusButton.place(x=0, y=30)
        eventsButton.place(x=0, y=60)

    def events_window(self):
        event_win = Toplevel(root)
        tree = ttk.Treeview(event_win, columns=('Date', 'Event'))
        tree.heading('#0', text='Date')
        tree.heading('#1', text='Event')
        tree.column('#0', width=150)
        tree.column('#1', width=700)
        tree.column('#2', width=0)
        tree.place(x=0, y=0)
        tree.pack(fill=BOTH, expand=1)
        treeview = tree
        seefire.getEvents(treeview)

    def rules_window(self):
        rule_win = Toplevel(root)
#        scrollbar = Scrollbar(rule_win)
#        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(rule_win, width=100)
        listbox.pack(fill=BOTH, expand=1)
        seefire.getRules(listbox)

#        listbox.config(yscrollcommand=scrollbar.set)
#        scrollbar.config(commmand=listbox.yview)


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
