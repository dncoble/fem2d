'''
Library for running FEM2D processes. 

Author: Daniel Coble
Copyright (c) 2022
MIT License
'''
import subprocess
import os
import numpy as np
'''
FEM2DProblem contains all the variables used for
'''
class FEM2DProblemData():
    
    '''
    **kwargs are name, values to fill card
    card format:
        ----- card 1
        title
        ----- card 2
        itype
        igrad
        item
        neign
        ----- card 3 skip card 3 if neign=0
        nvalu
        nvctr
        ----- card 4
        ieltyp
        npe
        mesh
        nprnt
        ----- card 5 skip card 5 if mesh=1
        nem
        nnm
        ----- card 6 skip cards 6-7 if mesh!=0, read card 6 for each element
        nod
        ----- card 7 loop on 1...nnm and x and y coordinate
        glxy
        ----- card 8 skip cards 8-11 if mesh<=1
        nrecl
        ----- card 9 read card 9 nrecl times
        nod1
        nodl
        nodinc
        x1
        y1
        xl
        yl
        ratio
        ----- card 10
        nrecel
        ----- card 11 read card 11 nrecel times
        nel1
        nell
        ielinc
        nodinc
        npe
        nodei
        ----- card 12 skip cards 12-14 if mesh!=1
        nx
        ny
        ----- card 13
        x0
        dxi
        ----- card 14
        y0
        dyi
        ----- card 15
        nspv
        ----- card 16 skip card 16 if nspv=0, repeat nspv times
        ispv
        ----- card 17 if nspv=0 or neign!=0
        vspv
        ----- card 18 skip card 18 if neign!=0
        nssv
        ----- card 19 skip card 19 if nssv=0 or neign!=0
        issv
        ----- card 20 skip card 20 if nssv=0 or neign!=0
        vssv
        ----- card 21 skip cards 21-27 if itype!=0
        a10
        a1x
        a1y
        ----- card 22
        a20
        a2x
        a2y
        ----- card 23
        a00
        ----- card 24
        iconv
        ----- card 25
        nbe
        ----- card 26 repeat nbe times
        ibn
        beta
        tinf
        ----- card 27 repeat nbe times
        inod
        ----- card 28 skip card 28 if itype!=1
        viscity
        penalty
        ----- card 29 skip cards 29-30 if itype!=2
        lnstrs
        ----- card 30
        e1
        e2
        anu12
        g12
        thkns
        ----- card 31 skip card 31 if itype!=3 or 5
        e1
        e2
        anu12
        g12
        g13
        g23
        thkns
        ----- card 32 skip card 32 if neign!=0
        f0
        fx
        fy
        ----- card 33 skip card 33 if item=0
        c0
        cx
        cy
        ----- card 34 skip cards 34-35 if item=0 or neign!=0
        ntime
        nstp
        intvl
        intial
        ----- card 35
        dt
        alfa
        gama
        epsln
        ----- card 36 skip card 36 if item=0 or intial=0 or neign!=0, repeat neq times
        glu
        ----- card 37 skip card 37 item<=0 or neign!=0 or intial=0, repeat neq times
        glv
        
    '''  
    def __init__(self, nodes_per_element, print_sol=True, **kwargs):
        self.vars = kwargs
        self.card = ''
        
        
    def add_card(self, *args):
        for arg in args:
            self.card += str(arg) + ' '
        self.card += '\n'
    
    def build_cards(self):
        self.card = '' # clear card
        ############ cards 1-4, 10
        return self.card
    
    def save_card(self, filename):
        with open(filename, 'w') as f:
            f.write(self.card)
    
    def run(self):
        self.build_cards()
        self.save_card('tempcard.inp')
        # solve with subprocess
        result = subprocess.run([
            r"./fem2d/fem2d.exe", 'tempcard.inp', 'solved_card.txt'
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