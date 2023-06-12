print('hello wrod')
print(type('ae'))

age = 21

print(type(age))
age = 0.1+0.2
print(age)

first_name = 'Angel eyes'
# [start:stop:step]
print(first_name[0:2])
print(first_name[:3])
print(first_name[1:])
print(first_name[0:6:2])
print(first_name[::3])
print(first_name[::-1])

# index[] or slice()
website = "https://bibooo.cn"
slice = slice(8,-3)
print(type(slice))
print(website[slice])
# if
age1 = int(input("How old are you?:"))
if age1== 100:
    print("old!")
elif age1 >= 18:
    print("you are yangmen")
elif age1 < 0:
    print("wtf")
else:
    print(',,,')
# and or not
# temp = int(input("what is the outsi?:"))
# if temp >= 0 and temp <= 30:
#     print("is good totay")
# elif temp < 0 or temp >30:
#     print("the temperature is bad today!")
temp = int(input("what is the outsi?:"))
if not(temp >= 0 and temp <= 30):
    print("is good totay")
elif temp < 0 or temp >30:
    print("the temperature is bad today!")
# while
# while 1==1:
#     name = print("hello I'm stuck in a l00p!~")
name = ""
# 0 ? ""  why
# while len(name) == 0:
#     name = input("Enter your name:")
# print("hello" + name)
while not name:
    name = input("Enter your name:")
print("hello" + name)
# for
# for i in range(10):
#     print(i)
for i in range(50,100+1,2):
    print(i)
for i in "Angel eyes":
    print(i)
