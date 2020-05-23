clear all;
clc;
syms q_1 q_2 q_3 l_1 l_2 l_3 c_1 s_1 c_2 s_2 c_3 s_3 a b x y z

origin_zero = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]

b_to_0_rot = [0 0 1 0; -1 0 0 0; 0 -1 0 0; 0 0 0 1];
b_to_0_trans = [1 0 0 a; 0 1 0 -b; 0 0 1 0; 0 0 0 1];

zero_to_one_rot = [c_1 -s_1 0 0; s_1 c_1 0 0; 0 0 1 0; 0 0 0 1]
zero_to_one_trans = [1 0 0 l_1; 0 1 0 0; 0 0 1 0; 0 0 0 1];
zero_to_one_rot_2 = [0 0 1 0; 0 1 0 0; -1 0 0 0; 0 0 0 1];

one_to_two_rot = [c_2 -s_2 0 0; s_2 c_2 0 0; 0 0 1 0; 0 0 0 1]
one_to_two_trans = [1 0 0 0; 0 1 0 l_2; 0 0 1 0; 0 0 0 1];

two_to_three_rot = [c_3 -s_3 0 0; s_3 c_3 0 0; 0 0 1 0; 0 0 0 1]
two_to_three_trans = [1 0 0 0; 0 1 0 l_3; 0 0 1 0; 0 0 0 1];

origin_to_three = origin_zero * b_to_0_trans* zero_to_one_rot * zero_to_one_trans * zero_to_one_rot_2 * one_to_two_rot * one_to_two_trans * two_to_three_rot * two_to_three_trans 

x = a + cos(q_1)*l_1 - l_3*(cos(q_2)*cos(q_3)*s_1 - sin(q_1)*sin(q_2)*sin(q_3)) - cos(q_2)*l_2*sin(q_1)
y = l_1*sin(q_1)- b + l_3*(cos(q_1)*cos(q_2)*cos(q_3) - cos(q_1)*sin(q_2)*sin(q_3)) + cos(q_1)*cos(q_2)*l_2
z = l_2*sin(q_2) + l_3*(cos(q_2)*sin(q_3) + cos(q_3)*sin(q_2))

dx_dq_1 = diff(x, q_1)
dx_dq_2 = diff(x, q_2)
dx_dq_3 = diff(x, q_3)
dy_dq_1 = diff(y, q_1)
dy_dq_2 = diff(y, q_2)
dy_dq_3 = diff(y, q_3)
dz_dq_1 = diff(z, q_1)
dz_dq_2 = diff(z, q_2)
dz_dq_3 = diff(z, q_3)

jacobian = [dx_dq_1 dx_dq_2 dx_dq_3; dy_dq_1 dy_dq_2 dy_dq_3; dz_dq_1 dz_dq_2 dz_dq_3]
jacobian_det = det(jacobian)

origin_zero_to_one_rot = origin_zero * zero_to_one_rot * zero_to_one_trans* zero_to_one_rot_2 * one_to_two_rot*one_to_two_trans;

