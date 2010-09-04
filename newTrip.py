# Get data for new trip and save to file

import time
import fileHandling

def data():
    """Enter and Save a new trip into the logbook!"""
    print \
          """
\n\n\n\n\n\n
                            +--------------------+
----------------------------|    ADD NEW TRIP    |------------------------------
                            +--------------------+
\n\n
"""
    # Unless noted, all are just basic strings to be returned later.
    date = raw_input("\t\tDate (DD/MM/YY): ")
    vehicle = raw_input("\t\tVehicle Plates: ")

    # Odometer
    odoGood = False
    while odoGood == False:
        try:
            # Make sure they're inputting an integer
            odoStart = int(raw_input("\n\t\tOdometer Start: "))
            odoEnd = int(raw_input("\t\tOdometer End: "))
            odoTotal = odoEnd - odoStart # Calculates distance travelled
            if odoStart <= odoEnd and odoTotal > 0: # Validate for other errors
                odoGood = True
            else:
                odoGood = False
                print "\t\nERROR: Invalid number entry.\n"
        except ValueError:
            print "\t\nERROR: Please enter whole numbers only!\n"

    # Trip Details
    tripFrom = raw_input("\n\t\tFrom: ")
    tripTo = raw_input("\t\tTo: ")
    conditions = raw_input("\t\tConditions: ")

    # Time, including calculation in hours.
    timeChecker = False
    while timeChecker == False:
        try:
            timeStart = raw_input("\n\t\tStart Time: ")
            timeEnd = raw_input("\t\tEnd Time: ")
            # Format the strings into useable objects
            timeStartString = "03/09/10 " + timeStart # It needs a full date to work, so this is my birthday!
            timeStartTuple = time.strptime(timeStartString, "%m/%d/%y %I:%M %p")
            timeEndString = "03/09/10 " + timeEnd # Maybe I should change the date so it is the entered date.
            timeEndTuple = time.strptime(timeEndString, "%m/%d/%y %I:%M %p")
            timeDiff = time.mktime(timeEndTuple) - time.mktime(timeStartTuple) # Idea to use mktime from user 'vegaseat'
            timeDiffHours = timeDiff / (60.0*60)
            if timeDiffHours > 0:
                timeChecker = True
            else:
                timeChecker = False
                print "\t\n\n ERROR: The time must be greater than zero."
        except ValueError:
            print "\t\n\nERROR: Please enter the time as \'11:25 AM\' or \'03:10 PM\'\n"

    # Supervisor's details
    supName = raw_input("\n\t\tSupervisor Name: ")
    supLicence = raw_input("\t\tSupervisor Licence: ")

    # Put the values in a list. Calculated values are at the end for easy reference.
    # Objects that are wrapped in str() are like this to be written to file.
    tripData = [date, vehicle, str(odoStart), str(odoEnd), tripFrom, tripTo, conditions,
                timeStart, timeEnd, supName, supLicence, str(round(timeDiffHours,2))]
    tripTotals = [round(timeDiffHours, 2), odoTotal]

    #print tripData, tripTotals # Debug only!

    fileHandling.saveTrip(tripData) # Save the data to log
    fileHandling.saveTotals(tripTotals) # Calculate and save totals

    print "\nTrip has been sucessfully saved!"
