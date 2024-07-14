import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shopping_trends_updated.csv')

#plot data relating the two things
dfGrouped = df.groupby(['Season','Color']).size().unstack()
dfGrouped.plot(kind='bar')

#customizing the plot
plt.title('Popular Seasonal Colors')
plt.xlabel('Season')
plt.ylabel('Sales')
plt.legend(title='Colors')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.xticks(rotation=0)

#showing the plot
plt.show()





#--------- useful for debugging -------------------------------------
# PRINT WHOLE DF AS STRING
# print(df.to_string())

# PRINT # OF ROWS
# print(len(df))

# print only first 10 rows
#print(df.head(10))