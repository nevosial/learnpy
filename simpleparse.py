#This program reads from a file

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

# Open a file for writing and create it if it doesn't exist
  f = open("textfile.txt","w+")

  # Open the file for appending text to the end
#  f = open("textfile.txt","a+")

  # write some lines of data to the file
  for i in range(10):
    f.write("This is line %d\r\n" % (i+1))

  # close the file when done
  f.close()

  # Open the file back up and read the contents
  f = open("textfile.txt","r")
  if f.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
    # contents = f.read()
    # print (contents)

    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      print (x)
      

  # Print the name of the OS
  print (os.name)

  # Check for item existence and type
  print ("Item exists: " + str(path.exists("textfile.txt")))
  print ("Item is a file: " + str(path.isfile("textfile.txt")))
  print ("Item is a directory: " + str(path.isdir("textfile.txt")))

  # Work with file paths
  print ("Item's path: " + str(path.realpath("textfile.txt")))
  print ("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))

    # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print ("It has been " + str(td) + "The file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")
