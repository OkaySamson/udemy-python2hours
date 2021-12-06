text = "Hello World"

#string slice
print(text[6])

print(text[:6] + "Earth")
text = text[:6] + "earth"
print(text)

print("\t" + text)
#creates tab indentation 

#string range slice 
print(text[0:5])

#triple quotation
desc = """we are making multiple line string
wecwecwecwecwecweccewcewcwecwe
ecwcqwecewcwecwecwecwecwecewee"""

#case sensitivity
print(text.upper())
print(text.lower())

print(text.lstrip())
#type text. then ctrl+space to see string mod options