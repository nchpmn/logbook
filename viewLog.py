# Retrieve and display each trip in the log, and the total hours and kilometres

import fileHandling
import os
import time

logfile = "log.txt"
totalfile = "totals.txt"

def tripViewer():
    """Check that the logbook exists before viewing a trip"""
    if os.path.exists(logfile) == False:
        # The log doesn't exist
        print "\n\nERROR: The logfile does not exist.\nviewLog module, in viewer()"
        time.sleep(1.75)
    else:
        # The logfile does exist
        log()
    
def log():
    """Display a single trip from the logbook"""
    print \
          """
\n\n\n\n\n\n
                           +----------------------+
---------------------------|    LOGBOOK VIEWER    |-----------------------------
                           +----------------------+
\n\n
"""
    home = 1
    page = 1
    print "\n\n\t\t\t\t-------- PAGE", page, "--------\n"
    trip = fileHandling.viewTrip(page) # Send the file off to external module
    # Here's the data! Whoo!
    print "\t\tDate:", trip[0], "\t\tVeichle:", trip[1]
    print "\t\tOdometer Start:", trip[2], "\tOdometer End:", trip[3]
    print "\t\tFrom:", trip[4], "\tTo:", trip[5], "\n\t\tConditions:", trip[6]
    print "\t\tStart:", trip[7], "\tEnd:", trip[8], "\tTotal:", trip[11]
    print "\t\tSupervisor:", trip[9], "\t\tLicence:", trip[10]
    print "\n\n\n"

    while home == 1:
        choice = raw_input("\t\tNext, Previous or Home? (n/p/h) ")
        # Of course, in the GUI version these will be buttons

        if choice.lower() == "n":
            try:
                # Next entry in the logbook
                page += 1
                trip = fileHandling.viewTrip(page) # Send the file off to external module
                print "\n\n\t\t\t\t-------- PAGE", page, "--------\n"
                # Here's the data! Whoo!
                print "\t\tDate:", trip[0], "\t\tVeichle:", trip[1]
                print "\t\tOdometer Start:", trip[2], "\tOdometer End:", trip[3]
                print "\t\tFrom:", trip[4], "\tTo:", trip[5], "\n\t\tConditions:", trip[6]
                print "\t\tStart:", trip[7], "\tEnd:", trip[8], "\tTotal:", trip[11]
                print "\t\tSupervisor:", trip[9], "\t\tLicence:", trip[10]
                print "\n\n\n"
            except IndexError:
                print "\n\n\t\tERROR: This is the last trip in the logbook. (EOF)"
                time.sleep(1.75)
                page -= 1

        elif choice.lower() == "p":
            page -= 1
            try:
                trip = fileHandling.viewTrip(page) # Send the file off to external module
                print "\n\n\t\t\t\t-------- PAGE", page, "--------\n"
                # Here's the data! Whoo!
                print "\t\tDate:", trip[0], "\t\tVeichle:", trip[1]
                print "\t\tOdometer Start:", trip[2], "\tOdometer End:", trip[3]
                print "\t\tFrom:", trip[4], "\tTo:", trip[5], "\n\t\tConditions:", trip[6]
                print "\t\tStart:", trip[7], "\tEnd:", trip[8], "\tTotal:", trip[11]
                print "\t\tSupervisor:", trip[9], "\t\tLicence:", trip[10]
                print "\n\n\n"
            except IndexError:
                print "\n\n\t\tERROR: This is the first trip in the logbook. (EOF)"
                page += 1
                time.sleep(1.75)

        elif choice.lower() == "h":
            home = 0

        else:
            print "ERROR: Please use N(ext) P(revious) or H(ome)."
            time.sleep(1.75)

def totals():
    """Display the total number of hours and KMs"""

    print \
          """
\n\n\n\n\n\n
                           +----------------------+
---------------------------|    LOGBOOK TOTALS    |-----------------------------
                           +----------------------+
\n\n
"""
    
    if os.path.exists(totalfile) == False:
        # The total doesn't exist
        print "ERROR: The logfile does not exist.\nviewLog module, in viewer()"
        time.sleep(1.75)
    else:
        # The totalfile does exist
        totaldata = fileHandling.getTotals()
        print "\n\n\t\t\t-------- TOTALS --------\n"
        print "\t\t\tTOTAL HOURS:\t", totaldata[0]
        print "\t\t\tTOTAL KMS:\t", totaldata[1]

        raw_input("\n\n\t\tEnter to go Home.")
