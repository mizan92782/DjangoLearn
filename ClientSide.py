import json
import requests


def GET():
  
  #! 1. hit api url to get data,this url provides data
  URL="http://127.0.0.1:8000/students/"

  #! 2. get response : data
  response = requests.get(url=URL)



  #! 3. extract data from response
  data=response.json()  # indent for pretty printing)

  #! 4. show and print data
  print(data)




#!  client side

def POST():
  
  
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


  
  
  
  
def PUT():
  
  
  # data put to this link
  URL='http://127.0.0.1:8000/students/create'


  data={
    'id': 2,
    'age'  : 20,
    
  }

  headers = {'Content-Type': 'application/json'}
  data_json = json.dumps(data)

  res = requests.put(url=URL, data=data_json, headers=headers)
  
  data=res.json()
  print(data)



#! delete data from thired party api

def DELETE():
  
  URL='http://127.0.0.1:8000/students/create'
  
  data={'id': 2}
  
  json_data=json.dumps(data)
  headers = {'Content-Type': 'application/json'}
  
  res =requests.delete(url=URL, data=json_data, headers=headers)
  
  
  
PUT()

GET()

print("========================================")


DELETE()
print("========================================")
GET()
