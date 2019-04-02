#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

"""
Created on Wed Mar 13 20:23:15 2019

 Kaleb Noble
 Date
 Python 1 - DAT-119 - Spring 2019
 Project Week #8
     This program creates a to-do list that allows users to view both unfinished
     and finished tasks in a list, then allows them to mark an item as completed.
     
     My teammates were Milo and Orion.
     
     NOTES:
         - The technique used under #4 was adapted from your notes. I set
         it so that the input would become equal to the task, minus 1 place,
         removing the need to type out the whole item that was completed.
         
         - I can fix function #2's loop once we learn exception throwing. I 
         honestly feel like that would be the easiest way to do this.  Either 
         that or an if-elif-if loop.
         
         - I'd honestly like to add in an option that would call up the menu
         if the user requested it. I ran out of time, however.
    

@author: katnob8
"""

#This function marks an item as complete.
def complete_an_item(to_do_list, item_completed, done_list):
    to_do_list.remove(item_completed)   #removes item from the to do list.
    done_list.append(item_completed)    #moves item to the done list.
    print("Okay! I've marked that item complete.")
    
'''   
UNUSED CODE - loop to allow user to continue marking items as done.====
    
    #finished = input("Are you finished (type 'y' when done)? ")

    #while finished == "n":
        #task = int(input("What other item did you get done? "))
        #item_completed = to_do_list[task - 1]
        #to_do_list.remove(item_completed)
        #done_list.append(item_completed)
        #print(to_do_list, done_list)
        #finished = input("Are you finished (type 'y' when done)? ")
        
    #if unfinished != "y" or unfinished != "n":
        #print("Please enter 'y' to continue or 'n' to go to the main menu.")
        #print()
        #task = int(input("What other item did you get done? "))
        #item_completed = to_do_list[task -1]
        #to_do_list.remove(item_completed)
        #done_list.append(item_completed)
        #print(to_do_list, done_list)
        #finished = input("Do you have anything else you got done? ")
'''
  
    return to_do_list

#function to add a task that needs to be completed to the to-do list.
def add_to_unfinished(to_do_list, task_to_add):
    
    #adds the task to the list, then asks if the user wants to add more
    #items.
    to_do_list.append(task_to_add)  
    unfinished = input("Do you want to add something else (type y to continue or any other button to stop)? ")
     
    #While the user types "y", continue adding items to the list. When any
    #other value is entered, the function returns to main.
    while unfinished == "y":
        task_to_add = input("What would you like to add to the list? ")
        to_do_list.append(task_to_add)
        unfinished = input("Do you want to add something else (type y to continue or any other button to stop)")
    
    return to_do_list

#function to allow the user to view finished items.
def view_finished_items(done_list):
    #iterates through the done_list and prints out each item on it in correct
    #format.
    index = 0
    for item in done_list:
        print(index + 1, ") ", item, end="\n")
        index += 1
        
    return done_list

#function to allow the user to view unfinished items.
def view_unfinished_items(to_do_list):
    #iterates through the to_do_list and prints out each item on it
    #in correct format.
    index = 0
    for item in to_do_list:
        print(index + 1, ") ", item, end="\n")
        index += 1
    
    return to_do_list

#main function
def main():
    #initialize the index and the various lists lists.
    index = 0
    to_do_list = []
    done_list = []
    
    #Welcome the user, list the options, and invite them to select one:
    print("Welcome to the To-Do List Application 1.0!")
    print()
    print("Please pick from the following options:")
    print()
    print("1) View unfinished items on the to-do list.")
    print("2) View finished items on the completed list.")
    print("3) Add an item to the to-do list.")
    print("4) Mark a to-do list item as complete.")
    print("5) Exit the application (WARNING: List will not be saved!).")
    print()
    
    selection = int(input("Selection: "))   #menu option user selects.
    
    #While loop to keep the program going while values 1-5 are entered into
    #selection.
    while selection != 5:
        if selection == 1:      #Allows user to view the to-do list items.
            print("Here's what you still need to do: ")
            view_unfinished_items(to_do_list)
            selection = int(input("What would you like to do now?: "))
        
        elif selection == 2:    #Allows user to view items completed so far.
            print("Here's what you've done so far: ")
            view_finished_items(done_list)
            print()
            selection = int(input("What would you like to do now?: "))
        
        elif selection == 3: #Allows user to add an item to the to-do list.
            task_to_add = input("What task should we add to the list? ")
            add_to_unfinished(to_do_list, task_to_add)
            #print(to_do_list)
            selection = int(input("What would you like to do now?: "))
            
        elif selection == 4:    #allows a user to note that an item's completed.
            task = int(input("What item did you get done? "))
            item_completed = to_do_list[task - 1]
            complete_an_item(to_do_list, item_completed, done_list)
            print()
            selection = int(input("What would you like to do now?: "))
            
        else:   #input validation
            print("Sorry, that's not an option. Try again!")
    
    #Exits the application.
    print("Thank you for using the ToDo List App!")
            

#print("Thank you for using the ToDo List Application)
        

    
#incantation to prevent main from running in imports
if __name__ == "__main__":
    main()
