import sys, time
# Replaces the "PRINT" func with a typewriter effect.
def typing(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)

typing ("Enter A Number Please:")
# Takes user's number input and confirms it.
UserNumber = input (" ")
time.sleep(0.5)
typing ("Your Number Is " + (UserNumber) + "?" + " (Y/N)")
inputyn = input (" ")
if inputyn == ("Y"):
   typing ("Great!")
if inputyn == ("N"):
   typing("Please Re-Input Your Number.") 
   UserNumber = input (" ")
   typing ("Is Your Number " + (UserNumber) + "?" + " (Y/N) ")
   inputynfail = input ("")
   if inputynfail == ("Y"): ("Great!") 
   if inputynfail == ("N"): ("Then Go Away!")
   else: typing ("Unrecoginzed Input.")
