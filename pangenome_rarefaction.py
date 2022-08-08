import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data
conservedgenes = pd.read_csv("number of conserved genes4.txt", sep = "\t")
totalgenes = pd.read_csv("number of genes in pan genome4.txt", sep = "\t")



# import data
#conserved_genes = pd.read_csv("number of conserved genes.txt", sep = "\t")
#no_of_genes = pd.read_csv("number of genes in pan genome.txt", sep = "\t")

#axis = conserved_genes.boxplot(return_type='axes')
#no_of_genes.boxplot(ax=axis)

# plot formatting
sns.set_theme(style="whitegrid")
sns.despine(right=True)
sns.set_style("ticks")
sns.set_palette("husl", 3)
ax = sns.lineplot(x="No. of Genomes", y="No. of Genes", data=conservedgenes)
ax = sns.lineplot(x="No. of Genomes", y="No. of Genes", data=totalgenes)

plt.ylim(4000,10000)
plt.xlim(0,10)
plt.yticks([4000,6000,8000,10000])


# removing x-axis grid lines
#axis.xaxis.grid(False)

#display plot
plt.show()

