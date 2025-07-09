import requests


#! 1. hit api url
URL="http://127.0.0.1:8000/students/"

#! 2. get response : data
response = requests.get(url=URL)



#! 3. extract data from response
data=response.json()

#! 4. show and print data
print(data)



