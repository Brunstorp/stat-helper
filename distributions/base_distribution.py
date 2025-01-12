import matplotlib.pyplot as plt
import numpy as np

class BaseDistribution:
    def __init__(self, **params):
        self.params = params
        
    def validate_params(self):
        raise NotImplementedError("Subclasses must implement parameter validation.")
    
    def pdf(self, x):
        """Probability density function"""
        raise NotImplementedError("Subclasses must implement the PDF.")

    def cdf(self, x):
        """Cumulative density function"""
        raise NotImplementedError("Subclasses must implement the CDF.")
    
    def plot(self, x_min=0, x_max=1, num_points=10000):
        """Plot the PDF of the distribution."""
        x = np.linspace(x_min, x_max, num_points)
        y = self.pdf(x)
        plt.plot(x, y, label=f"{self.__class__.__name__} PDF")
        plt.title(f"{self.__class__.__name__} Distribution")
        plt.xlabel("X")
        plt.ylabel("Density")
        plt.legend()
        plt.grid(True)
        plt.show()