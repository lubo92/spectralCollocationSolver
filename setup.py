from setuptools import setup

setup(name='spectralCollocationSolver',
      version='1.0.0',
      description='package contains functionality for solving a (non linear) differential equation with a spectral collocation method based on a barycentric Lagrange interpolation',
      author='Wolfgang Lubowski',
      author_email='w.lub92@gmail.com',
      packages=['spectralCollocationSolver'],
      python_requires='>=3.0',
      install_requires=['numpy','matplotlib'],
      classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4'
      ],
      zip_safe=False)
