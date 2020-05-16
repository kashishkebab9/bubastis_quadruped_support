import math
import numpy
import sympy

#|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|#
#|       DH Parameters           |#
#| rot z| trans z| trans x| rot x|#
#|-------------------------------|#
#| -pi/2|    a   |   -b   |  0   |#
#|  q_1 |    0   |   l_1  |  pi/2|#
#|  q_2 |    0   |   l_2  |  0   |#
#|  q_3 |    0   |   l_3  |  0   |#
#|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|#

a = 1
b = 1.5

q_1 = 0
q_2 = math.pi/4
q_3 = -math.pi/2

l_1 = 1
l_2 = 1
l_3 = 1

# origin to base_link transform (not shown in dh parameters)
origin_base_rot = sympy.Matrix([[0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]])

# base_link to joint_0 transforms
base_zero_trans = sympy.Matrix([[1, 0, 0, 0],[0, 1, 0, a],[0, 0, 1, b], [0, 0, 0, 1]])

#joint_0 to joint_1 transforms
zero_one_rot_z = sympy.Matrix([[math.cos(q_1), -1*math.sin(q_1), 0, 0], [math.sin(q_1), math.cos(q_1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
zero_one_trans = sympy.Matrix([[1, 0, 0, l_1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
zero_one_rot_x = sympy.Matrix([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])

#joint_1 to joint_2 transforms
one_two_rot_z = sympy.Matrix([[math.cos(q_2), -1*math.sin(q_2), 0, 0], [math.sin(q_2), math.cos(q_2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
one_two_trans = sympy.Matrix([[1, 0, 0, l_2], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

#joint_2 to end effector transforms
two_ee_rot_z = sympy.Matrix([[math.cos(q_3), -1*math.sin(q_3), 0, 0], [math.sin(q_3), math.cos(q_3), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
two_ee_trans = sympy.Matrix([[1, 0, 0, l_3], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

base_zero = base_zero_trans

zero_one = zero_one_rot_z * zero_one_trans * zero_one_rot_x
#print(zero_one)

one_two = one_two_rot_z * one_two_trans
#print(one_two)

two_ee = two_ee_rot_z * two_ee_trans
#print(two_ee)

origin_ee = origin_base_rot* base_zero * zero_one * one_two * two_ee
#print(origin_ee)
base_ee = base_zero * zero_one * one_two * two_ee
print(base_ee)
print(origin_ee)

# Jacobian//Differential Kinematics Aspect

# Below is the input for movement delta
x_des = 35
y_des = 0
z_des = 0

delta_x = sympy.Matrix([x_des, y_des, z_des])
print(delta_x)

# Matlab was used in order to determine symbollically the x y and z equations of Matrix origin_ee
x_exp = b + l_2 * math.sin(q_2) + l_3 * (math.cos(q_2) * math.sin(q_3) + math.cos(q_3)*math.sin(q_2))
y_exp = l_1 * math.sin(q_1) + l_3 * (math.cos(q_2) * math.cos(q_3) * math.sin(q_1) - math.sin(q_1) * math.sin(q_2) * math.sin(q_3)) + math.cos(q_2) * l_2 * math.sin(q_1)
z_exp = -a + (-1*math.cos(q_1)) * l_1 - l_3*(math.cos(q_1)*math.cos(q_2)*math.cos(q_3) - math.cos(q_1)*math.sin(q_2)*math.sin(q_3))-math.cos(q_1)*math.cos(q_2)*l_2

ee_position = sympy.Matrix([[x_exp], [y_exp], [z_exp]])

# Jacobian Matrix Components also determined symbolically using Matlab
dx_dq_1 = 0
dx_dq_2 = l_3*(math.cos(q_2)*math.cos(q_3) - math.sin(q_2)*math.sin(q_3)) + l_2*math.cos(q_2)
dx_dq_3 = l_3*(math.cos(q_2)*math.cos(q_3) - math.sin(q_2)*math.sin(q_3))

dy_dq_1 = l_3*(math.cos(q_1)*math.cos(q_2)*math.cos(q_3) - math.cos(q_1)*math.sin(q_2)*math.sin(q_3)) + l_1*math.cos(q_1) + l_2*math.cos(q_1)*math.cos(q_2)
dy_dq_2 = -l_3*(math.cos(q_2)*math.sin(q_1)*math.sin(q_3) + math.cos(q_3)*math.sin(q_1)*math.sin(q_2)) - l_2*math.sin(q_1)*math.sin(q_2)
dy_dq_3 = -l_3*(math.cos(q_2)*math.sin(q_1)*math.sin(q_3) + math.cos(q_3)*math.sin(q_1)*math.sin(q_2))

dz_dq_1 = l_1*math.sin(q_1) - l_3*(math.sin(q_1)*math.sin(q_2)*math.sin(q_3) - math.cos(q_2)*math.cos(q_3)*math.sin(q_1)) + l_2*math.cos(q_2)*math.sin(q_1)
dz_dq_2 = l_3*(math.cos(q_1)*math.cos(q_2)*math.sin(q_3) + math.cos(q_1)*math.cos(q_3)*math.sin(q_2)) + l_2*math.cos(q_1)*math.sin(q_2)
dz_dq_3 = l_3*(math.cos(q_1)*math.cos(q_2)*math.sin(q_3) + math.cos(q_1)*math.cos(q_3)*math.sin(q_2))

jacobian = sympy.Matrix([[dx_dq_1, dx_dq_2, dx_dq_3], [dy_dq_1, dy_dq_2, dy_dq_3], [dz_dq_1, dz_dq_2, dz_dq_3]])
#print(jacobian)
jacobian_det = jacobian.det()

if jacobian_det != 0:
    #print(jacobian_det)
    inv_jacobian = jacobian.inv()
    #print(inv_jacobian)
    delta_q = inv_jacobian * delta_x
    print(delta_q)
else:
    print("You are at the edge of the workspace or you have discovered a singularity!")
