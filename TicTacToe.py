from tkinter import *
import  tkinter.messagebox as msg

class TicTacToe:
	#creating the login screen
	def loginScreen(self):
		#creating window for login screen
		self.root1 = Tk()
		#defining window properties
		self.root1.title("Tic Tac Toe")
		self.root1.geometry("430x120")
		self.labelfont = ('times', 15, 'bold')
		self.p1 = Label(self.root1, text="Enter Player 1 name")
		#configurating the font
		self.p1.config(font=self.labelfont)
		self.p2 = Label(self.root1, text="Enter Player 2 name")
		self.p2.config(font=self.labelfont)
		self.e1 = Entry(self.root1)
		self.e2 = Entry(self.root1)
		self.commit = Button(self.root1, text="Start", command=lambda: self.Commit(self.root1))
		self.commit.config(font=self.labelfont)
		self.p1.grid(row=0)
		self.e1.grid(row=0, column=1, ipadx=20)
		self.p2.grid(row=1)
		self.e2.grid(row=1, column=1, ipadx=20)
		self.commit.grid(row=2,column=1, ipady=4, ipadx=10)
		self.root1.mainloop()

	#function used to store the players name and to destroy the loginScreen window
	def Commit(self,root):
		self.play1 = self.e1.get()
		self.play2 = self.e2.get()
		#Displaying warning if player's name's are not entered
		if self.play1 and self.play2:
			root.destroy()
			self.start()
		else:
			msg.showwarning("Warning","Please Enter the Names of the Players")

	#main function
	def start(self):
		#creating data
		self.board = [i for i in range(0,9)]
		self.buttonList = []
		self.index = 0
		self.currentPlayer = 0
		self.w = 0
		self.labelfont = ('times', 15, 'bold')
		#creating the tk window + configure
		self.root2 = Tk()
		self.root2.geometry("570x525")
		self.root2.title("Tic Tac Toe")

		#creating Menu
		self.m = Menu(self.root2)
		self.root2.config(menu=self.m)
		self.s1 = Menu(self.m)
		self.m.add_cascade(label="Options", menu=self.s1)
		self.s1.add_command(label="Reset" , command= lambda: self.reset(self.root2))
		self.s1.add_separator()
		self.s1.add_command(label='Quit', command= lambda: self.Quit(self.root2))

		#creating player display labels
		self.l1 = Label(self.root2, text="Player 1: "+ self.play1, anchor=W)
		self.l2 = Label(self.root2, text="Player 2: "+ self.play2, anchor=W)
		self.l1.pack(fill=BOTH)
		self.l2.pack(fill=BOTH)
		self.l1.config(font=self.labelfont)
		self.l2.config(font=self.labelfont)

		#creating frame to map buttons
		self.f1 = Frame(self.root2)
		for i in range(0,3):
			for y in range(0,3):
				self.b = Button(self.f1, text=" ", width=10 , height=9, bd=6, command= lambda i=self.index: self.Click(i,self.root2))
				self.b.grid(row=4+i, column= 4+y, sticky='NSEW')
				self.index = self.index + 1
				self.buttonList.append(self.b)
		self.f1.pack()
		self.root2.mainloop()

	#funtion used to quit the game
	def Quit(self,root):
		#creating a question
		n = msg.askquestion("Quit","Do you really want to Quit!")
		if n == 'yes':
			root.destroy()

	#funtion used to change the text of the button according to the player
	def Click(self,index,root):
		self.labelfont = ('times', '10', 'bold')
		if self.currentPlayer == 0 and self.board[index] != "O":
			self.buttonList[index].config(text="X", font=self.labelfont)
			self.currentPlayer = 1
			self.board[index] = "X"
			self.winCheck("X",root)
		elif self.currentPlayer == 1 and self.board[index] != "X":
			self.buttonList[index].config(text="O", font=self.labelfont)
			self.currentPlayer = 0
			self.board[index] = "O"
			self.winCheck("O",root)
		else:
			msg.showwarning("Warning","The index already has a input.Please Choose another Index")

	#the funtion used to check the win
	def winCheck(self,p,root):
		#boundary check
		if self.board[0] == self.board[1] == self.board[2] == p:
			self.win(p,root)
		elif self.board[0] == self.board[3] == self.board[6] == p:
			self.win(p,root)
		elif self.board[6] == self.board[7] == self.board[8] == p:
			self.win(p,root)
		elif self.board[2] == self.board[5] == self.board[8] == p:
			self.win(p,root)
		elif self.board[1] == self.board[4] == self.board[7] == p:
			self.win(p,root)
		elif self.board[3] == self.board[4] == self.board[5] == p:
                        self.win(p,root)
		#diagnol check
		elif self.board[8] == self.board[4] == self.board[0] == p:
			self.win(p,root)
		elif self.board[6] == self.board[4] == self.board[2] == p:
			self.win(p,root)

		#condition for checking draw
		if self.board.count("X") == 5 and self.w == 0 or self.board.count("O") == 5 and self.w == 0:
			answer = msg.askquestion("Draw","Do You Want To Play Again")
			if answer == 'yes':
				self.reset(root)
			else:
				root.destroy()

	#function to display win of the player
	def win(self,p,root):
		if p == "X":
			msg.showinfo("Win",self.play1+" Won the Game")
			self.w = 1
		else:
			msg.showinfo("Win",self.play2+" Won the Game")
			self.w = 1
		if self.w == 1:
			answer = msg.askquestion("Replay","Do You Want To Play Again")
			if answer == 'yes':
				self.reset(root)
			else:
				root.destroy()

	#function used to reset the game by destroying the window and again calling the loginScreen funtion
	def reset(self,root):
		root.destroy()
		self.loginScreen()

#used to exectue the class
if __name__ == "__main__":
	t = TicTacToe()
	t.loginScreen()
