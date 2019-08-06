# The main page for the lottery number and prediction program, Project_3_APIs
# Utilizing the textblob API, and also an import of the inbuilt random function

# 7/11/2019 @ 13:31 I just started the project.  I estimate this project
# of adding three API's to take approximately 9 hours when it's all said and done. I have one TextBlob API implemented
# already (the Common Numbers, pulling random TextBlob words from the lists CommonRedBallNumbers.txt and
# CommonWhiteBallNumbers.txt. I am still choosing my other two API implementation from the TextBlob library
# right now.
# @17:08 I have completed my Spanish translation to the text file Spanish_Random_Choices.txt, utilizing the
# TextBlob library. I am now going to create a separate menu choice for Instructions, in both Spanish and English,
# in its own class so I can call it.  I also need to update all of the menu choices in Spanish.
# @ 21:14 I took approximately two hours break today overall.  So far the project has taken approximately 6 hours.
# At this time my instructions and menus look good.  I had to fix an error that was being caused when there was
# nothing on the text files; the translation to Spanish from the other files to the Spanish_Random_Lotto_Choices.txt
# was having trouble when the other files were blank.  I attempted to use import os(ex: os.remove('example.txt'), but
# this also caused issues. It caused the files to erase completely and interrupted the entire program.
# Instead I have created a appendText to each file, prior to calling the classes/methods.  This ensures that something
# is at least on the file at all times when the classes/methods are called, so that there is not an issue with nothing
# being there to translate. Eventually I'd like to learn how to clear a file, and how to instruct the program on
# when to know a file is blank and stop attempting to translate.  For now, however, the program works.
# Next I am going to attempt utilizing the TextBlob library to pull frequent strings from a file (which in this case
# will be numeric strings), and state how often they are randomly chosen.  I plan to do this from ten White Ball lists
# and ten Red Ball lists, and then to create a menu to call upon it.  It will be printed to the Random_Lotto_Choices.txt
# and then can also be translated into Spanish to the Spanish_Random_Lotto_Choices.txt.
# 7/12/2019 @ 2:34am I am going to call it a night.  I had a little trouble with the TextBlob, but ended up creating
# a Random() class to call upon random numbers.  In order to create many individual sets of random white and red balls,
# I had to create different methods for each call. Otherwise the numbers would repeat as the same sets of numbers over
# and over again.  I created a Frequency() class to call upon it from the Choice's function menu.  I have tested the
# concept and it works.  I am going to complete it tomorrow.
# 12:08pm I am going to begin again today and complete the program.
# 14:44pm I have completed the program and it appears to be working.  I will make the video of its functions and then
# submit. In total the project has taken approximately 13 hours (excluding breaks), so I did underestimate the time
# by about 3 hours. Neat ideas for future goals on my list: 1) Creating a clear page menu 2) Figure out how to make
# the program know when a file is blank and not to pull text from it 3) Creating a GUI 4) Creating predictions
# utilizing AI 5) Make sure Frequent numbers go on Spanish list.
# 7/27/2019 @ 14:57 Throughout this week I have added menus for the SVM_MonthPredictor.py, Scatter.py, and
# Bar.py, utilizing SVM, SCATTER, and BAR as menu choices to do so.
# 8/6/2019 @ 8:23am I added the Pytorch number prediction project on file Torch_Pred.py to the project, and also
# added it under the choice PRED to the main menu.

import random
from textblob import TextBlob

