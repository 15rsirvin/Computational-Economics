import quantecon as qe
import numpy as np

psi = (0.1, 0.9)
cdf = np.cumsum(psi)
qe.random.draw(cdf, 5)