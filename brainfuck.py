memsize = 30000
cellsize = 255
halp = """  p to enter the code
  i to change the input
  s to customize memory size and cell size
   (30000 and 255 by default)
  q to exit application
  e to execute the code
              """
import sys
while(True):
    userchoice = input("Action: ")
    
    if(userchoice == "h"):
        print(" Help:")
        print(halp)
              
    elif(userchoice == "p"):
        print(" Program:")
        code = list(input("  Code: "))
        inpt = input("  Input: ").split()
        
    elif(userchoice == "i"):
        print(" Input:")
        inpt = input("  Input: ").split()
              
    elif(userchoice == "s"):
        print(" Customize settings:")
        memsize = int(input("  Memory size: "))
        cellsize = int(input("  Cell size: "))
        
    elif(userchoice == "q"):
        print(" exit:")
        if(input("  Enter to confirm exit") == ""):
            sys.exit()
        else: print("  Exit aborted.")
        
    elif(userchoice == "d"):
        print(" Dump:")
        print("  input pointer:", inptptr)
        print("  memory pointer:", memptr)
        print("  instructions:", instrctr)
        print("  memory:", mem)
        
    elif(userchoice == "e"):
        print(" Executing:")
        
        memptr = 0
        codeptr = 0
        inptptr = 0
        loopctr = 0
        instrctr = 0
        mem = []
    
        #detect unmatched square brackets
        while(codeptr < len(code)):
            if(code[codeptr] == "["):
                loopctr += 1
            elif(code[codeptr] == "]"):
                loopctr -= 1
            codeptr += 1
        codeptr = 0

        if(loopctr > 0):
            print("  error: unmatched '['")
        elif(loopctr < 0):
            print("  error: unmatched ']'")
    
        #create the memory cells
        while(memsize > 0):
            mem.append(int(0))
            memsize -= 1
        memsize = len(mem)

        print("  Output:")
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

            else: instrctr -= 1
            instrctr += 1
            codeptr += 1

        print("  Execution completed.")
    else: print(" Invalid command! Type 'h' to view the help menu.")

    
        
        
              
