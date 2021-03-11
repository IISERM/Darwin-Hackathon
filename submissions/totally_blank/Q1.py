f = open("seq.fasta")
line = f.readlines()[1]
f.close()
k = 5
k_mer = ""
k_mers = []
count = []
most = []
numbers = []
for x in range(0, len(line) - k):
    for i in range(x, x+k):
        k_mer += line[i]
    k_mers.append(k_mer)
    k_mer = ""
k_mers_out = (", ").join(set(k_mers))

for x in k_mers:
    j = k_mers.count(x)
    count.append(f"{x} = {j}")
    numbers.append(j)

v = 0
for x in numbers:
    if x > v:
        v = x

s = set(count)
for x in s:
    if x.find(str(v)) != -1:
        most.append(x)
most_2 = []
for x in most:
    v = x.split()[0]
    most_2.append(v)
most_out = (", ").join(most_2)

print(f"All the k-mers:\n {k_mers_out}\n")
print(f"Most occurring k-mers:\n {most_out}")

