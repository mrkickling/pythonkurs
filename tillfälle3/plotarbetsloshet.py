import matplotlib.pyplot as plt

x = []
y = []

f = open('arbetsloshet.txt')
for line in f.readlines():
    args = line.strip().split(" ")
    x.append(args[0])
    y.append(float(args[1]))

f.close()

print(x)
print(y)

plt.plot(x, y)
plt.ylabel('Arbetslöshet')
plt.xlabel('År')
plt.show()
