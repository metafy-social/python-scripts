import os
def mkFolder(direc):
    try:
        if not os.path.exists(direc):
            os.makedirs(direc)
    except OSError:
        print ('Unable to create ' +  direc)

        
        
mkFolder('./linux/')
