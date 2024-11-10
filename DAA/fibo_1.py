iterative_count=0
recursive_count=0

def fibo_iterative(n):
    global iterative_count
    iterative_count+=1
    
    if n<=0:
        return 0
    elif n==1:
        return 1
    
    fib=[0]*(n+1)
    fib[0]=0
    fib[1]=1
    
    for i in range(2,n+1):
        iterative_count+=1
        fib[i]=fib[i-1]+fib[i-2]
        
    return fib[n]


def fibo_recursive(n):
    global recursive_count
    recursive_count+=1
    
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)
    
def fibo_sequence(n):
    if n<=0:
        return []
    
    fibo=[0,1]
    
    for i in range(2,n):
        next_num=fibo[i-1]+fibo[i-2]
        fibo.append(next_num)
        
    return fibo

n=int(input("Enter a number : "))

while(True):
    print("*"*20,"MENU","*"*20)
    print("1.Use Recursive Method\n2.Use Iterative Method\n3.Exit")
    ch=int(input("Enter your choice : "))
    
    if (ch==1):
        fib_recur=fibo_recursive(n)
        fib_seq=fibo_sequence(n)
        print("Fibonacci Number of ",n," is : ",fib_recur)
        print("No. of steps needed are : ",recursive_count)
        print("Fibonacci Sequence for ",n," is : ",fib_seq)
        
    elif (ch==2):
        fib_iter=fibo_iterative(n)
        fib_seq2=fibo_sequence(n)
        print("Fibonacci Number of ",n," is : ",fib_iter)
        print("No. of steps needed are : ",iterative_count)
        print("Fibonacci Sequence for ",n," is : ",fib_seq2)
        
    elif (ch==3):
        print("Exiting Successfully!!")
        break
    
    else:
        print("Wrong Choice\nPlease Try Again!!")
        
        