clear all;
clc;
q_1 = 0
q_2 = pi/4
q_3 = -1*pi/2

l_1 = 1
l_2 = 1
l_3 = 1
a = 0
b = 0

origin_to_base = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]
b_to_0_rot = [0 0 1 0; -1 0 0 0; 0 -1 0 0; 0 0 0 1];
b_to_0_trans = [1 0 0 a; 0 1 0 -b; 0 0 1 0; 0 0 0 1];

zero_to_one_rot = [cos(q_1) -1*sin(q_1) 0 0; sin(q_1) cos(q_1) 0 0; 0 0 1 0; 0 0 0 1];
zero_to_one_trans = [1 0 0 l_1; 0 1 0 0; 0 0 1 0; 0 0 0 1];
zero_to_one_rot_2 = [0 0 1 0; 0 1 0 0; -1 0 0 0; 0 0 0 1];

one_to_two_rot = [cos(q_2) -1*sin(q_2) 0 0; sin(q_2) cos(q_2) 0 0; 0 0 1 0; 0 0 0 1];
one_to_two_trans = [1 0 0 0; 0 1 0 l_2; 0 0 1 0; 0 0 0 1];

two_to_three_rot = [cos(q_3) -1*sin(q_3) 0 0; sin(q_3) cos(q_3) 0 0; 0 0 1 0; 0 0 0 1];
two_to_three_trans = [1 0 0 0; 0 1 0 l_3; 0 0 1 0; 0 0 0 1];

b_to_three = b_to_0_rot * b_to_0_trans * zero_to_one_rot * zero_to_one_trans * zero_to_one_rot_2 * one_to_two_rot * one_to_two_trans * two_to_three_rot * two_to_three_trans 

