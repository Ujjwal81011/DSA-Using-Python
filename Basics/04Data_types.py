# mutable datatypes
# list
# dictionary

# immutabel datatypes
# int
# float
# complex
# string
# tuple
# set


# List
l= [10,20,30,40]
print(l,type(l))
l[2]=35
print(l)

# String
s= "this is string"
print(s)
s1='''
hello
welcome to the python world
'''
print(s1)

# Tuple => it contains more than one value
t = (5, "python", 1+3)
print(t)

# Dictionary
d = {
    1: "value",
    2: "key",
    3: "pair"
}
print(d)

# Set => it remove duplicate element automatically
s = {2,3,4,5,3}
print(s,type(s))