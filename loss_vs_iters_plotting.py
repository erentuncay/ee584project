# This file is used for plotting "Loss vs Iterations" graphs.

import numpy as np
import matplotlib.pyplot as plt

losses = np.zeros(5990)
iters = np.zeros(5990)
line_infos = []

with open('./training_dir/MEGA_R_101_1x/log.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    if "mega_core.trainer INFO: eta:" in line:
        line_infos.append(line)
    else:
        continue

for i in range(len(line_infos)):
    iters[i] = line_infos[i].split("iter:")[1].strip().split(" ")[0]
    losses[i] = line_infos[i].split("loss:")[1].strip().split(" ")[0]

plt.plot(iters,losses)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Training Loss vs Iterations')
plt.show()