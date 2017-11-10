""" Collection of functions for extracting basic statistcs from a data sample 
    without having to install any libraries that are not automatically included in Python.
"""

def number_of_records(data_sample):
    """ Returns the number of records from a data sample """
    return len(data_sample)


def calculate_sum(data_sample, row):
    """ Calculate the sum of a given numeric column from a data sample """
	total = 0
	for line in data_sample[1:]:
	    value = float(line[row])
	    total += value
	return total

def find_average(data_sample, row, headers=False):
    """ Find the average value of a given column from a data sample """
    total = calculate_sum(data_sample)
    size = len(data_sample, row)
    if headers:
        total -= 1
    average = total / size
    return '{:03.2f}'.format(average) #nicely formatted to 2 decimals


def find_max(theData, col):
    """ Find the max value of a given column from a data sample """
    tempList = []   
    for row in theData:
        price = float(row[col])
        tempList.append(price)
    return max(tempList)


def find_min(theData, col):
    """ Find the min value of a given column from a data sample """
    tempList = []
    for row in theData:
        price = float(row[col])
        tempList.append(price)
    return min(tempList)


def find_max_min(the_data, col, m):
    """ Find the max or min value of a given column from a data sample """
    tempList = [], val = 0
    for row in the_data:
        price = float(row[col])
        tempList.append(price)
        if m == "max": 
            val = max(tempList)
        elif m == "min":
            val = min(tempList)
        else: # hopefully we don’t come to this
            raise ValueError("The m parameter should be either 'min' or 'max'.")
    return val