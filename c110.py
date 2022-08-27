import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

df = pd.read_csv('newdata.csv')
data = df['average'].tolist()

#code to find the mean and std dev of 100 datapoint
dataset = []
for i in range(0, 100):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
    
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print('mean of sample',mean)
print('std deviation of sample',std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
        
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['average'], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)    
    
setup()

average_mean = statistics.mean(data)
print('mean of average is',average_mean)

mean = statistics.mean(mean_list)
print('mean of sample list is',mean)

def std_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print('std deviation of sample distribution is',std_deviation)

std_deviation()    
    

    






    


