import requests
import json
         
x=input("Enter the country code: ")
y=input("Enter zipcode: ")
response=requests.get("https://api.zippopotam.us/"+x+"/"+y)
z = json.loads(response.text)
print("Country: "+z["country"])
print("Place name :"+z["places"][0]['place name'])
print("State: "+z["places"][0]["state"])
