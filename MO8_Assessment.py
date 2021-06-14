# Lennisha wanted to make this look as real and pleasing to the eye, aside from putting this into html format




## Function to add participants
## Places names in proper appearance First Name Last Name
## Requests a name and number for the participant in the touranment
## Checks if (key, value == None) exists in the dictionaary items
#### TRUE ===================> Updates the value to Participant's name
#### FALSE ==================> Tells the user that the slot is taken
#### ELSE ===================> N/A
def AddParticipant(ParticipantName):
    ParticipantName.title()
    ParticipantNum = input(f'Choose a number for the participant: ')
    ParticipantNum = int(ParticipantNum)
    if (ParticipantNum, None) in ParticipantDictionary.items():
        ParticipantDictionary.update({ParticipantNum:ParticipantName})
        print(f'The participant was added to the roster. \n')
    elif (ParticipantNum, None) not in ParticipantDictionary.items():
        print('This spot has already been filled, please select a different slot. \n')
    else:
        print('This information does not yield any helpful information. \n')


## Function allows the user the ability to reuse AddParticipant function
## Closes sign up after iterating
def AddMore(ParticipantDictionary):
    a = 1
    while a <= len(ParticipantDictionary):
        More = input('Would you like to add another contestant? [y/n] ')
        if More == 'y':           
            AddParticipant(input(f'Please enter the participant\'s name: '))
            a = a + 1
        else:
            print(f'\n Sign up is now closing.')
            break


## Function to remove participants
## Requests a name and number for the participant in the touranment
## Rejects request if the provided information doesn't match a single dictinary item
## Checks if (key, value == Name) exists in the dictionaary items
#### TRUE ===================> Updates the value to None
#### FALSE ==================> Tells the user that the information provided is incorrect
#### ELSE ===================> N/A
def RemoveParticipant(ParticipantName):
    ParticipantName.title()
    ParticipantNum = input(f'Choose a number for the participant: ')
    ParticipantNum = int(ParticipantNum)
    if (ParticipantNum, ParticipantName) in ParticipantDictionary.items():
        ParticipantDictionary.update({ParticipantNum:None})
        print(f'The participant was removed from the roster. \n')
    elif (ParticipantNum, ParticipantName) not in ParticipantDictionary.items():
        print(f'{ParticipantName} is not in slot {ParticipantNum} \n')
    else:
        print('This information does not yield any helpful information. \n')


## Function allows the user the ability to reuse RemoveParticipant function
## Closes cancelation after iterating
def RemoveMore(ParticipantDictionary):
    b = 1
    while b <= len(ParticipantDictionary):
        Less = input('Would you like to remove another contestant? [y/n] ')
        if Less == 'y':           
            RemoveParticipant(input(f'Please enter the participant\'s name: '))
            b = b + 1
        else:
            print(f'\n Cancelation is now closing.')
            break


# View Participant
## Removes all Participants with a None value
## Returns result in an easy to digest way
def ViewParticipant(ParticipantDictionary):
    for key, value in dict(ParticipantDictionary).items():
        if value is None:
            removedItem = ParticipantDictionary.pop(key)
            ClearParticipantDictionary = dict(ParticipantDictionary.copy())
    for k, v in list(ClearParticipantDictionary.items()):
        print(f'{k}:  {v}')


