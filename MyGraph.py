import matplotlib.pyplot as plt
import numpy as np

# Python's interpreter goes line by line
# Modulenotfound error
# Python is an open source language, at the mercy of the developers
# You have these libraries that are pre-configured that have all this code that you don't have to know it all
# If you install too many libraries, some start competing for resources and take up more than they need
# KEEP ROOT INSTALL CLEAN, ONLY INSTALL LIBRARIES PER PROJECT
# Gets a copy of your root Python interpreter and uses those libraries you need, virtual environments

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

# Step 1: Create a virtual environment (different for PCs and Macs)
#       PC: py -3 -m venv nameofVE(myvenv)
#       MAC: python3-m venv nameofVE(myvenv)
#       Keep in mind that if you install libraries on VEs, will not work if you switch back to root
# Step 2: Activate your Virtual Environment
#       PC: .\myvenv\Scripts\activate (press tab to autofill the root directory)
#       MAC: source myvenv/bin/activate
# Step 3: Install 3rd party library
#       Same for PC and MAC: pip3 install (name of library) matplotlib
#       numpy is one of the dependencies that gets installed along with matplotlib

# To switch back to the root environment, click on the bottom right next to Python and switch to global

print("Hello there!")