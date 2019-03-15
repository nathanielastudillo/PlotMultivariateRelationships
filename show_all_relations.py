'''
author: nathanielastudillo
'''
import pandas as pd
import matplotlib.pyplot as plt

def show_all_relations(df):
    '''
    This function generates a matplotlib scatterplot for each unique data pair
    in a pandas dataframe.
    '''
    #jettisons numerical data
    df = df.select_dtypes(include='number')
    pairs = []
    '''
    add pairs of variables to list only when either permutation is not 
    already in the list
    '''
    for i in df:
      for j in df:
        if i == j: #avoid plotting the same pair against itself
          continue
        elif ([i,j] in pairs) or ([j,i] in pairs): #avoid plotting permutaions
          continue
        else:
          pairs.append([i,j])
          
    for pair in pairs:
      plt.scatter(df[pair[0]], df[pair[1]])
      plt.xlabel(pair[0])
      plt.ylabel(pair[1])
      plt.title("{} by {}".format(pair[0],pair[1]))
      plt.show()
