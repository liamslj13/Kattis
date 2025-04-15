map = {'a' : "@", 'b' : "8", 'c' : "(", 'd' : "|)", 'e' : "3",
       'f' : "#", 'g' : "6", 'h' : "[-]", 'i' : "|", 'j' : "_|",
       'k' : "|<", 'l' : "1", 'm' : "[]\\/[]", 'n' : "[]\\[]", 'o' : "0",
       'p' : "|D", 'q' : "(,)", 'r' : "|Z", 's' : "$", 't' : "\'][\'",
       'u' : "|_|", 'v' : "\\/", 'w' : "\\/\\/", 'x' : "}{", 'y' : "`/", 'z' : "2",
}


userin = input()
build = ""


for char in userin:
    if char.isalpha():
        build += map[char.lower()]
    else:
        build += char
        
print(build)