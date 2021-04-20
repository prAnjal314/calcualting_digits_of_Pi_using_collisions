import numpy as np
n = 10
z = np.pi/6

a = []
for i in range(n):
	b = []
	for j in range(n):
		b.append(0)
	a.append(b)

for i in range(n):
	if i == 0:
		a[0][0] += np.cos(z)
		a[0][1] += 1
	else:
		try:
			a[i][i - 1] += 1
			a[i][i] += 2 * np.cos(z)
			a[i][i + 1] += 1
		except:
			pass
print(a)
print(np.linalg.det(a))
print(np.cos(n*z))
