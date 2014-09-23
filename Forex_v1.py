import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import xlwt
from tempfile import TemporaryFile

r = requests.get("http://api-sandbox.oanda.com/v1/history?instrument=USD_EUR&count=720&granularity=D")
r.text

q = requests.get("http://api-sandbox.oanda.com/v1/history?instrument=EUR_GBP&count=720&granularity=D")
q.text

p = requests.get("http://api-sandbox.oanda.com/v1/history?instrument=GBP_USD&count=720&granularity=D")
p.text


datar = json.loads(r.text)
dataq = json.loads(q.text)
datap = json.loads(p.text)

USD_EUR = []
EUR_GBP = []
GBP_USD = []
inter = []
Arbitrage = []
i = 0

for item in datar['candles']:
	USD_EUR.append(item['highBid'])

for item in dataq['candles']:
	EUR_GBP.append(item['highBid'])

for item in datap['candles']:
	GBP_USD.append(item['highBid'])


for i in range(0, len(USD_EUR)):
	inter.append(USD_EUR[i]*EUR_GBP[i])

for j in range(0, len(EUR_GBP)):
	Arbitrage.append(inter[j]*GBP_USD[j])


book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

for n in Arbitrage:
	i = i + 1
	sheet1.write(i,0,n)

name = "this.xls"
book.save(name)



#plt.plot(USD_EUR, marker = 'o', linestyle = '--', color = 'r', label='USD Vs SGD')
#plt.plot(EUR_GBP, marker = '*', linestyle = ':', color = 'c', label='USD Vs EUR')
#plt.plot(GBP_USD, marker = '+', linestyle = '-.', color = 'y', label='EUR Vs SGD')

plt.plot(Arbitrage, marker = 'o', linestyle = '--', color = 'r', label = 'Arbitrage')

plt.show()



#print json.dumps(data, indent = 1)

#The command below provides the list of forex pairs available at OANDA
#curl -X GET "http://api-sandbox.oanda.com/v1/instruments?accountId=1"

