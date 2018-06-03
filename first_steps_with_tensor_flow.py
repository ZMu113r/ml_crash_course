import math

from IPythin import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.lf}'.format


def build_model():
    return


def main():
    # Load data set
    california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")

    # Randomize the data to avoid possible pathological ordering effects
    # that might harm the performance of the Stochastic Gradient Descent
    california_housing_dataframe = california_housing_dataframe.reindex(
        np.random.permutation(california_housing_dataframe.index))

    # Scale median house values to the thousands to make learning
    # a little bit easier by using values within a normal range
    california_housing_dataframe["median_house_value"] /= 1000.0

    # Examine the data
    california_housing_dataframe.describe()

    ############################
    # BUILDING THE FIRST MODEL #
    ############################
    #
    # For this MODEL the LABEL will be median_house_value
    # This will be the thing to be predicted
    #
    # The INPUT FEATURE for this MODEL will be total_rooms
    #
    # To train the model, the LinearRegressor Interface will be used
    # by the TensorFlow Estimator API.
    # This API provides useful methods for performing model training, evaluation, and inference
    build_model()
    return
