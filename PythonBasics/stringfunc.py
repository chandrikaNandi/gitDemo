#  different string function very necessary for selenium python automation

str = "Chandrika Sengupta Nandi"
str1 = "gupta"
str2 = "  clearspace "

print(str[1])  # h
print(str[0:9])  # Chandrika  extract substring

#  str1 in str means search if str1 is there in str, it gives true or false
print(str1 in str)

splitStr = str.split(" ")  # it separate str in several indexes
print(splitStr)
print(splitStr[1])  # output Sengupta

print("left" + str2.strip() + "check")
print("left" + str2.lstrip() + "check")
print("left" + str2.rstrip() + "check")