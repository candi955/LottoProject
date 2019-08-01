# Utilizing pandas and matplotlib APIs to create an excel format view of the data, and then evaluate the White and
# Red Ball data patterns individually via bar charts. Called from mainPage.py as BAR.

# 7/22/2019@9:42am I am starting from scratch, as I believe I got too far ahead of myself this week, and my programming
# was failing.  However I did save all attempts because I believe I can get them working eventually, it will just take
# more time and studying. Today I'm going to attempt to utilize an API for part of my project, and then
# another set of APIs for a separate part of the project. I estimate this to take approximately 4 hours.
# @ 12:36 I have successfully created an excel file with dates and winning 2019 AZ Powerball numbers called
# 'PastWinningNumbers_ExcelFormat.xlsx'.  I have been able to show all columns of the file so that a viewer can access
# it, and then plot charts for each ball showing how many of certain numbers for each ball were chosen during the
# Powerball drawings. To do this I utilized pandas and matplotlib. It took nearly three hours, so I actually
# underestimated the time it would take, but not by much.
# 7/24/2019 I am going to clean up the code (with classes) and make a menu.  I am going to hashtag some of the print
# functions (in case I need them to test the code later, or pull up some of the data to view it).
# 14:34 I have finished cleaning up the Bar.py and the Scatter.py.  I am not going to add menus to the
# mainPage.py to call them.


import pandas as pd
import matplotlib.pyplot as plt


class LottoNums():

    def _lottoAllList_(self):
        # Creating a variable for the full set of the Lotto Winning Number 2019 excel file using pandas (and not just the
        # five line header)

        lotto_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', pd.set_option('display.max_columns', None),
                                 pd.set_option('display.max_rows', None), index_col=None, na_values=[])

        # Printing full set for user
        print("Full set of 2019 winning Arizona Powerball data:" + "\n" + "\n")
        print(lotto_df)
        print("\n" + "\n")

    def _lottoDescrip_(self):

        # Creating separate bar charts to show how many of each ball chosen in AZ Powerball 2019 (WB1,WB2,WB3,WB4,WB5,RB)
        # Creating a variable to pull the dataset so that it can be used for pandas data formatting and charts
        # This variable can also be used for the description, which is what it will be utilized for in this method.

        lottoSet_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', index_col=None, na_values=['NA'])

        # Describing and printing description chart of full AZ Powerball 2019 data set for user
        print("Description-chart of 2019 winning Arizona Powerball data:" + "\n" + "\n")
        describe = lottoSet_df.describe()
        print(describe)
        print("\n" + "\n")

class BarCharts():

    # Creating separate bar charts to show how many of each ball chosen in AZ Powerball 2019 (WB1,WB2,WB3,WB4,WB5,RB)

    def _wb1Bar_(self):

        # Creating a variable to pull the dataset so that it can be used for pandas data formatting and plots
        lottoSet_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', index_col=None, na_values=['NA'])

        # WB1 Bar chart 2019
        countsWB1 = pd.value_counts(lottoSet_df['WB1']).plot.bar()
        countsWB1.plot()
        plt.title('Number of particular 1st chosen winning white balls, AZ PowerBall 2019')
        plt.ylabel('How many balls chosen')
        plt.xlabel('White Ball 1 number')
        plt.figure(1)
        plt.show()

    def _wb2Bar_(self):

        # Creating a variable to pull the dataset so that it can be used for pandas data formatting and plots
        lottoSet_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', index_col=None, na_values=['NA'])

        # WB2 Bar chart 2019
        countsWB2 = pd.value_counts(lottoSet_df['WB2']).plot.bar()
        countsWB2.plot()
        plt.title('Number of particular 2nd chosen winning white balls, AZ PowerBall 2019')
        plt.ylabel('How many balls chosen')
        plt.xlabel('White Ball 2 number')
        plt.figure(2)
        plt.show()

    def _wb3Bar_(self):
        # Creating a variable to pull the dataset so that it can be used for pandas data formatting and plots
        lottoSet_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', index_col=None, na_values=['NA'])

        # WB3 Bar chart 2019
        countsWB3 = pd.value_counts(lottoSet_df['WB3']).plot.bar()
        countsWB3.plot()
        plt.title('Number of particular 3rd chosen winning white balls, AZ PowerBall 2019')
        plt.ylabel('How many balls chosen')
        plt.xlabel('White Ball 3 number')
        plt.figure(3)
        plt.show()


    def _wb4Bar_(self):
        # Creating a variable to pull the dataset so that it can be used for pandas data formatting and plots
        lottoSet_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', index_col=None, na_values=['NA'])

        # WB4 Bar chart 2019
        countsWB4 = pd.value_counts(lottoSet_df['WB4']).plot.bar()
        countsWB4.plot()
        plt.title('Number of particular 4th chosen winning white balls, AZ PowerBall 2019')
        plt.ylabel('How many balls chosen')
        plt.xlabel('White Ball 4 number')
        plt.figure(4)
        plt.show()


    def _wb5Bar_(self):
        # Creating a variable to pull the dataset so that it can be used for pandas data formatting and plots
        lottoSet_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', index_col=None, na_values=['NA'])

        # WB5 Bar chart 2019
        countsWB5 = pd.value_counts(lottoSet_df['WB5']).plot.bar()
        countsWB5.plot()
        plt.title('Number of particular 5th chosen winning white balls, AZ PowerBall 2019')
        plt.ylabel('How many balls chosen')
        plt.xlabel('White Ball 5 number')
        plt.figure(5)
        plt.show()


    def _rb_Bar_(self):
        # Creating a variable to pull the dataset so that it can be used for pandas data formatting and plots
        lottoSet_df = pd.read_excel('PastWinningNumbers_ExcelFormat.xlsx', index_col=None, na_values=['NA'])

        # RB Bar chart 2019
        countsRB = pd.value_counts(lottoSet_df['RB']).plot.bar()
        countsRB.plot()
        plt.title('Number of particular chosen winning red balls, AZ PowerBall 2019')
        plt.ylabel('How many balls chosen')
        plt.xlabel('Red ball number')
        plt.figure(6)
        plt.show()

# Creating variables to pull the number lists, lotto number description, and bar charts when called from main menu.
nums = LottoNums()
bar = BarCharts()

# Calling methods
nums._lottoAllList_()
nums._lottoDescrip_()

bar._wb1Bar_()
bar._wb2Bar_()
bar._wb3Bar_()
bar._wb4Bar_()
bar._wb5Bar_()
bar._rb_Bar_()

