#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
class PDFCombiner:

    def __init__(self, master):
        
        master.title('PDF Combiner')
        master.resizable(False, False)    

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.PDF1path= StringVar()
        self.PDF1label = ttk.Label(self.frame_header,
        	textvariable = self.PDF1path
        	).grid(row = 0, column = 1)
        self.PDF1button = ttk.Button(self.frame_header,
        	text = "Choose PDF",
        	command = lambda: self.open(self.PDF1path)
        	).grid(row = 0, column = 0)
        self.PDF1path.set("unset")

        self.PDF2path = StringVar()
        self.PDF2label = ttk.Label(self.frame_header, 
        	textvariable = self.PDF2path
        	).grid(row = 1, column = 1)
        self.PDF2button = ttk.Button(self.frame_header,
        	text = "Choose PDF",
        	command = lambda: self.open(self.PDF2path)
        	).grid(row = 1, column = 0)
        self.PDF2path.set("unset")

        self.output = StringVar()
        self.outputlabel = ttk.Label(self.frame_header,
            textvariable = self.output
            ).grid(row = 2, column = 1)
        self.outputbutton = ttk.Button(self.frame_header,
            text = "Choose Output",
            command = lambda: self.open(self.output)
            ).grid(row = 2, column = 0)
        self.output.set("unset")

        self.clear= ttk.Button(self.frame_header, text = "Clear").grid(row = 3, column = 0)
        self.combine = ttk.Button(self.frame_header, text = "Combine").grid(row = 3, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

    def open(label, self):
        self.set(filedialog.askopenfilename())

def main():            
    
    root = Tk()
    feedback = PDFCombiner(root)
    root.mainloop()
    
if __name__ == "__main__": main()

	
