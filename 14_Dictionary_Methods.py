marks = {
    "Chayan": 100,
    "JNR": 49,
    "Roni": 30,
    0: "Chayan"
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Chayan":99 ,"Prio":100})  # It is mutable that is why it's change
print(marks.items())

print(marks.get("JNR"))
# print(marks["jnr"])   This is show error that is why we can use get function
print(marks["JNR"])