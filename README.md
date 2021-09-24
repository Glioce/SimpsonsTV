# SimpsonsTV

Reproduce capítulos aleatorios de los Simpsons.  
Podría ser consola de videojuegos.  

Basado en https://www.thingiverse.com/thing:4943159  
Guía original https://withrow.io/simpsons-tv-build-guide  

Cambios realizados
- Pantalla un poco diferente http://www.lcdwiki.com/2.4inch_SPI_Module_ILI9341_SKU:MSP2402
- Ensamblaje más más resistente
- Conectores de rasp accesibles desde afuera
- Emulación de videojuegos con RetroPie

## Instrucciones de instalación de software
Descargar imagen de RetroPie. Grabar en Micro SD. Instalar controlador de pantalla. Copiar videos. Copiar scripts pyhon. Configurar arranque. Copiar juegos (opcional).  

Este es el repo original https://github.com/buba447/simpsonstv  
El script de los botones se modificó. Ahora funciona con un push button simple.   

Por hacer:
- función para cambiar videos y cambiar a modo consola de juegos con botones frontales.
- Obtener salida de audio por HDMI y GPIO de forma simultánea

Notas sobre el audio  
La salida de audio por GPIO también se puede configurar de esta forma  
https://shallowsky.com/blog/hardware/pi-zero-audio.html  
https://www.youtube.com/watch?v=3pXB90IDNoY  
https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero/pi-zero-pwm-audio  

A veces se escucha un zumbido, no importa el GPIO que se utilize. Para solucionarlo se puede poner un circuito para filtrar, o poner una resistencia en serie con la bocina, esta forma no reduce por completo el zumbido, pero sí se reduce mucho.

## Instrucciones de armado
Imprimir piezas. Se necesitan 3 colores ...

## Cotización
Está en el Drive de Invento. El archivo se llama "Cotización Mini Arcade y TV de los Simpsons"
