#mapping a translator
eng2spa = {"one":"uno", "two":"dos", "three":"tres"}
#one = key, uno = value

print(eng2spa["one"])

person = {"Name":"Brian", "Age":"32", "Career":"developer"}
person["Career"] = "Python Programmer"
#updating dictionary

print(person["Name"])
print(person["Career"])

del person["Name"]
#delete specific entry
del person
#will delete entire dictionary