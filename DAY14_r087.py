a = int(input())
b = int(input())
c = int(input())
x = int(input())
a_count = 0
b_count = 0
c_count = 0
while x % 500 >= 500 and a!= 0:
    a_count += 1
    a -= 1
while x % 100 >= 100 and b!= 0:
    b_count += 1
    b -= 1
while x % 50 >= 50 and c!= 0:
    c_count += 1
    c -= 1
print(a_count + b_count + c_count)

