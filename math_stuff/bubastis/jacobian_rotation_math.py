#Script to figure out the joints required to to reach certain base_link roll/pitch/yaw angles
#Need to convert roll/pitch/yaw angles into different translations
#Need to determine change in translation required to achieve
#Use Jacobian Manipulator convert delta translation into delta joint angles

import math
import numpy as np

#need to make an OOP approach to try and control all four feet.

# Each Leg needs their own x and y offset from the base_link (variables a and b)
# each leg will have their own set of joint angles
# "Nominal anglews" are going to be global to the script
# The link lengths are global to the script

a_global = 1 #half of body length
b_global = 1 #half of body width

#l_1 is the shoulder
l_1 = 3.5
#l_2 is the elbow
l_2 = 5.0
#l_3 is the knee
l_3 = 5.0

#Set nom position to have the feet right underneath the shoulder joint
q_1_nom =  0
q_2_nom =  math.pi/4
q_3_nom = -math.pi/2

class quad_leg:

    def __init__(self, a_offset, b_offset, q_1, q_2, q_3):
        #constructor to define certain leg variables
        self.a_offset = a_offset
        self.b_offset = b_offset
        self.q_1 = q_1
        self.q_2 = q_2
        self.q_3 = q_3
        print(self.a_offset)
    def set_joint_angle(self, theta_1, theta_2, theta_3):
        #set shoulder, elbow, knee angles in radians
        self.q_1 = theta_1
        self.q_2 = theta_2
        self.q_3 = theta_3
        print(self.q_1)
        print(self.q_2)
        print(self.q_3)

    def set_nom_position(self):
        #set angles to q_1_nom, q_2_nom, q_3_nom
        self.q_1 = q_1_nom
        self.q_2 = q_2_nom
        self.q_2 = q_2_nom

    def ee_position(self):
        #algorithm to determine the current x, y, z position of the foot
        global l_1
        global l_2
        global l_3

        origin_base_rot = np.matrix([[0, 0, 1, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
        # base_link to joint_0 transforms
        base_zero_trans = np.matrix([[1, 0, 0, self.b_offset],[0, 1, 0, 0],[0, 0, 1, self.a_offset], [0, 0, 0, 1]])
        #joint_0 to joint_1 transforms
        #l_1 translation will be -l_1 if it is the right side of the vehicle and l_1 if on the left
        zero_one_rot_z = np.matrix([[math.cos(self.q_1), -1*math.sin(self.q_1), 0, 0], [math.sin(self.q_1), math.cos(self.q_1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        zero_one_trans = np.matrix([[1, 0, 0, l_1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        zero_one_rot_x = np.matrix([[0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]])
        #joint_1 to joint_2 transforms
        one_two_rot_z = np.matrix([[math.cos(self.q_2), -1*math.sin(self.q_2), 0, 0], [math.sin(self.q_2), math.cos(self.q_2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        one_two_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, l_2], [0, 0, 1, 0], [0, 0, 0, 1]])
        #joint_2 to end effector transforms
        two_ee_rot_z = np.matrix([[math.cos(self.q_3), -1*math.sin(self.q_3), 0, 0], [math.sin(self.q_3), math.cos(self.q_3), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        two_ee_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, l_3], [0, 0, 1, 0], [0, 0, 0, 1]])
        base_zero = base_zero_trans
        zero_one = zero_one_rot_z * zero_one_trans * zero_one_rot_x
        one_two = one_two_rot_z * one_two_trans
        two_ee = two_ee_rot_z * two_ee_trans
        origin_ee = origin_base_rot* base_zero * zero_one * one_two * two_ee
        base_ee = base_zero * zero_one * one_two * two_ee
        #print(origin_ee)
        position_matrix = np.matrix([[origin_ee.item(0, 3)], [origin_ee.item(1, 3)], [origin_ee.item(2, 3)]])
        print(position_matrix)

    def get_delta_q(self, z, x, y):
        #OK THIS IS SOME JANKY SHIT, BUUUUUT YOU HAVE TO INPUT (xyz) & FOR REASONS UNKNOWN, THE INDEXING GETS FUCKY
        #X RESULTS IN CHANGING Y
        #Y RESULTS IN CHANGING Z
        #Z RESULTS IN CHANGING
        #NOT JUST THAT, BUT SOME BECOME NEGATIVE?????? HELLLO?
        #I figured on page 37 the transformation this index shift looks like. it is very similar to the rotaion i have from base_link to joint 0
        delta_x = np.matrix([[-x],[-y],[z]])
        dx_dq_1 = l_3*math.cos(self.q_1)*math.sin(self.q_2)*math.sin(self.q_3) - l_2*math.cos(self.q_1)*math.cos(self.q_2) - l_1*math.sin(self.q_1)
        dx_dq_2 = l_3*(math.cos(self.q_2)*math.sin(self.q_1)*math.sin(self.q_3) + math.cos(self.q_3)*math.sin(self.q_1)*math.sin(self.q_2)) + l_2*math.sin(self.q_1)*math.sin(self.q_2)
        dx_dq_3 = l_3*(math.cos(self.q_2)*math.sin(self.q_1)*math.sin(self.q_3) + math.cos(self.q_3)*math.sin(self.q_1)*math.sin(self.q_2))
        dy_dq_1 = l_3*(math.sin(self.q_1)*math.sin(self.q_2)*math.sin(self.q_3) - math.cos(self.q_2)*math.cos(self.q_3)*math.sin(self.q_1)) + l_1*math.cos(self.q_1) - l_2*math.cos(self.q_2)*math.sin(self.q_1)
        dy_dq_2 = -1*l_3*(math.cos(self.q_1)*math.cos(self.q_2)*math.sin(self.q_3) + math.cos(self.q_1)*math.cos(self.q_3)*math.sin(self.q_2)) - l_2*math.cos(self.q_1)*math.sin(self.q_2)
        dy_dq_3 = -1*l_3*(math.cos(self.q_1)*math.cos(self.q_2)*math.sin(self.q_3) + math.cos(self.q_1)*math.cos(self.q_3)*math.sin(self.q_2))
        dz_dq_1 = 0
        dz_dq_2 = l_3*(math.cos(self.q_2)*math.cos(self.q_3) - math.sin(self.q_2)*math.sin(self.q_3)) + l_2*math.cos(self.q_2)
        dz_dq_3 = l_3*(math.cos(self.q_2)*math.cos(self.q_3) - math.sin(self.q_2)*math.sin(self.q_3))
        jacobian = np.matrix([[dx_dq_1, dx_dq_2, dx_dq_3], [dy_dq_1, dy_dq_2, dy_dq_3], [dz_dq_1, dz_dq_2, dz_dq_3]])
        #print(jacobian)
        jacobian_det = ((dx_dq_1)*((dy_dq_2 * dz_dq_3)-(dy_dq_3*dz_dq_2))) - ((dx_dq_2)*((dy_dq_1*dz_dq_3)-(dy_dq_3*dz_dq_1))) + ((dx_dq_3)*((dy_dq_1*dz_dq_2)-(dy_dq_2*dz_dq_1)))
        #print(jacobian_det)
        jacobian_inv = np.linalg.inv(jacobian)
        delta_q = jacobian_inv * delta_x

        q_1_delta = delta_q[0][0]
        q_2_delta = delta_q[1][0]
        q_3_delta = delta_q[2][0]
        self.q_1 = self.q_1 + q_1_delta
        self.q_2 = self.q_2 + q_2_delta
        self.q_3 = self.q_3 + q_3_delta

    def ee_position_xy(self):
        global l_1
        global l_2
        global l_3

        origin_base_rot = np.matrix([[0, 0, 1, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
        # base_link to joint_0 transforms
        base_zero_trans = np.matrix([[1, 0, 0, self.a_offset],[0, 1, 0, self.b_offset],[0, 0, 1, 0], [0, 0, 0, 1]])
        #joint_0 to joint_1 transforms
        #l_1 translation will be -l_1 if it is the right side of the vehicle and l_1 if on the left
        zero_one_rot_z = np.matrix([[math.cos(self.q_1), -1*math.sin(self.q_1), 0, 0], [math.sin(self.q_1), math.cos(self.q_1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        zero_one_trans = np.matrix([[1, 0, 0, l_1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        zero_one_rot_x = np.matrix([[0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]])
        #joint_1 to joint_2 transforms
        one_two_rot_z = np.matrix([[math.cos(self.q_2), -1*math.sin(self.q_2), 0, 0], [math.sin(self.q_2), math.cos(self.q_2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        one_two_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, l_2], [0, 0, 1, 0], [0, 0, 0, 1]])
        #joint_2 to end effector transforms
        two_ee_rot_z = np.matrix([[math.cos(self.q_3), -1*math.sin(self.q_3), 0, 0], [math.sin(self.q_3), math.cos(self.q_3), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        two_ee_trans = np.matrix([[1, 0, 0, 0], [0, 1, 0, l_3], [0, 0, 1, 0], [0, 0, 0, 1]])
        base_zero = base_zero_trans
        zero_one = zero_one_rot_z * zero_one_trans * zero_one_rot_x
        one_two = one_two_rot_z * one_two_trans
        two_ee = two_ee_rot_z * two_ee_trans
        origin_ee = origin_base_rot* base_zero * zero_one * one_two * two_ee
        base_ee = base_zero * zero_one * one_two * two_ee
        #print(origin_ee)
        position_matrix_xy = np.matrix([[origin_ee.item(0, 3)], [origin_ee.item(1, 3)]])
        return position_matrix_xy

rf = quad_leg(a_global, -b_global, q_1_nom, q_2_nom, q_3_nom)
lf = quad_leg(a_global, b_global, q_1_nom, q_2_nom, q_3_nom)
rb = quad_leg(-a_global, -b_global, q_1_nom, q_2_nom, q_3_nom)
lb = quad_leg(-a_global, b_global, q_1_nom, q_2_nom, q_3_nom)
# rf_xy = rf.ee_position_xy()
# lf_xy = lf.ee_position_xy()
# rb_xy = rb.ee_position_xy()
# lb_xy = lb.ee_position_xy()

#******************************************************************************#
#functions that will be applied to the entire body, all four legs, or base_link need to be global functions

#Rotation of the base_link

#need to first convert the input values of joystick to angles
pitch_angle = -math.pi/4 + ((math.pi/4 + 1) / (2)) * (pitch_joystick_value + 1)
roll_angle = -math.pi/4 + ((math.pi/4 + 1) / (2)) * (roll_joystick_value + 1)
yaw_angle = -math.pi/4 + ((math.pi/4 + 1) / (2)) * (yaw_joystick_value + 1)

def pitch(pitch_angle):

    global a_global
    global b_global
    pitch_a = math.cos(pitch_angle) * a_global
    pitch_delta_z = a_global*(math.sin(pitch_angle))
    pitch_delta_x = abs(a_global - pitch_a)
    rf_pitch_delta = np.matrix([-pitch_delta_x, 0, pitch_delta_z])
    lf_pitch_delta = np.matrix([-pitch_delta_x, 0, pitch_delta_z])
    lb_pitch_delta = np.matrix([-pitch_delta_x, 0, -pitch_delta_z])
    rb_pitch_delta = np.matrix([-pitch_delta_x, 0, -pitch_delta_z])
    print(pitch_delta)

    #fronts are going to move in the opposite translation as the backs 100% of the time

def roll(roll_angle):

    global a_global
    global b_global
    roll_delta_z = b_global *math.sin(roll_angle)
    roll_offset = b_global * math.cos(roll_angle)
    roll_delta_y = abs(b_global - roll_a)
    rf_roll_delta = np.matrix([0, -roll_delta_y, roll_delta_z])
    lf_roll_delta = np.matrix([0, -roll_delta_y, -roll_delta_z])
    rb_roll_delta = np.matrix([0, -roll_delta_y, roll_delta_z])
    lb_roll_delta = np.matrix([0, -roll_delta_y, -roll_delta_z])
    print(roll_delta)

    #sides are going to move in the opposite translation as the backs 100% of the time

# def yaw(yaw_angle):
#
#     global a_global
#     global b_global
#     pitch_delta_y = a_global*math.sin(pitch_angle)
#     yaw_a = a_global * math.cos(yaw_angle)
#     yaw_delta_x = a_global - yaw_a
#     rf_yaw_delta = np.matrix([-yaw_delta_x, yaw_delta_y, 0])
#     lf_yaw_delta = np.matrix([-yaw_delta_x, yaw_delta_y, 0])
#     rb_yaw_delta = np.matrix([-yaw_delta_x, yaw_delta_y, 0])
#     lb_yaw_delta = np.matrix([-yaw_delta_x, yaw_delta_y, 0])
#     print(yaw_delta)
