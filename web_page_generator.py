

import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        #sets title of GUI window
        self.master.title("Web Page Generator")

        self.lbl_text = tk.Label(self.master,text='Enter custom text or clock the Default HTML page button')
        self.lbl_text.grid(row=0,column=0, columnspan=6,padx=(27,0),pady=(10,0),sticky=N+W)

        self.txt_fname = tk.Entry(self.master,text='')
        self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=10,padx=(30,40),pady=(0,0),sticky=N+E+W)

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row = 2, column= 8,padx=(10,10) , pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
