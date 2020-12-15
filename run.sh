#!/bin/sh -e
# set -x

# get latest ffmpeg
PATH=$HOME/bin:$PATH

cd /media/freebox/Vidéos/repo/dessin_animes

#FIXME need somehow to sort alphabetically since vera connect on panasonic sort item by date (=creation time), thus need to process in the same order.
#find . -type f \( -name '*.avi' -or -name '*.mkv' -or -name '*.mp4' \) -print0 | sort -z | xargs -I{} -r0 /home/mathieu/Perso/scripts/nfofix --output /media/freebox/Vidéos/repo_new {}

find . -type f \( -name '*.avi' -or -name '*.mkv' -or -name '*.mp4' \) -exec /home/mathieu/Perso/scripts/nfofix --output /media/freebox/Vidéos/repo_new {} \;
