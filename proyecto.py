#He importado random para seleccionar preguntas aleatorias.
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext
#variable que almacena el nombre del usuario (se obtiene al iniciar trivial)
usuario = ""
#variable que almacena el nivel que va adquiriendo el usuario.
nivel = 0
#abro el fichero del ranking para sacar su información, (el diccionario)
ficheroRanking = open("ranking.txt", "r", encoding ="utf-8")
contenidoFichero = ficheroRanking.read()
#y le guardo como "ranking".
ranking = eval(contenidoFichero)
#cierro el fichero porque ya no le necesito.
ficheroRanking.close()
#He creado una lista de tematicas para que el usuario escoja la que mas le convenga.
#Cada tematica tiene un limite de preguntas como explicare más adelante.
tematicas = ["Mates", "Cultura_general", "Geografia", "Informatica", "Literatura"]
#Diccionario en el se ira almacenando la respuesta correcta de la pregunta actual.
respuestaCorrecta = {"dato" : ""}
#Variable que almacena los intentos que tiene el usario si fallara alguna pregunta (se iran restando)
vidas = 3
#Variable que almacena las preguntas acertadas.
preguntasAcertadas = 0
#Variables que almacenan las veces que se ha usado cada temática.
mates = 0
cultura_general = 0
geografia = 0
informatica = 0
literatura = 0
#Abro los ficheros que he creado con anterioridad y almaceno las preguntas y respuestas por temática.
lecturaFicheroMates = open("mates.txt", "r", encoding ="utf-8")
lecturaFicheroCultura = open("cultura_general.txt", "r", encoding ="utf-8")
lecturaFicheroGeografia = open("geografia.txt", "r", encoding ="utf-8")	
lecturaFicheroInformatica = open("informatica.txt", "r", encoding ="utf-8")
lecturaFicheroLiteratura = open("literatura.txt", "r", encoding ="utf-8")
#Almaceno en sus correspondientes variables las lineas de dichos ficheros.
#En cada linea hay una pregunta y una respuesta (estan separadas por ":")
#Pense en hacer todo en un fichero pero asi es mejor por si quiero añadir más preguntas en un futuro (asi no toco el programa)
contenidoFicheroMates = lecturaFicheroMates.readlines()	
contenidoFicheroCultura = lecturaFicheroCultura.readlines()	
contenidoFicheroGeografia = lecturaFicheroGeografia.readlines()	
contenidoFicheroInformatica = lecturaFicheroInformatica.readlines()	
contenidoFicheroLiterartura = lecturaFicheroLiteratura.readlines()	
#Cierro los ficheros porque ya no los necesito.
lecturaFicheroMates.close()
lecturaFicheroCultura.close()
lecturaFicheroGeografia.close()
lecturaFicheroInformatica.close()
lecturaFicheroLiteratura.close()

ficheroRanking = open("ranking.txt", "r", encoding ="utf-8")
contenidoFichero = ficheroRanking.read()
ranking = eval(contenidoFichero)
ficheroRanking.close()

# Aqui definimos las funciones que realiza el bot.
def start(update: Update, context: CallbackContext):
	# Al inicial, enviamos un mensaje al usuario.
	update.message.reply_text("¡Bot Trivial activado!")
	# Mostramos por terminal quién se ha conectado y le indico al usuario las reglas y de que trata el juego.
	print("Se ha conectado el usuario: " + update.effective_user.name)
	update.message.reply_text("¡Vamos a jugar al trivial! Empezaras siendo nivel 0, y según vayas acertando iras subiendo de nivel. (55 preguntas, 5 tematicas, 10 niveles, 3 vidas).")
	update.message.reply_text("¿Serás capaz de llegar al nivel 10? Escribe /Jugar para comenzar la partida.")
	update.message.reply_text("¡ATENCIÓN! ¡La primera letra de cada palabra siempre en mayuscula y no uses tildes!")

#Función que pondra en marcha el juego. Lo indicara por terminal y al usuario le pedira una temática.
def Jugar(update: Update, context: CallbackContext):
	print("El usario " + update.effective_user.name + " ha comenzado a jugar al Trivial")
	update.message.reply_text("Dime temática : " + str(tematicas))
	global usuario
	usuario = update.effective_user.name
	#SI EL USUARIO HA TERMINADO UNA PARTIDA Y DECIDE VOLVER A JUGAR, RESETEO TODAS LAS VARIABLES NECESARIAS
	global nivel
	nivel = 0
	global vidas
	vidas = 3
	global preguntasAcertadas
	preguntasAcertadas = 0
	global mates
	mates = 0
	global cultura_general
	cultura_general = 0
	global geografia
	geografia = 0
	global informatica
	informatica = 0
	global literatura
	literatura = 0
	#pasamos al siguiente "Estado" de la conversación.
	return 0

