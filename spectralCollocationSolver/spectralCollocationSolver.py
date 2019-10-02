from barycentricLagrangeInterpolation import InterpolatingFunction
from scipy.optimize import least_squares
from scipy.optimize import differential_evolution
from scipy.optimize import brute
from scipy.optimize import basinhopping
from scipy.optimize import shgo

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
        
    def solve(self, init, args, plot=False):
        '''
        This method solves the searches for the optimal solution to the provided differential equation.
        
        Parameters:
        init (ndarray(nNodes)): initial values of interpolating function at grid points
        args (tuple): tuple of args as neccessary in the "residuals" method
        
        Returns:
        scipy.optimize.optimize.OptimizeResult: result of solution search
        '''
        solution = least_squares(self.residuals,init,kwargs={"args":[args]},method='trf')
        #solution = brute(self.residuals,init,args=[args])
        return solution
    
    
    def createInit(self, init, args):
        '''
        searches for a globally optimal solution for a small number of sampling points,
        in order to use this solution as inital values for a least squares optimization on a finer grid
        
        Parameters:
        init (ndarray(nNodes)): initial values of interpolating function at grid points
        args (tuple): tuple of args as neccessary in the "residuals" method
        
        Returns:
        tbd
        '''
        #solution = least_squares(self.residuals,init,args=[args],method='trf')
        #solution = brute(self.residuals,init,args=tuple([args]),Ns=10)
        solution = basinhopping(self.residuals,init,minimizer_kwargs={"args":[args]})
        #solution = differential_evolution(self.residuals,init,args=tuple([args]))
        #solution = shgo(self.residuals,init,args=tuple([args]))
        return solution
    
    def getInitValues(self, points, values, weights, nodes, noiseScale):
        '''
        evalutes the raw inital solution at the new grid points
        
        Parameters:
        points(ndarray): grid points to evaluate function at
        values(ndarray): values at grid points of raw solution
        weights(ndarray): weights of raw solution
        nodes(ndarray): nodes of raw solution
        noiseScale(double): scaling factor of noise for perturbation of raw solution
        
        Returns:
        ndarray: values of raw solution at points of new grid
        '''
        initValues = np.ones(len(points))
        for i in range(len(points)):
            initValues[i] = self.f.evaluateFunction(points[i], values, weights, nodes)
        noiseCoeff = np.random.standard_normal(len(initValues))*noiseScale + 1
        return initValues*noiseCoeff