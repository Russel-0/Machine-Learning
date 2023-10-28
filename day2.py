import time

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

#     if len(name) == 0:
#         print("please enter name")
#         name = ""
#     elif len(name) < 3:
#         print("your name is too short")
#         name = ""
#     else:
#         print("Hello " + name)

# for i in range(10):
#     print(i+1)
    
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(0.5)

# while True:
#     name = input("Enter your name:")
#     if name != "":
#         break

data = "R.u.s.s.e.l"

for i in data:
    if i == ".":
        continue
    print(i, end="")
