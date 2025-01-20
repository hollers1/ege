'''alf = '0123456789ABCDEFGHI'
for x in alf:
    y=int('98897'+x+'21',19)+int('2'+x+'923',19)
    if y%18==0:
        print(y//18)
x=3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2025
k=0
s=''
while x!=0:
    if x%25==0:
        k+=1
    x//=25
    print(k,x)
   
def hexd(a):
    return hexd(a) - hexd(a-1)
print(hexd(1))

for n in range(1,1300):
    r=bin(n)[2:]
    if r.count('1')%2==0:
        r='10'+r[2:]+'0'
    else:
        r='11'+r[2:]+'1'
    q=int(r,2)
    if q < 35:        
        print(n, int(r, 2))

for n in range(1,1300):
    r=bin(n)[2:]
    if r.count('1')%2==0:
        r='10'+r[2:]+'0'
    else:
        r='11'+r[2:]+'1'
    q=int(r,2)
    if q >= 13:        
        print(n, int(r, 2))

f=[]
q=0
for n in range(1,1001):
    r=bin(n)[2:]
    if n%2==0:
        r='1'+r+'10'
    else:
        r='11'+r+'0'
    if 800<=int(r,2)<=1500:
        f+=[int(r,2)]
q = set(f)
print(len(q))

for n in range(1000, 3000):
    a=str(n)
    b = [sum(map(int, str(int(a[i])*2))) for i in range(0,4,2)]
    s = sum(b) + sum(int(a[i]) for i in range(1,4,2))
    if s%28==0:
        print(str(n))
        break

for n in range(1,1300):
    r=bin(n)[2:]
    if r.count('1')%2==0:
        r='10'+r[2:]+'0'
    else:
        r='11'+r[2:]+'1'
    q=int(r,2)
    if q >= 16:        
        print(n, int(r, 2)) 

from itertools import *
k=0
alf = '0123456789AB'
for i in product(alf, repeat=5):
    s=''.join(i)
    if s[0]!=0 and s.count('7')==1 and ((s.count('9')+s.count('A')+s.count('B') <=3)):
        k+=1
print(k) 
from itertools import *
alf='012345678'
k=0
for i in product(alf, repeat=12):
    s=''.join(i)
    if (s[1]>s[0] and sum(map(int, s)) % 2 == 0) or (sum(map(int, s)) % 2 != 0 and s[1]<s[0]):
        k+=1
print(k)

print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0,2):
                if not(((x<=y) <=z) or not(w)):
                    print(x, y, z, w)

for i in range(1,1000):
    n = bin(i)[2:]
    if n.count('1') %2 ==0:
        n = n+'0'
        n = n.replace(n[:2], '10')
    else:
        n = n+'1'
        n= n.replace(n[:2], '11')
    print(i, n,int(n,2))
    if int(n,2) >35:
        break

from itertools import *
alp = '01234567'
k =0
for i in product(alp, repeat=5):
    if i[0] != '0' and int(i[0]) % 2 == 0 and i.count('7') <= 2 and i[-1] != '2' and i[-1] != '6':
        k+=1
print(k)

for x in range(7050+1):
    t = 5**100 - x
    count = 0
    while t!=0:
        if t%5 == 0:
            count += 1
        t = t//5
    if count == 3:
        print(x)
from turtle import *
k=20
speed(1)
tracer(2)
lt(90)
for _ in range(10):
    fd(6*k)
    rt (120)

up()
for x in range(10):
    for y in range(15):
        goto(x*k,y*k)

        dot(5, 'red')

from turtle import *
k=20
speed(1)
tracer(2)
lt(90)
for _ in range(15):
    fd(4*k)
    rt (60)

up()
for x in range(1,10):
    for y in range(1,10):
        goto(x*k,y*k)

        dot(5, 'red')
from turtle import *
k=20
speed(1)
tracer(2)
lt(90)
for _ in range(8):
    fd(12*k)
    rt (90)

up()
for x in range(108):
    for y in range(150):
        goto(x*k,y*k)

        dot(5, 'red')

from turtle import *
k=10
speed(1)
tracer(2)
lt(90)
for _ in range(100):
    fd(10*k)
    rt(30)

up()
for x in range(-10,13):
    for y in range(-15,15):
        goto(x*k,y*k)

        dot(5, 'red')
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not((x or y) <= (z==x)):
                print(x,y,z)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x and not(y)) or (y==z) or w):
                    print(x,y,z, w)
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not((x <= y) and (y <= z)):
                print(x,y,z)

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not((z or y) <= (x==z)):
                print(x,y,z)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x <=z) <=y) or not(w)):
                    print(x,y,z, w)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x  <= y) <= z) or not(w)):
                    print(x,y,z, w)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((z == (not(x))) <= ((w <= (not(y))) and (y <= x))):
                    print(x,y,z, w)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(x<=z) or (y==w) or y):
                    print(x,y,z, w)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((y <= (not(x<=z))) or w):
                    print(x,y,z, w)
for A in range(200):
    f=True
    for x in range(200):
        for y in range(200):
            if not(((y + 3*x) < A) or (x > 20) or (y > 40)):
                f=False
    if f:
        print(A)
        
from itertools import *
alp = '0123456789Abbb'
k=0
for i in product(alp, repeat=5):
    if i[0] != '0' and i.count('9') == 1 and i.count('b') <= 3:
        k+=1
print(k)
from turtle import *
k=10
speed(1)
tracer(2)
lt(90)
for _ in range(2):
    fd(6*k)
    rt(90)
    fd(12*k)
    rt(90)
up()
fd(1*k)
rt(90)
fd(3*k)
lt(90)
down()
for _ in range(2):
    fd(77*k)
    rt(90)
    fd(45*k)
    rt(90)
up()
for x in range(-10,13):
    for y in range(-15,15):
        goto(x*k,y*k)

        dot(5, 'red')
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(x <= z) or (y == w) or y):
                    print(x, y, z, w)
for x in range(2031):
    res = 6**2030 + 6**100 - x
    k = 0
    while res != 0:
        if res % 6 == 0:
            k+=1
        res//=6
    print(k)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(x <= z) or (y == w) or y):
                    print(x, y, z, w)
    
for A in range(0,200):
    f = True
    for x in range(0,200):
        for y in range(0,200):
            if not(((x+y) <= 30) or (y<=(x+2)) or (y>=A)):
                f = False
    if f:
        print(A)

for i in range(1,50):
    n = bin(i)[2:]
    for _ in range(2):
        if n.count('1') %2 == 0:
            n = n+'0'
        else:
            n = n+'1'
    print(i, n,int(n,2))
from itertools import *
alp = '0123456789Abbb'
k=0
for i in product(alp, repeat=5):
    if i[0] != '0' and i.count('9') == 1 and i.count('b') <= 3:
        k+=1
print(k)
print(bin(151)[2:])
print(bin(155)[2:])
#print(int('11111000',2))
from ipaddress import *
for mask in range(33):
    net=ip_network('148.195.140.28/'+ str(mask), 0)
    print(net, net.netmask)

from ipaddress import *
net = ip_network('172.16.168.0/255.255.248.0', 0)
k=0
for add in net:
    if bin(int(add)).count('1') % 5 !=0:
        k+=1
print(k)
from ipaddress import *
mink=10**1000
for mask in range(33):
    net1 = ip_network('144.91.51.39/'+str(mask),0)
    net2 = ip_network('144.91.19.61/'+str(mask),0)
    if net1 == net2:
        if net1.num_addresses<mink:
            mink=net1.num_addresses
            net=net1
k=0
for add in net:
    dv=bin(int(add))[2:].zfill(32)
    if dv.count('1')%2==0:
        k+=1
print(k)
print()
    
print(bin(58)[2:])
print(bin(32)[2:])

from ipaddress import *
for mask in range(33):
    net1 = ip_network('144.91.51.39/'+str(mask),0)
    net2 = ip_network('144.91.19.61/'+str(mask),0)
    if net1 == net2:
        if net1.num_addresses<mink:
            mink=net1.num_addresses
            net=net1
k=0
for add in net:
    dv=bin(int(add))[2:].zfill(32)
    if dv.count('1')%2==0:
        k+=1
print(k)
print()

from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240', 0)
k=0
for add in net:
    if bin(int(add)).count('1') % 2 ==0:
        k+=1
print(k)
print(bin(94)[2:])
print(bin(64)[2:])
print(int('11110',2))
from ipaddress import *
mink=10**1000
for mask in range(33):
    net1 = ip_network('202.3.20.24/'+str(mask),0)
    net2 = ip_network('202.3.27.11/'+str(mask),0)
    if net1 == net2:
        if net1.num_addresses<mink:
            mink=net1.num_addresses
            net=net1
k=0
for add in net:
    dv=bin(int(add))[2:].zfill(32)
    if dv.count('1')%2==0:
        k+=1
print(k)

print(bin(192)[2:])
print(bin(67)[2:])
print(int('1110001000011',2))

a=set()
b={1,12}
c={12,13,14,15,16}
for x in range(100):
    if not((not(x in a)) <= ((not(x in b)) and (not(x in c)))):
        a.add(x)
print(a)

a=set()
b={2,4,9,10,15}
c={3,8,9,10,20}
for x in range(100):
    if not(((not(x in b)) == (x in a)) <= ((x in c) == (x in a))):
        a.add(x)
print(a)

a=set(x for x in range(100))
b = {2,4,6,8,10,12,14,16,18,20}
c = {5,10,15,20,25,30,35,40,45,50}
for x in range(100):
    if not(((x in a) <= (x in b)) and ((x in c) <= (not(x in a)))):
        a.remove(x)
print(a)

k=0
for a in range(100):
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if not((2*x + 5*y + 4*z !=80) or (a<6*x) or (a<y) or (a <3*z)):
                    k+=1
    if k == 0:
        print(a)
    k=0
        

k=0
for a in range(100):
    for x in range(100):
        for y in range(100):
            if not(((x-20<a) and (10-y<a)) or ((x+4)*y >45)):
                k+=1
    if k == 0:
        print(a)
    k=0

k=0
for a in range(1,1000):
    for x in range(1,1000):
        if not((x % a == 0) and (a<10) or (x % 44 !=0) and (x % 99 !=0) and (a<10)):
            k+=1
    if k == 0:
        print(a)
    k=0

k=0
for a in range(100):
    for x in range(100):
        if not((x&13==0) <= ((x&40!=0) <= (x&a!=0))):
            k+=1
    if k == 0:
        print(a)
    k=0

k=0
for a in range(100):
    for x in range(100):
        if not(((x % 2 == 0) <= (x % 3 !=0)) or (x+a>=80)):
            k+=1
    if k == 0:
        print(a)
    k=0

k=0
for a in range(100):
    for x in range(100):
        for y in range(100):
            if not((x+y<=22) or (y<=x-6) or (y>=a)):
                k+=1
    if k == 0:
        print(a)
    k=0

def f(s,m, fl):
    if s>=140: return m%2==0
    if m==0: return 0
    if fl == 0:
        h=[f(s+1,m-1,1), f(s+2,m-1,2), f(s*3,m-1,3)]
    elif fl == 1:
        h=[f(s+1,m-1,2), f(s*3,m-1,3)]
    elif fl == 2:
        h=[f(s+1,m-1,1), f(s*3,m-1,3)]
    elif fl == 3:
        h=[f(s+1,m-1,1), f(s*3,m-1,2)]
    return any (h) if (m-1)%2 == 0 else all(h)

for s in range(1,140):
    if f(s,2,0):
        print('19)',s)
print('20)', [s for s in range(1,140) if not f(s,1,0) and f(s,3,0)])
print('21)', [s for s in range(1,140) if f(s,1,0) and f(s,3,0)] and not(s,1,0))
 ''     
def f(s,m,):
    if s==42: return m%2==0
    if m==0: return 0
    if s<42:
        h=[f(s+1,m-1),]
    return any (h) if (m-1)%2 == 0 else all(h)

for s in range(1,140):
    if f(s,2,0):
        print('19)',s)
print('20)', [s for s in range(1,140) if not f(s,1,0) and f(s,3,0)])
print('21)', [s for s in range(1,140) if f(s,1,0) and f(s,3,0)] and not(s,1,0))

def f(s,m, fl):
    if s>39: return m%2==0
    if m==0: return 0
    if fl == 0:
        h=[f(s+1,m-1,1), f(s+2,m-1,2), f(s*3,m-1,3)]
    elif fl == 1:
        h=[f(s+1,m-1,2), f(s*3,m-1,3)]
    elif fl == 2:
        h=[f(s+1,m-1,1), f(s*3,m-1,3)]
    elif fl == 3:
        h=[f(s+1,m-1,1), f(s*3,m-1,2)]
    return any (h) if (m-1)%2 == 0 else all(h)

for s in range(1,140):
    if f(s,2,0):
        print('19)',s)
print('20)', [s for s in range(1,140) if not f(s,1,0) and f(s,3,0)])
print('21)', [s for s in range(1,140) if f(s,1,0) and f(s,3,0)] and not(s,1,0))

def f(s,m):
    if s>=39: return m%2==0
    if m==0: return 0
    if s<39:
        h=[f(s+1,m-1),f(s+3,m-1), f(s*2,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,40) if not f(s,1) and f(s,2)])
print('20)', [s for s in range(1,40) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,40) if f(s,2) and f(s,4) and not f(s,2)])


def f(s,m):
    if s >= 58: return m%2 ==0
    if m ==0: return 0
    if s < 58:
        h=[f(s+1,m-1), f(s+4,m-1), f(s*2,m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
print('1)', [s for s in range(1,)])
def f(s,m):
    if s>=39: return m%2==0
    if m==0: return 0
    if s<39:
        h=[f(s+1,m-1),f(s+3,m-1), f(s*2,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,40) if not f(s,1) and f(s,2)])
print('20)', [s for s in range(1,40) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,40) if f(s,2) and f(s,4) and not f(s,2)])

def f(s,m):
    if s >= 58: return m%2 ==0
    if m ==0: return 0
    if s < 58:
        h=[f(s+1,m-1), f(s+4,m-1), f(s*2,m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
print('1)', [s for s in range(1,58) if not f(s,1) and f(s,2)])
print('2)', [s for s in range(1,58) if not f(s,1) and f(s,3)])
print('3)', [s for s in range(1,58) if (f(s,2) or f(s,4)) and not f(s,2)])

def f(s,m):
    if s>=39: return m%2==0
    if m==0: return 0
    if s<39:
        h=[f(s+1,m-1),f(s+3,m-1), f(s*2,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,38) if not f(s,1) and f(s,2)])
print('20)', [s for s in range(1,38) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,38) if (f(s,2) or f(s,4)) and not f(s,2)])'''
'''
def f(s,m):
    if s>=62: return m%2==0
    if m==0: return 0
    if s<62:
        h=[f(s+1,m-1),f(s+2,m-1), f(s*3,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,62) if f(s,2)])
print('20)', [s for s in range(1,62) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,62) if not f(s,2) and f(s,4)])




def f(s1,s2,m):
    if (s1+s2) >= 231: return m%2==0
    if m==0: return 0
    h = [f(s1+2,s2,m-1), f(s1*2,s2,m-1), f(s1,s2+2,m-1), f(s1,s2*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

#print('1)', [s2 for s2 in range(1,213) if f(17,s2,2)])
print('2)', [s2 for s2 in range(1,213) if not f(17,s2,1) and f(17,s2,3)])
print('3)', [s2 for s2 in range(1,213) if (f(17,s2,2) or f(17,s2,4)) and not f(17,s2, 2)])


def f(s1,s2,m):
    if (s1+s2) <= 20: return m%2==0
    if m==0: return 0
    h = [f(s1-1,s2,m-1), f((s1+1)//2,s2,m-1), f(s1,s2-1,m-1), f(s1,(s2+1)//2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print('1)', [s2 for s2 in range(11,100) if f(10,s2,2)])
print('2)', [s2 for s2 in range(11,100) if not f(10,s2,1) and f(10,s2,3)])
print('3)', [s2 for s2 in range(11,100) if (f(10,s2,2) or f(10,s2,4)) and not f(10,s2, 2)])

# from itertools import product
# maxx = 0
# p=''
# for i in product('12', repeat=14):
#     if i.count('1') == 10 and i.count('2') == 4:
#         p = ''.join(i)
#         while '11' in p:
#             if '112' in p:
#                 p = p.replace('112','6',1)
#             else:
#                 p = p.replace('11','3',1)
#         c = 0
#         for k in p:
#             c = c + int(k)
#             maxx = max(c, maxx)
# print(maxx)

# count = 1000
# for i in range(1000, 10000):
#     s = str(i)
#     k1 = int(s[0]) + int(s[1])
#     k2 = int(s[1]) + int(s[2])
#     k3 = int(s[2]) + int(s[3])
#     if min(k1,k2,k3) == k1:
#         print(count,k2,k3)
#     elif min(k1,k2,k3) == k2:
#         print(count,k1,k3)
#     elif min(k1,k2,k3) == k3:
#         print(count,k2,k1)
#     count+=1
#
#
#
# for i in range(10000, 1000, -1):
#     s = str(i)
#     k1 = int(s[0]) + int(s[1])
#     k2 = int(s[2]) + int(s[3])
#     first = str(min(k1, k2))
#     second = str((max(k1, k2)))
#     s1 = first + second
#     if s1 == '117':
#         print(i)
#         break

# for i in range(1,1000):
#     n = i
#     if i % 2 == 0:
#         i = bin(i)[2:]+'10'
#     else:
#         i = '1'+bin(i)[2:]+'00'
#     if int(i, 2) > 107:
#         print(n)

# from itertools import product
# count = 0
# for num in product('012345', repeat=3):
#     s = ''.join(num)
#     if s[0] != '0':
#         if s.count('6') == 1:
#             if all(pair not in s for pair in '16 61 36 63 56 65 76 67'.split()):
#                 count += 1
# print(count)

# n = 6*'3'+75*'4'
# while ('35' in n) or ('355' in n) or ('3444' in n):
#     if '35' in n:
#         n = n.replace('35', '4')
#     else:
#         if '355' in n:
#             n = n.replace('355', '4')
#         else:
#             n = n.replace('3444', '3')
#     print(n)
# for i in '123456789ABCDE':
#     res = int('98'+i+'79641',22) + int('25'+i+'49',22) + int('63'+i+'5',22)
#     if res % 21 == 0:
#         res = res//21
#         print(res)
#         break
# from itertools import *
# s = 0
# count = 0
# for i in product('МУЖЧИНА', repeat=6):
#
#     if i.count('Ж') == 1 and i[0] != 'Ч' and i.count('М') < 2 and i.count('У') < 2 and i.count('Ч') < 2 and i.count('И') < 2 and i.count('Н') < 2 and i.count('А') < 2:
#         count += 1
#         if count % 2 == 0:
#             s+=1
# print(s)
# x = open('17 (1).txt')
# a = [int(n) for n in x]
# kmax = 10000000000000000
# smax = -111111111111111
# k = 0
# for i in range(len(a)):
#     if abs(a[i]) % 10 == 6:
#         kmax = min(a[i], kmax)
# print(kmax)
# for i in range(len(a)-1):
#     if (abs(a[i]) % 10 == 6) + (abs(a[i+1]) % 10 == 6) == 1:
#         if (abs(a[i])**2 + abs(a[i+1])**2) < kmax**2:
#             k += 1
#             smax = max(smax, abs(a[i])**2 + abs(a[i+1])**2)
# print(k, smax)
# #
# count = m = 0
# f = open('17 (1).txt')
# l = [int(i) for i in f]
# min_sp = 10 ** 10
# for i in range(len(l)):
#     if abs(l[i]) % 10 == 6:
#         min_sp = min(min_sp, l[i])
#         print(min_sp)
#
# for i in range(len(l) - 1):
#     if ((abs(l[i]) % 10 == 6 and (abs(l[i + 1])) % 10 != 6) or (
#             (abs(l[i])) % 10 != 6 and abs((l[i + 1])) % 10 == 6)) and ((l[i] ** 2 + l[i + 1] ** 2) < min_sp ** 2):
#         count += 1
#         m = max(m, (l[i] ** 2 + l[i + 1] ** 2))
# print(count, m)
# from itertools import *
# count = 0
# for i in product('012345',repeat = 3):
#     if i[0] != '0' and i.count('5')>=2 :
#         count+=1
# print(count)
# print(270*11)
# n = 6*'3'+75*'4'
# while ('35' in n) or ('355' in n) or ('3444' in n):
#     if '35' in n:
#         n = n.replace('35','4',1)
#     else:
#         if '355' in n:
#             n = n.replace('355', '4', 1)
#         else:
#             n = n.replace('3444', '3', 1)
# print(n)
# res_1 = 0
# for i in '123456789AB':
#     res = int('154'+i+'3', 12) + int('1'+i+'365', 12)
#     if res % 13 == 0:
#         res_1 = res/13
# print(res_1)
# f = open('12.txt')
# a = [int(x) for x in f]
# k = 0
# kmin = 1000000000000000000
# smax = -1000000000000000
# for i in range(len(a)-1):
#     if abs(a[i]) % 15 != 0:
#         kmin = min(a[i], kmin)
# print(kmin)
# for i in range(len(a)-1):
#     if a[i] % kmin == 0 and a[i+1] % kmin == 0:
#         k += 1
#         smax = max(a[i]+a[i+1], smax)
# print(k,smax)
# x = {
#     'flag': 'True',
#     'Oleg': 'False'
#     }
# req = x.get('Oleg')
# print(req)
# # print(map(int, 2, 4))
#p=9
# alp = '12345678'
# for x in alp:
#     for y in alp:
#         for z in alp:
#             for w in alp:
#                 if int((z+x+y+x+'7') + (x+y+'836') == (w+z+x+'64'),9):
#                     print(x,y,z,w)
# for p in range(1,10):
#     for x in range(1,p):
#         for y in range (0,p):
#             for z in range (1,p):
#                 for w in range(1,p):
#                     t1 = z*p**4+x*p**3+y*p**2+x*p**1+7
#                     t2 = x*p**4+y*p**3+8*p**2+3*p**1+6
#                     t3 = w*p**4+z*p**3+x*p**2+6*p**1+4
#                     if t1 + t2 == t3:
#                         print(t1,t2, t3)
#                         print(int(str(x)+str(y)+str(z)+str(w), 9))
#                         print(p)
# x = 343**5+343**4+49**6-7**13-21
# w=''
# while x!=0:
#     q=str(x%7)
#     w+=q
#     x//=7
#     print(x)
# print(w)
# alp = '012345678'
# for x in alp:
#     for y in alp:
#         if (int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)) % 61 == 0:
#             print((int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)) // 61)
# alp = '0123456789ABC'
# # for x in alp:
# #     if (int('26'+x+'98', 13)+ int('4'+x+'296', 13)) % 34 == 0:
# #         print((int('26'+x+'98', 13)+ int('4'+x+'296', 13)) // 34)
# x = 4**511+2**511-511
# s=''
# while x!=0:
#     s+= str(x%2)
#     x//=2
# print(s.count('1'))
# x =x 49**6+7**18-21
# s=''
# while x!=0:
#     s+= str(x%7)
#     x//=7
# print(s.count('6'))
# k=''
# for i in range(200,2300):
#     s = bin(i)[2:]
#     for q in s:
#         if q == '0':
#             k += '1'
#         else:
#             k += '0'
#     k = int(k,2)
#     r = i-k
#     print(i, r)
#     if r == 979:
#         break
#     k=''
# for i in range(1,1000):
#     s = bin(i)[2:]
#     if i % 2 == 0:
#         s = s + bin(s.count('1'))[2:]
#     else:
#         s = '1'+s+'00'
#     print(i, s, int(s, 2))
#     if int(s, 2) > 215:
#         break
# for i in range(1,1000):
# #     s = bin(i)[2:]
# #     for _ in range(2):
# #         if s.count('1') % 2 == 0:
# #             s = s[1:]
# #             s = int(s,2)
# #             s = bin(s)[2:]
# #         else:
# #             s = '1'+s+'00'
# #     print(i, s, int(s,2))
# #     if int(s,2) > 100:
# #         break

# for i in range(101000000, 200002000):
#     s = bin(i)[2:]
#     n = i
#     for _ in range(3):
#         if sum(map(int, str(n))) % 2 == 0:
#             s = s+'0'
#         else:
#             s = s+'1'
#         n = int(s, 2)
#     print(i, s, int(s,2))
# for i in range(1, 1500):
#     s = bin(i)[2:]
#     s = bin(i - s.count('0'))[2:]
#     s = s[-3:] + s
#     print(i,s,int(s,2))
#     if int(s,2) > 224:
#         break
# for i in range(1,1000):
#     s = bin(i)[2:]
#     if s.count('1') % 2 == 0:
#         s = s+'0'
#         s.replace(s[2:], '10')
#     else:
#         s = s+'1'
#         s.replace(s[2:], '11')
#     print(i,s,int(s,2))
#     if int(s,2) >=16:
#         break
# from itertools import *
# alp ='0123456789aaaaa'
# k=0
# for i in product(alp, repeat=5):
#     if i[0] != '0' and i.count('8') == 1 and i.count('a') >=2:
#         k+=1
# print(k)
# for x in range(1,3001):
#     arif = 7 ** 100 - x
#     c = 0
#     while arif != 0:
#         if arif % 7 == 0:
#             c+=1
#         arif //=7
#     if c == 2:
#         print(x)
# for x in range(4100, 10000):
#     arif = 3**100 - x
#     c=0
#     while arif != 0:
#         if arif % 3 == 0:
#             c += 1
#         arif //=3
#     if c == 1:
#         print(x)
# for x in range(8300,10000):
#     c = 0
#     t = 5**100 - x
#     while t != 0:
#         if t % 5 == 0:
#             c += 1
#         t //= 5
#     if c == 4:
#         print(x)
# for x in range(5000, 100000):
#     arif = 7 ** 100 - x
#     c = 0
#     while arif != 0:
#         if arif % 7 == 0:
#             c+=1
#         arif //=7
#     if c == 5:
#         print(x)
# for x in range(1, 2031):
#     t = 7**91 + 7**160 - x
#     c=0
#     while t!=0:
#         if t % 7 == 0:
#             c+=1
#         t //= 7
#     if c == 70:
#         print(x)
# for x in range(1,2031):
#     t = 6**260 + 6**160 + 6**60 -x
#     c=0
#     while t!=0:
#         if t % 6 == 0:
#             c+=1
#         t//=6
#     if c==202:
#         print(x)
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((w <= (y == z)) and (y == (z <= x))):
#                     print(x,y,z,w)
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(not(x <= w) or (y <= z) or not(y)):
#                     print(x, y, z, w)
# for A in range(200):
#     f = True
#     for x in range(200):
#         if not((x % 2 == 0) <= (x % 3 != 0) or (x + A >= 80)):
#             f = False
#     if f:
#         print(A)
#         break
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(not(x <= z) or (y == w) or y):
#                     print(x, y, z, w)
# for A in range(500):
#     f = True
#     for x in range(500):
#         for y in range(500):
#             if not((x >= 27) or (2*x < 3*y) or (A > (x+2)*(y-3))):
#                 f = False
#     if f:
#         print(A)
#         break
# for A in range(1,5000):
#     f = True
#     for x in range(1,5000):
#         if not((x % 33 == 0) <= ((x % A != 0) <= (x % 242 != 0))):
#             f = False
#     if f:
#         print(A)
# for A in range(500):
#     f = True
#     for x in range(500):
#         if not((x & 13 == 0) <= ((x & 40 != 0) <= (x & A != 0))):
#                 f = False
#     if f:
#         print(A)
#         break
# for A in range(500):
#     f = True
#     for x in range(500):
#         for y in range(500):
#             if not(((x + y) <= 22) or (y <= (x - 6)) or (y >= A)):
#                 f = False
#     if f:
#         print(A)
# for A in range(50000, 1, -1):
#     f = True
#     for x in range(1, 50000):
#         if not((x % A == 0) and (A < 10) or (x % 44 != 0) and (x % 99 != 0) and (A < 10)):
#             f = False
#     if f:
#         print(A)
# from turtle import *
# left(90)
# k = 8
# speed(2000)
# tracer(300)
# for i in range(3):
#     forward(7 * k)
#     right(90)
#     forward(12 * k)
#     right(90)
# pu()
# forward(4 * k)
# right(90)
# fd(6*k)
# lt(90)
# pd()
# for i in range(4):
#     forward(83*k)
#     right(90)
#     forward(77 * k )
#     right(90)
# pu()
# for x in range(-100, 100):
#   for y in range(-100, 20):
#     goto(x * k, y * k)
#     dot(5, "red")
#     dot(2, "white")
# mainloop()
# print(bin(58)[2:])
# print(bin(32)[2:])
# print(int('11100000',2))
from ipaddress import ip_network
k=0
net = ip_network("192.168.32.160/255.255.255.240", 0)

for add in range(33):
    swag=ip_network("192.168.32.160/"+str(add))
    if bin(swag)[2:].count('1') == 2

from itertools import *
alf='0123456789AAAAA'
k=0
for i in product(alf, repeat=8):
    #if (i[0] != '0' and i.count('0') == 2 and i.count('A') <= 4):
    print(i)

def f(n):
    if n <3: return n
    if n >=3: return (n-1)*f(n-2)
print((f(2025)-f(2023))/f(2021))

for a in range(1,100):
    f=True
    for x in range(1,100):
        for y in range(1,100):
            for z in range(1,100):
                if not((80!=5*y+2*x+4*z) or (a<6*x) or (a<y) or (a<3*z)):
                    f=False
    if f:
        print(a)

for a in range(1,200):
    f=True
    for x in range(1,200):
        if not((x % a == 0) and (a<10) or (x % 44 !=0) and (x % 99 !=0) and (a<10)):
            f=False
    if f:
        print(a)

a = set()
p = {1,2,3,4,5,6}
d = {3,5,15}
for x in range(100):
    if not((not(x in a)) <= ((not(x in p)) and (x in d)) or not(x in d)):
        a.add(x)
print(a)

from ipaddress import *
net = ip_network(f'172.16.168.0/255.255.248.0', 0)
k=0
for ip_add in net:
    if bin(int(ip_add)).count('1')%5!=0:
        k+=1
print(k)
from itertools import *
k=0
alf = '01a'
for s in product(alf,repeat=8):
    if s[0]!='0' and s.count('0')==2 and s.count('a')<=4:
        k+=5**s.count('a')*9**s.count('1')
print(k)

for n in range(1,100):
    s='1'*n
    while '111' in s:
        s=s.replace('111','2',1)
        s=s.replace('222','11',1)
        s=s.replace('1','2',1)
    if s.count('1') == 0:
        print(s,n)'''
