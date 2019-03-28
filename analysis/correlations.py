import seaborn as sns
from cleaning import cleaning_data as cd
import matplotlib.pyplot as plt
import os

GOOGLE_COLAB = False

for boolean in [True]:
    SOLAR = boolean
    FILENAME = 'solar_energy_norm.png' if SOLAR else 'wind_energy_norm.png'
    dataset, _ , _ = cd.load_data(GOOGLE_COLAB, SOLAR)
    dataset['norm_energy'] = dataset['energy']/dataset['power']
    sns.pairplot(dataset)
    plt.savefig(os.path.join('images', FILENAME))