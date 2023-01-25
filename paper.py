import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_paper():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    paper = f.generate()
    # Add noise to the fractal shape to make it look more like paper
    noise = np.random.normal(0, 0.05, paper.shape)
    paper = paper + noise
    paper = np.clip(paper, 0, 1)
    # Apply a paper-like color map to the fractal shape
    paper = plt.cm.gray(paper)
    # Return the fractal paper
    return paper

# Generate 10 fractal paper images
for i in range(10):
    paper = generate_fractal_paper()
    plt.imsave("fractal_paper_{}.png".format(i), paper)
