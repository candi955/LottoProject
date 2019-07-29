# 7/23/2019 @ 10:17am I am estimating this project to take approximately 9 hours to complete.  I am going to make
# scatter plot charts, and attempt linear regressions for all of the White and Red Balls.  I am going to search for
# APIs to help me do this.  I am starting with Numpy and XLRD.  From research it looks like I'm going to need to use
# pandas and matplotlib again to make this work. My third API chosen for this project remains to be seen.
# @ 16:34 It has been quite difficult to combine ideas from different coding and different API's to make this work
# for my project.  I have become caught up on trying to convert the np.array 'Dates' from the excel file to a type of
# format that the linear regression equation will find amiable.  However all of my attempts have failed, and I have
# been very slowed down in my progress.  At this time, I have realized that the dates are all equal distance apart in
# number of days, and perhaps I could use the array's index instead.  I am going to try this.  I need to at least know
# the charting and coding is working, and I figure once that is working I can always attempt to convert dates later.
# 21:34 I took a few hours break to hang out with my family.  I am going to start coding again now. At this point, with
# breaks included, it has taken approximately it has taken approximately 8 and a half hours.  The plots are working,
# but I still want to try to put a date on the side.  The linear regression appears to be working on the WB1 chart,
# which is my test chart.  I need to study the math behind it more to know how accurate it is though.  From my
# minimal experience it appears legible and somewhat accurate, but the amount of error within it could be far greater
# than what would normally be expected.
# 24:08 I am failing miserably at the date conversion, no matter what I try.  I have become fairly tired, and will
# continue in the morning.
# 7/24/2019 @ 11:27 I have decided to find my third API so that I can finish the project.  After some research I have
# decided to attempt to create an OLS Regression Result summary.  This might help me in future research to determine
# if my charting is at all accurate, and to learn more about how the Scatter Plot and Linear Regression works.  It also
# will require a third API, StatsModels, which will help me complete the requirements of this project.
# 13:48 I have completed the summary.  It took me some settings downloads to make it work and some research, as the
# statsmodel sm.OLS did not want to work at first.  On a github account I found out there was a person that had the
# same problem and loaded the package Patsy. I also had to load the Statsmodel package.  Either way, it seems to be
# working now.  I am going to clean it up with classes and make a mainPage.py menu to call it from the program by the
# user. I am going to hashtag some of the print functions (in case I need them to test the code later, or pull up
# some of the data to view it).
# 14:34 I have finished cleaning up the NeuralPage.py and the ML_Page.py.  I am now going to add menus to the
# mainPage.py to call them.

import numpy as np
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import statsmodels.api as sm