'''
st=123_456_794
fn=678_901_234
k=0
for x in range(st//16,fn//16+1):
    if st<=16*x<=fn:
        k+=1
    if st<=16*x+10<=fn:
        k+=1
    if st<=16*x+9<=fn:
        k+=1
print(k)
''''''
from functools import *
@lru_cache(None)
def f(n):
    if n == 1: return 1
    return f(n-1)+3*g(n-1)
def g(n):
    if n==1: return 1
    return f(n-1)-2*g(n-1)
print(sum(map(int,str(f(50)))))'''
'''
k=0
def f(n):
    if n <= 3: return n
    if n % 2 == 0 : return n + f(n-1)
    if n % 2 !=0: return n*n + f(n-2)

for i in range(1,2000):
    if f(i) < 10**8:
        k+=1
print(k)
#842
''''''
k=0
def f(n):
    if n > 20: return n*n*n+n
    if n % 2 == 0: return 3 * f(n+1) + f(n+3)
    if n % 2 != 0: return f(n+2)+ 2 * f(n+3)

for i in range(1,1001):
    if str(f(i)).count('1') == 0:
        k+=1
print(k)
#384
''''''
def f(n):
    if n > 30: return n*n + 3* n + 5
    if n % 2 == 0: return 2* f(n+1) + f(n+4)
    if n % 2 != 0: return f(n+2) + 3*f(n+5)

k = 0
for i in range(1, 1001):
    if str(f(i)).count('0') >= 2:
        k+=1
print(k)
#77
''''''
k=0
def f(n):
    if n > 30: return n*n+5*n+4
    if n % 2 == 0: return f(n+1)+ 3*f(n+4)
    if n % 2 != 0: return 2*f(n+2) + f(n+5)

for i in range(1,1001):
    if sum(map(int, str(f(i)))) == 27:
        k+=1
print(k)
#137
''''''
def f(n):
    if n == 0: return 5
    if n > 0: return 3*f(n-4)
    if n < 0: return f(n+3)
print(f(43))
#7971615
''''''
from functools import *
@lru_cache(None)
def f(n):
    if n <=1: return n
    if n % 2 == 0: return 1 + f(n//2)
    if n % 2 !=0: return 0
for i in range(1,101000):
    if f(i) == 16:
        print(i)
''''''
def f(n):
    if n <=5: return n
    if n % 3 == 0: return n + f(n//3+2)
    return -98977967967
for i in range(1,1000):
    if f(i) > 1000:
        print(i)
        break''''''
from turtle import *
k=10
lt(90)
speed(20)
tracer(20)
down()
for _ in range(2):
    fd(15*k)
    lt(90)
    fd(20*k)
    lt(90)
up()
rt(90)
bk(7*k)
lt(90)
fd(9*k)
down()
for _ in range(2):
    fd(17*k)
    rt(90)
    fd(15*k)
    rt(90)
up()
for x in range(-25,50):
    for y in range(-25,50):
        goto(x*k,y*k)
        dot(3.5,'red')''''''
for i in range(1,100000):
    s = ''
    n=''
    c = i
    ost = (c % 4)*2
    ostc = ost
    while ost !=0:
            s+=str(ost % 4)
            ost = ost // 4
    s = s[::-1]
    while c !=0:
        n+=str(c % 4)
        c = c // 4
    n=n[::-1]   
    if ostc == 0:
        n = n + n[-2:]
    else:        
        n = n + s
    if int(n,4) < 369:
        print(i)'''
