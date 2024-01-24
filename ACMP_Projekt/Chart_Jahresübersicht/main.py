import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.animation as animation


# Daten aus der CSV-Datei lesen
df = pd.read_csv('data.csv')

month = df['month'].tolist()  # Die Spalte in der CSV-Datei heißt "month"
opend = df['opend'].tolist()  # Die Spalte in der CSV-Datei heißt "opend"
closed = df['closed'].tolist() # Die Spalte in der CSV-Datei heißt "closed"

fig, axs = plt.subplots(figsize=(15, 6)) #figsize ändert die breite
linie1, = axs.plot(month, opend, color='orangered', label='opend', zorder=2) # Erste Linie
linie2, = axs.plot(month, closed, color='lime', label='closed', zorder=2)
axs.axhline(y=300, color='darkgray', linestyle='--', label='Anzahl der Tickets', zorder=1)
axs.axhline(y=400, color='darkgray', linestyle='--', zorder=1)
axs.axhline(y=500, color='darkgray', linestyle='--', zorder=1)
axs.axhline(y=600, color='darkgray', linestyle='--', zorder=1)
axs.axhline(y=700, color='darkgray', linestyle='--', zorder=1)
axs.axhline(y=800, color='darkgray', linestyle='--', zorder=1)
axs.legend()
fig.suptitle('Jahresübersicht der Erstellten & Geschlossenen Helpdesk-Tickets')

# Animation


def animate(i):

    linie1.set_data(month[:i +1], opend[:i +1])
    linie2.set_data(month[:i +1], closed[:i +1])
    return linie1, linie2

ani = animation.FuncAnimation(fig, animate, frames=len(month), interval=1000, blit=True)


plt.show()