#Función que se encarga de seleccionar la tematica elegida por el usuario y de hacerle la pregunta que corresponda.	
def trivial(update: Update, context: CallbackContext):
	mensajeRecibido = update.message.text
	#Meto las variables globales dentro de la función para poder sacar los datos actualizados a fuera a traves de variables locales.
	global mates
	preguntasMates = mates
	global cultura_general
	preguntasCultura = cultura_general
	global geografia
	preguntasGeografia = geografia
	global informatica
	preguntasInformatica = informatica
	global literatura
	preguntasLiteratura = literatura

	#Y si el texto coincide con "Mates:"
	if mensajeRecibido == "Mates":
		#Y si "mates" se ha elegido menos de las veces permitidas como veces como temática:
		if mates < 11:
			#sumo 1 a la variable global que almacena las veces que se ha usado esta temática..
			preguntasMates = preguntasMates + 1
			mates = preguntasMates
			#Imprimo por terminal la temática elegida.
			print(update.effective_user.name + " ha elegido mates.")
			#Creo una variable que alamacena temporalmente una de las lineas (random) que hemos extraido del fichero "mates.txt".
			ElijopreguntaYrespuesta = (random.choice(contenidoFicheroMates))
			#Ahora creo una variable que separa dicha linea en dos partes a traves de ":" creando dos posiciones (0 y 1).
			#La posición 0 es la pregunta y la posición 1 es la respuesta.
			preguntaYrespuesta = ElijopreguntaYrespuesta.split(":")
			#Ahora meto la pregunta en una lista.
			pregunta = preguntaYrespuesta[0]
			#Y la respuesta en un diccionario para que pueda ser leida como una palabra.
			respuestaCorrecta["dato"] = preguntaYrespuesta[1]
			#Le dijo al usuario la pregunta.
			update.message.reply_text(pregunta)
			#Y elimino la linea completa donde tengo almacenado el contenido del fichero.
			#Asi esta pregunta ya no se puede volver a repetir.
			contenidoFicheroMates.remove(ElijopreguntaYrespuesta)
		#Si mates ya ha sido usada como temática 12 veces
		else:
			#Le digo al usuario que ya no puede jugar con esta temática y que escoja otra.
			update.message.reply_text("Has agotado todas las preguntas de Mates. ELIGE OTRA TEMATICA.")
			#Elimino esta temática de la lista de temáticas disponibles para jugar.
			tematicas.remove("Mates")
			#Le mando las temáticas actualizadas.
			update.message.reply_text("Dime temática : " + str(tematicas) + " o pulsa /cancel si deseas terminar la partida.")
			#Imprimo por el terminal que dicha temática ya no se puede usar.
			print(update.effective_user.name + " ha agotado todas las preguntas de mates")
			#y retorno a la función "trivial" para comprobar la disponibilidad de la nueva tematica introducida por el usuario.
			return 0

	#EL RESTO ES LO MISMO CON LAS DIFERENTES TEMATICAS HASTA DONDE VUELVO A INTRODUCIR COMENTARIOS

	elif mensajeRecibido == "Cultura_general":
		if cultura_general < 11:
			preguntasCultura = preguntasCultura + 1
			cultura_general = preguntasCultura
			print(update.effective_user.name + " ha elegido cultura_general.")
			ElijopreguntaYrespuesta = (random.choice(contenidoFicheroCultura))
			preguntaYrespuesta = ElijopreguntaYrespuesta.split(":")
			pregunta = preguntaYrespuesta[0]
			respuestaCorrecta["dato"] = preguntaYrespuesta[1]
			update.message.reply_text(pregunta)
			contenidoFicheroCultura.remove(ElijopreguntaYrespuesta)
		else:
			update.message.reply_text("Has agotado todas las preguntas de Cultura_general. ELIGE OTRA TEMATICA.")
			tematicas.remove("Cultura_general")
			update.message.reply_text("Dime temática : " + str(tematicas) + " o pulsa /cancel si deseas terminar la partida.")
			print(update.effective_user.name + " ha agotado todas las preguntas de Cultura_general")
			return 0
		
	elif mensajeRecibido == "Geografia":
		if geografia < 11:
			preguntasGeografia = preguntasGeografia + 1
			geografia = preguntasGeografia
			print(update.effective_user.name + " ha elegido geografia.")
			ElijopreguntaYrespuesta = random.choice(contenidoFicheroGeografia)
			preguntaYrespuesta = ElijopreguntaYrespuesta.split(":")
			pregunta = preguntaYrespuesta[0]
			respuestaCorrecta["dato"] = preguntaYrespuesta[1]
			update.message.reply_text(pregunta)
			contenidoFicheroGeografia.remove(ElijopreguntaYrespuesta)
		else:
			update.message.reply_text("Has agotado todas las preguntas de Geografia. ELIGE OTRA TEMATICA.")
			tematicas.remove("Geografia")
			update.message.reply_text("Dime temática : " + str(tematicas) + " o pulsa /cancel si deseas terminar la partida.")
			print(update.effective_user.name + " ha agotado todas las preguntas de Geografia")
			return 0

	elif mensajeRecibido == "Informatica":
		if informatica < 11:
			preguntasInformatica = preguntasInformatica + 1
			informatica = preguntasInformatica
			print(update.effective_user.name + " ha elegido informatica.")
			ElijopreguntaYrespuesta = (random.choice(contenidoFicheroInformatica))
			preguntaYrespuesta = ElijopreguntaYrespuesta.split(":")
			pregunta = preguntaYrespuesta[0]
			respuestaCorrecta["dato"] = preguntaYrespuesta[1]
			update.message.reply_text(pregunta)
			contenidoFicheroInformatica.remove(ElijopreguntaYrespuesta)
		else:
			update.message.reply_text("Has agotado todas las preguntas de Informatica. ELIGE OTRA TEMATICA.")
			tematicas.remove("Informatica")
			update.message.reply_text("Dime temática : " + str(tematicas) + " o pulsa /cancel si deseas terminar la partida.")
			print(update.effective_user.name + " ha agotado todas las preguntas de Informatica")
			return 0

	elif mensajeRecibido == "Literatura":
		if literatura < 11:
			preguntasLiteratura = preguntasLiteratura + 1
			literatura = preguntasLiteratura
			print(update.effective_user.name + " ha elegido literatura.")
			ElijopreguntaYrespuesta = (random.choice(contenidoFicheroLiterartura))
			preguntaYrespuesta = ElijopreguntaYrespuesta.split(":")
			pregunta = preguntaYrespuesta[0]
			respuestaCorrecta["dato"] = preguntaYrespuesta[1]
			update.message.reply_text(pregunta)
			contenidoFicheroLiterartura.remove(ElijopreguntaYrespuesta)
		else:
			update.message.reply_text("Has agotado todas las preguntas de Literatura. ELIGE OTRA TEMATICA.")
			tematicas.remove("Literatura")
			update.message.reply_text("Dime temática : " + str(tematicas) + " o pulsa /cancel si deseas terminar la partida.")
			print(update.effective_user.name + " ha agotado todas las preguntas de Literatura")
			return 0

		#Mensaje de error si el usuario ha introducido una tematica invalida, "eliminada" o la ha escrito mal.
		#Le vuelvo a preguntar que temática quiere y le retorno al inicio de la función para realizar el proceso de comprobación.
	else:
		update.message.reply_text("Tematica no reconocida. Compruebe que se ha escrito correctamente y sin tildes y que aun siga estando disponible.")
		update.message.reply_text("Dime temática : " + str(tematicas))
		return 0
	#Si el usario ha elegido una tematica disponible (se le habra realizado una pregunta) y ahora vamos a comprobar si su repuesta es correcta.
	return 1

