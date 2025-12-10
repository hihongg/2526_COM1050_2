#Ex1:
a = int(input())
b = int(input())
c = int(input())
if (a >0 and b >0 and c >0) and (a + b > c) and (a + c > b) and (b + c > a):#nếu các cạnh là số duong và thỏa mãn bđt tam giác thì:
    if a == b == c:#nếu 3 cạnh bằng nhau
        print("tam giác đều")
    elif a == b or b == c or a == c:#nếu chỉ cần 2 cạnh bất kì bằng nhau
        print("tam giác cân")
    elif (a * a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == a * a + b * b):#thỏa mãn Pitago
        print("tam giác vuông")
    else:#còn lại
        print("tam giác thường")
else:#độ dài ko có số âm hoặc không thỏa mãn bđt tam giác
    print("không phải tam giác")   
