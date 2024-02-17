def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
def is_p(n):
    if (fact(n-1)+1)%n==0:
        return "YES"
    return "No"
def isf(n):
    while n%5==0:
        n=n/5
    if n<=1:
        return "YES"
    else:
        return "NO"
if name=="__main__":
    print("Hello, world!")
