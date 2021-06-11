# week3
Automation
Learn about Python requests module. Implement a program that prints details of a place based on the pincode and country code entered.

Requests Tutorial: https://realpython.com/python-requests/

Use this API: https://api.zippopotam.us/

Documentation: https://docs.zippopotam.us/docs/getting-started/

Example:

INPUT:

Enter country code: IN
Enter pincode: 683501
OUTPUT:

Country: India
Place Name: Udyogamandal
State: Kerala
Explanation:

User inputs in and 683501. The program uses requests module to make a request to https://api.zippopotam.us/in/683501. The result is parsed into JSON and output is to be printed.

URL Format: https://api.zippopotam.us/\<COUNTRY-CODE>/<PINCODE>
