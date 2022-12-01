# fem2d
Python wrapper for FEM2D program from J.N. Reddy. Use this to generate the problem data cards or alternatively solve straight from python. Postprocessing uses a polynomial fit to smooth the solution.
## How to use
### FEM2DProblemData
I highly recommend initializing `FEM2DProblemData` with the arrays `elem_connectivity` and `node_cords` generated with another software. Pass the problem data as a dictionary to `**kwargs`. After running `postprocess`, the variables `u`, `qx`, and `qy` can be accessed using `get_var`.
```
elem_connectivity = ...
node_coords = ...
problem_data = {...} # dictionary
fea_mesh = FEM2DProblemData(elem_connectivity, node_coords, **problem_data)
fea_mesh.save_card('example.inp') # to produce the data card file
solu = fea_mesh.run() # to run the problem and get the output card as a string
fea_mesh.postprocess()
points_of_interest = ... # points where we want to find fea solution
u = fea_mesh.get_var('u', points_of_interest)
qx = fea_mesh.get_var('qx', points_of_interest)
qy = fea_mesh.get_var('qy', points_of_interest)
```
See [data_format.md](data_format.md) for how to format the problem data dictionary. Variables follow same names as given in the FEM2D Input Description. Some data is generated automatically when the information is redundant.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

I couldn't verify the license for FEM2D by J.N. Reddy, although the program is [freely available](https://highered.mheducation.com/sites/0072466855/student_view0/executables.html) on the McGraw Hill website. Before running the code, download the .exe and place it in [/fem2d](/fem2d).