#Función que se va a encargar de compobar si el usuario a respondido correctamente
def ComprobacionRespuestas(update: Update, context: CallbackContext):
	#Meto las variable global dentro de la función para poder sacar los datos actualizados a fuera a través de una variables local.
	global vidas
	#Creo una variable local para obtener la información de la global (Vidas disponibles)
	restarvidas = vidas
	#Meto las variable global dentro de la función para poder sacar los datos actualizados a fuera a través de una variables local.
	global preguntasAcertadas
	sumarPreguntasAcertadas = preguntasAcertadas
	#Meto la variable global nivel para sacar su valor fuera de la función.
	global nivel
	#variable que almacena el texto escrito por el usuario. 
	respuestaRecibida = update.message.text

	#Ahora voy a comprobar cuantas respuestas van acertadas para mandar un mensaje u otro
	#todas funcionan igual , solo varia el numero de aciertos que será el que indique el nivel
	#asi que solo voy a explicar la primera al igual que antes

	#si las preguntas acertadas son igual a: (en este caso a 1)
	if preguntasAcertadas == 0:
		#y si la respuesta que tenbemos almacenada quitando salto de linea es igual a la respuesta recibida.
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			#se suma 1 a las preguntas acertadas.
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			#escribo por el terminbal que el usuario sube de nivel.
			print(update.effective_user.name + " ha acertado y ahora es nivel 1.")
			#Y se lo comunico al usuario por la app.
			update.message.reply_text("¡Correcto! Ahora eres nivel 1.")
			#actualizo la variable nivel
			nivel = nivel + 1
		#si la respuesta no coincide:
		else:
			#Resto una videa al usuario.
			restarvidas = restarvidas - 1
			vidas = restarvidas
			#Indico por el terminal que el usuario ha fallado y las vidas que le quedan.
			print(update.effective_user.name + " ha fallado y le quedan " + str(vidas) + " vidas.")
			#Y se lo comunico a el.
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
			
	elif preguntasAcertadas == 5:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 2.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 2.")
			nivel = nivel + 1
		else:
			restarvidas = restarvidas - 1
			vidas = restarvidas
			print(update.effective_user.name + " ha fallado y le quedan " + str(vidas) + " vidas.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 10:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 3.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 3.")
			nivel = nivel + 1
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 15:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 4.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 4.")
			nivel = nivel + 1
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 20:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 5.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 5.")
			nivel = nivel + 1
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 25:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 6.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 6.")
			nivel = nivel + 1
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 30:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 7.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 7.")
			nivel = nivel + 1
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 35:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 8.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 8.")
			nivel = nivel + 1
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 40:

		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y ahora es nivel 9.")
			update.message.reply_text("¡Correcto! Ahora eres nivel 9.")
			nivel = nivel + 1
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	elif preguntasAcertadas == 49:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado y finaliza la partida con nivel 10.")
			nivel = nivel + 1
			#COMO SE HA FINALIZADO LA PARTIDA:
			#abro el fichero "ranking" para actualizar el ranking.
			ficheroRanking = open("ranking.txt", "w", encoding ="utf-8")
			#llamo a la función para compararle.
			comparaRanking(nivel)
			#imprimo el ranking en el .txt
			ficheroRanking.write(str(ranking))
			#y cierro el fichero.
			ficheroRanking.close()
			#comunico al usuario que ha alcanzado el nivel maximo.
			update.message.reply_text("¡Correcto! Ahora eres nivel 10. Enhorabuena has terminado el juego con exito.")
			#le muestro el ranking.
			update.message.reply_text("RANKING: " + str(ranking))
			#y le doy la opcion de volver a jugar.
			update.message.reply_text("Si deseas volver a jugar, escribe /jugar")
			#finalizo la conversación.
			return ConversationHandler.END
		else:
			print(update.effective_user.name + " ha fallado.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")
	#Esta parte es igual solo que se llevara a cabo si el usuario lleva "x" aciertos pero no se corresponde con ningun nivel:
	else:
		if respuestaCorrecta["dato"].rstrip('\n') == respuestaRecibida:
			sumarPreguntasAcertadas = sumarPreguntasAcertadas + 1
			preguntasAcertadas = sumarPreguntasAcertadas
			print(update.effective_user.name + " ha acertado.")
			update.message.reply_text("¡Correcto!")
		else:
			restarvidas = restarvidas - 1
			vidas = restarvidas
			print(update.effective_user.name + " ha fallado y le quedan " + str(vidas) + " vidas.")
			update.message.reply_text("Incorrecto. Te quedan " + str(vidas) + " vidas.")

	#Despues de cada resolucion se le comunica al usuario cuantas preguntas lleva .
	update.message.reply_text("Actualmente llevas " + str(preguntasAcertadas) + " aciertos.")
	#Y tambien se muestra por el terminal.
	print(update.effective_user.name + " actualmente lleva " + str(preguntasAcertadas) + " aciertos.")

	#si despues de responder el usuario ha fallado, se comprueba cuantas vidas le quedan.
	#Y si tiene mas de 0:
	if vidas > 0:
		#seguimos haciendole preguntas, a no ser que quiera cancelar
		update.message.reply_text("Dime temática : " + str(tematicas) + " o pulsa /cancel si deseas terminar la partida.")
		return 0
	#si no tiene vidas:
	else:
		#COMO SE HA FINALIZADO LA PARTIDA:
		#abro el fichero "ranking" para actualizar el ranking si fuera necesario.
		ficheroRanking = open("ranking.txt", "w", encoding ="utf-8")
		#llamo a la función para compararle.
		comparaRanking(nivel)
		#imprimo el ranking en el .txt
		ficheroRanking.write(str(ranking))
		#y cierro el fichero.
		ficheroRanking.close()
		#se le comunica al usuario que la partida ha llegado a su fin.
		update.message.reply_text("GAME OVER")
		#se indica por el terminal, asi como su nivel alcanzado.
		print("El usuario " + str(usuario) + " ha finalizado la partida con nivel " + str(nivel) + ".")
		#le digo el nivel alcanzado al usuario.
		update.message.reply_text("Has finalizado la partida con nivel " + str(nivel) + ".")
		#y le muestro el ranking. 
		update.message.reply_text("RANKING: " + str(ranking))
		#y por ultimo se le da la opción de volver a jugar si lo desea.
		update.message.reply_text("Si deseas volver a intentarlo escribe /jugar ")
		#finalizo la conversación.
		return ConversationHandler.END
		