# Creating class for the different Balls (Random White, Random Red, Even White, Even Red, Odd White, Odd Red,
# and Common Winning White, Common Winning Red
class Balls:
    for x in range(1):

        # Creating Random White and Red Balls methods; appending to file Random_Lotto_Choices.txt
        def regWhiteBall(self):
            regWhite = str(random.sample(range(1, 70), 5))
            print("\n" + "----------------------" +"\n" + "Your random White Ball numbers are:" + "\n")
            print(regWhite)

            appendFile = open('Random_Lotto_Choices.txt', 'a')
            appendFile.write("\n" + "----------------------" + "\n" +
                             "Your random White Ball numbers are:" + "\n")
            appendFile.write(regWhite + "\n")
            appendFile.close()

        def regRedBall(self):
            regRed = str(random.sample(range(1,14), 1))
            print("\n" + "Your random Red Ball number is:" + "\n")
            print(regRed)

            appendFile = open('Random_Lotto_Choices.txt', 'a')
            appendFile.write("\n" + "Your random Red Ball number is:" + "\n")
            appendFile.write(regRed)
            appendFile.write("\n" + "----------------------" + "\n")
            appendFile.close()

        # Creating Even White and Red Balls Method, with two Even and three regular Random White, and one Even Red;
        # appending to file Random_Lotto_Choices.txt
        def evenWhiteBall(self):

            numEve = str(random.randint(1, 35) * 2)
            numEve2 = str(random.randint(1, 35) * 2)

            numReg = str(random.sample(range(1, 70), 3))

            if numEve != numEve2 and numEve2 != numReg:
                print("\n" + "----------------------" + "\n" +
                      "Your two even and three random White Ball numbers are:" + "\n")
                print(numEve + ", " + numEve2 + " and " + numReg)

                appendFile = open('Random_Lotto_Choices.txt', 'a')
                appendFile.write("\n" + "----------------------" + "\n" +
                      "Your two even and three random White Ball numbers are:" + "\n")
                appendFile.write(numEve + ", " + numEve2 + " and " + numReg + "\n")
                appendFile.close()

            else:
                print("***There were repeat numbers during this try, please try again.***")
                Choice()

        def evenRedBall(self):
            numEveRed = str(random.randint(1, 14) * 2)

            print("\n" + "Your even Red Ball is:" + "\n")
            print(numEveRed)

            appendFile = open('Random_Lotto_Choices.txt', 'a')
            appendFile.write("\n" + "Your even Red Ball is:" + "\n")
            appendFile.write(numEveRed)
            appendFile.write("\n" + "----------------------" + "\n")
            appendFile.close()

        # Creating Odd White and Red Balls Method, with two Odd and three regular Random White, and one Odd Red;
        # appending to file Random_Lotto_Choices.txt

        def oddWhiteBall(self):

            number_Odd = str(random.randint(1, 35) * 2 +1)
            number_Odd2 = str(random.randint(1, 35) * 2 +1)

            numReg = str(random.sample(range(1, 70), 3))

            if number_Odd != number_Odd2 and number_Odd2 != numReg:
                print("\n" + "Your two odd and three random White Ball numbers are:" + "\n")
                print(number_Odd + ", " + number_Odd2 + " and " + numReg)

                appendFile = open('Random_Lotto_Choices.txt', 'a')
                appendFile.write("\n" + "----------------------" + "\n" +
                                 "Your two odd and three random White Ball numbers are:" + "\n")
                appendFile.write(number_Odd + ", " + number_Odd2 + " and " + numReg + "\n")
                appendFile.close()

            else:
                print("***There were repeat numbers during this try, please try again.***")
                Choice()

        def oddRedBall(self):

            numOddRed = str(random.randint(1, 13) * 2 + 1)

            print("\n" + "Your odd Red Ball is:" + "\n")
            print(numOddRed)

            appendFile = open('Random_Lotto_Choices.txt', 'a')
            appendFile.write("\n" + "Your odd Red Ball is:" + "\n")
            appendFile.write(numOddRed)
            appendFile.write("\n" + "----------------------" + "\n")
            appendFile.close()

        # Creating Common Winning White and Red Balls Method, with two Common Winning and three regular Random White,
        # and one Common Winning Red; appending to file Random_Lotto_Choices.txt.  The Common Winning numbers use TextBlob
        # to pull from two files CommWhiteBallNumbers.txt and CommonRedBallNumbers.txt

        def commonWhiteBall(self):

            print("\n" + "----------------------" + "\n" +
                  "Your two common winning White Balls and three random White Balls are:" + "\n")
            appendFile = open('Random_Lotto_Choices.txt', 'a')
            appendFile.write("\n" + "----------------------" + "\n" +
                  "Your two common winning White Balls and three random White Balls are:" + "\n")
            text = open("CommonWhiteBallNumbers.txt")
            text = text.read()
            blob = TextBlob(text)
            wordlist = blob.words
            wordlist = list(wordlist)
            for word in random.sample(wordlist, 2):
                float(word.singularize())
                comWhiteB = str.split(word)
                print(comWhiteB)
                appendFile = open('Random_Lotto_Choices.txt', 'a')
                appendFile.write(str(comWhiteB))
            randWhiteBall = str(random.sample(range(1, 70), 3))
            print(randWhiteBall)
            appendFile = open('Random_Lotto_Choices.txt', 'a')
            appendFile.write(randWhiteBall + "\n")
            appendFile.close()

        def commonRedBall(self):
            text = open("CommonRedBallNumbers.txt")
            text = text.read()
            blob = TextBlob(text)
            wordList = blob.words
            wordList = list(wordList)
            for word in random.sample(wordList, 1):
                float(word.singularize())

                comRedB = word

                print("\n" + "Your common winning Red Ball number is:" + "\n" + "\n" + comRedB)

                appendFile = open('Random_Lotto_Choices.txt', 'a')
                appendFile.write(("\n" + "Your common winning Red Ball number is:" +
                                  "\n" + comRedB))
                appendFile.write("\n" + "----------------------" + "\n")
                appendFile.close()

