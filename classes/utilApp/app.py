# -*- coding: utf-8 -*-

import sys
import codecs
from PyQt4 import QtGui, QtCore
 
class TweetLabelinger(QtGui.QWidget):
	def __init__(self):
		super(TweetLabelinger, self).__init__()

		self.file = codecs.open("../uncategorized.tsv","r+",'utf-8')
		self.writeFile = codecs.open("../categorized.tsv","r+",'utf-8')
		self.initUi()
		self.readNextLine()

	def initUi(self):

		text = self.formattingText("")
		self.tweetLabel = QtGui.QLabel(text,self)
		self.tweetLabel.setGeometry(20,50,660,100)

		self.discontentButton = QtGui.QPushButton(u'不満',self)
		self.discontentButton.setGeometry(20,200,200,200)
		self.discontentButton.clicked.connect(self.clickDiscontentButton)

		self.satisfactionButton = QtGui.QPushButton(u'満足',self)
		self.satisfactionButton.setGeometry(250,200,200,200)
		self.satisfactionButton.clicked.connect(self.clickSatisfactionButton)

		self.otherButton = QtGui.QPushButton(u'なし',self)
		self.otherButton.setGeometry(480,200,200,200)
		self.otherButton.clicked.connect(self.clickOtherButton)

		self.setGeometry(200, 200, 700, 400)
		self.show()

	def clickDiscontentButton(self):
		self.writeFile.write(self.currentLine.replace("\n","") +"\tdiscontent\n")
		self.readNextLine()
	def clickSatisfactionButton(self):
		self.writeFile.write(self.currentLine.replace("\n","") +"\tsatisfaction\n")
		self.readNextLine()
	def clickOtherButton(self):
		self.writeFile.write(self.currentLine.replace("\n","") +"\tother\n")
		self.readNextLine()

	def readNextLine(self):
		isCategorized = True
		while isCategorized:
			isCategorized = False
			self.currentLine = self.file.readline()
			self.currentLine = self.currentLine.replace("\n","")
			self.writeFile.seek(0)
			for line in self.writeFile.readlines():
				line = line.split('\t')[0].replace("\n","")
				if line == self.currentLine:
					isCategorized = True

		text = self.formattingText(self.currentLine)
		self.tweetLabel.setText(text)

	def formattingText(self,text):
		text = insert(50,text,"\n")
		text = insert(100,text,"\n")
		text = insert(150,text,"\n")
		return text

def insert(pos, s, x):
  return x.join([s[:pos], s[pos:] ])

def main():
	app = QtGui.QApplication(sys.argv)
	example = TweetLabelinger()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()