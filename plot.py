import matplotlib.pyplot as plt

input_size = [] # n
n2 = [] # time (S)
nlgn = [] # time (S)

f = open('result.txt', 'r')
all_data = f.read()
data = all_data.split()
f.close()

for i in range(len(data)):
  if i%3 == 0:
    input_size.append(data[i])
  elif i%3 == 1:
    nlgn.append(data[i])
  else:
    n2.append(data[i])

print(input_size)
print(n2)
print(nlgn)
# # plot(x, y)
# plt.plot(input_size, n2, label='n^2')
# plt.plot(input_size, nlgn, label='nlgn')
# plt.xlabel('input size (n)')
# plt.ylabel('time (s)')
# plt.legend()
# plt.grid(True)
# plt.show()
