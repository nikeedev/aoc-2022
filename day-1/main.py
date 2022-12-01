file = open("input.txt", "r+")

elf_cals = []
i = 0

elf_cals.append([])

for line in file:
	print(line.strip())
	if line.strip() != '':
		elf_cals[i].append(int(line.strip()))
	else:
		elf_cals.append([])
		i += 1
	
print(elf_cals)



cal_cals = []


for cals in elf_cals:	
    k = 0
    for l in range(len(cals)):
        k += cals[l]
    cal_cals.append(k)
    k = 0

print(cal_cals)

cal_cals.sort(reverse=True)

print(cal_cals)

print("The biggest cal elf are: " + str(cal_cals[0]))

top_three = []
top_total = 0

for j in range(3):
    top_three.append(cal_cals[j])
    top_total += cal_cals[j]

print(top_three)

print("Top three total are: " + str(top_total))

file.close()

