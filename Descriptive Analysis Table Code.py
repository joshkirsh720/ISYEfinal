import csv
import statistics
import numpy
from prettytable import PrettyTable

file = open('CovidCases.csv')
csvreader = csv.reader(file)


data_by_states = {}
for row in csvreader:
	if row[1] in data_by_states.keys() and int(row[5]) >= 0:
		data_by_states[row[1]].append(int(row[5]))
		#if (row[2] != '0'):
			#data_by_states[row[1]].append(row[2])
	else:
		data_by_states[row[1]] = []



data_Arizona = data_by_states['AZ']
data_Florida = data_by_states['FL']
data_Georgia = data_by_states['GA']
data_SouthCarolina = data_by_states['SC']
data_SouthDakota = data_by_states['SD']

data_NewYork = data_by_states['NY']
data_Massachusetts = data_by_states['MA']
data_Pennsylvania = data_by_states['PA']
data_Ohio = data_by_states['OH']
data_Utah = data_by_states['UT']

innerTLeft = PrettyTable()
innerTRight = PrettyTable()


innerTLeft.field_names = ["State", "Mean", "St Dev", "Min", "Max"]
innerTRight.field_names = ["State", "Mean", "St Dev", "Min", "Max"]


innerTLeft.title = 'State without mask mandate new cases per capita'
innerTLeft.add_row(['AZ', statistics.mean(data_Arizona) /7151502, statistics.stdev(data_Arizona)/7151502, min(data_Arizona)/7151502, max(data_Arizona)/7151502])
innerTLeft.add_row(['FL', statistics.mean(data_Florida) / 21538187, statistics.stdev(data_Florida)/ 21538187, min(data_Florida)/ 21538187, max(data_Florida)/ 21538187])
innerTLeft.add_row(['GA', statistics.mean(data_Georgia) /10711908, statistics.stdev(data_Georgia)/10711908, min(data_Georgia)/10711908, max(data_Georgia)/10711908])
innerTLeft.add_row(['SC', statistics.mean(data_SouthCarolina)/5118425, statistics.stdev(data_SouthCarolina)/5118425, min(data_SouthCarolina)/5118425, max(data_SouthCarolina)/5118425])
innerTLeft.add_row(['SD', statistics.mean(data_SouthDakota)/886667, statistics.stdev(data_SouthDakota)/886667, min(data_SouthDakota)/886667, max(data_SouthDakota)/886667])


innerTRight.title = 'State with mask mandate new cases per capita'
innerTRight.add_row(['NY', statistics.mean(data_NewYork) / 8177025, statistics.stdev(data_NewYork) / 8177025, min(data_NewYork) / 8177025, max(data_NewYork)/ 8177025])
innerTRight.add_row(['MA', statistics.mean(data_Massachusetts) / 7029917, statistics.stdev(data_Massachusetts) / 7029917, min(data_Massachusetts) / 7029917, max(data_Massachusetts) / 7029917])
innerTRight.add_row(['PA', statistics.mean(data_Pennsylvania) / 13002700, statistics.stdev(data_Pennsylvania)/ 13002700, min(data_Pennsylvania)/ 13002700, max(data_Pennsylvania)/ 13002700])
innerTRight.add_row(['OH', statistics.mean(data_Ohio) / 11799448, statistics.stdev(data_Ohio)/ 11799448, min(data_Ohio)/ 11799448, max(data_Ohio)/ 11799448])
innerTRight.add_row(['UT', statistics.mean(data_Utah) /3271616, statistics.stdev(data_Utah)/3271616, min(data_Utah)/3271616, max(data_Utah)/3271616])



output = PrettyTable()
output.field_names = ['State without mask mandate', 'State with mask mandate']
output.add_row([innerTLeft, innerTRight])


final = PrettyTable()
final.field_names = ['New Cases Per Day Per Capita']
final.add_row([output])

print (innerTLeft)
print ("")
print (innerTRight)