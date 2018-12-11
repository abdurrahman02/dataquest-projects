#print (legislators[0])

legislators = []

gender = set([i[3] for i in legislators])
print (gender)

party = set([i[6] for i in legislators])
print (party)
print (legislators)

for l in legislators:
    if l[3] is None:
        l[3] = "M"


for l in legislators:
    if l[3] is "":
        l[3] = "M"

print (legislators[2])

birth_years = []
for i in legislators:
    d = i.split(" ")
    birth_years.append(d[0])
print(birth_years)

try:
    fl = float("hello")
except FloatingPointError:
    print ("Error converting to float.")