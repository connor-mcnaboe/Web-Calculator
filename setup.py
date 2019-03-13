# Created: 03/12/19
# Author: Connor McNaboe    
# Purpose: Script which installs required packages to run WebCalculator and sets up virtual enviroment 


## Before running this script, ensure that you have changed your directory to  WebCalc/ ##

import os

#-Install packages-#
os.system("pip3 install --upgrade pip") # Upgrade pip
os.system("pip3 install flask")
os.system("pip3 install flask-wtf")