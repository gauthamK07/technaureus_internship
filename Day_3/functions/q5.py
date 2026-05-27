
students=[
    {
        "name":"John",
        "age":23,
        "grade":"A"
    },
    {
        "name":"Jane",
        "age":21,
        "grade":"B"
    },
    {
        "name":"Bob",
        "age":19,
        "grade":"C"
    }
]
students.sort(key=lambda x: x["age"])
print(students)