#funcion que comparara si hay que hacer cambios en el ranking.
def comparaRanking(nivel):
	#si el nivel del usuario actual es menor que el nivel del tercer clasificado del ranking:
	if nivel < ranking["3º"][1]:
		#no pasa nada.
		pass
	#si el nivel del usuario actual es mayor que el nivel del tercer clasificado del ranking:
	elif  nivel > ranking["3º"][1]:
		#pero el nivel del usuario actual es menor que el nivel del segundo clasificad.o
		if nivel < ranking["2º"][1]:
			#asignamos la tercera posición al usuario actual. 
			ranking["3º"] = [usuario, nivel]
		#y si no, si el nivel del usuario actual es mayor que el nivel del segunda clasificado del ranking:
		elif nivel > ranking["2º"][1]:
			#pero es menor que el nivel del primer clasificado:
			if nivel < ranking["1º"][1]:
				#bajamos una posicion al segundo clasificado.
				ranking ["3º"] = ranking ["2º"]
				#y ponemos en el segundo lugar al usuario actual.
				ranking["2º"] = [usuario, nivel]
			#y si no,si el nivel del usuario actual es mayor que el del segundo y no es menor que el del primero:
			else:
				#bajamos una posicion al segundo clasificado
				ranking ["3º"] = ranking ["2º"]
				#bajamos una posicion al primer clasificado
				ranking ["2º"] = ranking ["1º"]
				#ponemos primero al uusario actual
				ranking["1º"] = [usuario, nivel]
		else:
			#si el nivel del usuario actual es igual al nivel del segundo clasificado
			#asignamos el puesto al uusario actual
			ranking["2º"] = [usuario, nivel]
			#y bajamos una posicion al segundo clasificado
			ranking ["3º"] = ranking ["2º"]
	else:
		#si el nivel del usuario actual es igual al nivel del tercer clasificado
		#asignamos el puesto al uusario actual
		ranking["3º"] = [usuario, nivel]



