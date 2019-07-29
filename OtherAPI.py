# Test page for Torch, dataframes, and calculating weight, error, and prediction with numbers.

# Side: note, great references for AI and number tools:

# https://skymind.ai/wiki/python-ai

import numpy as np
import pandas as pd
import xlrd
import torch

# 7/27/2019 @ 10:20am I am going to begin experimenting wih other various APIs.
# @ 13:42 I have created a program under class Other, method _other_ of which I don't think I will use as my main page.
# I am going to use the research for another program.
# 7/29/2019 @ 12:09pm I created another program, the page 3API.py, utilizing some of my research from this page, and
# and also from other listed reference pages.

class OtherAPI():
    def _other_(self):

        # references:


        # Creating variable to convert excel file to a dataframe, so can split data into independent (X) and
        # dependent (y) variables
        lottoExcel = xlrd.open_workbook('PastWinningNum_SVM_Excel.xlsx')

         # Creating variable to convert excel file to a dataframe (using pandas)
        sheets = lottoExcel.sheets()

        for sheet in sheets:
            lottoSheetData = np.array(
                [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
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
        target = lottoSheetData[:, len(lottoSheetData[0]) - 1]

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

        # ----------------------------------------------------------------------------------------
        # Pytorch API
        # reference: https://www.youtube.com/watch?v=nbJ-2G2GXL0
        # https://github.com/pytorch/tutorials/blob/master/beginner_source/examples_autograd/two_layer_net_autograd.py
        # https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e
        # Code in file autograd/two_layer_net_autograd.py



        dtype = torch.float
        device = torch.device("cpu")
        # device = torch.device("cuda:0") # Uncomment this to run on GPU

        # N is batch size; D_in is input dimension;
        # H is hidden dimension; D_out is output dimension.
        N, D_in, H, D_out = 64, 1000, 100, 10

        # Create random Tensors to hold input and outputs.
        # Setting requires_grad=False indicates that we do not need to compute gradients
        # with respect to these Tensors during the backward pass.
        x = torch.randn(N, D_in, device=device, dtype=dtype)
        y = torch.randn(N, D_out, device=device, dtype=dtype)

        print('\n' + '\n' + 'x and y')
        print(x, y)


        # Create random Tensors for weights.
        # Setting requires_grad=True indicates that we want to compute gradients with
        # respect to these Tensors during the backward pass.
        w1 = torch.randn(D_in, H, device=device, dtype=dtype, requires_grad=True)
        w2 = torch.randn(H, D_out, device=device, dtype=dtype, requires_grad=True)

        learning_rate = 1e-6
        for t in range(500):
            # Forward pass: compute predicted y using operations on Tensors; these
            # are exactly the same operations we used to compute the forward pass using
            # Tensors, but we do not need to keep references to intermediate values since
            # we are not implementing the backward pass by hand.
            y_pred = x.mm(w1).clamp(min=0).mm(w2)

            # Compute and print loss using operations on Tensors.
            # Now loss is a Tensor of shape (1,)
            # loss.item() gets the a scalar value held in the loss.
            loss = (y_pred - y).pow(2).sum()
            print(t, loss.item())

            # Use autograd to compute the backward pass. This call will compute the
            # gradient of loss with respect to all Tensors with requires_grad=True.
            # After this call w1.grad and w2.grad will be Tensors holding the gradient
            # of the loss with respect to w1 and w2 respectively.
            loss.backward()

            # Manually update weights using gradient descent. Wrap in torch.no_grad()
            # because weights have requires_grad=True, but we don't need to track this
            # in autograd.
            # An alternative way is to operate on weight.data and weight.grad.data.
            # Recall that tensor.data gives a tensor that shares the storage with
            # tensor, but doesn't track history.
            # You can also use torch.optim.SGD to achieve this.
            with torch.no_grad():
                w1 -= learning_rate * w1.grad
                w2 -= learning_rate * w2.grad

                # Manually zero the gradients after updating weights
                w1.grad.zero_()
                w2.grad.zero_()


OtherAPI()

other = OtherAPI()
other._other_()
