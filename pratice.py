ls_10 = list()
seed = int(input('Enter the seed value'))
m = int(input('Enter the max value'))
a = int(input('Enter the odd integer is not factor of m  '))
c = int(input('Enter the value which is not common factors with m'))


for n in range(5):
    seed = (seed * a + c ) % m
    ls_10.append(seed)

print(ls_10)

def find_max(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return  max(ls[0], find_max(ls[1:]))


print(find_max(ls_10))