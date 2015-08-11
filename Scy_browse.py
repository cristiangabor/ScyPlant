#!usr/bin/python
from __future__ import division
import sys
import databaseplante
import search
from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sqlite3


aplicatie=QApplication(sys.argv)

class Fereastra_3(QDialog):
	def __init__(self,eu):
		QDialog.__init__(self)
		self.setGeometry(90,90,800,700)
		search_f1=search
		#Fereastra_1_text=Fereastra_1()
		self.f1_text=Fereastra_1_text.text
		final_result=search_f1.search_plant(str(self.f1_text))
		self.layout=QGridLayout()
		self.layout1=QGridLayout()
		self.layout2=QGridLayout()


		self.popular_line_info=QLabel('<b>DENUMIRE POPULARA:</b>',self)
		self.stiintif_line_info=QLabel('<b>DENUMIRE STIINTIFICA:</b>',self)
		self.importanta_line_info=QLabel('<b>IMPORTANTA:</b>',self)
		self.descriere_line_info=QLabel('<b>DESCRIEREA PLANTEI:</b>',self)

		self.popular_line=QLabel('')
		self.stiintif_line=QLabel('',self)

		self.importanta_line=QLabel('',self)
		self.descriere_line=QLabel('',self)

		self.picture=QLabel()
		self.picture.setGeometry(0,0,300,300)
		self.pixmap=QPixmap('min/base.png')
		self.pixmap=self.pixmap.scaledToHeight(300)
		self.picture.setPixmap(self.pixmap)

		self.button_exit=QPushButton('Ok')
		self.button_exit.setFixedHeight(50)
		self.button_exit.setFixedWidth(70)
		
		self.line=QFrame()
		self.line.setFrameStyle(QFrame.VLine | QFrame.Plain)
		self.line.setLineWidth(2)
		self.line.sizeHint()

		self.button_exit.clicked.connect(self.close_window)

		self.layout.addWidget(self.popular_line_info,0,0)
		self.layout.addWidget(self.popular_line,1,0)
		self.layout.addWidget(self.stiintif_line_info,2,0)
		self.layout.addWidget(self.stiintif_line,3,0)
		self.layout.addWidget(self.importanta_line_info,4,0)
		self.layout.addWidget(self.importanta_line,5,0)
		self.layout.addWidget(self.descriere_line_info,6,0)
		self.layout.addWidget(self.descriere_line,7,0)
	
		self.layout2.addWidget(self.line,0,0)
		self.layout2.addWidget(self.picture,0,1)

		self.layout1.addLayout(self.layout,0,0)
		self.layout1.addLayout(self.layout2,0,2)
		self.layout1.addWidget(self.button_exit,3,6)

		self.setLayout(self.layout1)
		for a,b,c,d,e,f in final_result:
			self.popular_line=a

	def close_window(self):
		

		self.close()

