# This is a basic script for Syncing the entire Android Open Source Project for building.
import os
import sys
print ("============================================================")
print ("      Welcome to Android Open Source Project Sync Script    ")
print ("============================================================")
n=input("Press Y/y to Continue, N/n to Exit: ")
if (n=="Y") or (n=="y") :
    print("Starting Sync")
    print("Warning: Repo is needed to be installed in prior of running this script")
    # Change the branch to sync as per your choice, By default it is at Android 13 Sept r6 revision.
    os.system('repo init -u https://android.googlesource.com/platform/manifest.git -b android-13.0.0_r6')
    print ("Starting Repo Sync")
    os.system('repo sync -c --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j8')
else :
    print("Re run script to start sync incase you mistakenly pressed 'N' ")
