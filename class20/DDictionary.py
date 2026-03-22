student_data  = {
    "id1":{
        "name":"Johnny",
        "grade":"6",
        "subjects":["Math","English","Science"]

    },
    "id2":{
        "name":"Zara",
        "grade":"7",
        "subjects":["Math","English","Science"]

    },
    "id3":{
        "name":"Zara",
        "grade":"7",
        "subjects":["Math","English","Science"]

    }
}
print("the original ddictionary")
print(student_data)
special_dict = {}
for key,value  in student_data.items():
    if value not in special_dict.values():
        special_dict[key] = value
print("after removing the duplicates")
print(special_dict)

