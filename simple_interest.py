# Python3 program to find simple interest 
# for given principal amount, time and 
# rate of interest.
p=int(input("enter the value of p:"))
t=int(input("enter the value of t:"))
r=int(input("enter the value of r:"))

def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
si = (p * t * r)/100
      
print('The Simple Interest is', si)
 
      

