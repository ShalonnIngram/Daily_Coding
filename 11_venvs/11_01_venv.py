'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.

'''
# completed in the command line

# name of virtual environment : myvenv
# install files
pandas
numpy
matplotlib

# requirements file
cycler==0.10.0
kiwisolver==1.3.1
matplotlib==3.4.2
numpy==1.20.3
pandas==1.2.4
Pillow==8.2.0
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2021.1
six==1.16.0

# deactivate
deactivate

# remove directory
rm -rf virtualenv