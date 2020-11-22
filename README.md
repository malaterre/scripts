# scripts

Convert video for Freebox Mini 4K

So far only mkv and mp4 container seems to work

|       |   aac   | ac3 | mp3 |
|-------|---------|-----|-----|
| h264  | mp4/mkv | mkv | mkv |
| mjpeg |   mkv   | mkv | mkv |
| mpeg4 |   mkv   | mkv | mkv |

TODO:

* les mkv ont un canal 'indéfini'
* les mp4 multi-canaux sont toujours affichés en 'Français'
* mp4 a voir si on peut mettre un titre (affiché avec ``` à l'écran)
* Impossible d'afficher la vignette contenu en stream #1...a voir si ca marche en stream #0...pas mieux mini4k ne semble pas supporté les vignettes
* mkv -> mp4 ass subtitle pas supporté, voir : ffmpeg -i input.mkv -c copy -c:s mov_text output.mp4
