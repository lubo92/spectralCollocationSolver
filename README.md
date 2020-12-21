# Spectral Collocation Method Differential Equation Solver

## References
This package was developed by Wolfgang Lubowski for a project in fluid dynamics and heat transfer with the title "Solution of Prandtl’s boundary layer equations with a spectral collocation method based on barycentric Lagrange interpolation" supervised by Stefan Braun, institute of fluid mechanics and heat transfer, TU Wien in May 2020.

The implementation closely follows these papers:

R. Baltensperger and M. R. Trummer. Spectral differencing with a twist. SIAM J. Sci. Comp., 24(5):1465–1487, 2003.

J.-P. Berrut and L. N. Trefethen. Barycentric lagrange interpolation. SIAM Rev., 46(3):501–517, 2004.

## What does this package provide?
This package provides an differential equation sovler with the a spectral collocation method. This means, a differential equation is solved by interpolating the target function and solving the differential equation at every node (sampling point) of the interpolation. It can solve (nonlinear) differential equations of any degree. Partial differential equations are not supported. Since the underlying interpolation is a barycentric Lagrange interpolation on Gauss-Lobatto nodes (aka Chebishev points of second kind) this tool only works on the domain [-1,1].

If you need to operate on a domain other than [-1,1], you need to transform your variables, but be cautious since you also need to take this into account in your derivatives. For an example see my repository on solving the Blasius equation.

In order to make application easier, an example Jupyter notebook is also included.

## How do you install this package?
### Requirements
* numpy
* scipy
* matplotlib
* [barycentricLagrangeInterpolation](https://github.com/lubo92/barycentricLagrangeInterpolation)

This package requires Python 3, numpy and matplotlib.
### Get the package
#### Option 1: Download as zip (no git installation required)
Download this package as zip. Unpack it wherever it is suitable for you. When unpacked, run the following command in the package's base directory:
```
python3 setup.py install
```
Or if your Python installation requires root permission:
```
sudo -H python3 setup.py install
```
#### Option 2: Clone the repository
Clone the repository from Github:
```
git clone https://github.com/lubo92/spectralCollocationSolver
```
Then run the following command in the package's base directory:
```
python3 setup.py install
```
Or if your Python installation requires root permission:
```
sudo -H python3 setup.py install
```

## Examples
An usage example Jupyter notebook is provided in the file example.ipynb.

## Applications
I used this package to solve the Blasius equation. You can find this also on GitHub.

## Contact
If you have any questions - on the application of this package as well as on the mathematical background - don't hesitate to send an email to <w.lub92@gmail.com>.