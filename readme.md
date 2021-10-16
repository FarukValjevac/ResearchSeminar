# Research Seminar HW3

**Date**: 16.10.2021

## Important: Because you are using your personal credientials it is recommended to save you E-Mail password to the OS using the keyring library previosly installed from your requirements. 
Make sure your xlsx file is closed while saving with python, otherwise your will face an error. 

### Usage of keyring: 
- Open your python intepreter in the console and type these two steps:

<< import keyring

<< keyring.set_password("any_key_name", "your_mail", "your_password") -> I would not recommend to do this in a script, because in the script your password will be visible if someone has it - instead do it only in the console of your python intepreter.

The first parameter ot the set_password methos is the key, second is your mail, and third is your password

- Your password will be saved to the OS and can be retrieved with the following command (as in the example - config.py):

<< keyring.get_password("any_key_name", "your_mail")

The method get_password returns your password which is stored in the OS by putting the key and the mail. In order to get the right password the key and mail must match the key and mail in the set_password method. 

## Usage:

- Close the repo from github to your computer by pressing the download button or with the git-clone command followed by the link in github.
- Create a virtual environment by typing python -m venv env to your console (optional).
- In order to install all the required libraries to your python interpreter type "pip install -r /path/to/requirements.txt" in the console.
- Setup your config.py file by writing the query, num_page, sender, password with the keyring.get_password method.
- Run the main


Video of working example: https://www.loom.com/share/5af8eb7b53e8484ba6a4a3117de1983e



