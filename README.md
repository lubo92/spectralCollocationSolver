# Spectral Collocation Method Differential Equation Solver

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

## Mathematical Background and Literature
The code provided in this package closeley follows this paper:

[Berrut, Jean-Paul, and Trefethen, Lloyd N. "Barycentric lagrange interpolation." SIAM review 46.3 (2004): 501-517.] (https://people.maths.ox.ac.uk/trefethen/barycentric.pdf)

## Examples
An usage example Jupyter notebook is provided in the file example.ipynb.

## Applications
I used this package to solve the Blasius equation. You can find this also on GitHub.

## Contact
If you have any questions - on the application of this package as well as on the mathematical background - don't hesitate to send an email to <w.lub92@gmail.com>.