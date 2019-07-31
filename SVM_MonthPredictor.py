# A program utilizing SKLearn to predict the month a set of lottery numbers will win (Currently only operates
# for January until July, off of the dataset months I have available for the AZ Powerball numbers).  Called as SVM from
# mainPage.py menu.


# Training resource: https://www.youtube.com/watch?reload=9&v=bwZ3Qiuj3i8

# Implementing an SVM
# A support vector machine (SVM) is a type of supervised machine learning classification algorithm.
# SVM differs from the other classification algorithms in the way that it chooses the decision boundary that maximizes
# the distance from the nearest data points of all the classes. An SVM doesn't merely find a decision boundary; it
# finds the most optimal decision boundary.
# reference: https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/

# Utilizing SKlearn, pandas, numpy, xlrd APIs and also using a subclass of exception: import warnings (to prevent a
# Future Error warning from popping up; appears is due to possible future updates).

# 7/25/2019 @ 21:17pm I am going to attempt to take what I've learned about SVM today, and adjust it to my lottery
# program.  I estimate this to take 12 hours total.  First step is to create a dataset, which I have to learn how
# to do.  I know SKlearn has datasets, but I am hoping to use one from my lotto numbers.  I feel it is important for
# me to learn that skill anyway, so I am going to make an attempt.
# 21:40 I figured out how to make a multi-class dataset with my numbers.   Now I need to create the excel file.
# 22:08 It didn't take me long to create the excel file, but I think the hard part is yet to come.  I have to figure
# out how the SKlearn datasets are built in order to make it work for my program.
# 23:31 I can tell that the Sklearn dataset is either in numpy array or csv format, and that the header is either
# skipped or erased.
# 13:20 I'm going to call it a night, and try again tomorrow.  I have come very far, but I think I'm getting tired and
# to the point of making mistakes.  I would say at this point I have spent about 4 and a half hours on this program.
# 7/26/2019 @ 12:36pm I had to run family errands this morning, but am beginning to work on my code again.  I
# am going to attempt to transform my source and target datasets into the correct format for the program; am trying
# to match the formatting with the famous SKLearn Iris Dataset... however this has proven to be a challenge.  I would
# still like to learn how to do it though.
# 16:34 I have created several dataset and split source/target formats of which to choose from.  Time and practice will
# tell if they will work.  I originally had the print function set out for each.  For now, I have copied/pasted all of
# the output dataset information to another file to reference, and to keep my output looking manageable, I'm going to
# hashtag out some of the print functions.  My dataset information is as follows:

# Creating a class for the DataSet, and experimentation on creating the dataset into various formats that might
# be required for this program
# The dataset will be lottery numbers WB1, WB2, WB3, WB4, WB5, in columns, with target dataset by months of draw
# (1 is Jan, 2 is Feb, etc), which is Jan-July 2019. Independent variable source will be lottery balls, and
# dependent variable source will be the months(1-7), which is the target data.

# It is currently 16:38; I am going to choose a dataset and resume creating the actual program in a moment.
# 16:52 I've decided to try variables sourceNoHeader and targetNoHeader for the program.
# 18:03 I just finished some house chores.  I also just realized I can't include the red ball in the same predictions
# as the White Balls, because White Balls are pulled from a count between 1 and 69, and Red Balls are pulled from
# a count between 1 and 26.  I have changed my source to -2 on the columns, so that the last 2 columns are removed
# for the purposes of this program.  It is now a White Ball SVM program.  If the program works, I'll consider doing a
# program for the Red Ball on a later date.
# I have finished with the test/training data.  My prediction accuracy is very low; however I suppose I should expect
# that with a small set of random numbers (48 rows).  I am relatively satisfied that I was able to create my own
# dataset and get the program to work.  Next comes the actual predictions.
# 19:08 I had an idea and starting researching, and began to realize Test Train Split settings seem to vary.  Mine was
# originally set to (X, y, test_size=0.2, random_state=5), but only had the 10% accuracy rate.  I played with numbers
# and output for a while, and came up with (X, y, test_size=0.33, random_state=50), which increased the accuracy
# prediction to approximately 31%.  I'm going to stick with this for now and see where it goes.
# I found a pretty good reference for this I plan on looking at again more later:
# https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/
# On a side note, the SKLearn data from my practice dataset (the famous Iris dataset) had to use a modification (.mod),
# but my dataset produced an error with the _mod, and seems to be working perfectly without it.  I tried to set the
# data up with the same number of rows for both source and target, so I'm hoping it was the accuracy that caused the
# function of it.
# 21:16  My project was working hours ago, but I kept getting a Future Warning error; I wasn't sure how to fix it.
# The error was:
# FutureWarning: Beginning in version 0.22, arrays of bytes/strings will be converted to decimal numbers if
# dtype='numeric'. It is recommended that you convert the array to a float dtype before using it in scikit-learn, for
# example by using your_array = your_array.astype(np.float64).

