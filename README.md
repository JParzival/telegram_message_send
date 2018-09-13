# telegram_message_send
Función que envía un mensaje de telegram.

Pasos para que funcione:

1) Importar telepot (actualmente usé la última versión, 12.7).
2) Codificamos según está el código (def send_telegram_msg())
3) Necesitamos varias cosas para el bot:
- Un ID de Chat
- Un Token de uso de su API
- Un mensaje que enviar

Para ello lo primero que hacemos es irnos a telegram y hablar con @BotFather.
En ese momento pondremos /start, /newbot.
Entonces nos pedirá el nombre, por lo que tendremos que ponerle un nombre sin espacios que acabe en "bot".

En ese momento, obtendremos un token para la api. Copiamos ese token y lo reservamos para luego.

Ahora lo que tenemos que hacer es crear un nuevo grupo de telegram, y añadir al bot a dicho grupo.

Penúltimo paso: Vamos a la URL siguiente y lo ponemos de la siguiente manera:
https://api.telegram.org/bot<api>/getUpdates

Tendremos que ver todo lo que ha pasado, y si no nos sale un chat con un id con símbolo negativo delante entonces no está correcto. En caso de que esté correcto copiamos ese número ¡¡¡SIN OLVIDARNOS DEL MENOS!!! y ese será nuestro chatid.

En caso de que no salga, tendremos que echar al bot del grupo y volverlo a meter. En ese momento refrescamos la página web de la API y debería de salirnos.

El token que teníamos reservado será para la variable token del telepot.

Finalmente, la última variable que necesitamos es el mensaje, por lo que tendremos que customizarlo a nuestro gusto.
