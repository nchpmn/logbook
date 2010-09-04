# Checking the user's password against the stored value

import hashlib
import os
import fileHandling

passfile = "pass.txt"

def getHash(textToHash=None):
    """Get the MD5 Hash of a String"""
    return hashlib.md5(textToHash).hexdigest()

def checker():
    """Check the given value against a stored value"""
    if os.path.exists(passfile):
        # The file already exists - the program has been run before
        passFileHash = fileHandling.getPass()

        passCheck = 0
        while passCheck == 0:
            print "You'll need to know the password to continue."
            userPass = raw_input("Password: ")
            userPassSafe = userPass + "a" # Adds a letter to combat hacks
            userHash = getHash(userPassSafe) # Turn the user's password into a md5
        
            if passFileHash == userHash:
                # The user continues to the rest of the program
                print "You know the password!"
                passCheck = 1
            else:
                print "Please try again."

    else:
        # If the file is empty i.e. it was just created
        print "You are going to need to set a password."
        userPass = raw_input("New Password: ")
        userPassSafe = userPass + "a"

        # Turn the user's password into a md5
        userHash = getHash(userPassSafe)

        # Save the password Hash to file using module
        fileHandling.savePass(userHash)
