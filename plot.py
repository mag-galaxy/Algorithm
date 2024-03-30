# import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg
import matplotlib.figure
import numpy
import argparse
import pathlib
import sys

parser = argparse.ArgumentParser(description='plotting f(x)')
# add argument
parser.add_argument ('-o', '--output', default='output.png',\
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=250.0,\
                     help='resolution of plot in DPI (default: 250.0)')
args = parser.parse_args()

file_output = args.output
g_resolution = args.resolution

input_size = [] # n
n2 = [] # time (S)
nlgn = [] # time (S)

f = open('result.txt', 'r')
all_data = f.read()
data = all_data.split()
f.close()

for i in range(len(data)):
  if i%3 == 0:
    input_size.append(int(data[i]))
  elif i%3 == 1:
    nlgn.append(float(data[i]))
  else:
    n2.append(float(data[i]))

print(input_size)
print(n2)
print(nlgn)

# figure,anvas,axes object
fig = matplotlib.figure.Figure()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(111)

# plot(x, y)
ax.plot(input_size, n2, label='n^2')
ax.plot(input_size, nlgn, label='nlgn')
ax.set_xlim(500,6000)
ax.set_ylim(0.0, 0.04)
ax.set_xlabel('$input$ $size$ $n$')
ax.set_ylabel('$time$ $(s)$')
ax.set_title("n2 vs. nlgn")
ax.grid()
ax.legend()
fig.savefig(file_output, dpi = g_resolution)