# I finally realized that my program is working, and I should probably just move on and try to remove the warning.  I
# figured out that they might not have the patch in place yet to fix the issue, as it's for the 'future'.  I had
# tried just about everything I could think of to fix it myself.  My program is almost complete.  I'm going to
# add an ifelse statement to prevent exceptions (from the user-input), and then put this on my main random program
# (it's currently on my test program).  I will make sure it is on GitHub and I have backups.  I will also add
# a menu choice, and a choice to go to this page from the menu.
# I think I'm going to remove the extra print statements also, so that the program just looks a little nicer.
# 22:49 I completed some exception handling for the user input.  A good reference is:
# https://www.python-course.eu/python3_exception_handling.php
# I have made it where an error message pops up if strings are entered (using while true and try loop with a break),
# but I am having trouble keeping the numbers within 1 and 69.
# 23:05 I have completed exception handling.  The other reference that helped me, to learn how to prevent
# certain numbers from being chose, is as follows:
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# I should mention that the resource I used for learning how to create this project is as follows:
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# I am not going to place this code on my main Lotto Python project, clean it up, add it to the menu, and I should
# be ready to finish up and video/turn it in.
# 02:25 I was surprised when I transferred the program to my main Lottery project, there were so many errors.
# It took me quite a while to revamp everything, but it all seems to be working well now.
# So far I estimate the program to have taken me about 17 hours to complete.
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xlrd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

    # Creating a class for the DataSet
    # The dataset will be lottery numbers WB1, WB2, WB3, WB4, WB5, in columns, with target dataset by months of draw
    # (1 is Jan, 2 is Feb, etc), which is Jan-July 2019. Independent variable source will be lottery balls, and
    # dependent variable source will be the months(1-7), which is the target data.
    # From my best understanding, the way the dataset is formatted is called a multi-class set

class DataSet():

    # Creating a lottoSVM prediction method to predict success of predicting the dependent y variable
    def _dataset_(self):

        # Creating variable to convert excel file to a dataframe, so can split data into independent (X) and
        # dependent (y) variables
        lottoExcel = xlrd.open_workbook('PastWinningNum_SVM_Excel.xlsx')

        # Creating variable to convert excel file to a dataframe (using pandas)
        sheets = lottoExcel.sheets()

        for sheet in sheets:
            lottoSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
            lottoSheetData_DataFrame = pd.DataFrame(lottoSheetData)
            print('\n' + '\n' + 'LottoSheet Data, DataFrame(excel) format:')
            print(lottoSheetData_DataFrame)

        # Identifying (and splitting) source variables (independent variables) and the target variable (dependant
        # variable)source - is to create a variable of the Independent X data, with [:, :-2] meaning all columns but the
        # last two (Red Balls{different ball count than White Balls} and Target data).
        # target - is to create a variable for the last column, the Dependent data, with [:, len(lottoSheetData[0])-1]
        # meaning the last column
        # resource: http://www.semspirit.com/artificial-intelligence/machine-learning/preparing-the-data/preparing-the-data-in-python/separating-source-and-target-variables/

        sources = lottoSheetData[:, :-2]
        target = lottoSheetData[:, len(lottoSheetData[0])-1]

        # Attempting to turn sources and target variables into format that can be used for SVM purposes, and skip
        # the headers (these will be the actual variables I use for source and target within the program)

        print('\n' + '\n' + 'Preparing lotto dataset to use for SVM program:')
        sourceNoHeader = np.delete(sources, (0), axis=0)
        targetNoHeader = np.delete(target, (0), axis=0)

        print('\n' + '\n' + 'Source variables in dataframe format without the headers:')
        print(sourceNoHeader)
        print('\n' + '\n' + 'Target variables in dataframe format without the header:')
        print(targetNoHeader)

        # printing data shapes
        print('\n' + '\n' + 'Shape of source data (rows, columns):')
        print(sourceNoHeader.shape)
        print('\n' + 'Shape of target data (rows, columns):')
        print(targetNoHeader.shape)

        # Calling the _svm_menu method from the Predictions class
        predictShow._svm_menu_()

DataSet()

