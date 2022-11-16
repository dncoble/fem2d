'''
Library for running FEM1D processes. 

Author: Daniel Coble
Copyright (c) 2022
MIT License
'''
import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np
'''
FEMProblem contains all the variables used for
'''
class FEM1DProblemData():
    
    '''
    **kwargs are name, values to fill card
    card format:
        ----- card 1
        title
        ----- card 2
        model
        ntype
        item
        ----- card 3
        ielem
        nem \ generated automatically
        ----- card 4
        icont = 0 \ generated automatically
        nprnt
        ----- card 10
        nnm \ generated automatically
        ----- card 11 cards 11-15 are read for each element
        nod \ generated automatically
        glx
        ----- card 12
        ax0
        ax1
        ----- card 13
        bx0
        bx1
        ----- card 14
        cx0
        cx1
        ----- card 15
        fx0
        fx1
        fx2
        ----- card 16 cards 16-23 are only for truss/frame problems
        nnm \ generated automatically
        ----- card 17 skip cards 17-19 for truss problems. cards 17-21 are read
              for each element
        pr
        se
        sl
        sa
        si
        cs
        sn
        ----- card 18
        hf
        vf
        pf
        xb
        cnt
        snt
        ----- card 19
        nod \ generated automatically
        ----- card 20 skip cards 20-21 for frame problems.
        se
        sl
        sa
        cs
        sn
        hf
        ----- card 21
        nod \ generated automatically
        ----- card 22
        ncon \ generated automatically
        ----- card 23 repeat ncon times. skip card 23 if ncon=0
        icon
        vcon
        ----- card 24
        nspv \ generated automatically
        ----- card 25 repeat nspv times. skip card 25 if nspv=0
        ispv1
        ispv2
        vspv
        ----- card 26 skip card 26 for eigenvalue problems
        nssv \ generated automatically
        ----- card 27 repeat nssv times. skip card 27 if nssv=0
        issv1
        issv2
        vssv
        ----- card 28
        nnbc \ generated automatically
        ----- card 29 repeat nnbc times. skip card 29 if nnbc=0
        inbc1
        inbc2
        vnbc
        uref
        ----- card 30
        nmpc \ generated automatically
        ----- card 31 repeat nmpc times. skip card 31 if nmpc=0
        imc11
        imc12
        imc21
        imc22
        vmpc
        vmpc4
        ----- card 32 skip card 32 if item=0
        ct0
        ct1
        ----- card 33 skip cards 33-36 if item=0 or item=3
        dt
        alfa
        gama
        ----- card 34
        incond
        ntime
        intvl
        ----- card 35 skip cards 35-36 if incond=0
        guo
        ----- card 36 skip card 36 if item=1
        gui
        
    '''  
    def __init__(self, nodes_per_element, print_sol=True, **kwargs):
        self.vars = kwargs
        self.card = ''
        self.local_nodes = nodes_per_element
        self.print_sol = print_sol
        
        c = 1; nod = []
        for n in nodes_per_element:
            *l, = range(c, n+c)
            nod.append(l)
            c = l[-1]
        self.vars['nnm'] = c
        self.vars['nod'] = nod
        if(not 'title' in self.vars.keys()):
           self.vars['title'] = 'FEM 1D problem data'
        if(not 'nprnt' in self.vars.keys()):
            self.vars['nprt'] = 1
        
    def add_card(self, *args):
        for arg in args:
            self.card += str(arg) + ' '
        self.card += '\n'
    
    def build_cards(self):
        self.card = '' # clear card
        ############ cards 1-4, 10
        self.add_card(self.vars['title'])
        self.add_card(self.vars['model'], self.vars['ntype'], self.vars['item'])
        self.add_card(self.vars['ielem'], self.vars['nem'])
        self.add_card(0, self.vars['nprnt']) # set icont 0
        self.add_card(self.vars['nnm'])
        ############ cards 11-15
        for e in range(self.vars['nem']):
            self.add_card(*self.vars['nod'][e], self.vars['glx'][e])
            self.add_card(self.vars['ax0'][e], self.vars['ax1'][e])
            self.add_card(self.vars['bx0'][e], self.vars['bx1'][e])
            self.add_card(self.vars['cx0'][e], self.vars['cx1'][e])
            self.add_card(self.vars['fx0'][e], self.vars['fx1'][e], self.vars['fx2'][e])
        ############ cards 16-23
        if(self.vars['model'] == 4):
            self.add_card(self.vars['nnm'])
            for e in range(self.vars['nem']):
                if(self.vars['ntype'] != 0):
                    self.add_card(self.vars['pr'][e], self.vars['se'][e], self.vars['sl'][e],
                                  self.vars['sa'][e], self.vars['si'][e], self.vars['cs'][e],
                                  self.vars['sn'][e])
                    self.add_card(self.vars['hf'][e], self.vars['vf'][e], self.vars['pf'][e],
                                  self.vars['xb'][e], self.vars['cnt'][e], self.vars['snt'][e])
                else:
                    self.add_card(self.vars['se'][e], self.vars['sl'][e], self.vars['sa'][e],
                                  self.vars['cs'][e], self.vars['sn'][e], self.vars['hf'][e])
                self.add_card(*self.vars['nod'][e])
            if('icon' in self.vars):
                self.add_card(len(self.vars['icon'][e])) # ncon
                for icon_, vcon_ in zip(self.vars['icon'][e], self.vars['vcon'][e]):
                    self.add_card(icon_, vcon_)
            else:
                self.add_card(0)
        ############ cards 24-25
        if('ispv1' in self.vars):    
            self.add_card(len(self.vars['ispv1'])) # nspv
            for i in range(len(self.vars['ispv1'])):
                self.add_card(self.vars['ispv1'][i], self.vars['ispv2'][i], self.vars['vspv'][i])
        else:
            self.add_card(0)
        ############ cards 26-27
        if('issv1' in self.vars):
            self.add_card(len(self.vars['issv1'])) # nssv
            for i in range(len(self.vars['issv1'])):
                self.add_card(self.vars['issv1'][i], self.vars['issv2'][i], self.vars['vssv'][i])
        else:
            self.add_card(0)
        ############ cards 28-29
        if('inbc1' in self.vars):
            self.add_card(len(self.vars['inbc1'])) # nnbc
            for i in range(len(self.vars['nnbc'])):
                self.add_card(self.vars['inbc1'][i], self.vars['inbc2'][i], self.vars['vnbc'][i],
                              self.vars['uref'][i])
        else:
            self.add_card(0)
        ############ cards 30-31
        if('imcc11' in self.vars):
            self.add_card(len(self.vars['imc11'])) # nmpc
            for i in range(len(self.vars['imc11'])):
                self.add_card(self.vars['imc11'][i], self.vars['imc12'][i], self.vars['imc21'][i],
                          self.vars['imc22'][i], self.vars['vmpc'][i], self.vars['vmpc4'][i])
        else:
            self.add_card(0)
        ############ card 32-36
        if(self.vars['item'] != 0):
            self.add_card(self.vars['ct0'], self.vars['ct1'])
            if(self.vars['item'] != 3):
                self.add_card(self.vars['dt'], self.vars['alfa'], self.vars['gama'])
                self.add_card(self.vars['incond'], self.vars['ntime'], self.vars['intvl'])
                if(self.vars['incond'] != 0):
                    self.add_card(self.vars['guo'])
                    if(self.vars['item'] != 1):
                        self.add_card(self.vars('gui'))
        return self.card
    
    def save_card(self, filename):
        with open(filename, 'w') as f:
            f.write(self.card)
    
    def run(self):
        self.build_cards()
        self.save_card('tempcard.inp')
        # solve with subprocess
        result = subprocess.run([
            r"./fem1d/fem1d.exe", 'tempcard.inp', 'solved_card.txt'
        ])
        # while(not os.path.exists('solved_card.txt')):
        #     pass
        with open('solved_card.txt', 'r') as f:
            solution_card = f.read()
        if(self.print_sol):
            print(solution_card)
        os.remove('tempcard.inp')
        os.remove('solved_card.txt')
        return solution_card

