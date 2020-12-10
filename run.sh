#!/bin/sh -e

# sort alphabetically since vera connect on panasonic sort item by date (=creation time), thus need to process in the same order.
# set -x
cd /media/freebox/Vidéos/repo/dessin_animes
#find . -type f \( -name '*.avi' -or -name '*.mkv' -or -name '*.mp4' \) -exec /home/mathieu/Perso/scripts/nfofix {} \;
find . -type f \( -name '*.avi' -or -name '*.mkv' -or -name '*.mp4' \) -print0 | sort -z | xargs -I{} -r0 /home/mathieu/Perso/scripts/nfofix --output /media/freebox/Vidéos/repo_new {}
