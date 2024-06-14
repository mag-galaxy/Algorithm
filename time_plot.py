import matplotlib.backends.backend_agg
import matplotlib.figure

file_out = 'maxflow.png'

edge = []
vertex = []
capacity = []
time_ed = []
time_fat = []

with open ('time_result.txt', 'r') as f_read:
    all_data = f_read.read()
    line = all_data.split('\n')
    for i in range(len(line)):
        data = line[i].split()
        vertex.append(int(data[0]))
        edge.append(int(data[1]))
        capacity.append(int(data[2]))
        time_ed.append(float(data[3]))
        time_fat.append(float(data[4]))
f_read.close()

# figure,anvas,axes object
fig = matplotlib.figure.Figure()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)
ax1 = fig.add_subplot(111)

ax1.plot(vertex, time_ed, label='shortest path')
ax1.plot(vertex, time_fat, label='fattest path')
ax1.set_xlim(10,5000)
ax1.set_ylim(0.0, 90)
ax1.set_xlabel('$vertices$ $number$ $|V|$')
ax1.set_ylabel('$time$ $(s)$')
ax1.set_title("shortest path vs. fattest path")
ax1.grid()
ax1.legend()
fig.savefig(file_out, dpi = 200)
