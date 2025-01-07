# all things that need to happen to cleanup
import os
import shutil

def cleanup(): 
    if os.path.exists("build"):
        shutil.rmtree("build")
    
        if os.path.exists("build"):
            raise Exception("Failed to delete previously generated images")
        else: 
            print("Successfully deleted previous generated images")
    else:
        print("No cleanup necessary")