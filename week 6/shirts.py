import matplotlib.pyplot as plt
import numpy as np

data = """BLACKMEDIUMBLACKLARGEIVORYLARGEBLUELARGEBLUESMALLBLACKSMALLIVORYLARGEBLUEXLARGEIVORYLARGEPINKLARGEBLUELARGEBLACKLARGEIVORYLARGEPINKMEDIUMIVORYXLARGEIVORYLARGEPINKMEDIUMBLUEXLARGEIVORYLARGEPINKLARGEBLACKLARGEPINKMEDIUMBLACKLARGEBLUELARGEBLACKLARGEIVORYLARGEBLACKLARGEIVORYMEDIUMBLUEMEDIUMPINKMEDIUMBLACKXLARGEIVORYLARGEBLUELARGEPINKXLARGEIVORYMEDIUMBLUELARGEBLACKMEDIUMPINKSMALLIVORYMEDIUMPINKSMALLIVORYLARGEPINKLARGEBLACKXLARGEPINKXLARGEBLACKMEDIUMBLUEMEDIUMIVORYMEDIUMIVORYLARGEWHITEXLARGEIVORYLARGEBLUEMEDIUMBLACKXLARGEBLACKMEDIUMBLUEMEDIUM""".split()

counts = {}
for colorsize in data:
    color, size = colorsize.split(sep=None, maxsplit=1)
    counts[(color, size)] = counts.get((color, size), 0) + 1

colors, sizes = zip(*counts.keys())
colors, sizes = set(colors), set(sizes)

ind = np.arange(len(sizes))
width = 0.2

fig, ax = plt.subplots()
for i, color in enumerate(colors):
    counts_for_color = [counts.get((color, size), 0) for size in sizes]
    ax.bar(ind + i*width, counts_for_color, width, label=color)

ax.set_xticks(ind + width)
ax.set_xticklabels(sizes)
ax.legend()

plt.show()
