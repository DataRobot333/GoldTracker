import requests

URL = "https://webservice.tgnsrv.ir/Pr/Get/arianjewels8797/a09302718797a"
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

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
