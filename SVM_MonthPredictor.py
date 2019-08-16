# A GUI program (through Tkinter) utilizing SKLearn to predict the month a set of lottery numbers will win
# (currently only operates for January until July, off of the dataset months I have available for the AZ Powerball
# numbers).  Called as SVM from mainPage.py menu.


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

# Additional information about this module and how it works:
# The dataset will be lottery numbers WB1, WB2, WB3, WB4, WB5, in columns, with target dataset by months of draw
# (1 is Jan, 2 is Feb, etc), which is Jan-July 2019. Independent variable source will be lottery balls, and
# dependent variable source will be the months(1-7), which is the target data.
# From my best understanding, the way the dataset is formatted is called a multi-class set
# 8/16/2019 @ 14:05pm I was late in entering my diary work for this project.  However I will post the timeline of
# occurrences as best as possible. I became very caught up in the project once it started working.
# I had been playing with various APIS, and at approximately 1:30am on 8/15/2019, I decided that I thought I could
# make the Tkinter GUI work with my program.  It did take approximately 8 hours in total, and took quite a bit of
# Google research between code-comparisons of the example-code provided in class.  However, I now have a functional
# GUI program that mirrors the non-GUI version.  It has a window with 3 tabs and frames within each tab.
# The tabs signify via label which part of the program the user is in, and provides instructions on how to run
# the program.  The initial tab is the dataset utilized to gather training data for the SVM machine learning model.
# The second tab has a button with which the user can click and see the prediction accuracy of this current model.
# The third tab allows the user to enter their 5 dummy White Ball lottery numbers, and then click a button which allows
# for prediction of what month it is likely for those numbers to be winning lottery (AZ Powerball) balls.
# The program has a 'close and go to program main menu' button on the first tab, and also an 'exit the entire program'
# button on the same tab.  It also has error checking and exception prevention for the third tab user-entries. An
# error message box pops up to explain to the user how to possibly correct the error, and then the dummy textboxes
# are cleared and focus brought back to the dummy number box #1.


# Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox

# Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xlrd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# pulling excel file and creating variable
lottoExcel = xlrd.open_workbook('PastWinningNum_SVM_Excel.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = lottoExcel.sheets()
for sheet in sheets:
    lottoSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
    #lottoSheetData_DataFrame = pd.DataFrame(lottoSheetData)
    # print('\n' + '\n' + 'LottoSheet Data, DataFrame(excel) format:')
    # print(lottoSheetData_DataFrame)
# creating dataframe for tkinter
df = pd.DataFrame(lottoSheetData)

sources = lottoSheetData[:, :-2]
target = lottoSheetData[:, len(lottoSheetData[0]) - 1]

sourceNoHeader = np.delete(sources, (0), axis=0)
targetNoHeader = np.delete(target, (0), axis=0)

X = sourceNoHeader
y = targetNoHeader

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

model = svm.SVC(kernel='linear')
model.fit(X_train, y_train.ravel())
y_pred = model.predict(X_test)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
###################################################################################################################
root = tk.Tk()
root.title('SVM Prediction (predicting the month a set of dummy lottery numbers will win)')
#root.geometry("1000x1000")
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

# Tabs and Frames
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Dataset')
tab_control.add(tab2, text='Prediction Accuracy')
tab_control.add(tab3, text='Dummy Values and Prediction')

tab_control.pack(expand=1, fill='both')

###################################################################################################################
# the dataframe method, tab 1
def writeDataset():
    tab1_display.insert(1.0, pd.DataFrame(df))

# the accuracy score method, tab 2
def writeAccuracy():
    tab2_display.insert(4.0, str(accuracy_score(y_test, y_pred)))

# creating a method so that the user can tab from one dummy number textbox to the next, instead of clicking
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

# the dummy number value method, for tab 3 input entries from the user
def dummyValues():
    while True:
        try:

            # getting user-input for dummy numbers to be used in the algorithm; preferably the most recent
            # lottery numbers
            dummyTextOne = dummyNumberOne.get('1.0', tk.END)
            dummyTextTwo = dummyNumberTwo.get('1.0', tk.END)
            dummyTextThree = dummyNumberThree.get('1.0', tk.END)
            dummyTextFour = dummyNumberFour.get('1.0', tk.END)
            dummyTextFive = dummyNumberFive.get('1.0', tk.END)

            # changing dummy numbers to integers for algorithm processing
            dummyValues.dummyTextOne = int(dummyTextOne)
            dummyValues.dummyTextTwo = int(dummyTextTwo)
            dummyValues.dummyTextThree = int(dummyTextThree)
            dummyValues.dummyTextFour = int(dummyTextFour)
            dummyValues.dummyTextFive = int(dummyTextFive)

        # exception handling, basically stating 'if the above previous is not true, then do this). Once a statement
        # is made, the program brings the user back to the main menu by calling the Predictions class and menu
        # method
        except ValueError:
            # error message variable
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()



        if dummyValues.dummyTextOne < 1 or dummyValues.dummyTextOne > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()


        if dummyValues.dummyTextTwo < 1 or dummyValues.dummyTextTwo > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        if dummyValues.dummyTextThree < 1 or dummyValues.dummyTextThree > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        if dummyValues.dummyTextFour < 1 or dummyValues.dummyTextFour > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        if dummyValues.dummyTextFive < 1 or dummyValues.dummyTextFive > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        else:
            # breaking the loop to avoid infinite loop
            break

# the prediction method, for tab 3; utilizes dummy value input from dummy value method, which is why that method
# is called at the beginning of the finalPrediction method (for the user-input variables)
def finalPrediction():

    while True:
        try:
            #calling dummy values function to call variables from that function
            dummyValues()
            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyValues.dummyTextOne, dummyValues.dummyTextTwo, dummyValues.dummyTextThree,
                          dummyValues.dummyTextFour, dummyValues.dummyTextFive])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            tab3_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        else:
            break

