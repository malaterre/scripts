#!/bin/sh

find . -type f -name '*.avi' -or -name '*.mkv' -or -name '*.mp4' | wc
find . -type f -not \( -name '*.jpg' -or -name '*.nfo' \) | wc
