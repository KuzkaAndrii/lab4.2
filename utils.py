def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
def  is_p(n):
    if (fact(n-1)+1)%n==0:
        return "YES"
    return "No"
if name=="__main__":
    print("Hello, world!")
