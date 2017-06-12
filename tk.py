from Tkinter import *
import tkMessageBox
import os
class Application(Frame):
    def __init__(self, master=None, bd=10000, cursor='dot', height=768, width=576):
        Frame.__init__(self, master)
        self.pack(padx=5,pady=5)
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack(side='left', expand=0)
        self.alertButton = Button(self, fg='green', bg='black',text='confirm', command=self.hello())
        self.alertButton.pack()
        self.alertButton.bind('noob', self.__init__())
    def hello(self):
        name = self.nameInput.get()
        tkMessageBox.showwarning('Sunprise', 'you cant close it, %s' % name)
app = Application()
app.master.title('')
app.master.maxsize(1000,400)
app.mainloop()
i=0
while i<5:
    os.system()