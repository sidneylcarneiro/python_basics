import numpy as np

arr = np.random.randint(1, 99, 10)

print(arr)
print(max(arr))
print(sum(arr)/len(arr))
print(sum(arr))

print("Os primeiros 5 elementos")
print(arr[0:5])
print("Os últimos 3 elementos")
print(arr[7:])
arr1 = []
for x in arr:
    if x % 2 == 0:
        arr1.append(x)
print("Todos os elementos em posições pares")
arr1 = ", ".join(str(num) for num in arr1)
print(arr1)

print("Multiplique todos os elementos por 2")
print(arr * 2)

print("Substitua os três primeiros elementos por zero")
arr[0] = arr[1] = arr[2] = 0
print(arr)

