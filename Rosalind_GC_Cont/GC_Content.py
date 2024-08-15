gcPerc = {}


def get_gc_cont(dnaSeq):
    a = 0
    c = 0
    g = 0
    t = 0

    for nucleotide in dnaSeq:
        if nucleotide == 'A':
            a += 1
        if nucleotide == 'C':
            c += 1
        if nucleotide == 'G':
            g += 1
        if nucleotide == 'T':
            t += 1

    gcCont = (c + g) / (a + c + g + t)

    return gcCont


i = 0
id = ''
dnaSeq = ''

with open('rosalind_gc.txt', 'r') as file:
    for line in file:
        if line[0] == '>' and i < 1:
            id = line[1:-1]
            i += 1
        elif line[0] == '>' and i >= 1:
            gcPerc.update({id:get_gc_cont(dnaSeq)})
            id = line[1:-1]
            dnaSeq = ''
            i += 1
        else:
            dnaSeq += line[:-1]
            i += 1
    gcPerc.update({id: get_gc_cont(dnaSeq)})
file.close()

highest = gcPerc.get(id)

for gc in gcPerc.values():
    if gc > highest:
        highest = gc

id = list(gcPerc.keys())[list(gcPerc.values()).index(highest)]
highestGC = gcPerc.get(id) * 100

print(gcPerc)

print(id)
print(highestGC)

