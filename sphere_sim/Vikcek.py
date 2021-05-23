"""
Author : Fumiya Tokoro
2021/05/19

Vickek Model with Python
"""

import matplotlib.pyplot as plt
import numpy as np
import random
#import seaborn as sns

numParticle = 1000
L = 10.0
V_0 = 0.1
ETA = 0.05
R = 0.5


class Particle():

    def __init__(self):
        self.x = np.empty(2*numParticle)
        self.v = np.empty(2*numParticle)

        self.theta   = np.empty(numParticle)
        self.theta_N = np.empty(numParticle)

        self.value   = np.zeros(numParticle)

        for id in range(numParticle):
            self.x[2*id + 0] = random.uniform(-L/2 , L/2)
            self.x[2*id + 1] = random.uniform(-L/2 , L/2)

            self.theta[id] = random.uniform(0,2*np.pi)

            self.v[2*id + 0] = V_0 * np.cos(self.theta[id])
            self.v[2*id + 1] = V_0 * np.sin(self.theta[id])

        #print(self.x)
        self.iter = 0

    def Calculate(self):

        for id in range(numParticle):
            tvx = np.cos(self.theta[id])
            tvy = np.sin(self.theta[id])

            for j in range(numParticle):
                if(id == j):
                    continue


                rx = self.x[2*id+0] - self.x[2*j+0]
                ry = self.x[2*id+1] - self.x[2*j+1]

                r = np.sqrt(rx**2 + ry**2)

                if (rx >  L/2):
                    rx -= L
                if (rx < -L/2):
                    rx += L
                if (ry >  L/2):
                    ry -= L
                if (ry < -L/2):
                    ry += L

                if (r<R):
                    tvx += np.cos(self.theta[j])
                    tvy += np.sin(self.theta[j])
                    self.value[j] += 1
            self.theta_N[id] = np.arctan2(tvy, tvx) + ETA * random.uniform(-np.pi, np.pi)

            self.v[2*id + 0] = V_0 * np.cos(self.theta_N[id])
            self.v[2*id + 1] = V_0 * np.sin(self.theta_N[id])




    def Update(self):
        for id in range(numParticle):

            self.theta[id] = random.uniform(0, 2*np.pi)

            #self.v[2 * id + 0] = V_0 * np.cos(self.theta[id])
            #self.v[2 * id + 1] = V_0 * np.sin(self.theta[id])

            #particle new position
            self.x[2*id + 0] += self.v[2*id + 0]
            self.x[2*id + 1] += self.v[2*id + 1]


            #piriodic boundary condition

            if (self.x[2*id + 0] > L/2):
                self.x[2*id + 0] -= L
            if (self.x[2*id + 0] < -L/2):
                self.x[2*id + 0] += L
            if (self.x[2*id + 1] > L/2):
                self.x[2*id + 1] -= L
            if (self.x[2*id + 1] < -L/2):
                self.x[2*id + 1] += L

            self.theta[id] = self.theta_N[id]

    def Output(self):
        fig, ax = plt.subplots()
        ax.set_xlim(-L/2, L/2)
        ax.set_ylim(-L/2, L/2)

        plt.scatter(self.x[0::2], self.x[1::2], s=50, c=self.value, cmap='gist_ncar')
        #plt.colorbar()

        fig.savefig('image/image{}.png' % self.iter,format = 'png')


if __name__ == '__main__':
    particle = Particle()

    for iter in range(300):
        particle.Calculate()
        particle.Update()
        particle.Output()
        print('now calculating image{}'.format(iter))
        particle.iter += 1


