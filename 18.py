import json

person = {}
person["name"] = "Nishesh Paudel"
person["age"] = 23

print("Person dictionary:", person)

json_string = json.dumps(person)
print("Person dictionary as JSON string:", json_string)

deserialized_person = json.loads(json_string)
print("Deserialized Person dictionary from JSON string:", deserialized_person)