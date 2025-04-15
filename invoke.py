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
# st=123_456_794
# fn=678_901_234
# k=0
# for x in range(st//16,fn//16+1):
#     if st<=16*x<=fn:
#         k+=1
#     if st<=16*x+10<=fn:
#         k+=1
#     if st<=16*x+9<=fn:
#         k+=1
# print(k)
# print('x y z w')
# for x in range(0,2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not(y and (x or z) or (not(y or z)) or w):
#                     print(x,y,z,w)
# for i in range(1,100):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n = n + n[-2:]
#     else:
#         n = '1' + n + '0'
#     print(i, n, int(n,2))
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

# from turtle import *
# left(90)
# k=8
# speed(200)
# tracer(100)
# for _ in range(2):
#     fd(5*k)
#     lt(90)
#     bk(13*k)
#     lt(90)
# up()
# bk(10*k)
# rt(90)
# fd(9*k)
# lt(90)
# down()
# for _ in range(2):
#     fd(11*k)
#     rt(90)
#     fd(7*k)
#     rt(90)
# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*k, y*k)
#         dot("red")
# from itertools import*
# alp='012345678'
# k=0
# for i in product(alp, repeat=5):
#     if i[0] != '0' and i.count('5') == 1 and i[0] != i[1] and i[1] != i[2] and i[2] != i[3] and i[3] != i[4]:
#         k+=1
# print(k)
# for i in range(3, 10001):
#     n = '3' + '5' * i
#     while '333' in n or '555' in n:
#         if '555' in n:
#             n = n.replace('555', '3', 1)
#         else:
#             n = n.replace('333', '5', 1)
#     print(n, sum(map(int, n)))
# from ipaddress import *
# net = ip_network(f'192.168.32.48/255.255.255.240', 0)
# k=0
# # k=0
# # for ip_add in net:
# #     if bin(int(ip_add)).count('1')%5!=0:
# #         k+=1
# for i in net:
#     if bin(int(i)). count('1')% 2 !=0:
#         k+=1
# print(k)
# x = 2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
# k=0
# s=''
# while x != 0:
#     s += str(x % 9)
#     x //= 9
#
# print(s.count('0'))
# fl=True
# for a in range(1,1000):
#     for x in range(1,1000):
#         if not((x&a==0) or (not(x&37==0)) or (not(x&12==0))):
#             fl=False
#     if fl:
#         print(a)
# def f(n):
#     if n <= 3: return 1
#     if n > 3: return (n+3)*f(n-2)
# print(f(2028)/f(2024))
#
# from functools import lru_cache
#
# @lru_cache(None)
# def F(n):
#     if n<=3: return 1
#     if n>3: return (n+3)*F(n-2)
#
# for i in range(1, 2028,-1):
#     F(i)
#
# print(F(2028)/F(2024))
# print('x y z w')
# for x in range(0,2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if (not(x or y)) and (not(w)) or (not(z or w)) and y:
#                     print(x,y,z,w)
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if i % 3 == 0:
#         n = n + n[-2:]
#     else:
#         n = n + bin((i % 3)*3)[2:]
#     if int(n,2) >= 195:
#         print(int(n,2))
# from turtle import *
# lt(90)
# speed(200)
# tracer(200)
# k=8
# down()
# for _ in range(2):
#     fd(23*k)
#     lt(90)
#     bk(27*k)
#     lt(90)
# up()
# bk(5*k)
# rt(90)
# fd(11*k)
# lt(90)
# down()
# for i in range(2):
#     fd(26*k)
#     rt(90)
#     fd(32*k)
#     rt(90)
# up()
# for x in range(-10, 1000):
#     for y in range(-50, 50):
#         goto(x*k,y*k)
#         dot(4,'red')
# from itertools import *
# alp = '0123456'
# k=0
# for i in product(alp, repeat=7):
#     if i[0] != '0' and ((i.count('2') + i.count('0') + i.count('4') + i.count('6')) == 2):
#         k+=1
# print(k)
# arr = []
# for i in range(3,100):
#     n = '8'+ i*'4'
#     while '11' in n or '444' in n or '8888' in n:
#         if '11' in n:
#             n = n.replace('11','4',1)
#         if '44' in n:
#             n = n.replace('444', '88',1)
#         if '8888' in n:
#             n = n.replace('8888','1',1)
#     arr.append(sum(map(int, n)))
# print(max(arr))
# from ipaddress import *
# net = ip_network(f'112.208.0.0/255.255.128.0', 0)
# k=0
# k=0
# for ip_add in net:
#     if bin(int(ip_add)).count('1')%5!=0:
#         k+=1
# for i in net:
#     if (bin(int(i)). count('1')) % 11 ==0:
#         k+=1
# print(k)