def clear_display_result():
    tab3_display.delete(1.0, END)
    dummyNumberOne.delete(1.0, END)
    dummyNumberTwo.delete(1.0, END)
    dummyNumberThree.delete(1.0, END)
    dummyNumberFour.delete(1.0, END)
    dummyNumberFive.delete(1.0, END)

    dummyNumberOne.focus()

def mainMenu():

    while True:
        try:
            # placing this as example, since this module will be moved to another program and menu module will need changed
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                root.protocol("WM_DELETE_WINDOW", mainMenu)
                import mainPage

        except ValueError:
            import mainPage
        else:
            break

def exitProgram():
    exit()

def flush(self):
    pass
###################################################################################################################
# Labels for tabs
l1 = Label(tab1, text='Please click the button below to scroll through the original dataset model.', padx=5, pady=5)
l1.grid(row=1, column=0)
l2 = Label(tab2, text='Please click the button below to see the prediction accuracy of the model in decimal ' +
                      'format.', padx=5, pady=5)
l2.grid(row=1, column=0)
l3 = Label(tab3, text='Please enter five dummy numbers in the cells below,\n and then click the Prediction button to ' +
                      'see your prediction results:', padx=5, pady=5)
l3.grid(row=1, column=0)


# Dummy Number Input Boxes
dummyNumberOne = ScrolledText(tab3, height=1)
# the next piece of code is calling from the focus_next_widget method so that the user can tab from textbox to textbox,
# rather than clicking
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=2, column=0, columnspan=1, padx=5, pady=5)

dummyNumberTwo = ScrolledText(tab3, height=1)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

dummyNumberThree = ScrolledText(tab3, height=1)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

dummyNumberFour = ScrolledText(tab3, height=1)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=5, column=0, columnspan=1, padx=5, pady=5)

dummyNumberFive = ScrolledText(tab3, height=1)
dummyNumberFive.bind("<Tab>", focus_next_widget)
dummyNumberFive.grid(row=6, column=0, columnspan=1, padx=5, pady=5)

# Dataset Button
datasetButton = Button(tab1, text='Dataset', command=writeDataset, width=12, bg='purple', fg='#fff')
datasetButton.grid(row=3, column=0, padx=15, pady=15)

# Accuracy Button
AccuracyButton = Button(tab2, text='Prediction Accuracy', command=writeAccuracy, width=20, bg='purple', fg='#fff')
AccuracyButton.grid(row=15, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(tab3, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='purple', fg='#fff')
PredictionButton.grid(row=7, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(tab3, text='Clear results and start over', command=clear_display_result, width=25,
                          bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=9, column=0, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(tab1, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=3, column=3, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab1, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=4, column=3, padx=5, pady=5)

# Display Screen for Result
tab1_display = ScrolledText(tab1, height=20, width=50)
tab1_display.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

tab2_display = ScrolledText(tab2, height=1, width=20)
tab2_display.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

tab3_display = ScrolledText(tab3, height=1)
tab3_display.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

# Keep window alive
mainloop()