# Main Menu
## Function that allows interaction with the homepage and brings the user back to the page when done
## Sign Up -- 1. Brings up the sign up page
## Cancel --- 2. Brings up canceling page
## View ----- 3. Brings up viewing page
## Exit ----- 4. Brings up exit page
##### Warns user as to consequences of exiting
##### Ends coding sequence
def MainMenuUsage(MainMenu):
    if int(MainMenu) == 1:
        print('Sign Up'.center(50,' '))
        print(' ')
        print('Sign up participants on this page')
        FollowThru = input('Would you like to sign up a participant? [y/n]: ')
        if FollowThru == 'y':    
            AddParticipant(input(f'Please enter the participant\'s name: '))
            AddMore(ParticipantDictionary)
        else:
            print(f'\n Sign up is now closing.')
        print('\n How Can We Help You Today? \n \n 1. Sign Up \n 2. Cancel Sign Up \n 3. View Participants \n 4. Exit')
        MainMenu = input('\n Which option would you like to interact with today? ')
        print(' ')
        MainMenuUsage(MainMenu)


    if int(MainMenu) == 2:
        print('Cancelation'.center(50,' '))
        print(' ')
        print('Cancel participant entry on this page')
        FollowThru = input('Would you like to remove a participant? [y/n]: ')
        if FollowThru == 'y':    
            RemoveParticipant(input(f'Please enter the participant\'s name: '))
            RemoveMore(ParticipantDictionary)
        else:
            print(f'\n Cancelation is now closing.')
        print('\n How Can We Help You Today? \n \n 1. Sign Up \n 2. Cancel Sign Up \n 3. View Participants \n 4. Exit')
        MainMenu = input('\n Which option would you like to interact with today? ')
        print(' ')
        MainMenuUsage(MainMenu)


    if int(MainMenu) == 3:
        print('View Participants'.center(50,' '))
        print(' ')
        print('View participants on this page. \n The participants are:')
        ViewParticipant(ParticipantDictionary)
        print(f'\n Viewing is now closing.')
        print('\n How Can We Help You Today? \n \n 1. Sign Up \n 2. Cancel Sign Up \n 3. View Participants \n 4. Exit')
        MainMenu = input('\n Which option would you like to interact with today? ')
        print(' ')
        MainMenuUsage(MainMenu)


    elif int(MainMenu) == 4:
        print('Exit'.center(50,' '))
        print(' ')
        print('Proceeding with this page causes all of your hard work to disappear.')
        Exit = input('Are you certain you\'d like to exit? [y/n] ')
        if Exit == 'y':
            ParticipantDictionary.clear()
            print('Perfect. Have a great day!')
        else:
            print('Okay! Let\'s head back to the main menu and keep working.') 
            print('\n How Can We Help You Today? \n \n 1. Sign Up \n 2. Cancel Sign Up \n 3. View Participants \n 4. Exit')
            MainMenu = input('\n Which option would you like to interact with today? ')
            print(' ')


# Prints a line when user does not enter a menu option
    else:
        print('Oh goodness, I\'m sorry that isn\'t an option this time. Please try again.')











































# Start Up
## Prints a title and asks for a number of participants
## Starts the remainder of the program
print('Ding Ding Ding, It\'s Tournament Time!! \n')
NumberOfChallengers = input('How many participants are we talking? ')
if NumberOfChallengers.isdigit() == 1:
    NumberOfChallengers = int(NumberOfChallengers)
## Creates a dictionary based on how many contestants the user inputs
    ParticipantDictionary = {}
    x = 1
    while x <= NumberOfChallengers:
        ParticipantDictionary[x] = None
        x = x + 1
    
    print(f'Alright, we\'ve set up {NumberOfChallengers} challenger spots!')
    
# Main Menu
    print('\n How Can We Help You Today? \n \n 1. Sign Up \n 2. Cancel Sign Up \n 3. View Participants \n 4. Exit')
    MainMenu = input('\n Which option would you like to interact with today? ')
    print(' ')

    MainMenuUsage(MainMenu)
else:
    print('A number might be a bit better here.')
#------------------------------------ -----------STRETCH GOAL--------------------------------------------------------
#look for 1 participant, return position
## I'd like this to work the way it does in real life:
#### When searching, a particial look/ typing in a series of letters in a particular order should bring about a list of persons that share that letter order
## This will involve a spliting of strings to allow an easy search.
## Do keep in mind that this search may be for 1 letter or it may be several or the entire name.
## The only new territory here is the using of several characters to "Guess" the name


#alphabatize by last name
## As I've handeld the other problems before this, split and concequer
## I will set this function to search for ' ' to find where the last name begins
## After finding that we can split just the first letter, find what it is, (and make the same size in case capital > lower case)
## we create a match up of [0] from one name to compare it to a [0] of another name.
## this must be continued until all letters (i in name) are matched and ordered accodingly
##### to take this a step further, we can also match up the letters in the first name, if it comes down to it


#submit assessment as git link
## cd Code/DBC_Tournament_Tracker
# Save in folder
## git add .
## git commit -m MO8_Assessment.py
## git push


#save and load multiple tournaments
##This is a special task
#### Using the functions done above, make a list of multipe tounaments
#### Such that, when the user starts, they must select a tournament from the very first line
#### Once that is established, all other functions go to work, making names, matching spots, etc
#### Upon entering something like done, the user should be prompted to pick a different touranment
#### If one is not selected, a goodbye message must appeat.
#### If one is selected, let the functions run again
#### print the correct name for touranment