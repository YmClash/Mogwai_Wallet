import numpy as np

import matplotlib.pyplot as plot
import matplotlib.animation as animation

# les  constante

gril_X = 10
gril_Y = 10

# Probabilite cellule morte et celulle vivante
cell_A = 0.6
cell_B = 0.4

# les regle

regle_1_a = 2
regle_1_b = 3

regle_2_a =3
regle_2_b = 0




# compteur
nombre_cycle = 0
cycle_detect = False
etat = []

# grid = np.zeros((X, Y))
grid = np.random.choice([0, 1], size=(gril_X, gril_Y), p=[cell_A, cell_B])

fig, ax = plot.subplots()


def update(frame):
    global grid, nombre_cycle, cycle_detect, etat

    new_grid = np.copy(grid)
    for i in range(gril_X):
        for o in range(gril_Y):
            # on compte les voisin vivant
            vivant = np.sum(grid[max(0, i - 1):min(gril_X, i + 2), max(0, o - 1):min(gril_Y, o + 2)]) - grid[i, o]
            if grid[i, o] == 1:
                # regle pour une cellule vivante
                if vivant < regle_1_a or vivant > regle_1_b:
                    new_grid[i, o] = 0
            else:
                # Regle pour une cellule morte
                if vivant == regle_2_a:
                    new_grid[i, o] = 1

    if not cycle_detect:
        etat_current = new_grid.tobytes()
        if etat_current in etat:
            cycle_detect = True
        else:
            etat.append(etat_current)
            nombre_cycle += 1

    grid = new_grid
    ax.imshow(grid, cmap='binary')
    ax.set_title(f'Nombre de Cycle: {nombre_cycle}')
    return ax



# plateau = plot.figure()
#
# img = plot.imshow(grid, interpolation='nearest', cmap='binary')

anim = animation.FuncAnimation(fig, update, frames=100, interval=200)

plot.show()
