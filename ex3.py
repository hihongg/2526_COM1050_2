#ex3
n = int(input())
a = 0
if n > 0:#lấy n là số dương
    for i in range(1, n + 1):#chạy từ 1 đến n vì lấy số không âm với i là số đầu
        b = n - i#b là số còn lại
        if i <= b:#để tránh phân tích thành cách có thể đổi chỗ 2 số cho nhau
            print(i,"+",b)
            a += 1#đếm số cách phân tích
    print("số cách: ",a)  