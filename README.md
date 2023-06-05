# Trivial BOT
“Trivial_bot_telegram” es un juego de preguntas y respuestas enfocado a la enseñanza. Hay preguntas de todo tipo: (Matemáticas, Cultura general, Geografía, literatura e informática.)

![TRIVIAL](https://github.com/SamuelFernandezPerez/Trivial_Bot_telegram-PYTHON/assets/112828488/610933b2-f519-4598-8711-c94ef905291b)

-- **Instrucciones para jugar:**
   Para iniciar el Bot hay que introducir el comando ***/Start***
   Y para comenzar a jugar hay que introducir el comando ***/Jugar***
   Todas las preguntas se responden con una sola palabra, y esta tendrá la primera letra en Mayúscula y no se hará uso de tildes, de no ser así, la respuesta        será tomada como incorrecta.
   Las preguntas tipo: ¿Cuál es el resultado de sumar 2 + 2? Se responderán con números, es decir, en este caso la respuesta será “4”.
   Al igual pasara se introducimos mal el nombre de una temática, saltara un aviso de que se ha introducido mal y que se vuelva a escribir de nuevo.

- Al iniciarse juego, se indica al usuario que introduzca el nombre de la temática con la que desea empezar a jugar.
  Una vez introducida, se le realizara una pregunta con dicha temática.
  El usuario responderá y pasará una de estas dos opciones:
    •	Si acierta, se le suma un acierto y se le vuelve a indicar que temática quiere para la siguiente pregunta. 
    •	Si falla, se le restara un intento (vida). Y si sigue teniendo intentos disponibles (tiene 3) se le vuelve a indicar que temática quiere para la siguiente        pregunta. Por lo contrario, si no le quedan más intentos, finaliza la partida (Le saldrá la opción de volver a jugar y se resetea todo de nuevo)
- **¿Cuál es el objetivo?**
    El objetivo del juego es llegar al nivel máximo (nivel 10), según se vayan acertando preguntas se ira subiendo de nivel. Para llegar al nivel 10 el usuario       tendrá que haber respondido 50 preguntas correctamente y haber fallado como mucho 2. (si falla 3 pierde la partida)
- **¿En que orden se realiza las preguntas? ¿Son siempre las mismas?**
    El juego tiene 75 preguntas en total (15 por temática) por lo cual es improbable que se repitan dos partidas iguales, ya que solo se podrá contestar un máximo    de 53. Además de que las preguntas se realizan de forma aleatoria.
- **¿Puedo elegir siempre la misma temática?**
    No. Solo podrás elegir 11 preguntas por temática, por lo cual es obligatorio usar todas si quieres llegar al nivel máximo. Cuando hayas agotado las 11             preguntas de una temática, esta desaparecerá.
- **¿Qué obtengo por jugar?, es decir, ¿Cuál es la motivación?**
    Obtienes conocimiento y lo mas motivante, obtienes reconocimiento. Si quedas entre los tres primeros clasificados saldrás en el ranking.

Esta aplicación ha sido creada con **Visual Studio Code**.

Lenguaje utilizado: **Python**
