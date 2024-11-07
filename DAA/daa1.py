#fibonacci series

#0 1 1 2 3 5 8 13 21 34....

n=int(input("upto how many numbers do you want to print fibonacci series"))

def non_recursive(n):
    a=0
    b=1
    step_count=0
    arr=[0, 1]
    for i in range(1, n-1):
        fib= a + b
        a=b
        b=fib
        arr.append(fib)
        step_count+=1
    print(arr)
    print(step_count)
    
non_recursive(n)

