import json

employee_data ={
    "people":[
        {
            "id":1,
            "name": "Harshada",
            "email":"abc@gmail.com"
        },
        {
            "id":2,
            "name":"Monalisa",
            "email":"dg@gmail.com"
        }
    ],
    "people_status":[
        {
            "id":1,
            "married":False
        },
        {
            "id":2,
            "married":True
        }
    ]
}
print(employee_data)

data = json.dumps(employee_data)
print(data)