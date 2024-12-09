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


# 9. 進階運算
start = int(input("請輸入起始數字: "))
end = int(input("請輸入結束數字: "))

count = 0
total = 0
for i in range(start, end + 1):
    if i % 7 == 0 or i % 11 == 0:
        print(i)
        total += i
        count += 1

print("總共有", count, "個倍數。")
print("數字總和為:", total)


# 10. 文字反轉
while True:
    num = input("請輸入一個數字 (輸入9999結束): ")
    if num == "9999":
        break
    reversed_num = num[::-1]
    print("反轉數字為:", reversed_num)
    


'''
============================
以下是自己撰寫的實驗性質 跟 GPT優化過的版本
============================
'''
# 1. 數學模組應用 實驗性質 原始版
import math
a = 90*(math.pi/180)
print(math.degrees(90), "、", math.radians(5156.620156177409), "、", math.sin(a))


# 1-1. 數學模組應用 GPT優化版
import math
# 角度與弧度轉換
angle_degrees = 90
angle_radians = angle_degrees * (math.pi / 180)
print(f"{angle_degrees} 度對應的弧度值為: {angle_radians:.5f}")
print(f"弧度 {angle_radians:.5f} 對應的度數為: {math.degrees(angle_radians):.2f}")
# 計算正弦值
sin_value = math.sin(angle_radians)
print(f"角度 {angle_degrees} 度的正弦值為: {sin_value:.5f}")


# 2. 開平方根 實驗性質 原始版
a = int(input("請輸入被除數 :"))
basicN = 2
while True:
    basiclist = list()
    b = a / basicN  # 商
    c = a % basicN  # 餘
    if c == 0:
        print(a, "除以", basicN, "等於", b)
        basiclist.append(basicN)
        
    if c != 0:
        basicN += 1
    else:
        a = b
        
    if b == 1:
        break
    elif b != 1 and c == 0:
        continue
    else:
        continue
    
print("商:", basiclist)


# 2-1. 開平方根 GPT優化版
import math

def calculate_square_root(num):
    if num < 0:
        return "無法計算負數的平方根"
    return math.sqrt(num)

# 輸入數字並計算平方根
num = int(input("請輸入一個數字: "))
result = calculate_square_root(num)

print(f"{num} 的平方根是: {result:.2f}")


# 3. 最簡分數 實驗性質 原始版
def gcd(m, n) :
    if n == 0 :
        return m
    else :
        return gcd(n, m%n)

a, b = input("輸入第一個分數的分子分母 :").split(",")
c, d = input("輸入第二個分數的分子分母 :").split(",")
a, b, c, d = int(a), int(b), int(c), int(d)
x = b * d #分母相乘
m = (x / b) * a  # x 除以分母得到的數再乘分子
k = (x / d) * c  # x 除以分母得到的數再乘分子
# print("分母相乘後的第一個分數 :", int(m), "/", x)
# print("分母相乘後的第二個分數 :", int(k), "/", x)
y = m + k  #分子相加
g = int(y / gcd(y, x))  #分子除以公因數
h = int(x / gcd(y, x))  #分母除以公因數
print(a, "/", b, "+", c, "/", d, "的最簡分數 =", g, "/", h)


# 3. 最簡分數 GPT優化版
import math

def simplify_fraction(m, n):
    # 計算最大公因數
    gcd_value = math.gcd(m, n)
    return m // gcd_value, n // gcd_value  # 返回最簡分數

def main():
    try:
        # 輸入分數
        a, b = map(int, input("輸入第一個分數的分子分母 (以逗號分隔): ").split(","))
        c, d = map(int, input("輸入第二個分數的分子分母 (以逗號分隔): ").split(","))
        
        # 計算分數加法的分子和分母
        denominator = b * d
        numerator = (denominator // b) * a + (denominator // d) * c
        
        # 化簡分數
        simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
        
        print(f"{a}/{b} + {c}/{d} 的最簡分數為: {simplified_numerator}/{simplified_denominator}")
        
    except ValueError:
        print("輸入格式錯誤，請輸入有效的數字。")

if __name__ == "__main__":
    main()


