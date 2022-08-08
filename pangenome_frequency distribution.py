import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

genepa = pd.read_csv("gene presence absence.txt", sep = "\t")

sns.set_theme(style="whitegrid")
sns.set_style("ticks")
ax = sns.barplot(x="No. of Genomes", y="No. of Genes", data = genepa,
                 color='grey')

for bar in ax.patches:
    if bar.get_height() > 2000:
        bar.set_color('green')
    elif bar.get_height() > 1500:
        bar.set_color('red')
    else:
        bar.set_color('grey')

#ax.patch.set_visible(False)
#frameon=False
sns.despine(right=True, bottom=True)
plt.tick_params(axis = "x", which = "both", bottom = False, top = False)
plt.show()
