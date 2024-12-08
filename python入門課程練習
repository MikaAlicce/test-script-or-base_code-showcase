'''
============================
撰寫者：Mika
撰寫日期：2023/02-2023/03
撰寫語言：python
撰寫工具：spyder
主要用途：python基礎入門課程練習
============================
'''

# 1. 正三角形
n = int(input("請輸入數字: "))
for i in range(1, n + 1):
    print("@" * i)


# 2. 等腰三角形
n = int(input("請輸入數字: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "@" * (2 * i - 1))


# 3. 倒三角形
n = int(input("請輸入數字: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "@" * i)


# 4. 數字金字塔
n = int(input("請輸入數字: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1)))


# 5. 數字反轉
while True:
    num = input("請輸入一個數字 (輸入9999結束): ")
    if num == "9999":
        break
    reversed_num = num[::-1]
    print("反轉數字為:", reversed_num)


# 6. 閏年計算
try:
    year = int(input("請輸入西元年: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "是閏年。")
    else:
        print(year, "不是閏年。")
except ValueError:
    print("請輸入正確的年份。")


# 7. 九九乘法表
for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} * {i} = {j * i:<2}", end=" | ")
    print()


# 8. 數學運算
try:
    start = int(input("請輸入起始數字: "))
    end = int(input("請輸入結束數字: "))
    operator = input("請輸入運算符號 (+, -, *, /): ")
    
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            if operator == "+":
                print(f"{i} + {j} = {i + j}")
            elif operator == "-":
                print(f"{i} - {j} = {i - j}")
            elif operator == "*":
                print(f"{i} * {j} = {i * j}")
            elif operator == "/" and j != 0:
                print(f"{i} / {j} = {i / j:.2f}")
            else:
                print("運算錯誤。")
except ValueError:
    print("請輸入正確的數字。")




'''
============================
以下是實驗性質或GPT優化過的
============================
'''
'''數學應用 實驗性質 原本版'''
import math
a = 90*(math.pi/180)
print(math.degrees(90), "、", math.radians(5156.620156177409), "、", math.sin(a))


'''數學模組應用 GPT優化版'''
import math
# 角度與弧度轉換
angle_degrees = 90
angle_radians = angle_degrees * (math.pi / 180)
print(f"{angle_degrees} 度對應的弧度值為: {angle_radians:.5f}")
print(f"弧度 {angle_radians:.5f} 對應的度數為: {math.degrees(angle_radians):.2f}")
# 計算正弦值
sin_value = math.sin(angle_radians)
print(f"角度 {angle_degrees} 度的正弦值為: {sin_value:.5f}")



