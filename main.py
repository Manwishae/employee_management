'''This is the main python file that will run the system '''

#importing modules
import os, sys
from engine import system

#defining functions
def instruct():
    
    '''This function instructs the user about what to do '''

    print(f"{'_'*10} Employee management System {'_'*10}")
    print(f"\n\n{'_'*10} Use the following keys {'_'*10}\n\n I - for instructions \n N - to add new employee \n B - to remove employee \n C - delete all employees \n T - to show all employees \n E - to exit \n\n")

def startApplication():

    ''' This function starts the application '''

    arguments = sys.argv
    try:
        if arguments[1] == 'start' or arguments[1] =='run':
            system.window()
    
    except Exception as e:
        print("Error Occured")

startApplication()