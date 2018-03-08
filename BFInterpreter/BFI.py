"""
Angel A. Sanquiche Sanchez
angelsan720@gmail.com
angel.sanquiche@upr.edu

OK this has been a long standing project for me since some time back and being without highspeed internet makes me do some 
strange things so of course the natural thing to do is make a Brainfuck interpreter. My recent Theory of computability class
reminded me of Brainfuck and a few hours of wikipedia and sublime did wonders. Its array (here a list) is basically the tape
in the turing machine it has a pointer to a spot in the tape and a few simple functions. I left some troubleshooting funtions
behind and I might add a garbage collector later but I'm quite happy with what I've done, not perfect but I'm happy.

"""


import sys
from time import sleep

class BCI(object):
	"""docstring for BCI"""
	def __init__(self):
		self.stack = [0]
		self.text = ""
		self.stackPointer = 0
		self.textPointer = 0
		self.run = True
		self.map = {}

	def Load(self , text):
		#s = ''.join(text.split(" "))
		#s = ''.join(s.split("\n"))
		self.text = text

	def Interpret(self):
		while self.run:
			self.Interpreter()

	def Interpreter(self):
		
		if self.textPointer == len(self.text):
			self.run = False
			return

		if self.text[self.textPointer] == '>':
			self.stackPointer += 1
			if self.stackPointer == len(self.stack):
				self.stack = self.stack + [0]

		elif self.text[self.textPointer] ==  '<':
			if self.stackPointer:
				self.stackPointer -= 1
			else:
				self.stack = [0] + self.stack
		
		elif self.text[self.textPointer] == '+':
			self.stack[self.stackPointer] += 1
		
		elif self.text[self.textPointer] == '-':
			if self.stack[self.stackPointer]:
				self.stack[self.stackPointer] -= 1
			else:
				self.stack[self.stackPointer] = 0
		
		elif self.text[self.textPointer] == '.':
			print(chr(self.stack[self.stackPointer])),
		elif self.text[self.textPointer] == ',':
			#self.stack[self.stackPointer] = input("")
			self.GetInput()

		elif self.text[self.textPointer] == '[':
			self.PushBracket()
		
		elif self.text[self.textPointer] == ']':
			self.ReturnBracket()
		
		else:
			pass
		self.textPointer += 1

	def PushBracket(self):
		
		if self.textPointer in self.map.values():
			return
		else:
			s = 1

			index = self.textPointer
			while s:
				index += 1
				if len(self.text) == index:
					print("Unbalanced Brackets")
					self.run = False
					return
				elif self.text[index] == '[':
					s += 1
				elif self.text[index] == ']':
					s -= 1
			self.map[index] = self.textPointer

	def ReturnBracket(self):

		if self.stack[self.stackPointer]:
			self.textPointer = self.map[self.textPointer]

	def BFPrint(self , Text = False , Bmap = False , Stack = True):
		if Text:
			top , bottom = "" , ""
			for i in range(self.textPointer-10 , self.textPointer+10):
				try:
					top += self.text[i]
					if i == self.textPointer:
						bottom += "^"
					else:
						bottom += "-"
				except Exception as e:
					pass
			print ("--\n%s\n%s\n--"%(top , bottom))

		if Bmap:
			print(self.map)

		if Stack:
			print(self.stack)

	def GetInput(self):
		s = raw_input("")
		i = 0
		for letter in s:
			if self.stackPointer + i == len(self.stack):
				self.stack += self.stack + [0]
			self.stack[self.stackPointer+i] = ord(letter)
			i += 1


if __name__ == "__main__":
	Interpreter = BCI()
	try:
		Interpreter.Load(open(sys.argv[1] , 'r').read())
		Interpreter.Interpret()
	except Exception as e:
		print("error in inputfile")
		raise
