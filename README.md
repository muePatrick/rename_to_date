# Rename to date
## Intro
This little script takes a path to a folder as the only argument and renames all the jpg photos in that folder to the oldest date that is noted
in the file or exif information. I needed this since my dad is sorting the family holdiday pictures from a whole lot of differnet cameras, phones
and Whatsapp chats. After renaming the files you can go through them in any cheap photo book design software.  
(Now the filesize is added at the end of the filename to differentiate pictures copied from the camera from the ones send over Whatsapp, etc.)

## New file names
year.month.day hours(24h).minutes.seconds filesize MB  
i.e.: *2019-12-14 15.45.30 6MB*

## Requirements
* [ExifRead](https://pypi.org/project/ExifRead/) is needed to read the exif information of the files