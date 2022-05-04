import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import csv
from datetime import datetime

unemployment = []


with open("unemployment.csv") as file:
	reader = csv.reader(file)

	first = next(reader)
	i = first.index('Jan-20')
	unemployment.append(['States'] + first[i:])

	for row in reader:
		newrow = []
		for s in (row[i:]):
			if s != '':
				newrow.append(float(s))
			else:
				newrow.append(0)
		unemployment.append([row[0]] + newrow)



font = {'family' : 'normal',
        'size'   : 6}

matplotlib.rc('font', **font)

for i in unemployment:
	print(i)

plt.plot(unemployment[0][1:], unemployment[1][1:], label="Alabama")
plt.plot(unemployment[0][1:], unemployment[5][1:], label="California")
plt.plot(unemployment[0][1:], unemployment[11][1:], label="Georgia")
plt.plot(unemployment[0][1:], unemployment[33][1:], label="New York")


plt.xlabel("Months of the Pandemic")
plt.ylabel("Unemployment Rate")
plt.title("Unemployment over The Pandemic in Urban and Rural States")
plt.legend(loc="upper right")


nums = unemployment[33][2:6]
print(np.mean(nums), np.std(nums))
nums = unemployment[11][2:6]
print(np.mean(nums), np.std(nums))




frame = plt.gca()
n = 12
step = int(len(unemployment[0][1:])/n)
frame.axes.get_xaxis().set_ticks(np.arange(0,len(unemployment[0][1:]), step=step))

plt.show()

# GA_dates = []
# GA_cases = []
# NY_dates = []
# NY_cases = []
# plt.clf()


# with open("cases.csv") as file:
# 	reader = csv.reader(file)

# 	for row in reader:
# 		if(row[1] == "NY" and int(row[5]) != 0):
# 			NY_dates.append(row[0])
# 			NY_cases.append(float(row[5])/194.5)
# 		elif(row[1] == "GA" and int(row[5]) != 0):
# 			GA_dates.append(row[0])
# 			GA_cases.append(float(row[5])/106.2)


# combo_dates = sorted(np.unique(NY_dates + GA_dates), key= lambda date: datetime.strptime(date, "%m/%d/%y"))
# GA_cases_temp = GA_cases
# NY_cases_temp = NY_cases
# GA_cases = [0] * len(combo_dates)
# NY_cases = [0] * len(combo_dates)

# print(combo_dates)

# for i in range(0, len(GA_dates)):
# 	j = combo_dates.index(GA_dates[i])
# 	GA_cases[j] = GA_cases_temp[i]

# for i in range(0, len(NY_dates)):
# 	j = combo_dates.index(NY_dates[i])
# 	NY_cases[j] = NY_cases_temp[i]



# plt.plot(combo_dates, NY_cases, label="NY")
# plt.plot(combo_dates, GA_cases, label="GA")
# plt.xlabel("Time")
# plt.ylabel("New Cases")
# plt.title("New Cases Per Day in Georgia")
# plt.legend(loc="upper left")

# frame = plt.gca()
# n = 12
# step = int(len(NY_dates)/n)
# frame.axes.get_xaxis().set_ticks(np.arange(0,len(NY_dates), step=step))
# plt.show()