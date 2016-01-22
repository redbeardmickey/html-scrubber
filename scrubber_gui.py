from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import scrubber

class ScrubberGUI(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.parent = master
		self.pack()
		self.initUI()

	#This is where we lauch the file manager bar.
	def OpenFile(self):
		# name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",	filetypes =(("Text File", "*.txt"),("All Files","*.*")), title = "Choose a file.")
		self.directory = askdirectory()
		return self.folderText.set(self.directory)

	def scrub(self):
		self.scrubStatusText.set('Scrubbing...')
		return self.scrubStatusText.set(scrubber.main(self.directory, self.flagName.get()))
		# return print (self.flagName.get())

	def initUI(self):
		self.parent.title("ScrubberGUI")

		# self.parent.minsize(500, 300)
		self.folderText = StringVar()
		self.flagName = StringVar()
		self.scrubStatusText = StringVar()
		self.scrubStatusText.set('')
		self.folderText.set('Please select a target folder')
		self.flagName.set('internalOnly')

		self.open_dir = Button(self, text="Open Directory", command=self.OpenFile).grid(row=0, column=2, pady=(10, 10), padx=(10, 10), sticky="WE")
		self.targetFolder = Label(self, textvariable=self.folderText).grid(row=0, column=0, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="W")

		self.flagNameLabel = Label(self, text="Flag Class Name").grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="W")
		self.flagNameEntry = Entry(self, textvariable=self.flagName).grid(row=1, column=1, padx=(10, 10), pady=(0, 10), sticky="W")

		self.scrubBtn = Button(self, text="Scrub", command=self.scrub).grid(row=1, column=2, padx=(10, 10), pady=(0, 10), sticky="WE")

		self.scrubStatusLabel = Label(self, textvariable=self.scrubStatusText).grid(row=3, column=0, columnspan=2, padx=(10, 10), pady=(0, 10), sticky="W")
		self.quitBtn = Button(self, text="Quit", command=self.parent.destroy).grid(row=3, column=2, padx=(10, 10), pady=(0, 10), sticky="WE")


def main():
	root = Tk()
	app = ScrubberGUI(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()