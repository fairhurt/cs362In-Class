def recur_fibo(x):
    if x <= 1:
       return x
    else:
       return(recur_fibo(x-1) + recur_fibo(x-2))

def fact(num):
    factori = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
     print("The factorial of 0 is 1")
    else:
     for i in range(1,num + 1):
       factori = factori*i
     print("The factorial of",num,"is",factori) 
     return factori

terms = 12

def test_fibo():
 for i in range(terms):
     assert recur_fibo(i) == recur_fibo(i)

facto = 12
def test_fact():
    assert fact(facto)== 479001600