Balls()

# Creating a Definitions class to hold lottery group contact information
class Definitions():

    def lotteryContacts(self):
        # Creating a variable to call methods from the MainMenu() class
        returnMenu = MainMenu()

        # Creating an input string to ask the customer which AZ lotto contact they would prefer to view
        question = str(input("Please type the corresponding number associated with the Arizona lottery " +
                             "office location you are looking for / Escriba el número correspondiente asociado " +
                             "con la ubicación de la oficina de lotería de Arizona que está buscando:" +
                             "\n" + "\n" + "1 - Phoenix" + "\n" +
                             "2 - Tucson" + "\n" + "3 - Phoenix Sky Harbor (Lottery office / Oficina de loteria)" +
                             "\n" + "4 - Winning Numbers Hotline / Línea directa de números ganadores" + "\n" + "\n" +
                             "MAIN - to return to the Main Menu / Para volver al menu principal" +
                             "\n" + "\n" + "Please type your answer here / Por favor escriba su respuesta aquí: "))

        # Definitions with key and values of the lotto contacts

        contactsAZ = {'Arizona Lottery Phoenix office': '480-921-4400',
                      'Arizona Lottery Tucson office': '520-628-5107',
                      'Phoenix Sky Harbor (Lottery office)': '480-921-4424',
                      'Winning Numbers Hotline': '1-800-499-3798'}
        print(question)

        if question == "1":
            print(str(("\n" + "Arizona Lottery Phoenix office: " + contactsAZ['Arizona Lottery Phoenix office'] +
                       "\n")))
            returnMenu.menuContacts()


        if question == "2":
            print(str(("Arizona Lottery Tucson office: " + contactsAZ['Arizona Lottery Tucson office'])))
            returnMenu.menuContacts()

        if question == "3":
            print(str(("Phoenix Sky Harbor (Lottery office): " + contactsAZ['Phoenix Sky Harbor (Lottery office)'])))
            returnMenu.menuContacts()

        if question == "4":
            print(str(("Winning Numbers Hotline: " + contactsAZ['Winning Numbers Hotline'])))
            returnMenu.menuContacts()

        if question == "MAIN":
            returnMenu.main()

        else:
            print("Incorrect entry. Please try again.")
            returnMenu.main()
Definitions()

