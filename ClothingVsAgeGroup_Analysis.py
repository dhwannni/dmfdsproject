import pandas as pd
import matplotlib.pyplot as plt

# analysis on product ratings
# which products have the highest ratings? which have the lowest and should be reconsidered?

# Read CSV----------------------------------
df = pd.read_csv('shopping_trends_updated.csv')

# clean data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Plot Data----------------------------------
# Calculate the average review rating for each item purchased
bins = [18, 25, 35, 45, 55, 65, float('inf')]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '>65']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Filter for items purchased in the Clothing category
df_clothing = df[df['Category'] == 'Clothing']

# Group and count the data by Age Group and Item Purchased (Clothing)
age_clothing_counts = df_clothing.groupby(['Item Purchased','Age Group']).size().unstack()

# Plotting a grouped bar chart
age_clothing_counts.plot(kind='bar')
plt.suptitle('Clothing Items Purchased vs Age Group', y=0.95, fontsize=16, ha='center')  # Adjust title position
plt.xlabel('Clothing Product')
plt.ylabel('Count')
plt.legend(title='Age Groups', loc='upper right')
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.xticks(rotation=45)
plt.show()
