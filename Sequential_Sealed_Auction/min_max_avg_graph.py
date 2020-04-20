import numpy as np
import statistics
import matplotlib.pyplot as plt

#This data is a list of lists. Each sublist at position i is some n numner of results of POA
#for simulating with i+2 numner of bidders
data = np.loadtxt('zi_symmetric_overbidding_data.dat')

# calculate min, max, avg for each # of bidders
minimums =[min(curr) for curr in data]
maximums =[max(curr) for curr in data]
averages = [statistics.mean(curr) for curr in data]
x_axis = [i+2 for i in range(len(maximums))]

plt.plot(x_axis, minimums, label = "Minimums")
plt.plot(x_axis, averages, label = "Averages")
plt.plot(x_axis, maximums, label = "Maximums")

plt.xlabel('Number of Bidders')
plt.ylabel('Price of Anarchy')
plt.title('Price of Anarchy vs Number of Bidders')
plt.legend()
plt.show()



