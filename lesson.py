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