# STRING REVERSE
txt = "Hello World"[::-1]
print(txt)

# MULTI LINE STRING
a = """Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])

# Slicing
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[-5:-2])

#String Length
a = "Hello, World!"
print(len(a))

# strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))  # returns "Jello, World!"

# split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# 'in' method of string: to check if a sub-string is present in a string or not >>RETURNS TRUE OR FALSE
txt = "The rain in Spain stays mainly in the plain"#Check if the phrase "ain" is present in the following text
x = "ain" in txt
print(x)    # returns "TRUE"

# 'not in' method of string: to check if a sub-string is not present in a string or not >>RETURNS TRUE OR FALSE
txt = "The rain in Spain stays mainly in the plain" #Check if the phrase "ain" is NOT present in the following text
x = "ain" not in txt
print(x)    # returns "FALSE"


#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)    # returns "HelloWorld!"

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)    # returns "Hello World!"


#String Format: 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # returns "My name is John, and I am 36"

#Use the format() method to insert numbers into strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)   # returns "My name is John, and I am 36"

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#Escape Character
      
#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# Other escape characters used in Python:
"""
Code	Result
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""


      
#String Methods
      
#Python has a set of built-in methods that you can use on strings.

#Note: All string methods returns new values. They do not change the original string.
"""

METHOD	        DESCRPTION

capitalize()	Converts the first character to upper case

casefold()	Converts string into lower case

center()	Returns a centered string

count()	        Returns the number of times a specified value occurs in a string

encode()	Returns an encoded version of the string

endswith()	Returns true if the string ends with the specified value

expandtabs()	Sets the tab size of the string

find()	        Searches the string for a specified value and returns the position of where it was found

format()	Formats specified values in a string

format_map()	Formats specified values in a string

index()	        Searches the string for a specified value and returns the position of where it was found

isalnum()	Returns True if all characters in the string are alphanumeric

isalpha()	Returns True if all characters in the string are in the alphabet

isdecimal()	Returns True if all characters in the string are decimals

isdigit()	Returns True if all characters in the string are digits

isidentifier()	Returns True if the string is an identifier

islower()	Returns True if all characters in the string are lower case

isnumeric()	Returns True if all characters in the string are numeric

isprintable()	Returns True if all characters in the string are printable

isspace()	Returns True if all characters in the string are whitespaces

istitle()	Returns True if the string follows the rules of a title

isupper()	Returns True if all characters in the string are upper case

join()	        Joins the elements of an iterable to the end of the string

ljust()	        Returns a left justified version of the string

lower()	        Converts a string into lower case

lstrip()	Returns a left trim version of the string

maketrans()	Returns a translation table to be used in translations

partition()	Returns a tuple where the string is parted into three parts

replace()	Returns a string where a specified value is replaced with a specified value

rfind()	        Searches the string for a specified value and returns the last position of where it was found

rindex()	Searches the string for a specified value and returns the last position of where it was found

rjust()	        Returns a right justified version of the string

rpartition()	Returns a tuple where the string is parted into three parts

rsplit()	Splits the string at the specified separator, and returns a list

rstrip()	Returns a right trim version of the string

split()	        Splits the string at the specified separator, and returns a list

splitlines()	Splits the string at line breaks and returns a list

startswith()	Returns true if the string starts with the specified value

strip()	        Returns a trimmed version of the string

swapcase()	Swaps cases, lower case becomes upper case and vice versa

title()	        Converts the first character of each word to upper case

translate()	Returns a translated string

upper()	        Converts a string into upper case

zfill()	        Fills the string with a specified number of 0 values at the beginning

"""
      
