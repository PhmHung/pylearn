s1 = set([1,1,2,3,4,5,5])
print(s1)

print("--IGNORE-- THIS LINE--")

arr = [1,1,2,3,4,5,5]
s2 =  set(arr)
print(s2)

print ("--IGNORE-- THIS LINE--")

str1 = "Hello I am am a a Student in UET"
str2 = " "
s3 = set(str1.split())
for word in str1.split():
    if word in s3:
        str2 += word + " "
        s3.remove(word)

print(str2)