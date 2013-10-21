GetGoogleBooks
==============

A Python application to download Google Books to a given folder, and then convert the files into a pdf document that can be read with a PDF viewer. It's actually a mix of pysheng and img2pdf. 

Requirements
------------

You need the Python Image Library on your system, and of course Python >2.6. Not tested with Python3. 
img2pdf and PyZenity are other dependencies but are provided in this repository together (both GPL).

License
-------

Released under GPL v3.

Usage
-----

Simply run in a terminal : python download.py and follow the instructions. You will need to input the URL of the Google Book you want to download, naturally. Note that it will download only what is visible on the said Google Book page, i.e. snippets or full book depending on what is freely available. It will then create a folder where the pictures are downloaded and will create a PDF out of it in the BOOKS folder. 

Known issues
------------

img2pdf seems to have some issues when dealing with some colorspaces so all colorspace is defaulted to 1. This may give issues to covers, but this should render the text contents just fine. 

