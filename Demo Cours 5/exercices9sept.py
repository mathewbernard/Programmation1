a = 5
b = 3
c = 10
d = 7
p = True
q = False

print(a > b)
print(b >= c)  
print(not p)  
print(a == b or c > d)  
print(not (a == b) and d < c)  
print((a > b) and (b > c or d < c))  
print(not (a > b and b > c) or q)  
print((a > b or q) and (not p or d < c))  
print(not (a > b) or (b > c and not q) or (d == c))  
print(not ((a > b and c > d) or (q and not p)) and (b < a or c == d))


# 1 <= n <= 10


#Parce que avoir les parenthèse améliore la lisibilité des lignes de codes