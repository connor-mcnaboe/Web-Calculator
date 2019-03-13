# Created: 03/12/19
# Author: Connor McNaboe    
# Purpose: Script which installs required packages to run WebCalculator and sets up virtual enviroment 


## Before running this script, ensure that you have changed your directory to  WebCalc/ ##

import os
import sys

#-Create virtual enviroment-#
os.system("python3 -m venv wcvenc")
if "win" in sys.platform(): 
    os.system('wcvenv\\Scripts\\activate')
else: 
    os.system("source wcvenv/bin/activate")

#-Install packages-#
os.system("pip install --upgrade pip") # Upgrade pip
os.system("pip install flask")
os.system("pip install flask-wtf")