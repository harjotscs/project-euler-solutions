
# -*- coding: utf-8 -*-
'''
    File name: shortest_lattice_vector\solution__507.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #507 :: Shortest Lattice Vector
# 
# For more information see:
# https://projecteuler.net/problem=507

# Problem Statement 
'''
b'Let $t_n$ be the tribonacci numbers defined as:\n$t_0 = t_1 = 0$;\n$t_2 = 1$;\n$t_n = t_{n-1} + t_{n-2} + t_{n-3}$ for $n \\ge 3$\nand let $r_n = t_n \\text{ mod } 10^7$.\n\n\nFor each pair of Vectors $V_n=(v_1,v_2,v_3)$ and $W_n=(w_1,w_2,w_3)$ with $v_1=r_{12n-11}-r_{12n-10}, v_2=r_{12n-9}+r_{12n-8}, v_3=r_{12n-7} \\cdot r_{12n-6}$  and  $w_1=r_{12n-5}-r_{12n-4}, w_2=r_{12n-3}+r_{12n-2}, w_3=r_{12n-1} \\cdot r_{12n}$\n\n\nwe define $S(n)$ as the minimal value of the manhattan length of the vector $D=k \\cdot V_n+l \\cdot W_n$ measured as $|k \\cdot v_1+l \\cdot w_1|+|k \\cdot v_2+l \\cdot w_2|+|k \\cdot v_3+l \\cdot w_3|$\n for any integers $k$ and $l$ with $(k,l)\\neq (0,0)$.\n\nThe first vector pair  is (-1, 3, 28), (-11, 125, 40826).\nYou are given that $S(1)=32$ and $\\sum_{n=1}^{10} S(n)=130762273722$.\n\n\nFind $\\sum_{n=1}^{20000000} S(n)$.'
'''

# Solution 

# Solution Approach 
'''
'''