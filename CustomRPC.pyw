"""
Dev by: Voidzy#0283
GitHub: https://github.com/zVoidzy
Language: Python 3.9.5
"""

# Importing libraries and setttings and verifying if pypresence is installed
import os
current_path = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(current_path+"/"+'errors.txt'):
    os.remove(current_path+"/"+'errors.txt')
    
try:
    from pypresence import Presence
except(ImportError):
    file = open(current_path+"/"+'errors.txt', 'w')

    file.write("ERROR: \n")
    file.write("Pypresence not found! \nTry installing it by typing 'pip install pypresence' on your terminal!\n")
    file.write("Also make sure the correct Python interpeter is selected.\n")
    exit()

from settings import applicationID, details, state, large_image, large_image_text
from time import sleep

# Logging on your application to start RPC
rpc = Presence(applicationID, pipe=0)

# Starting RPC and veryfing if Discord is running
try:
    rpc.connect()
except:
    file = open(current_path+"/"+'errors.txt', 'w')

    file.write("ERROR: \n")
    file.write("Discord Client not detected! \n")
    exit()

# Updating RPC with the info in the settings file
try:
    rpc.update(details=details, state=state, large_image=large_image, large_text=large_image_text)
except:
    file = open(current_path+"/"+'errors.txt', 'w')

    file.write("ERROR: \n")
    file.write("Some informations in the settings.py file are incorrect!")
    exit()

# Keep alive
while True:
    sleep(9999)