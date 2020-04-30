import numpy as np
import statistics
import matplotlib.pyplot as plt

#This data is a list of lists. Each sublist at position i is some n numner of results of POA
#for simulating with i+2 numner of bidders
data = np.loadtxt('asymmetric_data.dat')

# calculate min, max, avg for each # of bidders
minimums =[min(curr) for curr in data]
maximums =[max(curr) for curr in data]
averages = [statistics.mean(curr) for curr in data]
x_axis = [i+2 for i in range(len(maximums))]

plt.plot(x_axis, maximums, label = "Maximum")
plt.plot(x_axis, averages, label = "Average")
plt.plot(x_axis, minimums, label = "Minimum")

plt.xlabel('Number of Bidders')
plt.ylabel('Price of Anarchy')
plt.title('Price of Anarchy vs Number of Bidders')
plt.legend()
plt.show()



