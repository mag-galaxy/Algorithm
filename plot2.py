import matplotlib.backends.backend_agg
import matplotlib.figure
import numpy

file_output = 'lcs.png'
resolution = 200

input_size = [] # string length
dp = [] # time (S)
brute = [] # time (S)

f = open('output.txt', 'r')
all_data = f.read()
data = all_data.split()
f.close()

brute_v = 0
dp_v = 0
for i in range(len(data)):
  if i%3 == 0:
    continue
  elif i%3 == 1:
    brute_v += (float(data[i]))
  else:
    dp_v += (float(data[i]))
  if i%15 == 14: # has 5 data, 15 lines
    input_size.append(int(data[i-2]))
    brute.append(brute_v/5.0)
    dp.append(dp_v/5.0)
    brute_v = 0
    dp_v = 0

print(input_size)
print(brute)
print(dp)

# figure,anvas,axes object
fig = matplotlib.figure.Figure()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(111)

ax.plot(input_size, dp, label='dp')
ax.plot(input_size, brute, label='brute')
ax.set_xlim(3,10)
ax.set_ylim(0.0, 0.001)
ax.set_xlabel('$input$ $size$ $n$')
ax.set_ylabel('$time$ $(s)$')
ax.set_title("dp vs. brute")
ax.grid()
ax.legend()
fig.savefig(file_output, dpi = resolution)
