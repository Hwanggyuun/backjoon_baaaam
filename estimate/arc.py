S = input()
T = input()

def A(a):
   return a + "A"
def B(b):
   b += "B"
   return b[::-1]
def A_(a):
   return a[:-1]
def B_(b):
   b = b[::-1]
   return b[:-1]

long = len(T)-len(S)
answer = 0
def dfs(fS):
    global answer
    if(len(fS)==len(T)):
       if(fS==T):
         print(1)
        
    else:
        if answer == 1:
            return 
        fS=A(fS)
        dfs(fS)
        fS =A_(fS)
        if answer == 1:
            return
        fS=B(fS)
        dfs(fS)
        fS =B_(fS)
dfs(S)
print(0)