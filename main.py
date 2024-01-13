 # Hello World Program
#print("Hello World");
# Variables
age = 18      # age is of type int
name = "John" # name is now of type str

# Data Types
#  * str => text
x = "Hello World" #str
#  * int, float, complex => numeric
x = 20 # int
x = 20.5 # float
x = 1j #complex
#  * list, tuple, range => sequence
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry") #tuple
x = range(6) #range
#  * dict => mapping
x = {"name" : "John", "age" : 36} #dict
#  * set, frozenset => set
x = {"apple", "banana", "cherry"} #set
x = frozenset({"apple,", "banana", "cherry"}) #frozenset
#  * bool +> boolean
x = True # bool True/False 
#  * bytes, bytearray, memoryview => binary
x = b"Hello" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview
#  * None => NoneType
x = None # none

# Specific Data Types
x = str("Hello World") #str
x = int(6) #int
x = float(20.5) #float
x = complex(20j) #complex
x = list(("apple", "banana", "cherry")) #list
x = tuple(("apple", "banana", "cherry")) #tuple
x = range(6) #range
x = dict(name="John", age=36) #dict
x = set(("apple", "banana", "cherry")) #set
x = frozenset(("apple", "banana", "cherry")) #frozenset
# * If bool() is 0 it returns false else it returns true for all the integers 
x = bool(1) #bool
x = bytes(5) #byte
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview

#Numericals - int, float, complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Int - Integer, is a whole number, positive or negative, without decimals, of unlimited length.

#Float - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Float can also be scientific numbers with an "e" to indicate the power of 10.

#Complex - Complex numbers are written with a "j" as the imaginary part:


## Casting
int() #Cast to int(Integer)
float() #Cast to Float
str() #Cast to String
int(1.7) #1
float(23) #23.0
str(13.5) #"13.5"