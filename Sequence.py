# Number sequence predictor program utilizing TensorFlow and Keras, to be called from the mainPage.py program.

# Uses Tensor, Keras, Numpy, and OS to allow user to place number inputs, then takes the mean and creates a y variable
# by adding those means to 1, and then to the sum of that, and so on. Then the user is prompted to input dummy numbers.
# Then after a series of training and error calculation (500 epochs), the system outputs a useable set of numbers,
# something that might fall into a prediction that will help the user play future Powerball lotteries.
# training reference: https://www.youtube.com/watch?v=K9ypGzuP6xQ

# 7/27/2019 @ 13:40 I have decided to pull from a practice file to create a Sequence file, but with my own set of
# real lottery data.  This will require user input. I estimate this to take approximately 5 hours.
# 17:21 The entry of my own numbers has been a little difficult.  Have had to perform updates on floats versus arrays,
# etc.
# 20:15 I spent quite a bit of time trying to get rid of Future Warnings, only to research and find out that the
# future warnings are just part of Open Source tensor flow, and appear to only go away with a paid version.
# 23:52 I added the Adam optimizer to keep the Nan's from happening at the end when the gradients are too far apart.
# It seems to be working.
# 13:12 I have added access to the program from the main menu. The program actually took me approximately 11 hours to
# create with clearing of number format errors, the research and experiment on getting rid of Future Warnings, and
# the initialization of the Adam optimizer.  It does appear to be working now, however. I underestimated creation time
# by quite a bit. 

import tensorflow as tf
from keras import optimizers
sgd = optimizers.SGD(lr=0.01, clipnorm=1.)
keras = optimizers.Adam(lr=0.01, epsilon=None, decay=0.0)
import numpy as np
import os
# keras reference to prevent Nan error: https://keras.io/optimizers/
# reference concerning Nan and large gradients: https://stackoverflow.com/questions/33962226/common-causes-of-nans-during-training/33980220
# reference Adam: https://www.programcreek.com/python/example/104282/keras.optimizers.Adam


# Receiving Future Warnings; through research found that with open source Tensor Flow it is difficult and possibly
# not possibly to completely rid the program of these.

# reference: https://github.com/tensorflow/tensorflow/issues/1258
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# a Predictions class, to create the program.  I wanted to create it as a class in case I wanted to add other methods
# and options to the program later.
class Predictions():

    #import tensorflow.python.util.deprecation as deprecation
    #deprecation._PRINT_DEPRECATION_WARNINGS = False

    # Creating method to pull and set up 2019 lottery data and to run program
    def _predictions_(self):

        # using tensorflow and keras to process number sequences
        # passing optimizer by name keras due to import of Adam optimizer

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Dense(1, input_dim=1))

        print('Please enter the five number (possibly from most recent Powerball lottery pick) in sequential order')

        ask1 = input(np.array('First pick:'))
        ask2 = input(np.array('Second pick:'))
        ask3 = input(np.array('Third pick:'))
        ask4 = input(np.array('Fourth pick:'))
        ask5 = input(np.array('Fifth pick:'))

        print('You chose as your independent set of X variables: ')
        print(ask1 + ',' + ask2 + ',' + ask3 + ',' + ask4 + ',' + ask5)

        model.compile(loss='mean_squared_error', optimizer='Adam')
        xs = np.array([ask1, ask2, ask3, ask4, ask5])
        meanX = (xs).astype(np.float)
        meanXmean = (meanX).mean()


        print('Average of the X variables chosen is: ')
        print(meanXmean)

        a = 1
        b = 1 + meanXmean
        c = b + meanXmean
        d = c + meanXmean
        e = d + meanXmean

        print('Your dependent variables, using the mean of X to create the sequence (1 + mean, 2 + mean, etc:')
        print(a, b, c, d, e)

        # creating dependent set of variables
        ys = (a, b, c, d, e)

        toContinue = input('\n' + '\n' + 'Please press 1 to continue with the sequence program, or 2 to start again.  You can press 3 ' +
                    'to return to the lottery program main menu:')

        print(toContinue)

        if toContinue == '1':
            print('Following is the error calculation for prediction of sequence (training; set to 500 epochs):')

            model.fit(xs, ys, epochs=2000)

            print('\n' + '\n' +'Please enter a set of five dummy numbers for our prediction model, in sequential order ' +
                      '(preferably from a recent past lottery if possible): ' + '\n')

            askDummy1 = input('First number:')
            askDummy2 = input('Second number:')
            askDummy3 = input('Third number:')
            askDummy4 = input('Fourth number:')
            askDummy5 = input('Fifth number:')

            print('You chose the dummy numbers:')
            print(askDummy1 + ',' + askDummy2 + ',' + askDummy3 + ',' + askDummy4 + ',' + askDummy5)

            print('Please see your sequential number prediction that could possibly be used for another lottery:')

            dummyNum_predict = np.array([askDummy1, askDummy2, askDummy3, askDummy4, askDummy5]).astype(np.float)
            j = model.predict(dummyNum_predict).astype(np.float)
            print(j)

            # reference concerning large gradients and Nan: https://stackoverflow.com/questions/33962226/common-causes-of-nans-during-training/33980220
            # reference for Nan prevention: https://github.com/keras-team/keras/issues/2134

            if toContinue == '2':

                Predictions()

            if toContinue == '3':

                import mainPage.py

            lastChoice = input('\n' + '\n' + 'Please press 1 to return to the sequence program, or 2 to return to' +
                               'the main lottery program menu:')

            print(lastChoice)

            if lastChoice == '1':

                Predictions()

            if lastChoice == '2':

                import mainPage.py

Predictions()

sequ = Predictions()

sequ._predictions_()




