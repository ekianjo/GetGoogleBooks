import subprocess, os
import PyZenity

#that's a one hour project probably :)
#need the jar file from https://github.com/bhattumang7/Google-Books-Downloader

#zenity dialog

a=PyZenity.InfoMessage("This Application will let you download Google Books available in browser mode in JPG format locally for offline reading", timeout=10)

b=PyZenity.GetText("Please paste the path of the Google book to download","paste your url here")


#zenity ask for folder where to save
#make try except to catch errors of permissions
#check internet connection too

#main command
#java -jar GoogleBooksDownloader.jar "http://books.google.com/...id=sdf?asdfsdf..."  "/location/where/you/want/to/save/your/file/"

#check if progress bar if possible
#run under subprocess

#check existence of files in said folder
#if files are there, confirm download is done
