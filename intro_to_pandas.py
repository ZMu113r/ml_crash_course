# This is a beginner tutorial on the pandas data analytics library
import pandas as pd
import numpy as np
pd.__version__


# There are familiar Python dict/list operations that can
# be used to access data in pandas
def accessing_data(city_names, population):
    cities = pd.DataFrame({'City name': city_names, 'Population': population})
    print(type(cities['City name']))
    cities['City name']

    print(type(cities['City name'][1]))
    cities['City name'][1]

    print(type(cities[0:2]))
    cities[0:2]
    return


def manipulating_data(population, cities):
    # Regular arithmetic manipulations can be used
    population / 1000

    # pandas Series data objects can be used as arguments in NumPy functions
    # NumPy is a good toolkit for scientific computing
    np.log(population)

    # Series.apply can be used in conjunction with a lambda function as an argument,
    # this function will be applied to each value in the Series
    population.apply(lambda val: val > 1000000)

    # Easy to modify existing Data Frames like so..
    cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
    cities['Population Density'] = cities['Population'] / cities['Area square miles']
    cities
    return


# Task: Modify the cities table by adding a new boolean column that
# is True if and only if both of the following are True:
#           The city is named after a saint
#           The city has an area > 50 square miles
# Hint: "San" in Spanish means "saint"
def exercise_1(cities):
    cities['san_greater_than_fifty'] = (cities['City name'].apply(lambda name: name.startswith('San'))) & \
                                       (cities['Area square miles'] > 50)
    cities
    return


# Index values are assigned to each Series item or Data Frame row upon creation.
# These values do not change even if the contents are re-ordered
def indexes(city_names, cities):
    city_names.index
    cities.index

    #Rows can be manually re-ordered using
    cities.reindex[2, 0, 1]
    # The above has the same effect as sorting by city name

    # By compounding this row re-ordering operation with NumPys permutation function,
    # one can throw in extra randomization
    cities.reindex(np.random.permutation(cities.index))
    return


# DataFrame.reindex([]) can even be used on indexes that aren't in the DataFrame
def exercise_2(cities):
    cities.reindex([4, 0, 2])
    cities.reindex([0, 4, 5, 2])
    return


def main():
    # Series are a data structure basically columns in your traditional 2D grid.
    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([8573782, 123153, 7673564])

    # Data Frames represent the actual grid in which the Series reside
    ################
    # MANUAL ENTRY #
    ################
    cities = pd.DataFrame({'City name': city_names, 'Population': population})

    #####################
    # READ IN FROM FILE #
    #####################
    california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
    # Shows interesting statistics about the Data Frame
    california_housing_dataframe.describe()
    # Displays the first few records of a data Frame
    california_housing_dataframe.head()
    # Graphs like histograms can be useful for things like quickly
    # analyzing the values within a given Series (column)
    california_housing_dataframe.hist('housing_median_age')

    print("LOOK OVER HERE")
    print(california_housing_dataframe)
    california_housing_dataframe.head(5).to_csv('intro_to_pandas_output.csv', encoding='utf-8')

    accessing_data(city_names, population)
    manipulating_data(population, cities)
    exercise_1(cities)
    indexes(city_names, cities)
    exercise_2(cities)

    return
