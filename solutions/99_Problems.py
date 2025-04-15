def search_up(N: str) -> int:
    if int(N) < 100:
        return 99
    N_int = int(N)
    count = 0
    while str(N_int)[-2:] != '99':
        N_int += 1
        count += 1
        
    return count


def search_down(N: str) -> int:
    if int(N) < 100:
        return 99
    N_int = int(N)
    count = 0
    while str(N_int)[-2:] != '99':
        N_int -= 1
        count += 1
    return count
    
    
    
def solve():
    N = input()
    down = search_down(N)
    up = search_up(N)
    
    
    if int(N) < 100:
        print('99')
    elif down < up:
        print(int(N) - down)
    else:
        print(int(N) + up)
    
solve()