# Setting up MainMenu class with menu for user to choose input to play again (GO) or exit program (QUIT)
class MainMenu():

    # Creating menu method with user input for non-contacts pages
    def main(self):

        lottoContacts = Definitions()
        mainM = MainMenu()

        chooseRunQuit = str(input("\n" + "Please choose / Por favor elija: " + "\n" + "\n" + "GO - to return to the " +
                                  "Powerball Success Number Generator / Para volver al generador de números de éxito " +
                                  "de Powerball" + "\n" +
                                  "CONT - to open the Arizona Powerball contacts page / Para volver al menú de " +
                                  "contactos de Powerball de Arizona " +
                                  "\n" + "QUIT - to exit the program / Para salir del programa" + "\n" + "\n" +
                                  "Please enter your choice here / Por favor ingrese su elección aquí: "))

        if chooseRunQuit == "GO":
            Choice()

        if chooseRunQuit == "CONT":
            lottoContacts.lotteryContacts()


        if chooseRunQuit == "QUIT":
            exit()

        else:
            print("Incorrect entry. Please try again. / Entrada incorrecta. Inténtalo de nuevo.")
            mainM.main()

    # Creating menu method with user input for the Contacts pages (gives customer the choice to return to the
    # Contacts page first, rather than the first choice being for the main menu)
    def menuContacts(self):

        lottoContacts = Definitions()
        mainM = MainMenu()

        chooseRunQuit = str(input("\n" + "Please choose / Por favor elija:" + "\n" + "\n" + "CONT - to return to the " +
                                  "Arizona Powerball Contacts menu / Para volver al menú de contactos de Powerball " +
                                  "de Arizona" + "\n" + "GO - to return to the " +
                                  "Powerball Success Number Generator / Para volver al generador de números de éxito " +
                                  "de Powerball" + "\n" +
                                  "QUIT - to exit the program / Para salir del programa" + "\n" + "\n" +
                                  "Please enter your choice here / Por favor ingrese su elección aquí: "))

        if chooseRunQuit == "CONT":
             lottoContacts.lotteryContacts()

        if chooseRunQuit == "GO":
            Choice()

        if chooseRunQuit == "QUIT":
            exit()

        else:
            print("Incorrect entry. Please try again. / Entrada incorrecta. Inténtalo de nuevo..")
            mainM.main()

MainMenu()

