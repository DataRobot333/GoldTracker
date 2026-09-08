import requests
import csv
from pathlib import Path

API_URL = "https://webservice.tgnsrv.ir/Pr/Get/arianjewels8797/a09302718797a"

CSV_FILE = Path("data/gold_price.csv")

CSV_FILE.parent.mkdir(exist_ok=True)

if not CSV_FILE.exists():
	with open(CSV_FILE, 'w', newline="") as file:
		writer = csv.writer(file)
		writer.writerow(["timestamp","iran_gold_18k", "USD", "EUR", "AED", "gold_ounce"])

try:
	response = requests.get(API_URL)
	data = response.json()
	row = [ data['TimeRead'],
		data['YekGram18'],
		data['Dollar'],
		data['Euro'],
		data['Derham'],
		data['OunceTala']
		]
	with open(CSV_FILE, "a", newline="") as file:
		writer = csv.writer(file)
		writer.writerow(row)
	print("saved:", row)

except Exception as e:
	print("error:", e)
"""

    print('Successful request')
    print('Data:', data)
else:
    print('Error in the request, details:', response.text)

globalprice = (((data['Dollar'] * data['OunceTala']) / 31.103) * 750)/999
iranprice = data['YekGram18']
pricebuble = ((iranprice - globalprice )/ globalprice) * 100
print("price bubble for gold is " + str(pricebuble))

derham_to_dollar = data['Derham'] * 3.6725
print("derham exchange to dollor: " + str(derham_to_dollar))
print("dollar price: " + str(data['Dollar']))

print("derham/dollar diff percentage: " + str(((data['Dollar']-derham_to_dollar)/ derham_to_dollar) * 100))
"""
