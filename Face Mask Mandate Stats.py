import csv
import statistics
import numpy
from prettytable import PrettyTable
from datetime import datetime
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest as ztest

file = open('CovidCases.csv')
csvreader = csv.reader(file)


mandate_start_date = datetime(2020, 4, 17)
mandate_end_date = datetime(2021, 5, 19)


data_by_states = {}
ga_data = [[],[]]
ny_data = [[],[]]
for row in csvreader:
	if (row[0] == 'submission_date'):
		print (row)
		break;
	date = datetime.strptime(row[0], '%m/%d/%Y')
	if row[1] == 'GA' and date > mandate_start_date and date < mandate_end_date:
		ga_data[0].append(date)
		ga_data[1].append(int(row[5]) / 10711908 * 1000)
	if row[1] == 'NY' and date > mandate_start_date and date < mandate_end_date:
		ny_data[0].append(date)
		ny_data[1].append(int(row[5]) / 8177025 * 1000)

'''
plt.plot(ga_data[0], ga_data[1])
plt.xlabel('Date')
plt.ylabel('number of new cases over state population times 1000')
plt.title('New Cases Per Capita in Goergia During New York Mask Mandate')
'''
plt.plot(ny_data[0], ny_data[1])
plt.xlabel('Date')
plt.ylabel('number of new cases over state population times 1000')
plt.title('New Cases Per Capita in New York During the Mask Mandate')
plt.show()

answer = ztest(ga_data[1], ny_data[1], value=0)
print (answer)