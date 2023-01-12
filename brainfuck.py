#create all variables
if(input("Proceed with default settings? ") == ""):
    print("Using default settings")
    memsize = 30000
    cellsize = 255
else:
    print("Customize:")
    memsize = int(input("Memory size: "))
    cellsize = int(input("Cell size: "))
code = list(input("Code: "))
inpt = input("Input: ").split()
memptr = 0
codeptr = 0
inptptr = 0
loopctr = 0
mem = []

#detect unmatched square brackets
while(codeptr < len(code)):
    if(code[codeptr] == "["):
        loopctr += 1
    elif(code[codeptr] == "]"):
        loopctr -= 1
    codeptr += 1
    
if(loopctr > 0):
    print("error: unmatched '['")
elif(loopctr < 0):
    print("error: unmatched ']'")
    
#create the memory cells
while(memsize > 0):
    mem.append(int(0))
    memsize -= 1
memsize = len(mem)

#interpret the code
while(codeptr < len(code)):

    if(code[codeptr] == "+"):
        mem[memptr] += 1
        if(mem[memptr] > cellsize):
            mem[memptr] = 0

    elif(code[codeptr] == "-"):
        mem[memptr] -= 1
        if(mem[memptr] < 0):
            mem[memptr] = cellsize
          
    elif(code[codeptr] == ">"):
        memptr += 1
        if(memptr > memsize - 1):
            memptr = 0
            
    elif(code[codeptr] == "<"):
        memptr -= 1
        if(memptr < 0):
            memptr = memsize - 1
           
    elif(code[codeptr] == "."):
        print(mem[memptr])
        
    elif(code[codeptr] == ","):
        if (inptptr > len(inpt)):
            mem[memptr] = 0
        else:
            mem[memptr] = int(inpt[inptptr])
            inptptr += 1
            
    elif(code[codeptr] == "["):
        if(mem[memptr] == 0):
            loopctr += 1
            while(loopctr != 0):
                codeptr += 1
                if(code[codeptr] == "["):
                    loopctr += 1
                elif(code[codeptr] == "]"):
                    loopctr -= 1
              
    elif(code[codeptr] == "]"):
        loopctr -= 1
        while(loopctr != 0):
            codeptr -= 1
            if(code[codeptr] == "["):
                loopctr += 1
            elif(code[codeptr] == "]"):
                loopctr -= 1
            codeptr -= 1

    codeptr += 1
