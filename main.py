

import io

error = False
nexttoken = ''
fullinput = []
flag = 0
fileread = True
start1 = False

def lexical():
    global fullinput
    global flag
    global nexttoken
    global fileread
    #utf-8 encoding for text operations
    if fileread:
        with io.open('grammar.txt', 'r', encoding='utf-8') as file:
            while True:
                c = file.read()
                
                if not c:
                    print('input:', fullinput)
                    break
                fullinput = list(c)    
             
            
            nexttoken = fullinput[flag] 
            print('nexttoken:', nexttoken)
            fileread = False 
            return
    if start1:
      flag = flag + 1 
      nexttoken = fullinput[flag]
      while nexttoken == ' ':
        print('Space detected.Next!') 
        flag = flag + 1
        nexttoken = fullinput[flag]

#['&','*','(','$']
def unconsumedinput():
    for i in range(flag, len(fullinput)):
        print(fullinput[i])

# functions.
def G():
    global start1
    start1 = True

    lexical()
    print("G->E")
    E()
    if nexttoken == '$':
        if not error:
            print("success")
    else:
        print("failure: unconsumed input =")
        unconsumedinput()

def E():
    if error:
        return
    print("E->T R")
    T()
    R()

def R():
    global flag
    if error:
        return
    if nexttoken == '+':
        print("R->+TR")
        lexical()
        T()
        R()
    elif nexttoken == '-':
        print("R->-TR")
        lexical()
        T()
        R()
    else:
        print("R->e")

def T():
    global flag
    if error:
        return
    print("T->F S")
    F()
    S()

def S():
    global flag
    if error:
        return
    if nexttoken == '*':
        print("S-> * F S")
        lexical()
        F()
        S()
    elif nexttoken == '/':
        print("S-> / F S")
        lexical()
        F()
        S()

def F():
    global flag
    global error
    if error:
        return
    if nexttoken == '(':
        print("F->( E")
        lexical()
        E()
        if nexttoken == ')':
            lexical()
        else:
            error = True
            print("error: unexpected token",nexttoken)
            print("unconsumed input:")
            unconsumedinput()
            return

    elif nexttoken == 'a' or 'b' or 'c' or 'd':
        print("F->M")
        M()
    elif nexttoken == '0' or '1' or '2' or '3':
        print("F->N")
        N()
    else:
        error = True
        print("error: unexpected token", nexttoken)
        print("unconsumed input:")
        unconsumedinput()

def M():
    global flag
    global error
    if error:
        return
    if nexttoken == 'a' or 'b' or 'c' or 'd':
        print("M->",nexttoken)
        lexical()
    else:
        error = True
        print("error: unexpected token", nexttoken)
        print("unconsumed_input")
        unconsumedinput()

def N():
    global flag
    global error
    if error:
        return
    if nexttoken == '0' or '1' or '2' or '3':
        print("N->",nexttoken)
        lexical()
    else:
        error = True
        print("error: unexpected token", nexttoken)
        print("unconsumed_input")
        unconsumedinput()

if __name__ == '__main__':
    G()








