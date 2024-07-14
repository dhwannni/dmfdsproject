import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shopping_trends_updated.csv')

#grouping by season and category
season_category_sum = df.groupby(['Season', 'Category'])['Purchase Amount (USD)'].sum().unstack()

#plotting data
season_category_sum.plot(kind='line', marker='x')

# customizing the plot
plt.title('Seasonal Purchase Amount by Category')
plt.xlabel('Season')
plt.ylabel('Total Purchase Amount (USD)')
# position anchor because its out of place
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
