x = open(r'C:\\Users\\hp\\Desktop\\seq.fasta')
a = x.read()
x.close()

k = int(input("Enter k:"))
i = 0
while(1):
    if(ord(a[i]) == 10):  # Check with \n instead of the ascii value
        break
    else:
        i += 1
l = []
a = a[i+1:]
d = {}
for i in range(0, len(a)-k+1):
    l.append(a[i:i+k])
    print(a[i:i+k], end=',')
print()

for c1 in l:
    f = 1  # ERROR!! No semicolon
    # Simplify this!
    # if c1 in d:
    #     break
    for c2 in d:
        if(c1 == c2):
            f = 0
            break
    if f == 0:
        continue
    d[c1] = l.count(c1)
print("Most occuring kmers:")
m = max(d.values())
for i, j in d.items():  # Good, but can you do better?
    if j == m:
        print(i, end=',')