# Creating an instructions class because it takes up so much room at the beginning of the program.  I will add it as
# a menu choice instead
class Instructions():

    # English instructions
    def engInstructions(self):

        mainM = MainMenu()
        engInstruct = str("\n" + "\n" + "Welcome to the Powerball Success Number Generator! " + "\n" + "\n" +
                           "I will explain how this program works. As is common knowledge, lottery success often " +
                           "relies on statistics. Those who study these statistics, and " + "\n" + "those who win, " +
                           "often suggest that asking the store clerk to have the Powerball system generate numbers " +
                           "for you is often a bad idea, as these numbers " + "\n" + "don't align statistically with " +
                           "the probability of winning." + "\n" + "\n" +
                           "In comes this program to the rescue.  You will be given the ability to choose between " +
                           "four different number-picking choices, which are designed to support winning a little" +
                           "\n" + "better than the automated Powerball numbers sold to players in-store. " + "\n" +
                           "\n" + "For the choice RA, you will be given five random White Ball numbers between " +
                           "1 and 69, and one Red Ball number between 1 and 26." + "\n" + "Choosing Evens or " +
                           "Odds will not be differentiated within this choice." + "\n" + "\n" +
                           "The next option, EV, will show you three Even White Ball numbers and two Odd White Ball numbers. " +
                           "The Red Ball will be an Even number. " + "According to my research, " + "\n" +
                           "an Even/Odd combination is more likely to win. However, having more Even numbers than Odd is supposed " +
                           "to further increase those chances of success." + "\n" + "\n" +
                           "We all know that fate can sometimes play an odd hand (pun intended).  So our tertiary choice " +
                           "is OD, which will show more Odd numbers than Even numbers, " + "\n" + "including the Red Ball (which will " +
                           "be Odd in this case)." + "\n" + "\n" +
                           "CO can be chosen so that you will see a list of numbers " +
                           "which include two random common winning White Ball numbers, and a common winning Red Ball number." +
                           "\n" + "\n" +
                           "You can type FREQ to print sets of lottery numbers and view their frequent number count." +
                           "\n" + "\n" +
                           "ESP will ensure your numbers are printed in Spanish." + "Other menus available include " +
                           " the following:" + "\n" + "\n" +
                           "1 - for Instructions in English" + "\n" +
                           "2 - para instrucciones en español" +
                           "\n" + "\n" +
                           "SVM - to try the SVM and KNN algorithm to " +
                           "predict the month numbers will be chosen" + "\n" +
                           "SCATTER - for PowerBall Scatter Plot charts and associated data" + "\n" +
                           "BAR - for PowerBall Bar charts and associated data" + "\n" +
                           "PRED - to enter two White Ball numbers and predict the last three in the set\n\n" +
                           "MN - to go to the Main Menu / Para ir al menu principal"  "\n" + "\n" +
                           "               *** Please note that if you wish to receive different numbers for any of " +
                           "the offered choices, you must restart the game ***" + "\n" + "\n" +
                           "I'm excited you are utilizing this program " + "to increase your lotto-winning " +
                           "chances.  " + "Good Luck!" + "\n" + "\n")

        print(engInstruct)
        mainM.main()

    # Spanish instructions
    def spanInstructions(self):

        mainM = MainMenu()

        spanInstruct = str("\n" + "\n" + "Welcome to the Powerball Success Number Generator! " + "\n" + "\n" +
                           "I will explain how this program works. As is common knowledge, lottery success often " +
                           "relies on statistics. Those who study these statistics, and " + "\n" + "those who win, " +
                           "often suggest that asking the store clerk to have the Powerball system generate numbers " +
                           "for you is often a bad idea, as these numbers " + "\n" + "don't align statistically with " +
                           "the probability of winning." + "\n" + "\n" +
                           "In comes this program to the rescue.  You will be given the ability to choose between " +
                           "four different number-picking choices, which are designed to support winning a little" +
                           "\n" + "better than the automated Powerball numbers sold to players in-store. " + "\n" +
                           "\n" + "For the choice RA, you will be given five random White Ball numbers between " +
                           "1 and 69, and one Red Ball number between 1 and 26." + "\n" + "Choosing Evens or " +
                           "Odds will not be differentiated within this choice." + "\n" + "\n" +
                           "The next option, EV, will show you three Even White Ball numbers and two Odd White Ball numbers. " +
                           "The Red Ball will be an Even number. " + "According to my research, " + "\n" +
                           "an Even/Odd combination is more likely to win. However, having more Even numbers than Odd is supposed " +
                           "to further increase those chances of success." + "\n" + "\n" +
                           "We all know that fate can sometimes play an odd hand (pun intended).  So our tertiary choice " +
                           "is OD, which will show more Odd numbers than Even numbers, " + "\n" + "including the Red Ball (which will " +
                           "be Odd in this case)." + "\n" + "\n" +
                           "CO can be chosen so that you will see a list of numbers " +
                           "which include two random common winning White Ball numbers, and a common winning Red Ball number." +
                           "\n" + "\n" +
                           "You can type FREQ to print sets of lottery numbers and view their frequent number count." +
                           "\n" + "\n" +
                           "ESP will ensure your numbers are printed in Spanish." + "Other menus available include " +
                           " the following:" + "\n" + "\n" +
                           "1 - for Instructions in English" + "\n" +
                           "2 - para instrucciones en español" +
                           "\n" + "\n" +
                           "SVM - to try the SVM and KNN algorithm to " +
                           "predict the month numbers will be chosen" + "\n" +
                           "SCATTER - for PowerBall Scatter Plot charts and associated data" + "\n" +
                           "BAR - for PowerBall Bar charts and associated data" + "\n" +
                           "PRED - to enter two White Ball numbers and predict the last three in the set\n\n" +
                           "MN - to go to the Main Menu / Para ir al menu principal"  "\n" + "\n" +
                           "               *** Please note that if you wish to receive different numbers for any of " +
                           "the offered choices, you must restart the game ***" + "\n" + "\n" +
                           "I'm excited you are utilizing this program " + "to increase your lotto-winning " +
                           "chances.  " + "Good Luck!" + "\n" + "\n")

        # Using TextBlob to translate the English instructions to Spanish
        text = spanInstruct
        # Select characters between 0 and 100,000
        text = text[0:100000]
        blob = TextBlob(text)
        print(blob.translate(to='es'))

        mainM.main()

Instructions()

