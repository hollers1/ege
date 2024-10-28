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
    if (s1+s2)>=53: return m%2==0
    if m==0: return 0
    h=[f(s1+1, s2, m-1), f(s1*2,s2,m-1), f(s1,s2+1,m-1), f(s1,s2*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

#print('19)', [s2 for s2 in range(1,48) if f(5,s2,2)])
print('20)', [s2 for s2 in range(1,48) if not f(5,s2,1) and f(5,s2,3)])
print('21)', [s2 for s2 in range(1,48) if not f(5,s2,2) and f(5,s2,4)])

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
print(a)'''

from ipaddress import *
net = ip_network(f'172.16.168.0/255.255.248.0', 0)
k=0
for ip_add in net:
    if bin(int(ip_add)).count('1')%5!=0:
        k+=1
print(k)
