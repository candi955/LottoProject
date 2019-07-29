
# training reference: https://www.youtube.com/watch?v=K9ypGzuP6xQ

import tensorflow as tf
import numpy as np
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

DELIMITER = ","

# setting a  minimum logging level
# reference: https://github.com/tensorflow/tensorflow/issues/1258
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class Predictions():

    warnings.simplefilter(action='ignore', category=FutureWarning)

    # Creating method to pull and set up 2019 lottery data and to run program
    def _predictions_(self):

        # using tensorflow and keras to process number sequences

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Dense(1, input_dim=1))

        # passing optimizer by name: default parameters will be used

        ask1 = input(np.array('Please enter the first White Ball Lottery number from the last pick:'))
        ask2 = input(np.array('Please enter the second White Ball Lottery number from the last pick:'))
        ask3 = input(np.array('Please enter the third White Ball Lottery number from the last pick:'))
        ask4 = input(np.array('Please enter the fourth White Ball Lottery number from the last pick:'))
        ask5 = input(np.array('Please enter the fifth White Ball Lottery number from the last pick:'))

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

        print('\n' + '\n' +'Please enter a set of four dummy numbers for our prediction model, in sequential order ' +
              '(preferably from a recent past lottery if possible): ' + '\n')

        askDummy1 = input('First number:')
        askDummy2 = input('Second number:')
        askDummy3 = input('Third number:')
        askDummy4 = input('Fourth number:')

        print('You chose the dummy numbers:')
        print(askDummy1 + ',' + askDummy2 + ',' + askDummy3 + ',' + askDummy4)

        print('Please see your sequential number prediction that could possibly be used for another lottery:')
        to_predict = np.array([askDummy1, askDummy2, askDummy3, askDummy4])
        j = model.predict(to_predict)
        print(j)

Predictions()

pred = Predictions()
pred._predictions_()
