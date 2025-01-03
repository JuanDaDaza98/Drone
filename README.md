Rama main contiene archivo backup para recuperacion de archivos configurados para pantalla LCD ST7796S 
Configuracion de compatibilidad Raspberry Pi zero 2W

*** CREDITOS ***
// tomado y adaptado de https://github.com/jobitjoseph/fbcp-ST7796?tab=readme-ov-file



COMANDOS PARA ACTIVACION DE CAMARA

ffmpeg -f v4l2 -i /dev/video0 -vf "scale=800:480,format=bgra" -f fbdev -pix_fmt bgra /dev/fb0


mplayer tv:// -tv driver=v4l2:device=/dev/video0 -fps 60 -vo fbdev:/dev/fb0 -vf scale=800:480,format=bgra
