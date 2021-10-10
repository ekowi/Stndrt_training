# kali ini kita akan belajar dictionary python, ini seperti RESP API atau JSON


# dict python didefinisikan menggunakan value and key sebagai contoh x {"value" : 1, "key" : 2}

users = {
    "id": "1",
    "name": "sulastri",
    "username": "hidden_knife",
    "email": "sauwa@gams.xyz",
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
print(users["name"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])