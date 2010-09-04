#!/usr/bin/python
# Logbook Program
# For changelog, see "CHANGELOG.txt" in this directory
# Nathan Chapman

import time
import passCheck # This is the passCheck.py 'module'
import newTrip # The newTrip.py 'module'
import viewLog # Again, the viewLog.py 'module'

logfile = "log.txt"
firstTime = True


def main(firstTime):
    """CHANGELOG LOCATED IN \'CHANGELOG.TXT\'"""

    if firstTime == True: # If we've just opened the program, check password
        print "Welcome!"
        # Check the password from the passCheck.py module on open
        passCheck.checker()
        firstTime = False

    choice = "N"

    while choice.lower() != "q":
        

        print \
              """
\n\n\n
                          +------------------------+
--------------------------| LEARNER DRIVER LOGBOOK |----------------------------
                          +------------------------+
\n\n
\t\t+--------------------------+
\t\t|        MAIN MENU         |
\t\t|                          |
\t\t|  1 - New Trip            |
\t\t|  2 - View Logbook        |
\t\t|  3 - Get Totals          |
\t\t|  Q - Quit                |
\t\t+--------------------------+
"""
        choice = raw_input("\n\t\tChoice: ")

        if choice == "1":
            # Enter the data using the newTrip module
            newTrip.data()
            main(firstTime)
        elif choice == "2":
            viewLog.tripViewer()
            main(firstTime)
        elif choice == "3":
            viewLog.totals()
        elif choice.upper() == "Q":
            pass
        else:
            print "\n\t\tERROR: Please use 1-3 or Q.\n"
            time.sleep(1.75)
            main(firstTime)

main(firstTime)

raw_input("Main Exit.")
