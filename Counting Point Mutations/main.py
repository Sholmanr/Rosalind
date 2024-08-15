
h = 0
t = ''

with open('rosalind_hamm.txt', 'r') as file:
    for line in file:
        t += line.strip()
    half = len(t) // 2
    s = t[half:]
    t = t[0:half]
    for n, b in zip(t,s):
        if n!= b:
            h += 1

file.close()

print(h)