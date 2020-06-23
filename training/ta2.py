import numpy as np
import matplotlib.pyplot as plt

"""
Task 1

"""

x=0.5
a=0.5
for i in range(200):
    x2=np.sin(x)-a*x+30
    if abs(x2-x) < 1.e-8:
        x=x2
        break
    else:
        x=x2
else:   # else syftar till om break inte påträffas
    print(f"Did not meet condition in {i} iterations")
print(f"The result after {i} iterations is {x}.")


"""
Task 2

"""

arrx = np.linspace(5, 30)
arry = []
for i in arrx:
    arry.append(np.sin(i)-a*i+30)

plt.plot(arrx, arry, 'b')
plt.plot(arrx, arrx, 'r')
plt.show()

"""
Task 3

"""

n = 1
arrx = []
while True:
    xn=np.sin(n)**2/n
    arrx.append(xn)
    n+=1
    if xn < 1.e-9:
        break
print(f"The list is {len(arrx)} long")


"""
Task 4

"""

arr_a = [-0.5, 0.5, -0.25, 0.25]
for a in arr_a:
    x = 1
    for i in range(0, 10000):
        x2=0.2*x-a*((x**2)-5)
        if abs(x2 - x) < 1.e-9:
            print(f"Sequence converged to x={x2} for a={a} in {i} iterations")
            break
        else:
            x=x2
    else:
        print(f"No convergence detected for a={a}")

"""
Task 5

"""

x = 1
a = 0.5
arrx = [x]
for i in range(0, 1000):
    x2=0.2*x-a*((x**2)-5)
    if abs(x2 - x) < 1.e-9:
        print(f"Sequence converged to x={x2} for a={a} in {i} iterations")
        break
    else:
        x=x2
        arrx.append(x)
else:
    print(f"No convergence detected for a={a}")
    
negx = []
posx = []    
for x in arrx:
    if x >= 0:
        posx.append(x)
    else:
        negx.append(x)
        
        
print(f"Negative values are {negx}")
print(f"Positive values are {posx}")

"""
Task 6

"""
def check_convergence(a, x0=1, cap=30):
    """
    Checks if the series converges in
    30 iterations or less for some
    constant a
    
    Returns
    -------
    boolean
        If a convergence was found
    """
    if x0 == 0:
        raise ValueError("x0 cannot be 0")
    
    x = x0
    pos = []
    neg = []
    
    for i in range(0, cap):
        if x >=0:
            pos.append(x)
        else:
            neg.append(x)
        x2=0.2*x-a*((x**2)-5)
        if abs(x2 - x) < 1.e-9:
            return True, list(pos), list(neg)
        x=x2
    else:
        return False, list(pos), list(neg)
    
print(f"a={0.5} converges: {check_convergence(0.5)}")
print(f"a={-0.5} converges: {check_convergence(-0.5)}")
print(f"a={0.25} converges: {check_convergence(0.25)}")
print(f"a={-0.25} converges: {check_convergence(-0.25)}")
# print(f"a={1} converges: {check_convergence(1)}")







