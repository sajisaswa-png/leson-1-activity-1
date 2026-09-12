student_details = {
    "id1":{"name":"sarha", "class":"v", "student intergration": "english,math,science"},
    "id2":{"name":"david", "class":"v", "student intergration": "english,math,science"},
    "1d3":{"name":"sara" , "class":"v", "student intergration": "english,math,science"},

    "1d4":{"name":"surya", "class":"v", "student intergration": "english,math,science"},
}

result = {}
seen_key =[]

for student_id, details in student_details.items():
 
 unique_key = (details["name"], details["class"], details["student intergration"])

 if unique_key not  in seen_key:
   seen_key.append(unique_key)
   result[student_id] = details

for k, v in result.items():
  print(k,":",v)