'''
Contains solution data and supports certain postprocessing operations
'''
class FEMSolution:
    
    def __init__(self, solution_card):
        self.solution_card = solution_card
        i = solution_card.index('Shear Force') + 94
        l = np.fromstring(solution_card[i:-110])
        n = [j.split(' ') for j in l.split('\n')]
        m = []
        for k in n:
            r = []
            for j in k:
                if j != '':
                    r.append(float(j))
            m.append(r)
        data_mat = np.array(m)
    
    
'''
Special class-Euler Bernoulli beam with elements of equal length, two nodes per
element. Assists in generating problem data.

Does not support:
    - transient or eigenvalue analysis
    - more than two nodes per element
    - mixed boundary conditions
    - multipoint constraints
'''
class EulerBernoulliBeam(FEM1DProblemData):
    
    def linear_gen_array(self, g):
        g0 = [] # intercepts
        g1 = [] # slopes
        for x, dx in zip(self.node_points[:-1], self.glx):
            x0 = x + .25*dx
            x1 = x + .75*dx
            gx0 = g(x0)
            gx1 = g(x1)
            s = (gx1-gx0)/(.5*dx) # slope
            o = gx0 - s*(.25*dx)# intercept
            g0.append(o)
            g1.append(s)
        return g0, g1
        
    
    def __init__(self, length, num_elements, b=None, c=None, f=None, glx=None, 
                 print_sol=True, **kwargs):
        self.solved = False
        self.length = length
        self.num_elements = num_elements
        self.num_nodes = num_elements + 1
        self.glx = [length/num_elements]*num_elements if glx == None else glx
        if(glx == None): # nodes of equal length    
            self.node_points = [i*length/(num_elements) for i in range(num_elements+1)]
        else:
            self.node_points = [0] + [sum(glx[0:i+1]) for i in range(len(glx))]
        
        self.local_node_points = [self.node_points[0]]
        for n in self.node_points[1:-1]:
            self.local_node_points += [n]*2
        self.local_node_points.append(self.node_points[-1])
        self.a = lambda x:0
        self.b = b if b != None else lambda x:0
        self.c = c if c != None else lambda x:0
        self.f = f if f != None else lambda x:0
        
        # initial data
        data = kwargs
        data['model'] = 3; data['ntype'] = 0; data['item'] = 0
        data['ielem'] = 0; data['nem'] = num_elements
        data['nprnt'] = 1
        
        data['glx'] = self.glx
        
        data['ax0'], data['ax1'] = self.linear_gen_array(self.a)
        data['bx0'], data['bx1'] = self.linear_gen_array(self.b)
        data['cx0'], data['cx1'] = self.linear_gen_array(self.c)
        data['fx0'], data['fx1'] = self.linear_gen_array(self.f)
        data['fx2'] = [0]*num_elements
        
        nodes_per_element=[2]*num_elements
        super().__init__(nodes_per_element, print_sol=print_sol, **data)
    
    '''
    x: value of the boundary condition
    loc: (float) x position of boundary condition (must be a nodal point)
    var_type: 'w', 'theta', 'm', or 'v'
    '''
    def specify_dof(self, x, loc, var_type):
        node = self.node_points.index(loc) + 1
        primary = var_type == 'w' or var_type == 'theta'
        secondary = var_type == 'm' or var_type == 'v'
        dof = 1 if (var_type == 'w' or var_type == 'v') else 2
        if(primary):
            if(not 'ispv1' in self.vars):
                self.vars['ispv1'] = []
                self.vars['ispv2'] = []
                self.vars['vspv'] = []
            self.vars['ispv1'].append(node)
            self.vars['ispv2'].append(dof)
            self.vars['vspv'].append(x)
        if(secondary):
            if(not 'issv1' in self.vars):
                self.vars['issv1'] = []
                self.vars['issv2'] = []
                self.vars['vssv'] = []
            self.vars['issv1'].append(node)
            self.vars['issv2'].append(dof)
            self.vars['vssv'].append(x)
    
    def run(self):
        solution_card = super().run()
        i = solution_card.index('Shear Force') + 94
        l = solution_card[i:-110]
        n = [j.split(' ') for j in l.split('\n')]
        m = []
        for k in n:
            r = []
            for j in k:
                if j != '':
                    r.append(float(j))
            m.append(r)
        data_mat = np.array(m)
        # data postprocessing
        x_local = data_mat[:,0]
        start_indices = [i for i, x in enumerate(x_local) if x == 0] + [x_local.size]
        local_matrices = [data_mat[start_indices[i]:start_indices[i+1],:] for i in range(len(start_indices[:-1]))]
        # prepend the global coordinates
        x = 0
        self.local_matrices = local_matrices
        for i, e in enumerate(local_matrices):
            local_matrices[i] = np.append(x+e[:,0:1], e, axis=1)
            x += e[-1, 0]
        global_matrix = local_matrices[0]
        for e in local_matrices[1:]:
            global_matrix = np.append(global_matrix, e, axis=0)
        
        self.local_matrices = local_matrices
        self.global_matrix = global_matrix
        self.x = global_matrix[:,0]
        self.x_local = global_matrix[:,1]
        self.w = global_matrix[:,2]
        self.theta = global_matrix[:,3]
        self.m = global_matrix[:,4]
        self.v = global_matrix[:,5]
        self.solved = True
        return solution_card
    
    # functions for primary and secondary variables after system is solved
    def displacement(self, x):
        if(self.solved):
            return np.interp(x, self.global_matrices[:,0], self.global_matrices[:,2])
        return 0
    
    def rotation(self, x):
        if(self.solved):
            return np.interp(x, self.global_matrices[:,0], self.global_matrices[:,3])
        return 0
    
    def moment(self, x):
        if(self.solved):
            return np.interp(x, self.global_matrices[:,0], self.global_matrices[:,4])
        return 0
    
    def shear_force(self, x):
        if(self.solved):
            return np.interp(x, self.global_matrices[:,0], self.global_matrices[:,5])
        return 0
    
    def plot_beam(self):
        xrange = np.arange(0, self.length, 0.01)
        frange = np.array([self.f(x) for x in xrange])
        plt.figure()
        plt.xticks(self.node_points)
        plt.yticks([])
        plt.plot(xrange, frange, c='k')
        plt.plot(self.node_points[:-1], self.vars['fx0'], c='k', marker='o', linewidth=0)
        plt.tight_layout()
        plt.show()