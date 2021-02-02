import matplotlib.pyplot as plt

data = {'mercedes': 11, 'renault': 16, 'ferrari': 6, 'fiat': 21}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Qual è il marchio più venduto?')


plt.show()