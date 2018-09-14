from csv import reader
from math import sqrt
from random import seed
from random import randrange
import pandas as pd
import datetime

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
            print (dataset)
            return dataset
        
def imprime10(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        a = 10
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
            a = a - 1
            print (row)
            if a == 0:
                break
        return dataset

def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        print(len(dataset[0]))
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        print([value_min, value_max])
        minmax.append([value_min, value_max])
        return minmax

def PandasPrint(dataset):
    data = pd.read_csv(dataset)
    print(data.head(10))
    return data

def minmaxCol(dataset):
    data = pd.read_csv(dataset)
    print("Maximos por columna")
    print("-------------------")
    print(data.max(axis=0))
    print("                    ")
    print("Minimos por columna")
    print("-------------------")
    print(data.min(axis=0))
    return data


        

def main():
    #imprime10('/Users/nico/Desktop/wine.csv')
    #dataset_minmax('/Users/nico/Desktop/wine.csv')
    #PandasPrint('/Users/nico/Desktop/wine.csv')
    minmaxCol('/Users/nico/Desktop/wine.csv')


main()
