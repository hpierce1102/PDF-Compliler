#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
class PDFCombiner:

    def __init__(self, master):
        
        master.title('PDF Combiner')
        master.resizable(False, False)    

        #Stores an index for all generated inputs
        #self.inputs = [0]
        self.chooseButtons = {}
        self.chooseLabelVars = {}
        self.chooseLabels = {}

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.clear_button = ttk.Button(self.frame_header, text = "Clear")
        self.clear_button.grid(row = 1, column = 0)
        self.combine_button = ttk.Button(self.frame_header, text = "Combine")
        self.combine_button.grid(row = 1, column = 1)

        self.generate_choose(0)



        #self.PDF1path= StringVar()
        #self.PDF1label = ttk.Label(self.frame_header,
        #	textvariable = self.PDF1path
        #	).grid(row = 0, column = 1)
        #self.PDF1button = ttk.Button(self.frame_header,
        #	text = "Choose PDF",
        #	command = lambda: self.open(self.PDF1path)
        #	).grid(row = 0, column = 0)
        #self.PDF1path.set("unset")

        #self.PDF2path = StringVar()
        #self.PDF2label = ttk.Label(self.frame_header, 
        #	textvariable = self.PDF2path
        #	).grid(row = 1, column = 1)
        #self.PDF2button = ttk.Button(self.frame_header,
        #	text = "Choose PDF",
        #	command = lambda: self.open(self.PDF2path)
        #	).grid(row = 1, column = 0)
        #self.PDF2path.set("unset")


        #self.output = StringVar()
        #self.outputlabel = ttk.Label(self.frame_header,
        #    textvariable = self.output
        #    ).grid(row = 2, column = 1)
        #self.outputbutton = ttk.Button(self.frame_header,
        #    text = "Choose Output",
        #    command = lambda: self.open(self.output)
        #    ).grid(row = 2, column = 0)
        #self.output.set("unset")

        

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        
        #print(self.clear_button)

    def open(self, label):
        label.set(filedialog.askopenfilename())
        if label.get():
            index = len(self.chooseLabels)
            #self.inputs.append(index)
            self.generate_choose(index)

    def clear():
        #self.
        pass        

    def generate_choose(self, ele):
        #x = 0
        #for i in self.inputs:
            self.chooseLabelVars[ele] = StringVar()
            self.chooseLabels[ele] = ttk.Label(self.frame_header,
                textvariable = self.chooseLabelVars[ele]
                ).grid(row = ele, column = 1)
            self.chooseButtons[ele] = ttk.Button(self.frame_header,
                text = "Choose PDF",
                command = lambda: self.open(self.chooseLabelVars[ele])
                ).grid(row = ele, column = 0)
            self.move_combine_button(ele + 1)

            #x += 1

    def move_combine_button(self, row):
        self.clear_button.grid(row = row, column = 0)
        self.combine_button.grid(row = row, column = 1)
    
    
            


def main():            
    
    root = Tk()
    feedback = PDFCombiner(root)
    root.mainloop()
    
if __name__ == "__main__": main()

	
