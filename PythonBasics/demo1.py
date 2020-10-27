
# if else condition (without proper indentation python will give error
name = "chandrika"
age = 40
# and , or are possible in if else
if name == "chandrik":
    if age < 35:
        print("first name right but not age")
    else:
        print("first name and age are right")
else:
    if age > 35:
        print(name)
        print(age)
    else:
        print("wrong statement")

# for loop
vegbasket = ["potato", 'onion', "radish", "carrot"]
j = 1
for i in vegbasket:
    print(j , i)
    j+=1

s = 0
# range function takes one args also like range(5), then it shows 0 1 2 3 4 i.e. till 5-1
# range function takes two args like range(1,5), then it shows 1 2 3 4 i.e. till 5-1
for k in range(5, 10):  # similar as for k=4; k<10; k++
    s = s+k
    print(k)
print(s)

for k1 in range(1, 12, 3):  # if we want to skip by 3
    print(k1)
print("---------------------------------------------------------------------")
# while loop
m = 10
while m >= 2:
    print(m)
    if m == 7:
        m-=1
        continue
    if m == 4:
        break
    m -= 1

# function define and use
def showname(n):
    print("my name is " + n)

def mathscal(a, b):
    return a*b


showname("chandrika")

#print(mathscal(3, 6))
print("the multiplication of 3 and 6 is ", mathscal(3, 6))
#print("{}{}".format("the multiplication of 3 and 6 is ", mathscal(3, 6)))
