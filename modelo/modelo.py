 #!/usr/bin/python
 # -*- coding: utf-8 -*-
class ModeloCalculator(object):
	"""Modelo de la calculadora, se encarga de hacer las operaciones"""
	def __init__(self):
		pass

	def managerMuestra(self, array, botton_clickeado):
		"""Para cada boton presente en un arreglo de nuemeros, esta funcion valida si ese boton
		coincide con el boton clickeado"""
		for button in array:#Array de bototnes de numeros
			if button.released.connect(botton_clickeado):
				True

	def mostrarNumeros(self, botton_clickeado, inputNumber):
		"""Pone en la caja de texto los caracteres segun el boton clickeado"""
		inicial = inputNumber.text()#obtengo el texto actual del input
		if botton_clickeado == "button0":#Si el nombre del objeto boton en donde se hizo click fue 'button0',entonces
			inputNumber.setText(inicial+'0')#se pone en la caja de texto lo que hubiese en el input mas el 0
		elif botton_clickeado == "button1":
			inputNumber.setText(inicial+'1')
		elif botton_clickeado == "button2":
			inputNumber.setText(inicial+'2')
		elif botton_clickeado == "button3":
			inputNumber.setText(inicial+'3')
		elif botton_clickeado == "button4":
			inputNumber.setText(inicial+'4')
		elif botton_clickeado == "button5":
			inputNumber.setText(inicial+'5')
		elif botton_clickeado == "button6":
			inputNumber.setText(inicial+'6')
		elif botton_clickeado == "button7":
			inputNumber.setText(inicial+'7')
		elif botton_clickeado == "button8":
			inputNumber.setText(inicial+'8')
		elif botton_clickeado == "button9":
			inputNumber.setText(inicial+'9')
		elif botton_clickeado == "button_decimal":
			inputNumber.setText(inicial+'.')
		elif botton_clickeado == "button_erase":#se borra un digito de la cadena
			self.erase(inicial, inputNumber)
		elif botton_clickeado == "button_c":#si se da click en el boton C, entonces lo que hubiese en incial sera reseteado
			inicial = '0'
		elif botton_clickeado == "suma":
			inputNumber.setText(inicial+'+')
		elif botton_clickeado == "resta":
			inputNumber.setText(inicial+'-')												
		elif botton_clickeado == "multiplicacion":
			inputNumber.setText(inicial+'x')
		elif botton_clickeado == "division":
			inputNumber.setText(inicial+'/')	
		else:#Si no se hizo click en ninguno de los anteriores botones fue porque se hozo click en el boton de 'resultado' (boton igual)
			self.getResultado(inicial, inputNumber)		
			
	def compruebaCadena(self, cadena):
		"""Retorna un booleano, True si la cadena resibida es correcta y se puede evaluar para su
		posterior resultado, False si la cadena presenta anomalias"""
		cadena = str(cadena) #Se pasa de QtString a str
		#Si la cadena empieza con operadores entonces no será una cadena valida
		if cadena.startswith('/') or cadena.startswith('x') or cadena.startswith('+') or cadena.startswith('-'):
			return False
		#Si la cadena termina con operadores entonces no será una cadena valida	
		elif cadena.endswith('/') or cadena.endswith('x') or cadena.endswith('+') or cadena.endswith('-'):
			return False
		#si la cadena es alfabetica	
		elif cadena.isalpha():
			return False
		elif cadena.count('.') > 1:#Si hay dos puntos decimales en un mismo numero es un error
			return False		
		else:
			return True	

	def getResultado(self, cadena, inputNumber):
		"""Muestra el resultado de una cadena valida"""
		cadena = cadena.replace('x', '*')#Se reemplaza 'x' por '*' para que eval pueda evaluar las expresiones con multiplicaciones
		try:
			if self.compruebaCadena(cadena) == False: #Si hay un error en la cadena...
				inputNumber.setText("Error")
			else:
				if cadena is int:
					int(cadena)
				elif cadena is float:
					float(cadena)	

				cadena = str(cadena)#eval funciona con la cadena primitiva de python, la cadena que viene es de typo QtString
				resultado = eval(cadena)
				inputNumber.setText(str(resultado)) #Muestro en el input el resultado
		except (ZeroDivisionError, Exception):
			inputNumber.setText("Error")
			
		
	def erase(self, cadena, inputNumber):
		"""Borra un digito de la cadena"""
		cadena = str(cadena)#se convierte de QtString a string
		longCadena = len(cadena)#longitud de la cadena

		if longCadena is 0:#Si la longitud de la cadena es cero es porque ya se han borrado todos los digitos
			inputNumber.setText('')
		else:
			firstCaracter = cadena[longCadena-1]#se obtine el ultimo elemento de la cadena (longitud -1)
			cadena = cadena.rstrip(firstCaracter)#se elimina el caracter desde mas a la derecha de la cadena
			inputNumber.setText(cadena)#se escribe la cadena en el input
