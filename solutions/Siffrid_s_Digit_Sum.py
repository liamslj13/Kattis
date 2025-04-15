# this is so fucking ass
def min(num: str, sum: int) -> str:
    res = '1' # initialize the numnbenr string
    sum -= 1
    for i in range(len(num)-1):
        res += '0'
    res_list = list(res)
    res_list.reverse()
    k = 0
    while sum != 0:
        if res_list[k] == '1':
            res_list[k] = str(1 + sum)
            sum=0
        elif sum >= 9:
            sum -= 9
            res_list[k] = '9'
        else:
            res_list[k] = str(sum)
            sum = 0
        k += 1
        
    res_list.reverse()    
    return "".join(res_list)
            

def max(num: str, sum: int) -> str:
    res = list("0" * len(num))
    k = 0
    while sum != 0:
        if sum >= 9:
            res[k] = '9'
            sum -= 9
        else:
            res[k] = str(sum)
            sum = 0
        k += 1
            
    return "".join(res)


N = input()
S = 0

for char in N:
    S += int(char)

print(f"{min(N, S)} {max(N, S)}")