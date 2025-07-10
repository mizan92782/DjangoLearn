import json
import requests


def serialzation():
  
  #! 1. hit api url to get data,this url provides data
  URL="http://127.0.0.1:8000/students/"

  #! 2. get response : data
  response = requests.get(url=URL)



  #! 3. extract data from response
  data=response.json()

  #! 4. show and print data
  print(data)




#!  client side

def deserialization():
  
  
  # data post to this link
  URL='http://127.0.0.1:8000/students/create'
 
 
  data={
    'name' : 'Rubi',
    'age'  : 8,
    'email' : 'rubi77@gmail.com'
  }

  headers = {'Content-Type': 'application/json'}
  data_json = json.dumps(data)

  response = requests.post(url=URL, data=data_json, headers=headers)
  
  print("Sent Data:", data_json)
  print("Server Response:", response.text)


  



deserialization()