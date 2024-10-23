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
from ipaddress import ip_network  # Стандартная библиотека
k=0
net = ip_network("192.168.32.160/255.255.255.240", 0)

for add in range(33):
    swag=ip_network("192.168.32.160/"+str(add))
    if bin(swag)[2:].count('1') == 2




