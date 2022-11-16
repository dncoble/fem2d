# fem1d
Python wrapper for FEM1D program from J.N. Reddy. Use this to generate the problem data cards or alternatively solve straight from python. 
## How to use
### FEM1DProblemData
Initialize an `FEM1DProblemData` object with the list `nodes_per_element` pass the problem data as a dictionary to `**kwargs`. 
```
nodes_per_element = [2, 3, 2, 2]
problem_data = {...} # dictionary
fea_mesh = FEM1DProblemData(nodes_per_element, **problem_data)
fea_mesh.save_card('example.inp') # to produce the data card file
solution = fea_mesh.run() # to run the problem and get the output card as a string
```
Names and descriptions of the required problem data are given in the table below. Some data is generated automatically when the information is redundant.

### EulerBernoulliBeam
For Euler-Bernoulli beam steady-state deflection problems, `EulerBernoulliBeam` implements `FEM1DProblemData` with a higher level interface. Pass `a`, `b`, `c`, and `f` as functions, and as long as they are piecewise linear breaking at node points, the code will calculate the problem data. Add boundary constraints or other DOF constraints with the method `specify_dof(x, loc, var_type)`.

```
def f(x): # example loading
    if(x >=0 and x <= 1):
        return 8000 - 8000*x
    if(x>= 2 and x<= 4):
        return 8000
    return 0

EI = 3000000
b = lambda x: EI

beam = EulerBernoulliBeam(6, 6, f=f, b=b, title='Euler Bernoulli Beam, 6 elements')
beam.specify_dof(0, 0, 'w') # deflection left boundary condition
beam.specify_dof(0, 0, 'm') # moment left boundary condition
beam.specify_dof(0, 2, 'w')
beam.specify_dof(0, 4, 'w')
beam.specify_dof(0, 6, 'w') # deflection right boundary condition
beam.specify_dof(-2000, 6, 'm') # moment right boundary condition

beam.run()
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

I couldn't verify the license for FEM1D by J.N. Reddy, although the program is [freely available](https://highered.mheducation.com/sites/0072466855/student_view0/executables.html) on the McGraw Hill website. Before running the code, download the .exe and place it in [/fem1d](/fem1d).