# Creating a class RandomWhite() so that for the White Balls Frequency all of the random numbers will actually be
# different sets from different methods (69 White Balls). At this time there will be ten sets at which to pull the
# frequency numbers from, to show how frequently certain White Balls pop up within the random number generator.
class RandomWhite():

    for x in range(1):

        def randWhite1(self):
            regWhite1 = str(random.sample(range(1, 70), 5))
            # print(regWhite1)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite1))
            appendFile.close()
        def randWhite2(self):
            regWhite2 = str(random.sample(range(1, 70), 5))
            # print(regWhite2)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite2))
            appendFile.close()
        def randWhite3(self):
            regWhite3 = str(random.sample(range(1, 70), 5))
            # print(regWhite3)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite3))
            appendFile.close()
        def randWhite4(self):
            regWhite4 = str(random.sample(range(1, 70), 5))
            # print(regWhite4)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite4))
            appendFile.close()
        def randWhite5(self):
            regWhite5 = str(random.sample(range(1, 70), 5))
            # print(regWhite5)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite5))
            appendFile.close()
        def randWhite6(self):
            regWhite6 = str(random.sample(range(1, 70), 5))
            # print(regWhite6)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite6))
            appendFile.close()
        def randWhite7(self):
            regWhite7 = str(random.sample(range(1, 70), 5))
            # print(regWhite7)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite7))
            appendFile.close()
        def randWhite8(self):
            regWhite8 = str(random.sample(range(1, 70), 5))
            # print(regWhite8)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite8))
            appendFile.close()
        def randWhite9(self):
            regWhite9 = str(random.sample(range(1, 70), 5))
            # print(regWhite9)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite9))
            appendFile.close()
        def randWhite10(self):
            regWhite10 = str(random.sample(range(1, 70), 5))
            # print(regWhite10)
            appendFile = open('FrequentWhiteList.csv', 'a')
            appendFile.write(str(regWhite10))
            appendFile.close()


RandomWhite()

# Creating a class RandomRed() so that for the Red Balls Frequency all of the random numbers will actually be
# different sets from different methods (26 Red Balls). At this time there will be ten sets at which to pull the
# # frequency numbers from, to show how frequently certain Red Balls pop up within the random number generator.

class RandomRed():

    for x in range(1):

        def randRed1(self):
            regRed1 = str(random.sample(range(1, 27), 1))
            # print(regRed1)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed1))
            appendFile.close()
        def randRed2(self):
            regRed2 = str(random.sample(range(1, 27), 1))
            # print(regRed2)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed2))
            appendFile.close()
        def randRed3(self):
            regRed3 = str(random.sample(range(1, 27), 1))
            # print(regRed3)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed3))
            appendFile.close()
        def randRed4(self):
            regRed4 = str(random.sample(range(1, 27), 1))
            # print(regRed4)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed4))
            appendFile.close()
        def randRed5(self):
            regRed5 = str(random.sample(range(1, 27), 1))
            # print(regRed5)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed5))
            appendFile.close()
        def randRed6(self):
            regRed6 = str(random.sample(range(1, 27), 1))
            # print(regRed6)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed6))
            appendFile.close()
        def randRed7(self):
            regRed7 = str(random.sample(range(1, 27), 1))
            # print(regRed7)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed7))
            appendFile.close()
        def randRed8(self):
            regRed8 = str(random.sample(range(1, 27), 1))
            # print(regRed8)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed8))
            appendFile.close()
        def randRed9(self):
            regRed9 = str(random.sample(range(1, 27), 1))
            # print(regRed9)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed9))
            appendFile.close()
        def randRed10(self):
            regRed10 = str(random.sample(range(1, 27), 1))
            # print(regRed10)
            appendFile = open('FrequentRedList.csv', 'a')
            appendFile.write(str(regRed10))
            appendFile.close()

RandomRed()

