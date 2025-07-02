#1
import json
name= input("Enter the name : ")
age=int(input("Enter age : "))
data={"name":name,"age":age}
stringify_json=json.dumps(data)
print("Serialised data of json : ",stringify_json)

#2
name= input("Enter the name : ")
age=int(input("Enter age : "))
user={"name":name,"age":age}
with open("user.json","w") as f:
    json.dump(user,f)
print("Data written to json folder")

with open("user.json","r") as f:
    loaded=json.load(f)
    print("Read from file :  ",loaded)


