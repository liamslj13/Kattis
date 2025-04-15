while True:
    nums = input().split()
    count = 0
    
    if nums[0] == "0" and nums[1] == "0":
        break
    
    n1, n2 = list(nums[0].zfill(10)), list(nums[1].zfill(10))
    carry = False
    for i in range(len(n1)-1, -1, -1):
       if int(n1[i]) + int(n2[i]) + carry > 9:
           carry = True
           count += 1
       else:
           carry = False
           
    if count > 1:
        print(f"{count} carry operations.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print("No carry operation.")
        