# for a in range(1,2000):
#     fl = True
#     for x in range(1,2000):
#         if not((x % a !=0) <= ((x%28 == 0) <= (x%49 != 0))):
#             fl = False
#     if fl:
#         print(a)
# arr = []
# k=0
# n=4*3125**2019+3*625**2020-2*125**2021+25**2022+25**2022-4*5**2023-2024
# s=''
# while n != 0:
#     arr.append(str(n%25))
#     n //= 25
# for i in arr:
#     if int(i) > 10:
#         k+=1
# print(k)

# def f(s, m):
#     if s >= 435: return m % 2 == 0
#     if m == 0: return 0
#     if s < 435:
#         h =[f(s+5, m-1), f(s*3, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print('1)', [s for s in range(1, 435) if not f(s,1) and f(s, 2)])
# print('2)', [s for s in range(1, 435) if not f(s, 1) and f(s,3)])
# print('3)', [s for s in range(1, 435) if (f(s, 2) or f(s, 4)) and not f(s, 2)])

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((x<=z)<=y) or (not(w))):
#                     print(x,y,z,w)

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((z <= y) and ((not(x)) <= w)) <= ((z == w) or (y and (not(x))))):
#                     print(x,y,z,w)

# for i in range(4,100):
#     n = bin(i)[2:]
#
#     if i % 4 == 0:
#         n = n + n[-2:]
#     else:
#         n = bin((i % 4)*2)[2:] + n
#     if int(n,2) < 68:
#         print(i)

# from itertools import *
# k=0
# alp = '0123456789Aaaa'
# for i in product(alp, repeat=5):
#     if i[0] != '0' and i.count('9') == 1 and i.count('a') <= 3:
#         k+=1
# print(k)
# from turtle import *
# lt(90)
# k=20
# speed(10)
# tracer(10)
# down()
# for _ in range(4):
#     fd(3*k)
#     lt(270)
#     fd(5*k)
#     rt(90)
#
# lt(270)
#
# for _ in range(3):
#     fd(5*k)
#     rt(90)
#     fd(3*k)
#     lt(270)
# up()
# for x in range(-50,500):
#     for y in range(-50,50):
#         goto(x*k,y*k)
#         dot(3,'red')
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((z <= y) and ((not(x)) <= w)) <= ((z == w) or (y and (not(x))))):
#                     print(x, y, z, w)
# for i in range(1, 2000):
#     n = bin(i)[2:]
#     orig = ''
#     op = 0
#     for j in n:
#         if j == '1':
#             orig += '0'
#         else:
#             orig += '1'
#     for j in orig:
#         if j == '0':
#             op += 1
#         else:
#             break
#     orig = orig[op:]
#     if len(orig) !=0:
#         if (i - int(orig, 2)) == 979:
#             print(i)
#     else:
#         print('')
# q = 0
# for x in range(43, -1, -1):
#     n1 = 1 * 44**3 + x * 44**2 + 2 * 44 + 3
#     n2 = 3 * 44**3 + 2 * 44**2 + x * 44 + 1
#     if (n1 + n2) % 42 == 0:
#         print((n1 + n2) // 42)
#         break
# for a in range(101):
#     fl = True
#     for x in range(101):
#         for y in range(101):
#             if not((x+y<=22) or (y<=x-6) or (y>=a)):
#                 fl=False
#     if fl:
#         print(a)

# from ipaddress import *
# net = ip_network(f'99.165.134.0/255.255.254.0', 0)
# k=0
# for i in net:
#     if (bin(int(i)).count('1')) % 3 ==0:
#         k+=1
# print(k)

# from turtle import *
# lt(90)
# speed(20)
# tracer(20)
# k=13
# down()
# for _ in range(4):
#     fd(9*k)
#     lt(270)
# up()
# for _ in range(3):
#     fd(k)
#     lt(270)
#     fd(k)
#     lt(90)
# down()
# for _ in range(2):
#     fd(9*k)
#     lt(270)
#     fd(11*k)
#     lt(270)
# up()
# for x in range(50):
#     for y in range(0,50):
#         goto(x*k,y*k)
#         dot(3.5,'red')

