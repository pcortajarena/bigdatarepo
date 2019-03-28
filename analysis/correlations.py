import seaborn as sns
from ..cleaning import cleaning_data as cd


dataset = cd.load_data()
dataset['norm_energy'] = dataset['energy']/dataset['power']
subset = dataset.sample(n=len(dataset)//30, random_state=42)
sns.pairplot(subset)