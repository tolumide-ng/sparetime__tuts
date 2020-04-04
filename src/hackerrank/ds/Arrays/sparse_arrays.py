try:
    n = int(input())
except TypeError as e:
    print(f'Expected an integer {e}')

strings = []

for _ in range(n):
    val = input()
    strings.append(val)

try:
    q = int(input())
except TypeError as e:
    print(f'Expected an integer {e}')

querries = []

for _ in range(q):
    val = input()
    querries.append(val)

result = []

for val in querries:
    result.append(querries.count(val))

print(*result, sep='\n')
