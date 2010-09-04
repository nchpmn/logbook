# Any file IO operations are to pass through this module.

import os

# Filename Variables
passfile = "pass.txt"
logfile = "log.txt"
totalfile = "totals.txt"

# Password Functions (passCheck module)
def getPass():
    """Get the password Hash from file"""
    f = open(passfile, 'r') # Opens the file 'pass.txt'
    passTemp = f.read() # Gets contents of the file
    f.close() # Closes the file so we can't change it by accident
    return passTemp

def savePass(userHash):
    """Save the password Hash to file"""
    f = open(passfile, 'w') # Opens 'pass.txt'
    f.write(userHash) # Writes the md5 Hash to the file
    f.close() # Closes the file

# New Trip Functions (newTrip module)
def saveTrip(tripData):
    """Compile and save the tripData to log"""
    f = open(logfile, 'a+')
    for item in tripData:
        # Compile the list into a string for writing
        f.write(item)
        f.write("{><}")
    f.write("\n") # New line to differentiate between lines when reading
    f.close()

def saveTotals(tripTotals):
    """Add totals together and write to file"""
    if os.path.exists(totalfile) == False:
        # Create the file since it doesn't exist yet
        f = open(totalfile, 'w')
        totals = str(tripTotals[0]) + "{><}" + str(tripTotals[1]) # Convert to strings for concatenating
        f.write(totals)
        f.close() # Close to be sure
    else:
        # If the file exists, add the totals instead of overwriting
        f = open(totalfile, 'r')
        oldTotals = f.read().split("{><}") # Get the old totals
        f.close()
        totalHours = round(float(tripTotals[0]),2) + round(float(oldTotals[0]),2) # New Total Hours
        totalKMs = int(tripTotals[1]) + int(oldTotals[1]) # New Total KMs
        totals = str(totalHours) + "{><}" + str(totalKMs) # Convert to strings for concatenating
        f = open(totalfile, 'w') # Open in write this time to overwrite previous value
        f.write(totals)
        f.close()

# Logbook Reading Functions (viewLog module)
def viewTrip(page):
    number = page
    f = open(logfile, 'r')
    for i in range(0,int(number)):
        # Load the data set that corresponds to the page number
        writtendata = f.readline().split("{><}")
    return writtendata
    f.close()

def getTotals():
    f = open(totalfile, 'r')
    filedata = f.read().split("{><}")
    f.close()
    return filedata
    
