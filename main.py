from image import image
import os
from Tkinter import *
import tkFont
import tkFileDialog

class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bd=2)
        self.master = master
        self.createMenus()
        self.createWindow()

    def createMenus(self):
        self.menubar = Menu(self)
        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="Exit", command=None)
        menu.add_command(label="Open File", command=self.fileOpen)
        #self.menubar.add_command(label="Add Format", command=lambda: Item(master, ['', 'text1', ''], 3))
        #self.menubar.add_command(label="Generate .STK", command=(lambda: self.saveToFile()))
        self.master.config(menu=self.menubar)

    def createWindow(self):
        self.mainFrame = Canvas(width=680, height=400, bg="GREY")
        self.mainFrame.pack()
        self.fnButton = Button(self.mainFrame, text = '...', width = 3, command=self.fileOpen)
        self.fnLabel = Text(self.mainFrame, height = 1, width = 24, wrap="none")
        self.fnLabel.insert('1.0', 'Choose input file')
        self.fnLabel.config(state=DISABLED)
        self.svButton = Button(self.mainFrame, text = 'Export TGA', width = 10, command=self.saveNewFile)
        self.infoEntry = Text(self.mainFrame, height = 24, width = 51,state = DISABLED, background = '#424242', foreground = "#2195E7")

        self.fileButton = self.mainFrame.create_window(200, 20, anchor = NW, window = self.fnButton)
        self.fileName = self.mainFrame.create_window(22, 22, anchor = NW, window = self.fnLabel)
        self.saveButton = self.mainFrame.create_window(22, 50, anchor = NW, window = self.svButton)
        self.iEntry = self.mainFrame.create_window(300, 20, anchor = NW, window = self.infoEntry)

    def fileOpen(self):
        self.openFile = tkFileDialog.askopenfilename(filetypes = (('TARGA Image', '*.tga'),))
        if self.openFile:
            TGA = image(self.openFile)
            self.fnLabel.config(state=NORMAL)
            self.fnLabel.delete('1.0', END)
            self.fnLabel.insert('1.0', self.openFile)
            self.fnLabel.config(state=DISABLED)
            #self.writeToLog('INPUT FILE OPEN: ' + self.openFile, 'NA')
            #self.scanFile(self.openFile)

    def saveNewFile(self):
        self.openSaveFile = tkFileDialog.asksaveasfilename(filetypes = (('TARGA Image', '*.tga'),))
        if self.openSaveFile:
            if len(self.openSaveFile.split('.')) == 1:
                self.openSaveFile += '.tga'
            else:
                if self.openSaveFile.split('.')[-1] != 'txt':
                    self.openSaveFile += '.tga'

if __name__ == '__main__':
    root = Tk()
    app = MainWindow(root)
    app.master.title('TGA handler')
    app.pack()
    root.update()
    if "favicon.ico" in os.listdir(os.getcwd()):
        root.iconbitmap(True, "favicon.ico")
    root.minsize(root.winfo_width(), root.winfo_height())
    root.resizable(False, False)
    app.mainloop()

    try:
        root.destroy()
    except:
        pass