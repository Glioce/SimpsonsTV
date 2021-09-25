# SimpsonsTV

Reproduce capítulos aleatorios de los Simpsons.  
Podría ser consola de videojuegos.  

Basado en https://www.thingiverse.com/thing:4943159  
Guía original https://withrow.io/simpsons-tv-build-guide  
Repo original https://github.com/buba447/simpsonstv  

Cambios realizados
- Pantalla un poco diferente http://www.lcdwiki.com/2.4inch_SPI_Module_ILI9341_SKU:MSP2402
- Ensamblaje más fácil, se necesita menos pegamento
- Conectores de rasp accesibles desde afuera
- Emulación de videojuegos con RetroPie

## Instrucciones de instalación de software

### Retropie
Descargar imagen de RetroPie. Elegir la opción "Raspberry Pi 0/1"  
https://retropie.org.uk/download/  

Grabar en Micro SD usando Raspberry Imager.  
https://www.raspberrypi.org/software/  

Conectar a red wifi y activar ssh.

Opcional Kodi y gamepad  
Se intentó instalar Kodi dentro de RetroPie, pero la instalación falla. Al parecer intenta descargar archivos que ya no están en línea. Posiblemente se solucione cuando se publique una actualización.  
Si un día se puede instalar, este video puede ser útil  
https://www.youtube.com/watch?v=bR6NMkgRYuU

Configuración inicial de RetroPie (gamepad)
https://retropie.org.uk/docs/Controller-Configuration/

### Controlador de pantalla  
https://github.com/juj/fbcp-ili9341  
Clonar repo, entrar al directorio, crear directorio "build" y entrar a ese nuevo directorio
```bash
git clone https://github.com/juj/fbcp-ili9341.git
cd fbcp-ili9341
mkdir build
cd build
```

Generar archivos de configuración con los parámetros de nuestra pantalla
```bash
cmake -DILI9341=ON -DGPIO_TFT_DATA_CONTROL=5 -DGPIO_TFT_RESET_PIN=6 -DSPI_BUS_CLOCK_DIVISOR=6 -DSTATISTICS=0 ..
```

Parámetros opcionales
- DSTATISTICS=1 para mostrar información en la pantalla.
- DGPIO_TFT_BACKLIGHT=16 para controlar la retroiluminación con un GPIO.

Ahora compilar  y  lanzar el ejecutable recién compilado
```bash
make
sudo ./fbcp-ili9341
```

Aquí hay un video para entender cómo usar el controlador. El diagrama de conexión se tomó del video. No se deben seguir todos los pasos.  
https://www.youtube.com/watch?v=KciKqGX8g94  


Copiar videos. Copiar scripts pyhon. Configurar arranque. Copiar juegos (opcional).  

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
