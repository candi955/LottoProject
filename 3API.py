

# Uses Tensor, Keras, Numpy, and OS to allow user to place number inputs, then takes the mean and creates a y variable
# by adding those means to 1, and then to the sum of that, and so on. Then the user is prompted to input dummy numbers.
# Then after a series of training and error calculation (500 epochs), the system outputs a useable set of numbers,
# something that might fall into a prediction that will help the user play future Powerball lotteries.
# training reference: https://www.youtube.com/watch?v=K9ypGzuP6xQ

import tensorflow as tf
import numpy as np
import os
import keras

# had to install pip install the tensorflow==2.0.0-beta1 to attempt to remove Future Warning
    # Using TensorFlow backend.
    # WARNING:tensorflow:From C:\Users\canda_000\.conda\envs\tensor\lib\site-packages\tensorflow\python\ops\resource_
    # variable_ops.py:435: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a
    # future version.
    # Instructions for updating:
    # Colocations handled automatically by placer.

# Other warning:
    # Successfully built the termcolor gast absl-py
    # tb-nightly 1.14.0a20190603 has requirement setuptools>=41.0.0, but you'll have setuptools 40.8.0 which is
    # incompatible.


#import warnings
#warnings.simplefilter(action='ignore', category=FutureWarning)


DELIMITER = ","


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

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Dense(1, input_dim=1))

        # passing optimizer by name: default parameters will be used

        print('Please enter the five number (possibly from most recent Powerball lottery pick) in sequential order')

        ask1 = input(np.array('First pick:'))
        ask2 = input(np.array('Second pick:'))
        ask3 = input(np.array('Third pick:'))
        ask4 = input(np.array('Fourth pick:'))
        ask5 = input(np.array('Fifth pick:'))

        print('You chose as your independent set of X variables: ')
        print(ask1 + ',' + ask2 + ',' + ask3 + ',' + ask4 + ',' + ask5)

        model.compile(loss='mean_squared_error', optimizer='sgd')
        xs = np.array([ask1, ask2, ask3, ask4, ask5]).astype(np.float)
        meanX = np.mean([xs])

        print('Average of the X variables chosen is: ')
        print(meanX)

        a = 1
        b = 1 + meanX
        c = b + meanX
        d = c + meanX
        e = d + meanX

        print('Your dependent variables, using the mean of X to create the sequence (1 + mean, 2 + mean, etc:')
        print(a, b, c, d, e)

        # creating dependent set of variables
        ys = (a, b, c, d, e)

        print('Following is the error calculation for prediction of sequence (training; set to 500 epochs):')
        model.fit(xs, ys, epochs=500)

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
        to_predict = np.array([askDummy1, askDummy2, askDummy3, askDummy4, askDummy5])
        j = model.predict(to_predict)
        print(j)

Predictions()

pred = Predictions()
pred._predictions_()
