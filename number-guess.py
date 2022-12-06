print("This Program basically tries to guess Which Number you're thinkng of from the set of numbers given")
print()

#blah blah blah
print("Think of any number from 1 to 63 and I'll try to guess it.")
print() #some spaces to make it not look scuffed.
input("Press [Enter] if you guessed the number ")
print()

#The Set of numbers, im gonna throw at your face
print("""1,3,5,7
9,11,13,15
17,19,21,23
25,27,29,31
33,35,37,39
41,43,45,47
49,51,53,55
57,59,61,63""")
ask="Do you find the number you're thinking of here? (y/n): "
s1=input(ask)
print()
print("""2,3,6,7
10,11,14,15
18,19,22,23
26,27,30,31
34,35,38,39
42,43,46,47
50,51,54,55
58,59,62,63""")
s2=input(ask)
print()
print("""4,5,6,7
12,13,14,15
20,21,22,23
28,29,30,31
36,37,38,39
44,45,46,47
52,53,54,55
60,61,62,63""")
s3=input(ask)
print()
print("""32,33,34,35
36,37,38,39
40,41,42,43
44,45,46,47
48,49,50,51
52,53,54,55
56,57,58,59
60,61,62,63""")
s4=input(ask)
print()
print("""8,9,10,11
12,13,14,15
24,25,26,27
28,29,30,31
40,41,42,43
44,45,46,47
56,57,58,59
60,61,62,63""")
s5=input(ask)
print()
print("""16,17,18,19
20,21,22,23
24,25,26,27
28,29,30,31
48,49,50,51
52,53,54,55
56,57,58,59
60,61,62,63""")
s6=input(ask)

#the guess main structure below
if s1=="y":
      g1=1
elif s1=="Y":
      g1=1
elif s1=="n":
      g1=0
elif s1=="N":
      g1=0
else:
    print(guesserror)
if s2=="y":
      g2=2
elif s2=="Y":
      g2=2
elif s2=="n":
      g2=0
elif s2=="N":
      g2=0
else:
    print(guesserror)
if s3=="y":
      g3=4
elif s3=="Y":
      g3=4
elif s3=="n":
      g3=0
elif s3=="N":
      g3=0
else:
    print(guesserror)
if s4=="y":
      g4=32
elif s4=="Y":
      g4=32
elif s4=="n":
      g4=0
elif s4=="N":
      g4=0
else:
    print(guesserror)
if s5=="y":
      g5=8
elif s5=="Y":
      g5=8
elif s5=="n":
      g5=0
elif s5=="N":
      g5=0
else:
    print(guesserror)
if s6=="y":
      g6=16
elif s6=="Y":
      g6=16
elif s6=="n":
      g6=0
elif s6=="N":
      g6=0
else:
    print(guesserror)


