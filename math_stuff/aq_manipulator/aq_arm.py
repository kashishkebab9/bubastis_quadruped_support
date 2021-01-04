#!/usr/bin/python

import math
import numpy as np

q_0 = 0
q_1 = 0
q_2 = 0
q_3 = 0
q_4 = 0
q_5 = 0
q_6 = 0

a_offset = 1
l_1 = 1
l_2 = 1
l_3 = 1
l_4 = 1
l_5 = 1
l_6 = 1
l_7 = 1
j_0_x_rot = -(math.pi/2)
j_1_x_rot = (math.pi/2)

base_to_zero_rot = np.matrix([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
base_to_zero_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, -a_offset], [0, 0, 1, 0], [0, 0, 0, 1]])
base_to_zero = base_to_zero_trans * base_to_zero_rot

zero_to_one_act = np.matrix([[math.cos(q_0), -math.sin(q_0), 0, 0], [math.sin(q_0), math.cos(q_0), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
zero_to_one_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, l_1], [0, 0, 0, 1]])
zero_to_one_rot = np.matrix([[1, 0, 0, 0], [0, math.cos(j_0_x_rot), -math.sin(j_0_x_rot), 0] ,[0, math.sin(j_0_x_rot), math.cos(j_0_x_rot), 0], [0, 0, 0, 1]])
zero_to_one = zero_to_one_act * zero_to_one_trans * zero_to_one_rot
base_to_one = base_to_zero * zero_to_one

one_to_two_act = np.matrix([[math.cos(q_1), -math.sin(q_1), 0, 0], [math.sin(q_1), math.cos(q_1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
one_to_two_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, -l_2] ,[0, 0, 1, 0], [0, 0, 0, 1]])
one_to_two_rot = np.matrix([[1, 0, 0, 0], [0, math.cos(j_1_x_rot), -math.sin(j_1_x_rot), 0] ,[0, math.sin(j_1_x_rot), math.cos(j_1_x_rot), 0], [0, 0, 0, 1]])
one_to_two = one_to_two_act * one_to_two_trans * one_to_two_rot
base_to_two = base_to_one * one_to_two

two_to_three_act = np.matrix([[math.cos(q_2), -math.sin(q_2), 0, 0], [math.sin(q_2), math.cos(q_2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
two_to_three_trans =np.matrix([[1, 0, 0, 0], [0, 1, 0, 0] ,[0, 0, 1, l_3], [0, 0, 0, 1]])
two_to_three_rot = np.matrix([[1, 0, 0, 0], [0, math.cos(j_0_x_rot), -math.sin(j_0_x_rot), 0] ,[0, math.sin(j_0_x_rot), math.cos(j_0_x_rot), 0], [0, 0, 0, 1]])
two_to_three = two_to_three_act * two_to_three_trans * two_to_three_rot
base_to_three = base_to_two * two_to_three

three_to_four_act = np.matrix([[math.cos(q_3), -math.sin(q_3), 0, 0], [math.sin(q_3), math.cos(q_3), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
three_to_four_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, -l_4] ,[0, 0, 1, 0], [0, 0, 0, 1]])
three_to_four_rot = np.matrix([[1, 0, 0, 0], [0, math.cos(j_1_x_rot), -math.sin(j_1_x_rot), 0] ,[0, math.sin(j_1_x_rot), math.cos(j_1_x_rot), 0], [0, 0, 0, 1]])
three_to_four = three_to_four_act * three_to_four_trans * three_to_four_rot
base_to_four = base_to_three * three_to_four


four_to_five_act = np.matrix([[math.cos(q_4), -math.sin(q_4), 0, 0], [math.sin(q_4), math.cos(q_4), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
four_to_five_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0] ,[0, 0, 1, l_5], [0, 0, 0, 1]])
four_to_five_rot = np.matrix([[1, 0, 0, 0], [0, math.cos(j_0_x_rot), -math.sin(j_0_x_rot), 0] ,[0, math.sin(j_0_x_rot), math.cos(j_0_x_rot), 0], [0, 0, 0, 1]])
four_to_five = four_to_five_act * four_to_five_trans * four_to_five_rot
base_to_five = base_to_four * four_to_five


five_to_six_act = np.matrix([[math.cos(q_5), -math.sin(q_5), 0, 0], [math.sin(q_5), math.cos(q_5), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
five_to_six_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, -l_6] ,[0, 0, 1, 0], [0, 0, 0, 1]])
five_to_six_rot = np.matrix([[1, 0, 0, 0], [0, math.cos(j_1_x_rot), -math.sin(j_1_x_rot), 0] ,[0, math.sin(j_1_x_rot), math.cos(j_1_x_rot), 0], [0, 0, 0, 1]])
five_to_six = five_to_six_act * five_to_six_trans * five_to_six_rot
base_to_six = base_to_five * five_to_six
print(base_to_six)
