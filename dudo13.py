import math
a=input("zadaj koeficient")
b=input("zadaj koeficient")
c=input("zadaj koeficient")
a=int(a)
b=int(b)
c=int(c)
uhol=(b**2+c**2-a**2)/(2*b*c)
alfar=math.acos(uhol)
alfa=math.degrees(alfar)
print("alfa",alfa)

uholb=(a**2+c**2-b**2)/(2*a*c)
betar=math.acos(uholb)
beta=math.degrees(betar)
print("beta",beta)

uholc=(a**2+b**2-c**2)/(2*a*b)
deltar=math.acos(uholc)
delta=math.degrees(deltar)
print("delta",delta)

if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
  print("je pravouhlý")

if a==b==c:
  print("je rovnostranný")

if a==b or a==c or b==c:
  print("je rovnoramenný")