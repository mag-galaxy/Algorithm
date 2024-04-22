import matplotlib.backends.backend_agg
import matplotlib.figure
import numpy

file_output = 'lcs.png'
resolution = 200

input_size = [] # string length
dp = [] # time (S)
brute = [] # time (S)

with open('output.txt', 'r') as f_read:
  for line in f_read:
    all_data = line.split()
    input_size.append(int(all_data[0]))
    brute.append(double(all_data[1])
    dp.append(double(all_data[2]))

print(input_size)
print(dp)
print(brute)

# figure,anvas,axes object
fig = matplotlib.figure.Figure()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(111)

ax.plot(input_size, dp, label='dp')
ax.plot(input_size, brute, label='brute')
ax.set_xlim(3,10)
ax.set_ylim(0.0, 2.0)
ax.set_xlabel('$input$ $size$ $n$')
ax.set_ylabel('$time$ $(s)$')
ax.set_title("dp vs. brute")
ax.grid()
ax.legend()
fig.savefig(file_output, dpi = g_resolution)
