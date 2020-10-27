print("hello")  # testing comments
a = 4
print(a)
b = "string testing"
print(b)
c, d, e = "testing", 2.00001, 8
# here concatenation is possible as string is concatenated "+" with string only
print(c+" python", d, e)
# here concatenation is not possible as string is concatenated "+" with other data type, it will give error
# print(c, "float"+d, e)
print("{} {}".format("checking format function :", c))
# checking the variable type
print(type(d))

# data type LIST
listvalue = [2, 4, "chandrika", 3.05, 10]
print(listvalue)  # output [2, 4, 'chandrika', 3.05, 10]
print(listvalue[0])  # output 2 that is indexing starts with 0
print(listvalue[-1])  # output 10 that is last value od list
print(listvalue[1:4])  # output 2nd value to 4th value [4, 'chandrika', 3.05]
listvalue.insert(3, "nandi")
print(listvalue)  # output [2, 4, 'chandrika', 'nandi', 3.05, 10]
listvalue.append("finish")
print(listvalue)  # output [2, 4, 'chandrika', 'nandi', 3.05, 10, 'finish']
listvalue[3]="NANDI"  # update
del listvalue[5]  # delete
print(listvalue)  # output [2, 4, 'chandrika', 'NANDI', 3.05, 'finish']
print(len(listvalue))  # output 6 that is no od data in list
# tuple data type is same as list but it can not be modified once it is assigned
tupleval = (1, 2, "tuple is immutable", 3, 4)
print(tupleval[3])
# Dictionary data type is like key:value pair
# key can be int or str and value is also can be int or str
dictval = {2: 4, 3: "dictionary", "data type": 5, "A": "example"}
print(dictval)
print(dictval[3])  # output dictionary, values are calling by its key, there is no index value
print(dictval["data type"])  # output 5
dicval1 = dictval.copy()
print(dicval1)
del dicval1["A"]
print(dicval1)  # output {2: 4, 3: 'dictionary', 'data type': 5}
# we ca assign an empty dictionary and add values run time
dictionary1 = {}
dictionary1["first name"]  = "Chandrika"
dictionary1["Last name"]  = "Nandi"
dictionary1["Age"]  = 45
print(dictionary1)
# we can also modify dictionary
dictionary1["first name"]  = "ChandrikaSG"
dictionary1["addr"] = "Seawoods"
print(dictionary1)   # output 'first name': 'ChandrikaSG', 'Last name': 'Nandi', 'Age': 45, 'addr': 'Seawoods'





