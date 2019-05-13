from barycentricLagrangeInterpolation import InterpolatingFunction
from scipy.optimize import least_squares

import numpy as np
import matplotlib.pyplot as plt

class SpectralCollocationSolver(object):
    def __init__(self):
        print('initializing spectral collocation solver class')
        plt.rcParams["figure.figsize"] = [20, 7]
        
    def setupUtilities(self, nNodes):
        '''
        this method creates everything needed for barycentric Langrange interpolation
        and saves everything to a static variable:
        - grid points
        - according weights for grid points
        - basis functions
        - the matrices for first, second and third derivative
        
        Parameters:
        nNodes (int): number of grid points
        
        Returns:
        nothing (everyting saved to static variables)
        '''
        
        self.nNodes=nNodes         # number of grid points for interpolation
        self.nPoints=1000          # number of points calculated in interpolation function (not really important value)
        self.f = InterpolatingFunction()        # interpolating function class object
        self.nodes = self.f.calculateNodes(self.nNodes)        # grid points
        self.weights = self.f.calculateWeights(self.nodes)     # weights of grid points
        self.l= self.f.calculateBasisFunctions(self.nodes,self.weights,self.nPoints)        # basis functions
        self.D1 = self.f.differentiationMatrix(1,self.nodes,self.weights)    # matrix for first derivative
        self.D2 = self.f.differentiationMatrix(2,self.nodes,self.weights)    # matrix for second derivative
        self.D3 = self.f.differentiationMatrix(3,self.nodes,self.weights)    # matrix for third derivative
        
    def solve(self, init, args):
        solution = least_squares(self.residuals,init,args=[args])
        self.f.interpolateFunction(solution.x,self.l,plot=True,nodes=self.nodes)
        return solution