from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(9, 3))

x = np.linspace(0, 10, 50)

sine = np.sin(x)
cos = np.cos(x)

plt.plot(x, sine, label="sine", color="blue", lineStyles="--", linewid)