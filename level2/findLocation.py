s0 = 127*'A'
s1 = ''.join([chr(ord('a')+c) for c in range(26)])
s = s0+s1
print(s)