# import itertools
# alphabet = "ДОБРЫНЯ"
# ar = itertools.permutations(alphabet)
# arl = []
# for e in ar:
#     arl.append(list(e))
# print(*arl[3377])

# import itertools
# alp = "БДНОРЫЯ"
# arl = []
# for i in itertools.permutations(alp):
#     arl.append(list(i))
# print(*arl[3377])

# for x in range(43,0,-1):
#     arg1 = 1*44**3+x*44**2+2*44**1+3
#     arg2 = 3*44**3+2*44**2+x*44**1+1
#     if (arg1 + arg2) % 42 == 0:
#         print((arg1+arg2) // 42)

# fl = True
# for a in range(1,1000):
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if not((x+y<=22) or (y<=x-6) or (y>=a)):
#                 fl = False
#     if fl:
#         print(a)

# from turtle import *
# lt(90)
# k=15
# speed(20)
# tracer(20)
# for _ in range(4):
#     fd(9*k)
#     lt(270)
# up()
# for _ in range(3):
#     fd(k)
#     lt(270)
#     fd(k)
#     lt(90)
# down()
# for _ in range(2):
#     fd(9*k)
#     lt(270)
#     fd(11*k)
#     lt(270)
# up()
# for x in range(0,100):
#     for y in range(0,100):
#         goto(x*k,y*k)
#         dot(3.5 ,'red')

# for a in range(1,10000):
#     fl = True
#     for x in range(1,10000):
#         if not((x % 33 == 0) <= ((x % a !=0) <= (x % 242!=0))):
#             fl = False
#     if fl:
#         print(a)
#
# from turtle import *
# lt(90)
# speed(10)
# tracer(10)
# k=10
# down()
# for _ in range(4):
#     fd(28*k)
#     rt(90)
#     fd(26*k)
#     rt(90)
# up()
# fd(8*k)
# rt(90)
# fd(7*k)
# lt(90)
# down()
# for _ in range(4):
#     fd(67*k)
#     rt(90)
#     fd(98*k)
#     rt(90)
# up()
#
# for x in range(0,50):
#     for y in range(0,50):
#         goto(x*k,y*k)
#         dot(3.5,'red')
#
# for x in range(1, 2031):
#     a = 3**100 - x
#     s=''
#     k=0
#     while a != 0:
#         if a % 3 == 0:
#             k+=1
#         a//=3
#     if k == 5:
#          print(x,k)
#
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((not(x<=w)) or (y<=z) or (not(y))):
#                     print(x,y,z,w)
#
#
# for x in range(1,100):
#     n = bin(x)[2:]
#     if n.count('0') % 2 == 0:
#         n = '10' + n[2:] + '0'
#     else:
#         n = '11' + n[2:] + '1'
#     if int(n,2) > 50:
#         print(x)
#
# def f(s, m):
#     if s >= 65: return m % 2 == 0
#     if m == 0: return 0
#     if s < 65:
#         h =[f(s+1, m-1), f(s*3, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# s=6
# print('1)', [x for x in range(1, 58) if not f(x, 1) and f(x, 2)])
# print('2)', [x for x in range(1, 65) if not f(x, 1) and f(x, 3)])
# print('3)', [x for x in range(1, 65) if (f(x, 2) or f(x, 4)) and not f(x, 2)])
#
# from ipaddress import *
# net = ip_network('106.184.0.0/255.248.0.0', 0)
# k=0
# for add in net:
#     if bin(int(add)).count('1') % 2 !=0:
#         k+=1
# print(k)