'''     
for i in range(1,100):
    co = i
    n =''
    while i !=0:
        n+=str(i % 4)
        i = i // 4
            
    print(co,n)''''''
from itertools import *
alp = 'аеиклпр'
k = 0
s = 1
for i in product(alp, repeat=6):
    if (s % 2 == 0) and (i[0] != 'к') and (i.count('и') >= 2):   
        k+=1
    s+=1
print(k)'''
'''
from ipaddress import *
net = ip_network('116.29.170.89/255.255.255.224', 0)
k=0
for add in net:
    print(bin(int(add)))
    print(bin(int(add))[17:])
    print(bin(int(add))[:17])
    if bin(int(add))[:1].count('1') <= bin(int(add))[17:].count('1'):
        k+=1
print(k)''''''
def f(st,fn):
    if st==fn: return 1
    if st > fn or st==17: return 0
    return f(st+1,fn)+ f(st*2,fn)
print(f(1,10)*f(10,35))''''''
from ipaddress import *
net = ip_network('116.29.170.89/255.255.255.224', 0)
k=0
for add in net:
    print(bin(int(add)))
    print(bin(int(add))[17:])
    print(bin(int(add))[:17])
    if bin(int(add))[:1].count('1') <= bin(int(add))[17:].count('1'):
        k+=1''''''
def f(st,fn):
    if st==fn: return 1
    if st>fn: return 0
    return (f(st+1,fn) + f(st*3,fn))
print(f(2,28)*f(28,90))''''''
def f(st,fn,k):
    if st == fn: return 1
    if st> fn: return 0
    if k == 0: return (f(st+1,fn,0) + f(st+2,fn,0) + f(st*2, fn, 2))
    if k == 2: return (f(st+1,fn,0) + f(st+2,fn,0))
print(f(1,11,0))''''''
def f(st,fn,k):
    if fn == st: return 1
    if st> fn: return 0
    if k < 2: return f(st+1,fn,k)+f(st*2,fn,k+1)
    if k >= 2: return f(st+1,fn,k)
print(f(1,11,0))''''''
def f(st,fn,k):
    if fn == st: return 1
    if st> fn: return 0
    return f(st+1,fn,k) + f(int(str(st)+'1'),fn,k)
print(f(1,333,0))''''''
def f(st,fn,k):
    if fn == st: return 1
    if st> fn: return 0
    return f(st+1,fn,k) + f(st+3,fn,k) + f(st+st-1,fn,k) 
print(f(2,10,0))''''''
def f(st,fn,k):
    if fn == st: return 1
    if st < fn: return 0
    return f(st-1,fn,k) + f(st-3,fn,k) + f(st//3,fn,k) 
print(f(22,2,0))''''''
def f(st,fn,k):
    if fn == st: return 1
    if st > fn: return 0
    return f(st+1,fn,k) + f(st*2,fn,k) + f(st*2+1,fn,k) 
print(f(int('101',2),int('101110',2),0))
#print(bin(23)[2:])''''''
k=0
def f(n):
    if n == 0: return 0
    if n > 0 and n % 2 == 0: return f(n//2)
    if n>0 and n % 2 !=0: return 1+f(n-1)
for i in range(1,901):
    if f(i) == 9:
        k+=1
print(k)''''''

def f(st,fn):
    if st==fn: return 1
    if st > fn: return 0
    if st == 17: return 0
    return (f(st+2,fn) + (f(st+3, fn)) + (f(st*2, fn)))
print(f(3,10)*f(10,25))
''''''
def f(st,fn):
    if st==fn: return 1
    if st < fn: return 0
    return f(st-1,fn) + f(st//3, fn)
print(f(30,8)*f(8,1))
''''''
def f(st,fn):
    if st==fn: return 1
    if st < fn: return 0
    return f(st-2,fn) + f(st//2, fn)
print(f(32,8)*f(8,1))''''''

from ipaddress import *
net = ip_network('112.160.0.0/255.240.0.0', 0)
k=0
for add in net:
    if bin(int(add)).count('1') % 5 == 0:
        k+=1
print(k)''''''
from ipaddress import *
k = 0
net = ip_network('172.16.128.0/255.255.192.0',0)
for add in net:
    if bin(int(add)).count('1')%2!=0:
       k+=1
print(k)
''''''
from ipaddress import *
k=0
net = ip_network('172.16.128.0/255.255.192.0',0)
for add in net:
    if bin(int(add)).count('1') % 2 != 0:
        k+=1
print(k)''''''
from ipaddress import *
k=0
net = ip_network('112.160.0.0/255.240.0.0',0)
for add in net:
    if bin(int(add)).count('1') % 3 != 0:
        k+=1
print(k)''''''
from ipaddress import *
k=0
net = ip_network('112.160.0.0/255.240.0.0', 0)
for i in net:
    if bin(int(i)).count('1') % 5 !=0:
        k+=1
print(k)''''''
from ipaddress import *
k=0
net = ip_network('115.198.0.0/255.254.0.0',0)
for i in net:
    if bin(int(i)).count('1') % 5 == 0:
        k+=1
print(k)''''''
from ipaddress import *
k=0
net = ip_network('112.160.0.0/255.240.0.0', 0)
for i in net:
    if bin(int(i)).count('1') % 5 ==0:
        k+=1
print(k)''''''
s='8'*65
while '222' in s or '888' in s:
    if '222' in s:
        s=s.replace('222','8',1)
    else:
        s=s.replace('888','2',1)
print(s)''''''
s='4'+'5'*90
while '25' in s or '355' in s or '4555' in s:
    if '25' in s:
        s = s.replace('25','3',1)
    if '355' in s:
        s = s.replace('355','4',1)
    if '4555' in s:
        s = s.replace('4555','2',1)
print(s)''''''
s = '1'+ '0'* 75
while '10' in s or '1' in s:
    if '10' in s:
        s=s.replace('10','001',1)
    else: 
        s=s.replace('1','00',1)
print(s.count('0'))''''''
s = '5'*200
while '555' in s or '333' in s:
    if '555' in s:
        s=s.replace('555','3',1)
    else:
        s=s.replace('333','5',1)
print(sum(map(int,s)))''''''
s = '5'*400
k=0
while '555' in s or '333' in s:
    if '555' in s:
        s=s.replace('555','3',1)
    else:
        s=s.replace('333','5',1)
        k+=3
print(k)''''''
s = '8'*100
while '888' in s or '77' in s:
    if '888' in s:
        s=s.replace('888','8777',1)
    else:
        s=s.replace('77','8',1)
print(s.count('8'),s.count('7'))''''''
for i in range(61,300):
    s = '1'*i
    while '111' in s:
            s=s.replace('111','2',1)
            s=s.replace('222','1',1)
    if s == '221':
        print(i)
        break''''''
k=0
for i in range(1,101):
    s = '1'*i
    while '111' in s:
            s=s.replace('111','2',1)
            s=s.replace('222','3',1)
            s=s.replace('333','1',1)
    if s == '321':
        k+=1
print(k)''''''
f =open('17-1.txt')
a = [int(x) for x in f]
k=0
smin=1000000000000000
for i in range(len(a)-1):
    if(a[i] % 7 ==0 and a[i+1]%17 !=0) or (a[i+1]%7==0 and a[i]%17!=0):
        k+=1
        smin=min(smin,a[i]+a[i+1])
print(k,smin)''''''
f = open('17-1.txt')
a = [int(x) for x in f]
k=0
smin= 45788429785498754789
for i in range(len(a)-1):
    if (abs(a[i]) % 10 == 6 and  a[i] % 3 == 0) or (abs(a[i+1]) % 10 == 6 and  a[i+1] % 3 == 0):
        k+=1
        smin = min(smin,a[i],a[i+1])
print(k,smin)''''''
s = '9'*100
while '33333' in s or '999' in s:
    if '33333' in s:
        s = s.replace('33333', '99',1)
    else:
        s = s.replace('999', '3',1)
print(s)''''''
for i in range(3, 10001):
    s = '5'+'2'*i
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2',1)
        if '522' in s:
            s = s.replace('522', '27',1)
        if '2222' in s:
            s = s.replace('2222', '5',1)
    if sum(map(int,s)) == 63:
        print(i)
        break''''''
s = '9'*136
while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99',1)
    else:
        s = s.replace('9999', '2',1)
print(s)''''''
for i in range(3, 10001):
    s = '1'+'8'*i
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8',1)
        if '388' in s:
            s = s.replace('388', '81',1)
        if '888' in s:
            s = s.replace('888', '3',1)
    if s.count('1') == 3:
        print(i)
        break''''''
mmax = -11231341244
for i in range(3, 10001):
    s = '1'+'2'*i
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2',1)
        if '322' in s:
            s = s.replace('322', '21',1)
        if '222' in s:
            s = s.replace('222', '3',1)
    mmax = max(mmax,sum(map(int,s)))
print(mmax)''''''
s = '8'*83
while '111' in s or '88888' in s:
    if '111' in s:
        s = s.replace('111', '88',1)
    else:
        s = s.replace('88888', '8',1)
print(s)''''''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not(x <= y )) or ((not(w)) <= (not(z))) or w):
                    print(x,y,z,w)''''''
def f(n):
    s = ''
    while n !=0:
        s += str(n % 4)
        n = n // 4
    s = s[::-1]
    return s
for i in range(1,100):
    
    st = ''
    n = i
    ost = (n % 4)*2
    if n % 4 == 0:
        st = f(n) + f(n)[:2]
    else:
        st = f(n) + f(ost)
    if int(st,4) >=1025:
        print(i, int(st,4))
        break''''''
from turtle import *
k = 15
speed(5)
tracer(5)
lt(90)
for _ in range(3):
    down()
    for _ in range(2):
        fd(10*k)
        rt(90)
        fd(10*k)
        rt(90)
    up()
    fd(5*k)
    rt(90)
    fd(5*k)
    lt(90)

for x in range(50):
    for y in range(50):
        goto(x*k,y*k)
        dot(3.5,'red')''''''
from itertools import *
k=1
coun = 0
alp = 'АГИЛМНОФ'
for i in product(alp, repeat = 5):
    if k % 2 != 0 and i[0] != 'Н' and i.count('О') <= 1:
        coun +=1
    k += 1
print(coun)''''''
for i in range(3,10001):
    s = '4'+'1'*i
    while '31' in s or '411' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31','1',1)
        if '411' in s:
            s = s.replace('411','13',1)
        if '1111' in s:
            s = s.replace('1111','4',1)
    if sum(map(int,s)) == 36:
        print(i,s)
        break''''''
from ipaddress import *
net = ip_network('23.140.159.160/255.255.252.0',0)
k = 0
for add in net:
    add = bin(int(add))[2:].zfill(32)


    if add[:16].count('1') >= add[16:].count('1'):
        k+=1
print(k)''''''
for x in range(1,24):
    arr1 = 1 * 25**8 + x * 25**7 + 2 * 25**6 + x * 25**5 + 3 * 25**4 + x * 25 **3 + 4 * 25**2 + x * 25**1 + 5
    arr2 = 2 * 25**4 + x* 25**3 + 0 + 2 * 25** 1 + 4
    arr3 = 1*25**4 + x*25**3 + 0 + 9 * 25**1 + 9
    if (arr1 + arr2 + arr3) % 24 == 0:
        print((arr1+arr2+arr3) // 24)''''''
for a in range(101):
    fl = True
    for x in range(101):
        for y in range(101):
            if not((x<4) or (x>=20) or (y >= (3*x + a)) or (y < 100)):
                fl = False
    if fl:
        print(a)''''''
f = open('17var03.txt')
a = [int(x) for x in f]
kmaxi = -423423432423
kmin = 2432743264326
k=0
for i in range(len(a)):
    if abs(a[i]) % 100 == 90:
        kmaxi = max(kmaxi, a[i])
print(kmaxi)
for i in range(len(a)-2):
    if (((999<abs(a[i])<10000) + (999<abs(a[i+1])<10000) + (999<abs(a[i+2])<10000)) >= 1) and (a[i]+a[i+1]+a[i+2] > kmaxi):
        k+=1
        kmin = min(kmin, a[i]+a[i+1]+a[i+2])
print(k,kmin)''''''
def f(s1,s2,m):
    if (s1+s2) <= 20: return m%2==0
    if m==0: return 0
    h = [f(s1+1,s2,m-1), f((s1+5)//2,s2,m-1), f(s1,s2-1,m-1), f(s1,(s2+1)//2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print('1)', [s2 for s2 in range(11,100) if f(10,s2,2)])
print('2)', [s2 for s2 in range(11,100) if not f(10,s2,1) and f(10,s2,3)])
print('3)', [s2 for s2 in range(11,100) if (f(10,s2,2) or f(10,s2,4)) and not f(10,s2, 2)])''''''
def f(s,m):
    if s>=205: return m%2==0
    if m==0: return 0
    if s<205:
        h=[f(s+1,m-1),f(s+5,m-1), f(s*4,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,205) if f(s,2)])
print('20)', [s for s in range(1,205) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,205) if not f(s,2) and f(s,4)])''''''
def f(st,fn,k):
    if fn == st: return 1
    if st == 6 or st == 17: return 0
    if st > fn: return 0
    return f(st+2,fn,k) + f(st+3,fn,k) + f(st*5,fn,k) 
print(f(1,31,0))''''''
f = open('17var03.txt')
a = [int(x) for x in f]
kmaxi = -423423432423
kmin = 2432743264326
k=0
for i in range(len(a)):
    if abs(a[i]) % 100 == 90:
        kmaxi = max(kmaxi, a[i])
print(kmaxi)
for i in range(len(a)-2):
    if (((999<abs(a[i])<10000) + (999<abs(a[i+1])<10000) + (999<abs(a[i+2])<10000)) >= 1) and (a[i]+a[i+1]+a[i+2] > kmaxi):
        k+=1
        kmin = min(kmin, a[i]+a[i+1]+a[i+2])
print(k,kmin)''''''
from fnmatch import *
mask='54?1?3*7'
for x in range(5387910,10**10+1,18579):
    if fnmatch(str(x),mask):
        print(x,x//18579)''''''
f = open('17-1.txt')
a = [int(x) for x in f]
b = []
kmin = 45834478453487
for i in range(len(a)-2):
    if a[i]<a[i+1]>a[i+2]:
        b.append(i)
print(b)
for i in range(len(b)):
    kmin = min(kmin,b[i]-b[i-1])
    
print(len(b),kmin)''''''
f = open('17-1.txt')
a = [int(x) for x in f]
b = []
kmin = 45834478453487
for i in range(1,len(a)-1):
    if a[i-1]<a[i]>a[i+1]:
        b.append(i)
print(b)
for i in range(1,len(b)):
    kmin = min(kmin,b[i]-b[i-1])
    
print(len(b),kmin)  ''''''
f = open('17-2.txt')
a = [int(x) for x in f]
kmin = 483757645674
b = []
for i in range(len(a)):
    kmin = min(kmin,a[i])
    if a[i] == kmin:
        b.append(i+1)
   
print(a.count(kmin), max(b))''''''
f = open('17-8.txt')
a = [int(x) for x in f]
kmax = -21478237823553
k=0
for i in range(len(a)-1):
    if ((bin(a[i]).count('1')>5) and (bin(a[i]).count('1')%2!=0)) + ((bin(a[i+1]).count('1')>5) and (bin(a[i+1]).count('1')%2!=0))!=0:
        k+=1
        kmax = max(kmax,a[i]+a[i+1])
print(k,kmax)''''''
f =open('17-1.txt')
a = [int(x) for x in f]
kmax = -4237857635763
k=0
for i in range(len(a)-1):
    if (a[i] % 9 == 0 and oct(a[i+1])[-1] == '3') + (a[i+1] % 9 == 0 and oct(a[i])[-1] == '3') == 1:
        k+=1
        kmax = max(kmax,a[i],a[i+1])
print(k,kmax)''''''
f = open('17-1.txt')
a = [int(x) for x in f]
b=[]
kmax = -4357834576345
k=0
for i in range(1, len(a)-1):
    if a[i-1]>a[i]<a[i+1]:
        k+=1
        b.append(a[i])
print(k,max(b))''''''
f = open('17-339 (2).txt')
a = [int(x) for x in f]
k = 0
kmin = 37573454375435
kmax = -4563476543657
for i in range(len(a)):
    if a[i]>0 and a[i] % 19 == 0:
        kmin = min(kmin, a[i])
print(kmin)
for i in range(len(a)-1):
    if (a[i] + a[i+1]) < kmin:
        k+=1
        kmax = max(kmax, a[i] + a[i+1])
print(k,kmax)''''''
f = open('17-403.txt')
a = [int(x) for x in f]
k = 0
kmin = 378782347623
kmin1 =5343453454435
for i in range(len(a)):
    kmin = min(kmin,a[i])
print(kmin)
for i in range(len(a)-1):
    if ((a[i] % 77) * (a[i+1] % 77)) == kmin**2:
        k+=1
        kmin1 = min(kmin1, a[i]*a[i+1])
print(k,kmin1)''''''
def fn(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] != '0':
            if int(n) // int(n[i]) == 197:
                return True
    return False

f = open('17-298.txt')
a = [int(x) for x in f]
k = 0
kmax = -4578348534
kmax1= -45787834857934
for i in range(len(a)):
    if a[i] % 197 == 0:
        kmax = max(kmax,a[i])
print(kmax)
for i in range(len(a)-1):
    if (fn(a[i]) + fn(a[i+1]) == 1) and (a[i] + a[i+1]) < kmax:
        k+=1
        kmax1 = max(kmax1, a[i] + a[i+1])
print(k,kmax1)''''''

f = open('17-379 (1).txt')
a = [int(x) for x in f]
k = 0
kmax = -45673465734534
kmax1 = -43578347534
for i in range(len(a)):
    if a[i] % 100 == 15:
        kmax = max(kmax,a[i])
print(kmax)
for i in range(len(a)-2):
    if (((999<a[i]<10000) + (999<a[i+1]<10000) +(999<a[i+2]<10000)) == 1) and (a[i] + a[i+1] + a[i+2]) >= kmax:
        k+=1
        kmax1 = max(kmax1, a[i] + a[i+1] + a[i+2])
print(k,kmax1) ''''''

f = open('17-408.txt')
a = [int(x) for x in f]
k = 0
kmax = -43758347857843
kmax1 =-2478534675346
for i in range(len(a)):
    if (99<a[i]<1000) and (a[i] % 10 ==3):
        kmax = max(kmax,a[i])
print(kmax)
for i in range(len(a)-2):
    fl1 = (abs(a[i]) % 10 == 3) and (99<abs(a[i])<1000)
    fl2 = (abs(a[i+1]) % 10 == 3) and (99<abs(a[i+1])<1000)
    fl3 = (abs(a[i+2]) % 10 == 3) and (99<abs(a[i+2])<1000)
    if fl1 + fl2 + fl3 > 0 and a[i]+ a[i+1] + a[i+2] < kmax:
        k+=1
        kmax1 = max(kmax1, a[i]+ a[i+1] + a[i+2])
print(k, kmax1)''''''

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= y) and (z == (w<=x)) and (not(w))):
                    print(x,y,z,w)''''''
for i in range(1,100):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = n.replace('1','11')
    else:
        n = n.replace('0','00')
    if int(n,2) > 70:
        print(i,int(n,2))''''''
from turtle import *
lt(90)
speed(10)
k=10
tracer(10)
for i in range(5):
    fd(30*k)
    rt(90)
    fd(40*k)
    rt(90)
up()
fd(20*k)
rt(90)
fd(5*k)
rt(90)
down()
for i in range(7):
    fd(10*k)
    rt(90)
up()
for x in range(0,50):
    for y in range(0,50):
        goto(x*k,y*k)
        dot(3.5,'red')''''''
from itertools import *
alp = '012345'
k=0
for i in product(alp, repeat = 6):
    if i.count('0') == 1 and i[0] != '0':
        x = ''.join(i)
        x = x.replace('1','8').replace('3','8').replace('5','8')
        if x.count('80') == 0 and  x.count('08') == 0:
            k+=1
print(k)''''''
n = 2024 * '1'
while '11111' in n or '222' in n:
    if '11111' in n:
        n = n.replace('11111','22',1)
    else:
        n = n.replace('222','2',1)
print(n)''''''
from ipaddress import *
k=0
net = ip_network('204.16.168.0/255.255.248.0',0)
for add in net:
    if bin(int(add)).count('1') % 5 != 0:
        k+=1
print(k)''''''
def f(n):
    s = ''
    while n !=0:
        s+=str(n%9)
        n = n//9
    s=(s[::-1])
    return int(s)


x1 = 9**2025 + 9**1000

for i in range(1, 5769):
    if str(f(x1-f(i))).count('0') == 1026:
        print(i)''''''
fl = True
for a in range(99,1000):
    for x in range(1,1000):
        if not(((x % 9 == 0) <= (not(x % 6 == 0))) or (x + a >= 100)):
            fl = False
    if fl == True:
        print(a)
        break''''''
f = open('17var011.txt')
a = [int(x) for x in f]
k = 0
kmin = 457374857435
kmax= -45782378942376
for i in range(len(a)):
    kmin = min(kmin,a[i])
print(kmin)
for i in range(len(a)-1):
    if ((a[i] % 27 == kmin) + (a[i+1] % 27 == kmin)) > 0:
        k+=1
        kmax = max(kmax,a[i]+a[i+1])
print(k,kmax)''''''
def f(n):
    s = ''
    while n !=0:
        s+=str(n%9)
        n = n//9
    s=(s[::-1])
    return int(s)


x1 = 9**2025 + 9**1000

for x in range(5769, 1,-1):
    if str(f(x1-x)).count('0') == 1026:
        print(x)
        break''''''
def f(st,fn):
    if st == fn: return 1
    if st < fn: return 0
    return f(st-2,fn) + f(st//2,fn)
print(f(50,11)*f(11,2))''''''
def f(s,m):
    if s<=31: return m%2==0
    if m==0: return 0
    if s>=32:
        h=[f(s-2,m-1),f(s-5,m-1), f(s//3,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(200,1,-1) if f(s,2)])
print('20)', [s for s in range(200,1,-1) if not f(s,1) and f(s,3)])
def f(s1,s2,m):
    if (s1+s2) >= 99: return m % 2 ==0
    if m == 0: return 0
    h = [f(s1+1,s2,m-1), f(s1*3,s2,m-1), f(s1,s2+1,m-1), f(s1,s2*3,m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
print('1', [s2 for s2 in range(1,90) if f(8,s2,2)])
print('2', [s2 for s2 in range(1,90) if not f(8,s2,1) and f(8,s2,3)])
print('3', [s2 for s2 in range(1,90) if f(8,s2,2)])''''''
def fn(n):
    if n % 2 !=0:
        return n//2+1
    else:
        return n // 2

def f(s1,s2,m):
    if (s1+s2) <= 32: return m%2==0
    if m==0: return 0
    h = [f(s1-1,s2,m-1), f(fn(s1),s2,m-1), f(s1,s2-1,m-1), f(s1,fn(s2),m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('1)', [s2 for s2 in range(23,100) if f(10,s2,2)])
print('2)', [s2 for s2 in range(23,100) if not f(10,s2,1) and f(10,s2,3)])
print('3)', [s2 for s2 in range(23,100) if f(10,s2,4) and not f(10,s2, 2)])
''''''
def f(s1,s2,m):
    if (s1+s2) >= 99: return m % 2 ==0
    if m == 0: return 0
    h = [f(s1+1,s2,m-1), f(s1*3,s2,m-1), f(s1,s2+1,m-1), f(s1,s2*3,m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
#print('1', [s2 for s2 in range(1,90) if f(8,s2,2)])
#print('2', [s2 for s2 in range(1,90) if not f(8,s2,1) and f(8,s2,3)])
print('3', [s2 for s2 in range(1,90) if f(8,s2,2)])''''''
def f(s,m):
    if s>=25: return m%2==0
    if m==0: return 0
    if s<25:
        h=[f(s+2,m-1),f(s*2,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,25) if f(s,2)])
print('20)', [s for s in range(1,25) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,25) if not f(s,2) and f(s,4)])''''''
def f(s1,s2,m):
    if s1+s2 >=69: return m%2==0
    if m == 0: return 0
    h = [f(s1+2,s2,m-1), f(s1*2,s2,m-1), f(s1,s2+2,m-1), f(s1,s2*2,m-1)]
    return any(h) if (m-1)%2 ==0 else all(h)
print('19', [s2 for s2 in range(1,64) if f(5,s2,2)])
print('19', [s2 for s2 in range(1,64) if not f(5,s2,1) and f(5,s2,3)])
print('19', [s2 for s2 in range(1,64) if not f(5,s2,2) and f(5,s2,4)])''''''

def f(s1,s2,s3,m):
    if (s1+s2+s3) >= 73: return m % 2 ==0
    if m == 0: return 0
    h = [f(s1+3,s2,s3,m-1), f(s1,s2+3,s3,m-1), f(s1,s2,s3+3, m-1), f(s1+13,s2,s3, m-1),f(s1,s2+13,s3, m-1),f(s1,s2,s3+13, m-1),f(s1+23,s2,s3, m-1),f(s1,s2+23,s3, m-1),f(s1,s2,s3+23, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
print('1', [s3 for s3 in range(1,23) if f(2,s3,s3*2,2)])
print('2', [s3 for s3 in range(1,23) if not f(2,s3,s3*2,1) and f(2,s3,s3*2,3)])
print('3', [s3 for s3 in range(1,23) if not f(2,s3,s3*2,2) and f(2,s3,s3*2,4)])
''''''
def f(s,m):
    if 36<=s<=60: return m%2==0
    if s>60: return (m+1)%2==0
    if m==0: return 0
    if s<36:
        h=[f(s+1,m-1),f(s*2,m-1),f(s*3,m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,36) if f(s,2)])
print('20)', [s for s in range(1,36) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,36) if not f(s,2) and f(s,4)])
''''''
f = open('24-2.txt')
k=0
for s in f:
    if s.count('A') > s.count('E'):
        k+=1
print(k)''''''
f = open('24-3.txt')
arr = [x for x in f]
a = [0] * 100
for i in range(len(arr)):
    if arr[i] == 'A':
        a[ord(i+1)] +=1
print(a)
''''''
f = open('24-4.txt')
a =[0]*100
s=f.readline()
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        a[ord(s[i+1])] +=1
k=a.index(max(a))
print(chr(k))
''''''
# 4:D
from collections import Counter
f = open('24-5.txt')
s = f.readlines()
gcount = 43564364554
a = [0]* 100
for i in range(len(s)):
    gcount = min(s[i].count('G'),gcount)
print(gcount)
for i in range(len(s)):
    if s[i].count('G') == gcount:
        print(Counter(s[i]))
        break
''''''
from collections import Counter
f = open('24-5.txt')
s = f.readlines()
m = Counter(s[0])
print(m)''''''
from collections import Counter
f = open('24-5.txt')
s = f.readlines()
gcount = 43564364554
a = [0]* 100
for i in range(len(s)):
    gcount = min(s[i].count('G'),gcount)
print(gcount)
for i in range(len(s)):
    if s[i].count('G') == gcount:
        print(Counter(s[i]))
        break''''''
# 5:T
f = open('24-6.txt')
s = f.readlines()
m = -4578347857
for i in range(len(s)):
    if s[i].count('A') < 25:
        m = max(rfind())''''''

from collections import Counter
f = open('24-5.txt')
s = f.readlines()
gcount = 43564364554
a = [0]* 100
for i in range(len(s)):
    gcount = min(s[i].count('G'),gcount)
print(gcount)
for i in range(len(s)):
    if s[i].count('G') == gcount:
        print(Counter(s[i]))
        break''''''
f = open('24-6.txt')
s = f.readlines()
l = -4578347857
for i in range(len(s)):
    if s[i].count('A') < 25:
        for m in range(ord('A'), ord('Z')+1):
            l = max(s[i].rfind(chr(m)) - s[i].find(chr(m)), l)
print(l)'''
#1004
'''
f = open('24-7.txt')
s = f.readline()
k = 1
count = 0
for i in range(len(s)-1):
    if s[i] == 'P' and s[i+1] == 'P':
        k=1
    else:
        k+=1
        count = max(k,count)
        
print(count)
'''
#188
'''
f = open('24-8.txt')
s = f.readline()
s = s.split('A')
k=0
for i in range(len(s)-1):
    k = max(len(s[i] + 'A' + s[i+1]), k)
print(k)'''
# 337
f = open('24Demo.txt')
s = f.readline()
k=0
kmax=0
s = s.replace('A', 'I')
s = s.replace('O', 'I')
s = s.replace('C', 'M')
s = s.replace('D', 'M')
s = s.replace('F', 'M')

s = s.replace('MI', '1')
for i in range(len(s)-1):
    if s[i] == s[i-1]:
        k+=1
        kmax = max(k,kmax)
    else:
        k=1
print(kmax)
    
    
        
    

    


    
    

    

    
    
        