#Función que permite al usuario abandonar la partida en cualquier momento
def cancel(update: Update, context: CallbackContext) -> int:
	update.message.reply_text("Gracias por jugar " + update.effective_user.name)
	update.message.reply_text("Si deseas volver a jugar en otro momento, escribe /jugar")
	print(update.effective_user.name + " deja de jugar.")
	return ConversationHandler.END
#Función que se aplica cuando el usuario introduce un texto no reconocido por el programa
def noComprendo(update: Update, context: CallbackContext):
	update.message.reply_text("No sé qué me quieres decir.")
# Programa principal del bot
def main():
	print("Iniciamos el bot Trivial")
	updater = Updater("1669640364:AAHedOZnSSEy_d0adkDVkf9rDuMZgA739Eo", use_context=True)

	dispatcher = updater.dispatcher

	# Configuración de los comandos
	dispatcher.add_handler(CommandHandler("start", start))
	#conversación "Trivial"
	jugandoAlTrivial = ConversationHandler(
		entry_points=[CommandHandler("Jugar", Jugar)],
		states = {
			0 : [MessageHandler(Filters.text & ~Filters.command, trivial)],
			1 : [MessageHandler(Filters.text & ~Filters.command, ComprobacionRespuestas)]
			},
		fallbacks=[CommandHandler('cancel', cancel)],)

	dispatcher.add_handler(jugandoAlTrivial)
	dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, noComprendo))

	# Comienza a escuchar
	updater.start_polling()
	updater.idle()


# Programa principal que ejecuta el bot
if __name__ == '__main__':
	main()
  