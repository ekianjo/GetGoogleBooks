from os import listdir
from os.path import isfile, join
import subprocess


mypath="BOOKS/The Law"


onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

onlyfiles.sort()

#print onlyfiles

longstring=""

for element in onlyfiles:
	longstring+='''"{0}/{1}"'''.format(mypath,element)+" "

print longstring

cmd = 'python img2pdf.py {0} -o TheLaw.pdf -C 1'.format(longstring)

proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

proc.terminate