class Fereastra_2(QDialog):
	def __init__(self,eu):
		QDialog.__init__(self)

		self.image_data=0
		self.setGeometry(90,90,600,500)
		self.laybel()

	def laybel(self):
		# LAYOUT
		self.layout_1=QGridLayout()
		self.layout_2=QGridLayout()
		self.layout_3=QGridLayout()

		# THE LINE
		self.line=QFrame()
		self.line.setFrameStyle(QFrame.VLine | QFrame.Plain)
		self.line.setLineWidth(2)
		self.line.sizeHint()

		# THE BUTTONS
		self.buttonBox=QDialogButtonBox(self)
		self.buttonBox.setOrientation(Qt.Vertical)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
		self.buttonBox.rejected.connect(self.cancel_press)
		self.buttonBox.accepted.connect(self.ok_button)

		self.adauga_button=QPushButton('Adauga',self)
		self.adauga_button.clicked.connect(self.add_data)

		# QLabel = Ce apare scris
		self.popular_line=QLabel('DENUMIRE POPULARA:',self)
		self.stiintif_line=QLabel('DENUMIRE STIINTIFICA:',self)
		self.importanta_line=QLabel('IMPORTANTA:',self)
		self.descriere_line=QLabel('DESCRIEREA PLANTEI:',self)
	

		# QLineEdit= Ce introducem text
		self.mesaj_label=QLabel('')
		self.popular_edit=QLineEdit(self)
		self.popular_edit.setMinimumWidth(100)
		
		self.stiintif_edit=QLineEdit(self)
		self.importanta_edit=QLineEdit(self)
		self.descriere_edit=QPlainTextEdit(self)
	
		self.var=[self.popular_line,self.popular_edit,self.stiintif_line,self.stiintif_edit,self.importanta_line,
		self.importanta_edit,self.descriere_line,self.descriere_edit]
		self.var1=[self.adauga_button,self.buttonBox,self.mesaj_label]
		
		self.add_Widdgets_to_layout1(self.layout_1,7,self.var)
		self.add_Widdgets_to_layout1(self.layout_2,2,self.var1)
		
		
		self.layout_3.addLayout(self.layout_1,0,0)
		self.layout_3.addLayout(self.layout_2,0,2)
		self.layout_3.addWidget(self.line,0,1,3,1)

		
		self.setLayout(self.layout_3)
	
	def ok_button(self):

		acces_database=databaseplante
		identificator=str(self.popular_edit.text())
		identificator_lower=identificator.title()

		if self.image_data !=0 and self.popular_edit.text() !='' and self.stiintif_edit.text() !='' and self.importanta_edit.text() !=0 and self.descriere_edit.toPlainText() !='':
			acces_database.insert_text(str(identificator_lower),str(self.stiintif_edit.text()),str(self.importanta_edit.text()),str(self.descriere_edit.toPlainText()),self.image_data)
		
			self.cancel_press()


	def add_data(self):
		self.value=0
		
		self.value=self.load_pic()

		
		if self.value !=0:
			self.mesaj_label.setText("<font color='red'>Incarcata!</font>")
			self.image_data=self.value
		
		
	def load_pic(self):

		filename=QFileDialog.getOpenFileName(self,'Open file','/home')

		fname=open(filename)
		
		data=fname.read()
		
		fname.close()

		#with open(filename) as file:
		#	poza=file.read()
		
		return data	

	def add_Widdgets_to_layout1(self,lay,nr,list):
			counter=0
			for i in range(0,nr+1):
				lay.addWidget(list[counter],i,0)
				counter +=1

			self.result=lay
			return self.result

	def cancel_press(self):
		self.popular_edit.setText("")
		self.stiintif_edit.setText("")
		self.importanta_edit.setText("")
		self.descriere_edit.setPlainText("")
		self.image_data=0
		self.value=0
		self.mesaj_label.setText('')
		self.close()


class Fereastra_1(QWidget):


	def __init__(self):
		QWidget.__init__(self)
		window=QWidget()

		self.layout=QHBoxLayout()
		self.layout1=QGridLayout()
		self.dialog_nou_Fereastra_3=Fereastra_3(self)
		self.dialog_nou_Fereastra_2=Fereastra_2(self)
		
		self.setWindowTitle('ScyPlant')
		self.setGeometry(100,100,400,400)
		
		self.buton_cautare=QPushButton('Cauta')
		self.buton_cautare.setToolTip('Cauta plante')
		self.buton_cautare.clicked.connect(self.conexiune_Fereastra_3)
		self.text=QLineEdit()
		self.text.setMinimumWidth(100)
  		self.text.setStyleSheet("QLineEdit { background: rgb(229,255,104); selection-background-color: rgb(233,99,0); }")
  	
		self.poza=QLabel()
		self.poza.setGeometry(10,10,200,200)
		self.pixmap=QPixmap('min/base.png')
		self.pixmap=self.pixmap.scaledToHeight(300)
		self.poza.setPixmap(self.pixmap)


		self.printButton=QPushButton('',self)
		self.printButton.setIcon(QIcon('min/test1.png'))
		self.printButton.setIconSize(QSize(43,42))
		self.printButton.setGeometry(QRect(10,10,49,30))
		self.printButton.setToolTip('Adauga plante in baza de date')
		self.printButton.clicked.connect(self.conexiune_Fereastra_2)

		self.layout1.addWidget(self.buton_cautare,3,1)
		self.layout1.addWidget(self.text,3,0)
		self.layout1.addWidget(self.poza,2,0)
		self.layout.addWidget(self.printButton)
		self.layout.addStretch()
		self.layout1.addLayout(self.layout,0,0)

		self.setLayout(self.layout1)
			
	def conexiune_Fereastra_2(self):
		self.dialog_nou_Fereastra_2.exec_()
		
	def conexiune_Fereastra_3(self):
		search_product=search
		Fereastra_3_set_Text=Fereastra_3(self)
		if self.text.text() !='':
			search_result=search_product.search_plant(str(self.text.text()))
			if search_result !=[]:
				self.dialog_nou_Fereastra_3.exec_()



	def run(self):
		self.show()
		aplicatie.exec_()

app=Fereastra_1()
app.run()





































































