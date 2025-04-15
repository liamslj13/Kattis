N = int(input())

while N != 0:
    bitstr = ['?'] * 32
    for _ in range(N):
        cmnd = input().strip().split()
        
        if len(cmnd) == 2:
            cmnd[1] = int(cmnd[1])
        else:
            cmnd[1] = int(cmnd[1])
            cmnd[2] = int(cmnd[2])
            
        if cmnd[0] == 'SET':
            bitstr[int(cmnd[1])] = '1'
            
        elif cmnd[0] == 'CLEAR':
            bitstr[int(cmnd[1])] = '0'
            
        elif cmnd[0] == 'AND':
            if bitstr[cmnd[1]] == '1' and bitstr[cmnd[2]] == '1':
                bitstr[cmnd[1]] = '1'
            elif bitstr[cmnd[1]] == '0' or bitstr[cmnd[2]] == '0':
                bitstr[cmnd[1]] = '0'
            else:
                bitstr[cmnd[1]] = '?'
                
        else: # or
            if bitstr[cmnd[1]] == '1' or bitstr[cmnd[2]] == '1':
                bitstr[cmnd[1]] = '1'
            elif bitstr[cmnd[1]] == '?' or bitstr[cmnd[2]] == '?':
                bitstr[cmnd[1]] = '?'
            else:
                bitstr[cmnd[1]] = '0'
    
    string = "".join(bitstr)
    print(string[::-1])
    
    N = int(input())