# -*- coding: utf-8 -*-
import sys
from vista.vista import *
from modelo.modelo import *

class ControladorCalculator(QtGui.QMainWindow):
	"""Controlador de la calculadora, pasa al modelo los eventos provenientes de la vista"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.vista = Ui_MainWindow() #Construimos un objeto vista
		self.vista.setupUi(self)
		#Arreglo de botones de la calculadora
		self.buttons = [	self.vista.button0,
							self.vista.button1,
			                self.vista.button2,
			                self.vista.button3,
			                self.vista.button4,
			                self.vista.button5,
			                self.vista.button6,
			                self.vista.button7,
			                self.vista.button8,
			                self.vista.button9,
			                self.vista.button_c,
							self.vista.button_erase,
							self.vista.button_decimal,
							self.vista.suma,
							self.vista.resta,
							self.vista.multiplicacion,
							self.vista.division,
							self.vista.resultado
			            ]
		# self.opButtons = [self.vista.button_c,
		# 				  self.vista.button_erase,
		# 				  self.vista.suma,
		# 				  self.vista.resta,
		# 				  self.vista.multiplicacion,
		# 				  self.vista.division	
		# 				]
		self.inputNumber = self.vista.inputNumber#Caja de texto de la calculadora
		self.modelo = ModeloCalculator()#Necesito un objeto modelo para algunas gestiones
		self.managerMuestra()#Manejador de la muestra de caracteres en la calculadora		                
		#Vamos a hacer los slots personalizados para los botones
		# QtCore.QObject.connect(self.vista.)

	def getbuttons(self):
		"""Retorna el arreglo de botones"""
		return self.buttons

	def getInputNumber(self):
		"""Retorna la caja de texto donde se mostraran los numeros y operaciones"""
		return self.inputNumber

	def managerMuestra(self):
		"""Manager de la muestra de caracteres en la caja de texto"""
		self.modelo.managerMuestra(self.buttons, self.buttonReleased)
	
	def buttonReleased(self):
		"""Funcion que se encrga de determinar qué boton ha sido seleccionado y
		luego de esto, manda el nombre del objeto del boton en forma de string al modelo
		para que este haga las gestiones pertienentes"""
 		sending_button = self.sender()#Guardo el boton clickeado
 		#self.inputNumber.setText('%s Clicked!' % str(sending_button.objectName()))
 		self.modelo.mostrarNumeros(str(sending_button.objectName()), self.inputNumber)		