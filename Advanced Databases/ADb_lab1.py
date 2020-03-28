#Jakub Jachowicz
#Lab1

#EXERCISE1

import math

k = 1240*math.sqrt(7)
m = 4467
l = 2j
d = k + m
c = d + l


#EXERCISE2

print(d)
print('%.3f' % d)
print('%.20f' % d)


#EXERCISE3

r = 17
h = 33
S = 2*math.pi*r*(r+h)


#EXERCISE4
"""
Multiline comment
"""

#line comment


#EXERCISE5

x1 = 7
t = 13
B = (x1+r)/(r*math.sin(2*x1)+3.3456)*x1**(t*r)

print('\nB equals %d\n' % B)


#EXERCISE6

import numpy as np

a = math.sqrt(2)
M = np.array([[a, 1, -a],[0, 1, 1], [-a, a, 1]])

Minv = np.linalg.inv(M)
Mdet = np.linalg.det(M)
Mt = M.T


#EXERCISE6.2

print('M(1,1) = %f' % M[0,0])
print('M(3,3) = %f' % M[2,2])
print('M(3,2) = %f' % M[2,1])

w1 = M[:,2]
w2 = M[1,:]


#EXERCISE7

root_vector = np.roots([1,-7,-3,-43,-28,-60])

print('\nRoots are %s\n' % root_vector)


#EXERCISE8

string_ar = np.arange(3.5,7.5,2)
string_lin= np.linspace(3.5,7.5,2)

print('Vector created using arrange: %s' % string_ar)
print('Vector created using linspace: %s' % string_lin)


#EXERCISE9

def fun1(x):
    return x**3-3*x

import matplotlib.pyplot as plt

#Chart 1
x = np.linspace(-1,1)
y = fun1(x)
plt.plot(x,y)
plt.xlim(-1,1)
plt.title('Chart 1')
plt.legend(['Result'])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle = '-')
plt.show()

#Chart 2
x = np.linspace(-5,5)
y = fun1(x)
plt.plot(x,y)
plt.xlim(-5,5)
plt.title('Chart 2')
plt.legend(['Result'])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle = '-')
plt.show()

#Chart 3
x = np.linspace(0,5)
y = fun1(x)
plt.plot(x,y)
plt.xlim(0,5)
plt.title('Chart 3')
plt.legend(['Result'])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle = '-')
plt.show()


#EXERCISE10

def Q(m,v):
    return m*v**2/2

def Q_cal(m,v):
    return m*v**2/2*4.1855

m = 2.5                 #[kg]
v = 60*1000/3600        #[m/s]

print('The amount of heat is %.2f Joules, which is %.2f calories\n' % (Q(m,v),Q_cal(m,v)))

m = 3                   #[kg]

v = np.linspace(0,200)  #[km/h]
v = v*1000/3600         #scale to [m/s]

fig = plt.figure()
plt.plot(v,Q(m,v),v,Q_cal(m,v))
plt.xlim((0,56))
plt.title('Dependence of heat on velocity')
plt.legend(['Joules','calories'])
plt.xlabel('Velocity [m/s]')
plt.ylabel('Heat')
plt.grid(linestyle = '-')

fig = plt.figure()
plt.semilogy(v,Q(m,v),v,Q_cal(m,v))
plt.xlim((0,56))
plt.title('Dependence of heat on velocity')
plt.legend(['Joules','calories'])
plt.xlabel('Velocity [m/s]')
plt.ylabel('Heat')
plt.grid(linestyle = '-')

#EXERCISE11

class Quaternion:
    
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __str__(self):
        return '{0} + {1}i + {2}j + {3}k'.format(self.a, self.b, self.c,self.d)
    
    def __add__(self, q):
        return Quaternion(self.a + q.a, self.b + q.b, self.c + q.c, self.d + q.d)
    
    def __sub__(self, q):
        return Quaternion(self.a - q.a, self.b - q.b, self.c - q.c, self.d - q.d)

    def __mul__(self, q):
        return Quaternion(self.a*q.a - self.b*q.b - self.c*q.c - self.d*q.d, self.a*q.b + self.b*q.a + self.c*q.d - self.d*q.c, self.a*q.c - self.b*q.d + self.c*q.a + self.d*q.b, self.a*q.d + self.b*q.c - self.c*q.b + self.d*q.a)
    
    def conj(self):
        return Quaternion(self.a/(self.a**2+self.b**2+self.c**2+self.d**2),(-self.b)/(self.a**2+self.b**2+self.c**2+self.d**2),(-self.c)/(self.a**2+self.b**2+self.c**2+self.d**2),(-self.d)/(self.a**2+self.b**2+self.c**2+self.d**2))
    
    def __truediv__(self, q):
        return self*q.conj()
    
    def normalise(self):
        n = math.sqrt(self.a*self.a + self.b*self.b + self.c*self.c + self.d*self.d)
        self = Quaternion(self.a/n,self.b/n,self.c/n,self.d/n)
        return self
    
Qex1 = Quaternion(5,1,-2,3)
Qex2 = Quaternion(5,1,2,3)
print('Quaternions:\n%s\n%s\n' % (Qex1,Qex2))
print('Result of addition:\n%s\n' % (Qex1-Qex2))
print('Result of multiplication:\n%s\n' % (Qex1*Qex2))
print('Result of division:\n%s\n' % (Qex1/Qex2))
print('Result of conjugation:\n%s\n' % Qex1.conj())
print('Result of normalisation:\n%s\n' % Qex1.normalise())