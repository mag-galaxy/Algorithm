import matplotlib.backends.backend_agg
import matplotlib.figure
import numpy

file_output = 'lcs.png'
resolution = 200

input_size = [] # string length
dp = [] # time (S)
brute = [] # time (S)
final_input_size = [] # string length
final_dp = [] # time (S)
final_brute = [] # time (S)

with open('output.txt', 'r') as f:
  i = 0
  for line in f:
    if i%3 == 0:
      input_size.append(int(line))
    elif i%3 == 1:
      brute.append(float(line))
    else:
      dp.append(float(line))
    if i%5 == 4: # has 5 data
      final_input_size.append(input_size[i])
      final_brute.append(brute[i] + brute[i-1] + brute[i-2] + brute[i-3] + brute[i-4])
      final_dp.append(dp[i] + dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])
f.close()

print(final_input_size)
print(final_brute)
print(final_dp)

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