# Creating a Frequency() class, and attempting to gather word frequency, or possibly number
# frequency utilizing TextBlob strings
class Frequency():

    def frequWhiteRandom(self):

        # Setting up variable to pull from methods in RandomWhite() class
        pullRandomWhiteFrequ = RandomWhite()

        # Adding Frequent Random White Balls to FrequentWhiteList.csv file
        # Side note: Main menu option is performed when Frequency menu chosen in Choices() class

        appendFile = open('FrequentWhiteList.csv', 'a')
        appendFile.write("\n" + "\n")

        # appending White Ball frequent random numbers to list
        pullRandomWhiteFrequ.randWhite1()
        pullRandomWhiteFrequ.randWhite2()
        pullRandomWhiteFrequ.randWhite3()
        pullRandomWhiteFrequ.randWhite4()
        pullRandomWhiteFrequ.randWhite5()
        pullRandomWhiteFrequ.randWhite6()
        pullRandomWhiteFrequ.randWhite7()
        pullRandomWhiteFrequ.randWhite8()
        pullRandomWhiteFrequ.randWhite9()
        pullRandomWhiteFrequ.randWhite10()

    def frequRedRandom(self):
        pullRandomRedFrequ = RandomRed()

        # Adding Frequent Random Red Balls to FrequentRedList.csv file
        # Side note: Main menu option is performed when Frequency menu chosen in Choices() class

        appendFile = open('FrequentRedList.csv', 'a')
        appendFile.write("\n" + "\n")

        # appending Red Ball frequent random numbers to list
        pullRandomRedFrequ.randRed1()
        pullRandomRedFrequ.randRed2()
        pullRandomRedFrequ.randRed3()
        pullRandomRedFrequ.randRed4()
        pullRandomRedFrequ.randRed5()
        pullRandomRedFrequ.randRed6()
        pullRandomRedFrequ.randRed7()
        pullRandomRedFrequ.randRed8()
        pullRandomRedFrequ.randRed9()
        pullRandomRedFrequ.randRed10()


    def freqRandomWhiteTextBlob(self):

        # Pulling string count (word count) utilizing TextBlob from FrequentWhiteList.csv, and then appending to
        # FreqWhiteList.csv
        appendFile = open('FrequentWhiteList.csv')
        appendFile = appendFile.read()

        # Select characters between 0 and 100,000
        appendFile = appendFile[0:100000]
        blob = TextBlob(appendFile)
        strBlob = str(blob.word_counts)

        appendFile = open('ML_FrequWhiteList.csv', 'a')

        appendFile.write(strBlob)
        appendFile.close()

        # Printing the same TextBlob of frequent random numbers to the program
        print(strBlob)

    def freqRandomRedTextBlob(self):

        # Pulling string count (word count) utilizing TextBlob from FrequentWhiteList.csv, and then appending to
        # FreqRedList.csv

        appendFile = open('FrequentRedList.csv')
        appendFile = appendFile.read()
        # Select characters between 0 and 100,000
        appendFile = appendFile[0:100000]
        blob = TextBlob(appendFile)
        strBlob = str(blob.word_counts)

        appendFile = open('ML_FrequRedList.csv', 'a')
        appendFile.write(strBlob)
        appendFile.close()

        # Printing the same TextBlob of frequent random numbers to the program
        print(strBlob)

Frequency()

# Creating a Choice() function to implement program instructions and user-input choices menu: RANDOM, EVEN, ODD, COMMON;
# User input/answers to the menu will call the methods from the Balls() class for implementation
def Choice():

    #Naming variables to pull methods from the Balls() class
    regularWB = Balls()
    regularRB = Balls()

    evenWB = Balls()
    evenRB = Balls()

    oddWB = Balls()
    oddRB = Balls()

    commonWB = Balls()
    commonRB = Balls()

    english = Instructions()
    spanish = Instructions()

    randW = RandomWhite()

    randR = RandomRed()

    frequ = Frequency()

    mainM = MainMenu()




# Setting introduction and instructions for Powerball Success Number Generator

    print("\n" + "\n" + "Welcome to the Powerball Success Number Generator! " + "\n" + "\n" +
          "Bienvenido al Powerball Success Number Generator" + "\n" + "\n")