class Regression():
    def _wb1Reg_(self):
        #WB1
        # Pulling excel file data for WB1 up and changing into a numpy array
        print("\n" + "\n")
        # print('Excel data set in array format:' + '\n' + '\n')

        book = xlrd.open_workbook('PastWinningNumbers_ExcelFormat.xlsx')
        sheets = book.sheets()
        for sheet in sheets:

            data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
            # print(data)
            data.shape = (49, 7)
            # print(data.shape)
        # Creating a linear regression scatter plot chart for WB1

        lottoSet_df = pd.read_excel(book, index_col=None,
                                    na_values=['NA'])

        # print('\n' + '\n' + 'LottoSet_df:')
        # print(lottoSet_df)

        x = np.array(lottoSet_df['WB1'])
        y = np.array(lottoSet_df.index)

        # print('\n' + '\n' + 'WB1:')
        # print(x)
        # print('\n' + '\n' + 'Dates, indexed:')
        # print(y)

        xerr = [1]*48

        plt.rc('font', family='serif', size=13)
        m, b = polyfit(x, y, 1)
        plt.plot(x, y, 's', color='#0066FF')
        plt.plot(x, m*x + b, 'r-') #BREAKS ON THIS LINE
        plt.errorbar(x, y, xerr=xerr, yerr=0, linestyle="None", color='black')
        plt.title('Scatter Plot of winning WB1, 2019', fontsize=14)
        plt.xlabel('White Ball 1', fontsize=14)
        plt.ylabel('Index', fontsize=14)
        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.grid(False)
        plt.xlim(0, 70)
        plt.ylim(0, 50)
        plt.scatter(x, y, 1)
        plt.show()

        # Attempting to use statsmodels to get summary of WB1 regression

        print('OLS Regression results for White Ball 1:' + '\n' + '\n')

        model = sm.OLS(y, x)
        results = model.fit()
        print(results.summary())

    def _wb2Reg_(self):
        #WB2
        # Pulling excel file data for WB2 up and changing into a numpy array
        print("\n" + "\n")
        # print('Excel data set in array format:' + '\n' + '\n')

        book = xlrd.open_workbook('PastWinningNumbers_ExcelFormat.xlsx')
        sheets = book.sheets()
        for sheet in sheets:

            data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
            # print(data)
            data.shape = (49, 7)
            # print(data.shape)
        # Creating a linear regression scatter plot chart for WB2

        lottoSet_df = pd.read_excel(book, index_col=None,
                                    na_values=['NA'])

        # print('\n' + '\n' + 'LottoSet_df:')
        # print(lottoSet_df)

        x = np.array(lottoSet_df['WB2'])
        y = np.array(lottoSet_df.index)

        # print('\n' + '\n' + 'WB2:')
        # print(x)
        # print('\n' + '\n' + 'Dates, indexed:')
        # print(y)

        xerr = [1]*48

        plt.rc('font', family='serif', size=13)
        m, b = polyfit(x, y, 1)
        plt.plot(x, y, 's', color='#0066FF')
        plt.plot(x, m*x + b, 'r-') #BREAKS ON THIS LINE
        plt.errorbar(x, y, xerr=xerr, yerr=0, linestyle="None", color='black')
        plt.title('Scatter Plot of winning WB2, 2019', fontsize=14)
        plt.xlabel('White Ball 2', fontsize=14)
        plt.ylabel('Index', fontsize=14)
        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.grid(False)
        plt.xlim(0, 70)
        plt.ylim(0, 50)
        plt.scatter(x, y, 1)
        plt.show()

        # Attempting to use statsmodels to get summary of WB1 regression

        print('OLS Regression results for White Ball 2:' + '\n' + '\n')

        model = sm.OLS(y, x)
        results = model.fit()
        print(results.summary())

    def _wb3Reg_(self):
        #WB3
        # Pulling excel file data for WB3 up and changing into a numpy array
        print("\n" + "\n")
        # print('Excel data set in array format:' + '\n' + '\n')

        book = xlrd.open_workbook('PastWinningNumbers_ExcelFormat.xlsx')
        sheets = book.sheets()
        for sheet in sheets:

            data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
            # print(data)
            data.shape = (49, 7)
            # print(data.shape)
        # Creating a linear regression scatter plot chart for WB3

        lottoSet_df = pd.read_excel(book, index_col=None,
                                    na_values=['NA'])

        # print('\n' + '\n' + 'LottoSet_df:')
        # print(lottoSet_df)

        x = np.array(lottoSet_df['WB3'])
        y = np.array(lottoSet_df.index)

        # print('\n' + '\n' + 'WB3:')
        # print(x)
        # print('\n' + '\n' + 'Dates, indexed:')
        # print(y)

        xerr = [1]*48

        plt.rc('font', family='serif', size=13)
        m, b = polyfit(x, y, 1)
        plt.plot(x, y, 's', color='#0066FF')
        plt.plot(x, m*x + b, 'r-') #BREAKS ON THIS LINE
        plt.errorbar(x, y, xerr=xerr, yerr=0, linestyle="None", color='black')
        plt.title('Scatter Plot of winning WB3, 2019', fontsize=14)
        plt.xlabel('White Ball 3', fontsize=14)
        plt.ylabel('Index', fontsize=14)
        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.grid(False)
        plt.xlim(0, 70)
        plt.ylim(0, 50)
        plt.scatter(x, y, 1)
        plt.show()

        # Attempting to use statsmodels to get summary of WB3 regression

        print('OLS Regression results for White Ball 3:' + '\n' + '\n')

        model = sm.OLS(y, x)
        results = model.fit()
        print(results.summary())

    def _wb4Reg_(self):
        #WB4
        # Pulling excel file data for WB4 up and changing into a numpy array
        print("\n" + "\n")
        # print('Excel data set in array format:' + '\n' + '\n')

        book = xlrd.open_workbook('PastWinningNumbers_ExcelFormat.xlsx')
        sheets = book.sheets()
        for sheet in sheets:

            data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
            # print(data)
            data.shape = (49, 7)
            # print(data.shape)
        # Creating a linear regression scatter plot chart for WB4

        lottoSet_df = pd.read_excel(book, index_col=None,
                                    na_values=['NA'])

        # print('\n' + '\n' + 'LottoSet_df:')
        # print(lottoSet_df)

        x = np.array(lottoSet_df['WB4'])
        y = np.array(lottoSet_df.index)

        # print('\n' + '\n' + 'WB4:')
        # print(x)
        # print('\n' + '\n' + 'Dates, indexed:')
        # print(y)

        xerr = [1]*48

        plt.rc('font', family='serif', size=13)
        m, b = polyfit(x, y, 1)
        plt.plot(x, y, 's', color='#0066FF')
        plt.plot(x, m*x + b, 'r-') #BREAKS ON THIS LINE
        plt.errorbar(x, y, xerr=xerr, yerr=0, linestyle="None", color='black')
        plt.title('Scatter Plot of winning WB4, 2019', fontsize=14)
        plt.xlabel('White Ball 4', fontsize=14)
        plt.ylabel('Index', fontsize=14)
        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.grid(False)
        plt.xlim(0, 70)
        plt.ylim(0, 50)
        plt.scatter(x, y, 1)
        plt.show()

        # Attempting to use statsmodels to get summary of WB4 regression

        print('OLS Regression results for White Ball 4:' + '\n' + '\n')

        model = sm.OLS(y, x)
        results = model.fit()
        print(results.summary())

    def _wb5Reg_(self):
        #WB5
        # Pulling excel file data for WB5 up and changing into a numpy array
        print("\n" + "\n")
        # print('Excel data set in array format:' + '\n' + '\n')

        book = xlrd.open_workbook('PastWinningNumbers_ExcelFormat.xlsx')
        sheets = book.sheets()
        for sheet in sheets:

            data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
            # print(data)
            data.shape = (49, 7)
            # print(data.shape)
        # Creating a linear regression scatter plot chart for WB4

        lottoSet_df = pd.read_excel(book, index_col=None,
                                    na_values=['NA'])

        # print('\n' + '\n' + 'LottoSet_df:')
        # print(lottoSet_df)

        x = np.array(lottoSet_df['WB5'])
        y = np.array(lottoSet_df.index)

        # print('\n' + '\n' + 'WB5:')
        # print(x)
        # print('\n' + '\n' + 'Dates, indexed:')
        # print(y)

        xerr = [1]*48

        plt.rc('font', family='serif', size=13)
        m, b = polyfit(x, y, 1)
        plt.plot(x, y, 's', color='#0066FF')
        plt.plot(x, m*x + b, 'r-') #BREAKS ON THIS LINE
        plt.errorbar(x, y, xerr=xerr, yerr=0, linestyle="None", color='black')
        plt.title('Scatter Plot of winning WB5, 2019', fontsize=14)
        plt.xlabel('White Ball 5', fontsize=14)
        plt.ylabel('Index', fontsize=14)
        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.grid(False)
        plt.xlim(0, 70)
        plt.ylim(0, 50)
        plt.scatter(x, y, 1)
        plt.show()

        # Attempting to use statsmodels to get summary of WB5 regression

        print('OLS Regression results for White Ball 5:' + '\n' + '\n')

        model = sm.OLS(y, x)
        results = model.fit()
        print(results.summary())


    def _RB_Reg_(self):
        #RB
        # Pulling excel file data for RB up and changing into a numpy array
        print("\n" + "\n")
        # print('Excel data set in array format:' + '\n' + '\n')

        book = xlrd.open_workbook('PastWinningNumbers_ExcelFormat.xlsx')
        sheets = book.sheets()
        for sheet in sheets:

            data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
            # print(data)
            data.shape = (49, 7)
            # print(data.shape)
        # Creating a linear regression scatter plot chart for WB4

        lottoSet_df = pd.read_excel(book, index_col=None,
                                    na_values=['NA'])

        # print('\n' + '\n' + 'LottoSet_df:')
        # print(lottoSet_df)

        x = np.array(lottoSet_df['RB'])
        y = np.array(lottoSet_df.index)

        # print('\n' + '\n' + 'RB:')
        # print(x)
        # print('\n' + '\n' + 'Dates, indexed:')
        # print(y)

        xerr = [1]*48

        plt.rc('font', family='serif', size=13)
        m, b = polyfit(x, y, 1)
        plt.plot(x, y, 's', color='#0066FF')
        plt.plot(x, m*x + b, 'r-') #BREAKS ON THIS LINE
        plt.errorbar(x, y, xerr=xerr, yerr=0, linestyle="None", color='black')
        plt.title('Scatter Plot of winning RB, 2019', fontsize=14)
        plt.xlabel('Red Ball', fontsize=14)
        plt.ylabel('Index', fontsize=14)
        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.grid(False)
        plt.xlim(0, 70)
        plt.ylim(0, 50)
        plt.scatter(x, y, 1)
        plt.show()

        # Attempting to use statsmodels to get summary of RB regression

        print('OLS Regression results for Red Ball:' + '\n' + '\n')

        model = sm.OLS(y, x)
        results = model.fit()
        print(results.summary())



# To show all ScatterPlots and OLS Regression Results when called from mainPage.py

# Creating variable to pull methods from Regression() class
show = Regression()

# Calling methods
show._wb1Reg_()
show._wb2Reg_()
show._wb3Reg_()
show._wb4Reg_()
show._wb5Reg_()
show._RB_Reg_()

