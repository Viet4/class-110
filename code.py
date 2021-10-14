import pandas as bear
import statistics as stats
import random
import csv
import plotly.figure_factory as ff

df = bear.read_csv("newdata.csv")

data = df["average"].tolist()

#fig = ff.create_distplot([data], ["12345678dojcvhdfvfdlkgkjsdfjdvdjfbvdkjgb"], show_hist=False)
#fig.show()

def get_mean_sample(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean_sample = stats.mean(dataset)

    return mean_sample

def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["AVERAGE"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = get_mean_sample(1000)
        mean_list.append(set_of_mean)
    show_figure(mean_list)
    mean_list_mean = stats.mean(mean_list)
    print(mean_list_mean)

setup()
print(stats.mean(data))
print("\n")
def stand_devi():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = get_mean_sample(1000)
        mean_list.append(set_of_mean)
    mean_list_stdev = stats.stdev(mean_list)
    print(mean_list_stdev)

stand_devi()
print(stats.stdev(data))








