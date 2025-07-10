
def deserialization():
  
  
  # data post to this link
  URL='http://127.0.0.1:8000/students/create'
 
 
  data={
    'name' : 'Rubi',
    'age'  : 8,
    'email' : 'rubi77@gmail.com'
  }
  
  # convert ot json
  data_json=json.dumps(data)
  
  # now ,post this data
  post = requests.post(url=URL, data=data_json)
  
  #print json formet daa to see
  print(data_json)
  