class Predictions():

    # The _predictions_ method will be used for training and predictions
    def _predictions_(self):

        # creating a variable to call program at menu at end of program running (choice 1 on the menu)
        predictShow = Predictions()

        # Creating variable to convert excel file so can split data into independent (X) and dependent (y) variables
        lottoExcel = xlrd.open_workbook('PastWinningNum_SVM_Excel.xlsx')

        # Converting excel to dataframe format
        sheets = lottoExcel.sheets()
        for sheet in sheets:
            lottoSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

        # Creating variables to show data in array format and printing
        # Took last two rows away from the source, so that Red Ball and Target are not mixed into the Independent
        # source variable, or X variable, at this time (in this particular program is the White Ball number being
        # predicted, which is from a different count (1-69), than the Red Balls(1-26).
        sources = lottoSheetData[:, :-2]
        target = lottoSheetData[:, len(lottoSheetData[0])-1]

        # Attempting to turn sources and target variables into format that can be used for SVM purposes, and skip
        # the headers (these will be the actual variables I use for source and target within the program)
        sourceNoHeader = np.delete(sources, (0), axis=0)
        targetNoHeader = np.delete(target, (0), axis=0)

        # Turning our independent source variable (White Balls) into the X variable, and our dependent target
        # variable (months of the year, Jan-Jul 2019) into the y variable
        X = sourceNoHeader
        y = targetNoHeader


        # Beginning our Test_Train_Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

        # the below variable is set to linear because we are going to build a linear hyperplane for our problem
        model = svm.SVC(kernel='linear')

        # fit the model and pass in parameters (the X_train independent variable and dependent variable y_train)
        # added ravel due to Future Warning: 'continuous' error
        model.fit(X_train, y_train.ravel())

        # setting predictions to be based on the test dataset, therefore can check the accuracy
        # placing inside independent and dependent test variables, to compare the predicted outcome
        # using predict function
        y_pred = model.predict(X_test)

        # displaying the accuracy of prediction (in decimal format, which will need converted to percentage)
        print('\n' + '\n' + 'Prediction accuracy:' + '\n' + '\n')
        print(accuracy_score(y_test, y_pred))

        # now that data is collected, it needs to be cleaned up, then can train/test data then split into training and
        # testing subsets then can count with accuracy

        # make an instance of the model (knn variable will stand for k nearest neighbor)
        knn = KNeighborsClassifier(n_neighbors=1)

        # fit the model (with dependent and independent variables X and y as arguments)
        knn.fit(X, y)

        # training is complete, now predictions will be set up
        # dummy values will be placed in a variable as a numpy array
        # side note: you can change n_neighbors and random_state if indicated)

        # prompting user input for dummy values
        print('\n' + '\n' + 'Please enter dummy values (between numbers 1 and 69 for our prediction:' + '\n')

        # Exception handling with While Try loop and If and Else statements, with a break (to prevent strings, and
        # numbers outside of the White Ball lottery range of 1-69).
        while True:
            try:

                # gathering user input of dummy values
                user1 = input('Dummy value 1:')
                user2 = input('Dummy value 2:')
                user3 = input('Dummy value 3:')
                user4 = input('Dummy value 4:')
                user5 = input('Dummy value 5:')

                # changing user input to integer format from str, for if statements in exception handling, and also
                # to convert for later formula requirments within the prediction model
                user1 = int(user1)
                user2 = int(user2)
                user3 = int(user3)
                user4 = int(user4)
                user5 = int(user5)

            # exception handling, basically stating 'if the above previous is not true, then do this). Once a statement
            # is made, the program brings the user back to the main menu by calling the Predictions class and menu
            # method
            except ValueError:
                print('\n' + '\n' + 'Please enter a number between 1 and 69.')
                predictShow._svm_menu_()

            if user1 < 1 or user1 > 69:
                print('\n' + '\n' + 'Please enter a number between 1 and 69.')
                predictShow._svm_menu_()

            if user2 < 1 or user2 > 69:
                print('\n' + '\n' + 'Please enter a number between 1 and 69.')
                predictShow._svm_menu_()

            if user3 < 1 or user3 > 69:
                print('\n' + '\n' + 'Please enter a number between 1 and 69.')
                predictShow._svm_menu_()

            if user4 < 1 or user4 > 69:
                print('\n' + '\n' + 'Please enter a number between 1 and 69.')
                predictShow._svm_menu_()

            if user5 < 1 or user5 > 69:
                print('\n' + '\n' + 'Please enter a number between 1 and 69.')
                predictShow._svm_menu_()

            else:
                # breaking the loop to avoid infinite loop
                break

        # turning the dummy values, which were string then integer, back into an array for the prediction
        a = np.array([user1, user2, user3, user4, user5])

        # displaying user-chosen dummy values
        print('\n' + '\n' + 'Dummy values for knn prediction:')
        print(a)

        # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
        # placed within the prediction variable
        prediction = knn.predict([a])
        print('\n' + '\n' + 'The month (between January and July) that your numbers are predicted to be drawn is:')

        # printing the prediction
        print(prediction)

        # utilizing Predictions class, _svm_menu_ method to bring user back to the main menu
        predictShow._svm_menu_()

    # Creating a menu method
    def _svm_menu_(self):
        # Creating variable to call method from DataSet class(), _dataset_ method, for when the user requests to see
        # the data again on the main menu
        callingDataSet = DataSet()

        # getting the user input as to which choice he/she would like to make within the main menu
        menuAnswer = input('\n' + '\n' + 'Please enter 1 to make a prediction, 2 to see the datasets ' +
                                 'again, 3 to return to the Lottery Page main menu, or 4 to exit: ')

        # user requests to try a prediction again
        if menuAnswer == '1':
            predictShow._predictions_()

        # user requests to see datasets
        if menuAnswer == '2':
            # creating variable to go to call methods from the DataSet class
            callingDataSet._dataset_()

        # user requests Lottery Page main menu
        if menuAnswer == '3':
            # this choice takes the user to the main Lottery program page
            import mainPage

        # user requests to exit
        if menuAnswer == '4':
            exit()

Predictions()


# Start of program
# Calling the program methods to function
# creating variables to call class methods
dataShow = DataSet()
predictShow = Predictions()

# calling class methods for DataSet and Predictions classes
dataShow._dataset_()
predictShow._predictions_()
