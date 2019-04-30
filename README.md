## bulk-dts-convert.py

This script is a wrapper around [mkvdts2ac3.sh](https://github.com/JakeWharton/mkvdts2ac3), and uses it to convert mkv audio tracks in bulk. It's meant for english-speaking Chromecast users and converts only DTS to AC3 (Chromecast does not support DTS audio).

The included copy of `mkvdts2ac3.sh` is slightly modified to also convert DTS-HD. You must install the dependencies for `mkvdts2ac3.sh` before using this script.

* Takes one argument - a directory which will be scanned recursively for .mkv files - e.g. `python3 bulk-dts-convert.py /home/me/myvideos`
* Converts files under only two conditions:
    * if the only audio track is DTS
    * if the default track is DTS and there are no other tracks with english defined as the language.