# def f(n):
#     if n <= 0: return 0
#     if n > 0 and n % 3 == 2: return f(n-1) + 1
#     if n > 0 and n % 3 < 2: return f((n - (n % 3))//3)
#
# for i in range(10,10000):
#     if f(i) == 6:
#         print(i)
# k = 0
# def f(n):
#     if n <= 0: return 0
#     if n % 2 == 0: return f(n//2)
#     if n % 2 !=0: return 1 + f(n-1)
#
# for i in range(1,501):
#     if f(i)==8:
#         k+=1
# print(k)
# from functools import *
# @lru_cache(None)
# def f(n):
#     if n < 3: return 2
#     if n > 2 and n % 2 == 0: return f(n-2)+f(n-1)-n
#     if n >2 and n % 2 != 0: return f(n-1)+2*n
#
# print(f(32))
# from functools import *
#
#
# @lru_cache(None)
# def f(a, b):
#     if a == 0:
#         return b
#     if a > 0:
#         return f(a // 10, 10 * b + (a % 10))
#
#
# print(f(a,))
'''
y = 31
x = 5
x = y//x
z = y//x
print(z)''''''
f = open('17-403.txt')
k=0
kmin = 554545
a = [int(x) for x in f]
kmin1 = min(a)

for i in range(len(a)-1):
    if (a[i] % 77 * a[i+1] % 77) == kmin1**2:
        k+=1
        kmin = min(kmin, a[i]*a[i+1])
print(k, kmin)
''''''
def triplewise(lst):
    return (lst[i-2:i+1] for i in range(2, len(lst)))

def non4dig(x):
    return (x < 1000) or (x >= 10000)

with open("17-380.txt", 'r') as f:
    a = list(map(int, f))

mx25 = max(filter(lambda x: x % 100 == 25, a))
n = sum(1 for a, b, c in triplewise(a) if (non4dig(a) or non4dig(b) or non4dig(c)) and a + b + c <= mx25)
print(n)''''''
f = open('17-403.txt')
a =[int(x) for x in f]
kmini = min(a)
k=0
kmax = -342324324423
for i in range(len(a)-1):
    if ((a[i] % 65) * (a[i+1] % 65)) == kmini:
        k+=1
        kmax = max(kmax,a[i]+a[i+1])
print(k,kmax)''''''
f = open('17-379.txt')
a =[int(x) for x in f]
kmaxi = -3422342342
k=0
kmax = -342324324423
for i in range(len(a)):
    if a[i] % 100 == 15:
        kmaxi = max(kmaxi,a[i])
for i in range(len(a)-2):
    if ((999<a[i]<10000) + (999<a[i+1]<10000)+ (999<a[i+2]<10000) == 1) and (a[i]+a[i+1]+a[i+2] >= kmaxi):
        k+=1
        kmax = max(kmax,a[i]+a[i+1]+a[i+2])
print(kmaxi)
print(k,kmax)''''''
f = open('17-381.txt')
a =[int(x) for x in f]
kmaxi = -3422342342
k=0
kmax = -342324324423
for i in range(len(a)):
    if abs(a[i]) % 100 == 39 and 999<a[i]<10000:
        kmaxi = max(kmaxi,a[i])
for i in range(len(a)-2):
    if ((999<a[i]<10000) + (999<a[i+1]<10000)+ (999<a[i+2]<10000) == 1) and ((a[i]+a[i+1]+a[i+2])**2 <= kmaxi**2):
        k+=1
        kmax = max(kmax,a[i]+a[i+1]+a[i+2])
print(kmaxi)
print(k,kmax)'''
'''
f = open('17-380.txt')
a =[int(x) for x in f]
kmaxi = -3422342342
k=0
kmax = -342324324423
for i in range(len(a)):
    if a[i] % 100 == 25:
        kmaxi = max(kmaxi,a[i])
for i in range(len(a)-2):
    if ((999<a[i]<10000) + (999<a[i+1]<10000)+ (999<a[i+2]<10000) <= 2) and ((a[i]+a[i+1]+a[i+2]) <= kmaxi):
        k+=1
        kmax = max(kmax,a[i]+a[i+1]+a[i+2])
print(kmaxi)
print(k,kmax)'''
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
def f(st, fn):
    if st > fn: return 0
    if st == fn: return 1
    return f(st+2, fn) + f(st+3, fn)
print(f(1,59))''''''
def f(st,fn):
    if st > fn: return 0
    if st == fn: return 1
    return f(st+1,fn) + f(st+2,fn) + f(st+st-1,fn)
print(f(2,9))''''''
def f(s,m):
    if s>=39: return m%2==0
    if m==0: return 0
    if s<39:
        h=[f(s+1,m-1),f(s+3,m-1), f(s*2,m-1)]
    return any (h) if (m-1)%2 == 0 else all(h)

print('19)', [s for s in range(1,38) if not f(s,1) and f(s,2)])
print('20)', [s for s in range(1,38) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,38) if (f(s,2) or f(s,4)) and not f(s,2)])

