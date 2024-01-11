##Strings
"Hello" #Double quotation
'Hello' # single quotation

multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
#print(multiline_string)

#Strings as Arrays
a = "Hello, World!"
#print(a[2])

#Looping Through a String
#Since strings are arrays we can loop through it
for x in "banana":
  x = x #Remove this
  #print(x)

#String Length
# We use len() to get the length of the string
a = "Hello, World!"
#print(len(a))

#Check String - To check if a certain phrase or character is present in a string, we can use the keyword in
#Keyword - in

txt = "How's your day going?"
#print("day" in txt) # True

#Slicing strings- returning a range of characters from the string
b = "Hello, World!"
#Slicing

#print(b[2:5]) # get the characters from 2 to 5
#NOTE: it starts from 0

#Slicing from the start
print(b[:5])

#Slicing to the end
print(b[2:])

#Negative Indexing
print(b[-5:-2]) #from -5 to -2

#TODO: Remove # from all print after the lesson
