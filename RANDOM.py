import os,sys
try:
    os.system("git pull")
    __import__('RANDOM').clon_email()
except:
    sys.exit()
