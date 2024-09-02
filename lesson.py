#2 行 2 列で数値を出力します。
print("0 8")
print("1 3")

#解答コード
print("0 8\n1 3")
#############################

#入力された 9 個の数値を 3 行 3 列の形式で出力します。
n = input().split()
for i in range(len(n)):
    if i % 3 == 0 and i != 0:
        print()
        print(n[i], end=" ")
    elif i % 3 == 2:
        print(n[i], end="")
    else:
        print(n[i], end=" ")
#解答コード
N = input().split()

for i in range(len(N)):
    print(N[i], end="")
    if i % 3 == 2:
        print()
    else:
        print(" ", end="")
###################################
#2 行 N / 2 列で N 個の数値を半分ずつ出力します
n = int(input())
x = int(n / 2)
print(" ".join(str(i) for i in range(1,x+1)))
print(" ".join(str(i) for i in range(x+1,n+1)))
#解答コード
N = int(input())

for i in range(1, N + 1):
    if i % (N // 2) == 0:
        print(i)
    else:
        print(i, end=" ")
######################################
#数値 N と M が与えられるので、 1 行目には N 個、 2 行目には M 個の数値を出力します
n,m = map(int,input().split())
print(" ".join(str(i) for i in range(1,n + 1)))
print(" ".join(str(i) for i in range(1,m + 1)))
#解答コード
values = input().split()
N = int(values[0])
M = int(values[1])

for i in range(1, N + 1):
    if i == N:
        print(i)
    else:
        print(i, end=" ")

for i in range(1, M + 1):
    if i == M:
        print(i)
    else:
        print(i, end=" ")
###############################################
#自然数 N と N 個の要素の数列 M が与えられます。1 ≦ i ≦ N の各 i について、i 行目には以下の数列を出力してください。
#* 1 以上 M_i 以下のすべての自然数を昇順、半角スペース区切りで出力してください。
n = int(input())
m = map(int,input().split())
for i in m:
    for j in range(1, i + 1):
        if j == i:
            print(j)
        else:
            print(j, end=" ")
#解答コード
N = int(input())

M = [0] * N
values = input().split()
for i in range(N):
    M[i] = int(values[i])

for i in range(N):
    for j in range(1, M[i] + 1):
        if j == M[i]:
            print(j)
        else:
            print(j, end=" ")
###################################
#自然数 N, M と N 個の自然数からなる数列 A と M 個の自然数からなる数列 B が与えられます。
#数列 A の値を B_1 個、B_2個、... B_M 個で分割し、それぞれの数列を改行区切りで出力してください。
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

current_index = 0

for i in b:
    print(" ".join(map(str, a[current_index:current_index + i])))
    
    current_index += i
#解答コード
values = input().split()
N = int(values[0])
M = int(values[1])

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

B = [0] * M
values = input().split()
for i in range(M):
    B[i] = int(values[i])

head = 0
for i in B:
    for j in range(i):
        if j == i - 1:
            print(A[head])
        else:
            print(A[head], end=" ")

        head += 1
#####################################
#1 行目に整数 N が与えられます。
#2 行目以降に、N 組の整数 a_i と b_i が N 行で与えられます。(1 ≦ i ≦ N)
#8 組目の a_i と b_i を出力してください。
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if i == 7:
        print(a,b)
#解答コード
N = int(input())
a = []
b = []
for i in range(N):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

print(a[7], b[7])
#########################################
#3 行 3 列の行列が与えられます。上から i 番目、左から j 番目の整数は a_{i,j} です。
#3 行 3 列の行列をそのまま出力してください。
for i in range(3):
    numbers = input()
    print(numbers)
#解答コード
a = []
for i in range(3):
    a_i = list(map(int, input().split()))
    a.append(a_i)

for i in range(3):
    print(*a[i])
#########################################
#要素数 N の数列 A と数値 M が与えられます。A の M 番目の値を出力してください。
n,m = map(int,input().split())
a = list(map(int,input().split()))
print(a[m-1])
#解答コード
N, M = map(int, input().split())
A = [int(x) for x in input().split()]

print(A[M-1])
############################################
#縦 H マス、横 W マスの H × W マスからなる迷路 S があります。
#上から i 行目、左から j 列目のマス は S_ij とあらわされ、 S_ij が「#」のとき壁であり、
#「.」のとき道です。整数 r、c が与えられるので、S_rc が壁かどうか判定してください。
#S_rc が壁なら「Yes」を、壁ではないなら「No」と出力してください。
H,W,r,c = map(int,input().split())
a = []
for i in range(H):
    row = list(input())#list()不要
    a.append(row)
if a[r-1][c-1] == "#":
    print("Yes")
else:
    print("No")
#解答コード
H, W, r, c = map(int, input().split())
maze = [input() for _ in range(H)]

if maze[r-1][c-1] == "#":
    print("Yes")
else:
    print("No")
###########################################
#0 以上 9 以下の整数が N 個与えられます。各数値の出現回数を求め、
#「0」の出現回数、「1」の出現回数、...「9」の出現回数、をこの順に半角スペース区切りで1行に出力してください。
n = int(input())
numbers = map(int,input().split())
a = [0] * 10
for i in numbers:
    a[i] += 1
print(*a)
#解答コード
N = int(input())
A = [int(x) for x in input().split()]

count = [0] * 10
for num in A:
    count[num] += 1

print(" ".join(map(str, count)))
###########################################################
#文字列が N 個与えられます。各文字列の出現回数を文字列の辞書順に出力してください。
n = int(input())
a = []
for i in range(n):
    word = input()
    a.append(word)
unique_a = sorted(set(a))
for i in unique_a:
    count = a.count(i)
    print(i,count)
#解答コード
N = int(input())
count = {}

for _ in range(N):
    s = input()
    if s not in count:
        count[s] = 1
    else:
        count[s] += 1

for word, times in sorted(count.items()):
    print(word, times)
###########################################
#N 個の文字列 S_1, ... , S_N と、Q 個の文字列 T_1, ... , T_Q が与えられます。各 T_i について、以下の処理を行ってください。
#・ S_j == T_i を満たす最小の j を出力する。ただし、そのような j が存在しない場合は -1 を出力する。
N,Q = map(int,input().split())
s_list = []
for i in range(N):
    s = input()
    s_list.append(s)
for i in range(Q):
    word = input()
    if word in s_list:
        print(s_list.index(word) + 1)
    else:
        print(-1)
#解答コード
N, Q = map(int, input().split())

S = {}
for i in range(N):
    s = input()
    if s not in S:
        S[s] = i + 1

for _ in range(Q):
    t = input()
    if t in S:
        print(S[t])
    else:
        print(-1)
###########################################
#N 個の要素からなる数列 A が与えられます。数列 A は昇順にソートされています。A の重複した要素を取り除いて昇順に出力してください。
N = int(input())
A = list(map(int,input().split()))
unique_sortA = sorted(set(A))
print(*unique_sortA)
#解答コード
N = int(input())
A = {int(x) for x in input().split()}

print(" ".join(map(str, A)))
############################################
#N 個の要素からなる数列 A が与えられます。2 ≦ i ≦ N の各 i に対して、A_i と同じ値が A_1 から A_{i-1} の間にあるかどうかを判定してください。
N = int(input())
a = list(map(int,input().split()))
index = 1
for i in a[1:N+1]:
    if i in a[0:index]:
        print("Yes")
    else:
        print("No")
    index += 1
#解答コード
N = int(input())
A = [int(x) for x in input().split()]

memo = {A[0]}
for i in range(1, N):
    if A[i] in memo:
        print("Yes")
    else:
        memo.add(A[i])
        print("No")
##########################################
#文字列 S が与えられるので、 S を整数に変換できる場合には "YES" , そうでない場合は "NO" を出力してください。
s = input()
try:
    s = int(s)
    print("YES")
except ValueError:
    print("NO")
#解答コード
s = input()

if s.isdigit():
    print("YES")
else:
    print("NO")
################################
#正しい数式を表す文字列 S が与えられるので、その数式を計算した結果を出力してください。
#ただし、出てくる計算は足し算・引き算のみとし、数式に項として出てくる数字は全て 1 桁の正の数であるものとします。
#例として、1-2, 2+1-7 のような文字列は与えられる可能性がありますが、1+(-2) や -4-2+4, 5+-2 のような文字列は与えられないことが保証されている点に注意してください。
s = input()
result = int(s[0])
index = 1
while index < len(s):
    sign = s[index]
    number = int(s[index + 1])
    if sign == "+":
        result += number
    else:
        result -= number
    index += 2
print(result)
#解答コード
s = input()

ans = 0
add = True
for i in range(len(s)):
    if i % 2 == 0:
        if add:
            ans += int(s[i])
        else:
            ans -= int(s[i])
    else:
        if s[i] == "+":
            add = True
        else:
            add = False

print(ans)