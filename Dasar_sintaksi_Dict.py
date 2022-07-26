users = {  # {} artinya dictionery
"id": 1,
  "name":"Leanne Graham",
  "username":"Bret",
  "email":"Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
        }
  }
}

print(users)
print("="*20)
print(users["id"])  #[] adalah elemen dari dictionery, fungsinya untuk mengambil data berdasarkan text kuncinta
print("="*20)
print(users["name"])
print("="*20)
print(users["username"])
print("="*20)
print(users["email"])
print("="*20)
print(users["address"]["street"])
print("="*20)
print(users["address"]["suite"])
print("="*20)
print(users["address"]["city"])
print("="*20)
print(users["address"]["zipcode"])
print("="*20)
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print("="*20)
print("by ATEP SULAEMAN")



