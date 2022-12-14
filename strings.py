# strings: ordered, immutable, text representation

my_string = "Hello World"
my_job = 'I\'m a developer'
hello = """Hello \
World""" # multiline string \ to continue in the next line
print(hello)

# reverse a string using slicing
reversed = my_string[::-1]
print(reversed)

# counts how many times a character appears in a string
print(my_string.count("l"))

# string to list split by space
my_list = my_string.split(" ")

# list to string. This is faster than using a for loop and concatenating the string
my_string = "-".join(my_list)
print(my_string)

#