def f(s,m):
    if s>=39: return m%2==0
    if m == 0: return 0
    if s<39:
        h=[f(s+1,m-1),f(s+3,m-1), f(s*2,m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
print([s for s in range(1,38) if not f(s,1) and f(s,2)])''''''
f = open('17-338.txt')
a = [int(x) for x in f]
kmin = 437985784357843
kmax = -234327534765
k=0
for i in range(len(a)):
    kmin = min(kmin,a[i])
print(kmin)
for i in  range(len(a)-1):
    if ((a[i] % 117 == kmin) + (a[i+1] % 117 == kmin)) != 0:
        k+=1
        kmax = max(kmax, a[i]+a[i+1])
print(k,kmax)''''''
def palindrome(n):
    s=''
    while n !=0:
        s+=str(n % 3)
        n = n // 3
    s = s[::-1]  
    s_lower = s.lower()
    return s_lower == s_lower[::-1]
       
f = open('17-370.txt')
a = [int(x) for x in f]
k=0
kmax = -345734567843
kmin = 4374376843768
for i in range(len(a)):
    if (99<a[i]<=999) and (palindrome(a[i])):
        kmax = max(kmax,a[i])
print(kmax)
for i in range(len(a)-1):
    if (((999<abs(a[i])<10000) + (999<abs(a[i+1])<10000 )) == 1) and ((a[i]**2 + a[i+1]**2) % kmax == 0):
        k+=1
        kmin = min(kmin, a[i]**2 + a[i+1]**2 )
print(k,kmin)''''''
f = open('17-339.txt')
a = [int(x) for x in f]
k = 0
kmin = 435423534543
kmax = -7489342789534789
for i in range(len(a)):
    if a[i] > 0 and a[i] % 19 == 0:
        kmin = min(kmin, a[i])
print(kmin)
for i in range(len(a)-1):
    if (a[i] + a[i+1]) <  kmin:
        k+=1
        kmax = max(kmax, a[i] + a[i+1])
print(k,kmax)''''''
f = open('17-409.txt')
a = [int(x) for x in f]
k = 0
kmax1 = -567345763457643
kmax = -23745327685324678
for i in range(len(a)):
    if a[i] % 10 == 7 and 999<a[i]<10000:
        kmax = max(kmax, a[i])
print(kmax)
for i in range(len(a)-2):
    if (((abs(a[i]) % 10 == 7) + (abs(a[i+1]) % 10 == 7) + (abs(a[i+2]) % 10 == 7)) >= 2) and (999<abs(a[i])<10000) and (999<abs(a[i+1])<10000) and (999<abs(a[i+2])<10000) and ((a[i]+a[i+1]+a[i+2]) > kmax):
        k+=1
        kmax1 = max(kmax, a[i]+a[i+1]+a[i+2])
print(k,kmax1)''''''
def u(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] != '0':
            if int(n) // int(n[i]) == 197:
                return True
    return False

f = open('17-298.txt')
a = [int(x) for x in f]
k = 0
kmax = -2457863475684
kmax1 = -2457683426785
for i in range(len(a)):
    if a[i] % 197 == 0:
        kmax = max(kmax,a[i])
print(kmax)
for i in range(len(a)-1):
    if ((u(a[i]) + u(a[i+1])) == 1) and (a[i] + a[i+1]) < kmax:
        k+=1
        kmax1 = max(kmax1, a[i] + a[i+1])
print(k,kmax1)''''''
f = open('17-365.txt')
a = [int(x) for x in f]
k = 0
kmax = -4235768234567823
kmin = 455893458734578
kmin1=78463267832423
for i in range(1,len(a)-1):
    if (((a[i-1] % 10 == 1) + (a[i+1] % 10 == 1)) == 1):
        kmax =  max(kmax, (a[i-1]+a[i+1])//2)
for i in range(1,len(a)-1):
    if (((a[i-1] % 10 == 1) + (a[i+1] % 10 == 1)) == 1) and a[i-1] < kmax and a[i+1] < kmax:
        k+=1
        if a[i-1] == -9997 or a[i+1] == -9997:
            print(a[i-1],a[i+1])

    
    
    
#-9997''''''
f = open('24-6.txt')
f = f.readline()
k=1
kmax=0
f = f.replace('C','0')
f = f.replace('D','0')
f = f.replace('F','0')
f = f.replace('A','1')
f = f.replace('O','1')
f = f.replace('001','2')

for i in range(len(f)-1):
    if f[i] == '2' and f[i+1] =='2':
        k+=1
        kmax = max(k,kmax)
    else:
        k=1
print(kmax)''''''
f = open('24-5.txt')
lenmax = 0
curlen = 0
acount = 0
f = f.readline()
f = f.replace('B','A')
for i in range(len(f)):
    if f[i] != 'A':
        curlen+=1
        lenmax = max(curlen,lenmax)                
    else:
        acount+=1
        if acount == 3:
            curlen = 0
            acount = 0
print(lenmax)''''''
f = open('24-4.txt').readline()
maxi = 0
k=0

f = f.split('A')
for i in range(len(f)-1):
    if len(f[i]) + len(f[i+1]) >= 12 and f[i].count('B') + f[i+1].count('B') >= 2:
        k +=1
print(k)
''''''
f = open('24-4.txt').readline().split('A')
print(len([x for x in f[1:-1] if len(x)>=12 and x.count('B')>=2]))'''
'''print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not(x<=y)) or ((not(z)) == (w<=x)) or w):
                    print(x,y,z,w)''''''
for i in range(100):
    n = bin(i)[2:]
    if i % 4 == 0:
        n = n + n
    else:
        n = n + n[::-1]
    print(i,n,int(n,2))''''''
from turtle import *
lt(90)
speed(10)
tracer(10)
k=15
for _ in range(3):
    fd(2*k)
    rt(90)
    fd(3*k)
    lt(90)
rt(180)
fd(6*k)
rt(90)
fd(9*k)
up()
bk(4*k)
rt(90)
down()
for i in range(3):
    fd(1*k)
    rt(90)
    fd(2*k)
    lt(90)
rt(180)
fd(4*k)
rt(90)
fd(6*k)
rt(90)
fd(k)
up()
for x in range(50):
    for y in range(-5,50):
        goto(x*k,y*k)
        dot(3.5,'red')''''''
from itertools import *
k=0
for i in product('123456',repeat=4):
    if i.count('3') == 1 and ((i.count('2') + i.count('4') + i.count('6')) <= (i.count('1') + i.count('3') + i.count('5'))):
        k+=1
print(k)''''''
n = '1'*2025
while '1111' in n or '5555' in n:
    if '1111' in n:
        n = n.replace('1111','55',1)
    else:
        n = n.replace('5555','5',1)
print(n)''''''
from ipaddress import *
k=0
net = ip_network('210.66.110.0/255.255.252.0',0)
for add in net:
    if bin(int(add)).count('1') % 6 != 0:
        k+=1
print(k)''''''
def shest(n):
    s = ''
    while n !=0:
        s+= str(n%6)
        n = n//6
    return s[::-1]
k=0
for x in range(1,1001):
    arr1 = 6**2025 + 6**25 - x
    if shest(arr1).count('0') == 2002:
        k+=1
print(k)''''''
b = [int(x) for x in range(200,301)]
for a in range(1,301):
    fl = True
    for x in range(1,301):
        if not((x % a == 0) or ((x in b) <= (x % 77 != 0))):
            fl = False
    if fl:
        print(a)''''''
def f(n):
    if n == 2000: return 0
    if n > 2000: return n+f(n-1)
print(f(3000))''''''
f = open('17var03.txt')
a = [int(x) for x in f]
k = 0
kmin1 = 2454235234
kmin2 = 2452475242435
for i in range(len(a)):
    kmin1 = min(a[i],kmin1)
print(kmin1)
for i in range(len(a)-1):
    if ((a[i] % 44) + (a[i+1] % 44) == kmin1):
        k+=1
        kmin2 = min(abs(a[i] - a[i+1]),kmin2)
print(k,kmin2)''''''
def f(s1,m):
    if (s1)<=21: return m%2==0
    if m==0: return 0
    h=[f(s1-3, m-1), f(s1-7,m-1), f(s1//4,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s1 for s1 in range(22,400) if f(s1,2)])
print('20)', [s1 for s1 in range(22,400) if not f(s1,1) and f(s1,3)])
print('21)', [s1 for s1 in range(22,400) if not f(s1,2) and f(s1,4)]) ''''''
def f(st,fn):
    if st > fn: return 0
    if st == fn: return 1
    if st < fn: return f(st+1,fn) + f(st*2,fn) + f(st*3,fn)
print(f(3,9) * f(9,30))''''''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x or (not y)) and (not (y == z)) and w):
                    print(x,y,z,w)''''''
from re import *
#s =open('24.txt').readline()
s = 'ABBBSBSAJSBASJYHASBASBSBSBASASBCSA'
reg = r'[ABC]{1,4}'

for x in finditer(reg,s):
    print(x.group())
    
#print(max([len(x.group()) for x in finditer(reg,s)]))''''''
from re import *
s =open('24.txt').readline()
reg = r'(ZX|ZY)+'

print(max([len(x.group())//2 for x in finditer(reg,s)]))''''''
from re import *
s = open('24.txt').readline()
reg = r'(BA|BO|CA|CO|DA|DO)+'
print(max([len(x.group())//2 for x in finditer(reg,s)]))''''''
from re import *
s = open('24.txt').readline()
reg = r'(?=((AA|CC)+))'
print(max([len(x.group(1))//2 for x in finditer(reg,s)]))''''''
from re import *
s = open('24.txt').readline()
reg = r'([123][ABC][123])+'
reg = rf'(?=({reg}))'
print(max([len(x.group(1))//3 for x in finditer(reg,s)]))''''''
from re import *
s = open('24.txt').readline()
reg = r'(YZZ|XY|YZ)+'
reg = rf'(?=({reg}))'
print(s[:100])
print([x.group(1) for x in finditer(reg,s[:100])])''''''
from re import *
s = open('24.txt').readline()

reg = rf'([1-9][0-9]*)([-*]([1-9][0-9]*))+'

m= max([x.group() for x in finditer(reg,s)],key = len)
print(len(m),m)''''''
from re import *
s = open('24.txt').readline()
num = r'([1-9][0-9]*|0)'

proiz = rf'(({num}\*)*0(\*{num})*)'

reg = rf'{proiz}(\+{proiz})+'

print(max([len(x.group()) for x in finditer(reg,s)]))''''''
from re import *
s = open('24.txt').readline()
num = r'([1-9][0-9]*|0)'
reg = rf'(AF)[0-9]*([*+]{num})*'

m = max([x.group() for x in finditer(reg,s)], key = len)
print(len(m), m)''''''
print('x y z w| 1')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w and z or (not w)) and x or y):
                    print(x,y,z,w)
print('x y z w| 0') 
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((w and z or (not w)) and x or y):
                    print(x,y,z,w)''''''
def f(n):
    s=''
    while n:
        s+=str(n%3)
        n = n//3
    return s[::-1]

for i in range(1,101):
    if sum(map(int,f(i))) % 3 == 0:
        n = '112' + f(i)[2:]
    else:
        n = f(i) + f(sum(map(int,f(i))))
    if int(n,3)>702 and int(n,3) % 2 == 0:
        print(i,n,int(n,3))''''''
from turtle import *
lt(90)
speed(1000)
tracer(1000)
k=20
rt(270)
for _ in range(2):
    fd(7*k)
    rt(120)
rt(120)
for _ in range(2):
    rt(120)
    fd(5*k)
    rt(240)
rt(240)
for _ in range(2):
    fd(17*k)
    rt(120)
up()
for x in range(-10,60):
    for y in range(-10,60):
        goto(x*k,y*k)
        dot(3.5,'red')''''''
from itertools import *
alp = 'АВКОРТЬ'
k=1
for i in product(alp,repeat = 5):
    i=''.join(i)    
    if (i.count('Т') <= 1) and (i.count('В') == 2) and (not ('ЬЬ' in i)) and (k % 2 != 0):
        
        print(k,i)
    k+=1  ''''''
n = '2'+ 110*'3'
while '2' in n:
    if '23' in n:
        n = n.replace('23','332',1)
    else:
        n = n.replace('2','33',1)
print(n,sum(map(int,n)))''''''
from ipaddress import *
k=0
kmax=-342
for mask in range(15,21):
    net = ip_network('14.253.13.6/'+str(mask),0)

    for ip in net:
        if net[0]<ip<net[-1]:
            k = bin(int(ip)).count('1')
            kmax = max(k,kmax)
print(kmax)''''''
f = open('17.txt')
a = [int(x) for x in f]
k=0
kk=0
kmax=-344
for i in range(len(a)):
    if (1000<=abs(a[i])<=9999) and (abs(a[i]) % 10 == 3):
        k+=1
print(k)
for i in range(len(a)-2):
    b = sorted([a[i],a[i+1],a[i+1]])
    if (b[1] + b[2]) < k**2:
        kk+=1
        kmax = max(kmax, abs(sum(b)))
#print(kk,kmax)''''''
a = [int(x) for x in open('17.txt')]
kk=0
kmax=-5634
k=len([x for x in a if 1000<=abs(x)<10000 and abs(x)%10==3])
print(k) 
for i in range(len(a)-2):
    d = sorted([a[i],a[i+1],a[i+2]])
    if ((d[1]**2)+(d[2]**2)) < k**2:
        kk+=1
        kmax=max(kmax,abs(a[i]+a[i+1]+a[i+2]))
print(kk,kmax)''''''
from re import *
f = open('24.txt').readline()
num = r'([1-7][0-7]*|0)'
reg = rf'{num}(\*{num})*(\-{num})*'
reg = rf'(?=({reg}))'

m = max([x.group(1) for x in finditer(reg,f)],key=len)
print(m,len(m))''''''
a = [int(x) for x in open('17.txt')]
kk=0
kmax=-324234324
k=len([x for x in a if 10000<=abs(x)<100000 and abs(x)%10==7])
print(k) 
for i in range(len(a)-2):
    d = sorted([a[i],a[i+1],a[i+2]])
    if (d[1]**2+d[2]**2) < k**2:
        kk+=1
        kmax=max(kmax,a[i]+a[i+1]+a[i+2])
print(kk,kmax)  ''''''
a = [int(x) for x in open('17.txt')]
k = 0
kk=0
kmax=-42397873824
k = len([x for x in a if 10000<=abs(x)<100000 and abs(x) % 10 == 7])**2
for i in range(len(a)-2):
    b = sorted([a[i],a[i+1],a[i+2]])
    if (b[1]**2 + b[2]**2) < k:
        kk+=1
        kmax = max(kmax,sum(b))
print(kk,kmax)''''''
a = [int(x) for x in open('17.txt')]
k = 0
kk=0
kmax=-341783247832
k = len([x for x in a if 1000<=abs(x)<10000 and abs(x) % 10 == 3])**2
for i in range(len(a)-2):
    b = sorted([a[i],a[i+1],a[i+2]])
    if (b[1] + b[2]) > k:
        kk+=1
        kmax = max(kmax,sum(b))
print(kk,kmax)''''''
from functools import *
@lru_cache(None)
def f(n):
    if n<=5: return 1000
    else: return n+3+f(n-2)
    
for i in range(5,53100): f(i)
    
print(3*f(53079)-(f(53077) + f(53075) + f(53073)))'''
'''
for x in range(0,22):
    a1 = 7*22**8+4*22**7+1*22**6+8*22**5+x*22**4+x*22**3+4*22**2+6*22**1+1
    a2 = 7*22**7+1*22**6+9*22**5+6*22**4+2*22**3+5*22**2+x*22**1+4
    a3 = 3*22**5+9*22**4+6*22**3+x*22**2+9*22+9
    if (a1+a2+a3) % 21 == 0:
        print((a1+a2+a3) / 21)
        break''''''
def f(s1,s2,m):
    if (s1+s2) <= 165: return m%2==0
    if m==0: return 0
    h = [f(s1-2,s2,m-1), f(s1,s2-2,m-1), f(s1//3,s2,m-1),f(s1,s2//3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print('1)', [s2 for s2 in range(300,149,-1) if f(17,s2,2)])
print('2)', [s2 for s2 in range(3000,149,-1) if not f(17,s2,1) and f(17,s2,3)])
print('3)', [s2 for s2 in range(3000,149,-1) if (f(17,s2,2) or f(17,s2,4)) and not f(17,s2, 2)])''''''
def f(st,fn):
    if st<fn: return 0
    if st == fn: return 1
    if st == 9: return 0
    return f(st-1,fn) + f(st//2,fn)
print(f(65,31)*f(31,14)*f(14,4))'''
from re import *
f = open('24.txt').readline()
num = r'([1-7][0-7]*|0)'
reg = rf'({num}(\*{num})*(\-{num})*)'
reg = rf'(?=({reg}))'
print(f[:500])
print(max([len(x.group(1)) for x in finditer(reg,f)]))
