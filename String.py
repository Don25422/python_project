text = "Hello world"
language = "Python"
greeting = "Hello"
name = "Don"
space = " "

print(text)
print(language)

# accessing an element in a string
print(text[0])
print(text[1])

# size of a string
print(len(text))

# modifying a string
print(text.upper())
print(language.lower())

# string concatenation- Joining strings
print(greeting + name)
print(greeting +" "+ name)
print(f"{greeting} {name}")
print(" ".join([greeting, name]))
print(greeting +space+ name)