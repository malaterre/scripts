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

Sous-titres:

impossible de faire marcher:

 ffmpeg -y -i input.mkv -map 0 -c copy -c:s mov_text -tag:s:s:0 tx3g output_1.mp4
 ffmpeg -y -i input.mkv -map 0 -c copy -c:s mov_text -tag:s:s:0 tx3g output_2.mov
 ffmpeg -y -i input.mkv -map 0 -c copy -c:s mov_text                 output_3.mp4
 ffmpeg -y -i input.mkv -map 0 -c copy -c:s mov_text                 output_4.mov


sous-titres => mkv seulement

BUGS:

Watch out for:
* https://code.videolan.org/videolan/x264/commit/f9af2a0f71d0fca7c1cafa7657f03a302da0ca1c
* https://trac.ffmpeg.org/ticket/8084
