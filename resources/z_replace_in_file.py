import fileinput
import sys

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)



datum = system.exec_command("date +%d.%m.%Y")
replaceAll("/home/jan-hendrik/Desktop/test.txt","DATUM",datum)