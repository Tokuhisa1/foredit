fibs=[0,1]
print fibs[-1]
print fibs[-2]
for i in range(8):
	fibs.append(fibs[-2]+fibs[-1])
print fibs