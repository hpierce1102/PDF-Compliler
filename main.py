#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import PyPDF2

class PDFCombiner:

    def __init__(self, master):
        
        master.title('PDF Combiner')
        master.resizable(False, False)    

        self.chooseButtons = {}
        self.chooseLabelVars = {}
        self.chooseLabels = {}

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.clear_button = ttk.Button(
            self.frame_header, 
            text = "Clear",
            command = self.clear)
        self.clear_button.grid(row = 1, column = 0)

        self.combine_button = ttk.Button(
            self.frame_header, 
            text = "Combine",
            command = self.combine)
        self.combine_button.grid(row = 1, column = 1)

        self.generate_choose(0)        

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

    def open(self, ele):
        self.chooseLabelVars[ele].set(
            filedialog.askopenfilename(filetypes=[('PDF','*.pdf')]))

        index = len(self.chooseLabels)
        if self.chooseLabelVars[ele].get() and ele == index - 1:
            self.generate_choose(index)

    def clear(self):
        for ele in range(0, len(self.chooseLabels)):
            self.chooseLabelVars[ele] = None
            self.chooseLabels[ele].grid_forget()
            self.chooseButtons[ele].grid_forget()
        self.chooseButtons = {}
        self.chooseLabelVars = {}
        self.chooseLabels = {}

        self.generate_choose(0)

    def combine(self):
        mergedPDF = PyPDF2.PdfFileMerger()

        for ele in self.chooseLabelVars:
            try:
                mergedPDF.append(self.chooseLabelVars[ele].get())
            except:
                print("Skipped" + str(self.chooseLabelVars[ele].get()))

        output = open(filedialog.asksaveasfilename(defaultextension = ".pdf"), "wb")
        mergedPDF.write(output)

    def generate_choose(self, ele):
            self.chooseLabelVars[ele] = StringVar()

            self.chooseLabels[ele] = ttk.Label(
                self.frame_header,
                textvariable = self.chooseLabelVars[ele]
                )
            self.chooseLabels[ele].grid(row = ele, column = 1)

            self.chooseButtons[ele] = ttk.Button(self.frame_header,
                text = "Choose PDF",
                command = lambda: self.open(ele)
                )
            self.chooseButtons[ele].grid(row = ele, column = 0)

            self.move_combine_button(ele + 1)

    def move_combine_button(self, row):
        self.clear_button.grid(row = row, column = 0)
        self.combine_button.grid(row = row, column = 1)

def main():            
    
    root = Tk()
    feedback = PDFCombiner(root)
    root.mainloop()
    
if __name__ == "__main__": main()