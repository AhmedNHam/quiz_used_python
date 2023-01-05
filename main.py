print("q1_what is color of rgb")
print("1_red, green, blue")
print("2_red, gray, blue")
print("3_red, green, black")


q1 = input("enter ans")
x = 1 if q1 == "1" else 0
print("1_next q")
print("2_exit")

val1 = input("enter your choice")

if val1 == "1":
    print("q2_what is the eiffel tower tall")
    print("1_150 meter")
    print("2_300 meter")
    print("3_250 meter")
else:
    print("your score is :", x)
    exit()

q2 = input("enter ans")
x += 1 if q2 == "2" else 0
print("1_next q")
print("2_exit")

val2 = input("enter your choice")
if val2 == "1":
    print("q3_what is the sky color")
    print("1_black")
    print("2_green")
    print("3_blue")
else:
    print("your score is :", x)
    exit()
q3 = input("enter ans")
x += 1 if q3 == "3" else 0
print("1_your score")
print("2_exit")

val3 = input("enter your choice")
if val3 == "1":
    print("Your score is:", x)
    print("thank you for your time")
else:
    print("thank you for your time")
    exit()