# Setting up the actual input method LotteryChoices for Choice() class; also added spanish translation to the menu

    LotteryChoices = str(input("Please choose / Por favor elija: " + "\n" + "\n" +
                               "RA - to choose random Powerball numbers / Para imprimir una lista aleatoria " +
                               "de números" + "\n" +
                               "EV - to choose a greater number of even figures within your random Powerball " +
                               "numbers / Para elegir más incluso que los números aleatorios de Powerball" + "\n" +
                               "OD - to choose a greater number of odd figures within your random Powerball " +
                               "numbers / Elegir más números de Powerball al azar" + "\n" +
                               "CO - choose a set of random numbers that include common winning numbers / " +
                               "Elegir números aleatorios que incluyan números ganadores comunes" + "\n" +
                               "FREQ - to print sets of lottery numbers and " +
                               " view their frequent number count / Para imprimir juegos de números de lotería " +
                               "y ver su conteo frecuente de números" + "\n" + "\n" +
                               "ESP - para imprimir la lista en espanol / To print your list in Spanish" +
                               "\n" +
                               "1 - for Instructions in English" + "\n" +
                               "2 - para instrucciones en español" +
                               "\n" + "\n" +
                               "SVM - to try the SVM and KNN algorithm to " +
                               "predict the month numbers will be chosen / para probar el algoritmo SVM y KNN " +
                               "para predecir los números de mes que se elegirán" + "\n" +
                               "SEQ - to predict lottery sequence / Para predecir la secuencia de lotería" + "\n" +
                               "SCATTER - for PowerBall Scatter Plot charts and associated data / "
                               " Para PowerBall Scatter Plot chart y datos asociados" + "\n" +
                               "BAR - for PowerBall Bar charts and associated data / para gráficos de barras " +
                               "PowerBall y datos asociados" + "\n" + "\n" +
                               "PRED - to enter two White Ball numbers and predict the last three in the set / " +
                               "para ingresar dos números de White Ball y predecir los últimos tres en el set" +
                               "MN - to go to the Main Menu / Para ir al menu principal"  "\n" + "\n" +
                               "Enter your choice here / Ingresa tu elección aquí: "))


    if LotteryChoices == "RA":
        regularWB.regWhiteBall()
        regularRB.regRedBall()

        mainM.main()

    if LotteryChoices == "EV":
        evenWB.evenWhiteBall()
        evenRB.evenRedBall()

        mainM.main()

    if LotteryChoices == "OD":
        oddWB.oddWhiteBall()
        oddRB.oddRedBall()

        mainM.main()

    if LotteryChoices == "CO":
        commonWB.commonWhiteBall()
        commonRB.commonRedBall()

        mainM.main()

    if LotteryChoices == "MN":

        mainM.main()

    if LotteryChoices == "SVM":

        import SVM_MonthPredictor

    if LotteryChoices == "SEQ":

        import Sequence

    # ESP choice is to translate Random_Lotto_Choices.txt into Spanish on the Spanish_Random_Lotto_Choices.txt file
    if LotteryChoices == "ESP":

        # Putting text on the random file so that if ESP is input by user, and file is empty, there won't be an
        # exception
        appendFile = open('Random_Lotto_Choices.txt', 'a')
        appendFile.write("If you have chosen Spanish translation, please make sure " +
                         "\n" + "you make an initial lottery choice prior to requesting translation.")
        appendFile.close()

        # Using TextBlob to translate Random_Lotto_Choices.txt to Spanish onto the Spanish_Random_Lotto_Choices.txt file
        text = open('Random_Lotto_Choices.txt')
        text = text.read()
        # Select characters between 0 and 12,000
        text = text[0:12000]
        blob = TextBlob(text)
        strBlob = str(blob.translate(to='es'))
        print(blob.translate(to='es'))

        # Adding the translated text to the Spanish_Random_Lotto_Choices.txt file
        appendFile = open('Spanish_Random_Lotto_Choices.txt', 'a')
        appendFile.write(("\n" + strBlob +
                          "\n" + "\n" + "----------------------"))
        appendFile.close()

        mainM.main()


    # Giving the user options to pull the program instructions up in English
    if LotteryChoices == "1":
        english.engInstructions()

        mainM.main()
    # Giving the user options to pull the program instructions up in Spanish (Textblob is used to translate
    # in the spanInstructions method)
    if LotteryChoices == "2":
        spanish.spanInstructions()

        mainM.main()

    # from the Frequency() class pulling from the Random() class methods, utilizing variables set in the
    # Choice() class to pull from Frequency() class methods
    if LotteryChoices == "FREQ":

        # printing and putting frequent White and Red Balls to frequent files
        frequ.frequWhiteRandom()
        frequ.frequRedRandom()

        # utilizing TextBlob to pull frequent White and Red Balls from frequent files and doing a "word" count on them,
        # then putting on ML (Machine Learning) csv files.
        frequ.freqRandomWhiteTextBlob()
        frequ.freqRandomRedTextBlob()

        mainM.main()

    # To show the user the Scatter plots and associated data from the Scatter.py.
    if LotteryChoices == "SCATTER":
        import Scatter

        mainM.main()

    # To show the user the Bar charts and associated data from the Bar.py.
    if LotteryChoices == "BAR":
        import Bar

        mainM.main()

    if LotteryChoices == "PRED":
        import Torch_Pred       

    else:
        print("Incorrect entry. Please try again. / Entrada incorrecta. Inténtalo de nuevo..")
        mainM.main()


Choice()

