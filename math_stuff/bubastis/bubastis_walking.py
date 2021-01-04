#Quadruped step taking function
#need to make a function defined for pushing foot up
#although, there might be an issue with continuity. the legs will just go to the position instead of gradually going up
#need to make a function to allow for gradual movement
class quad_leg:

    def __init__(self, a_offset, b_offset, q_1, q_2, q_3, l_1):
        #constructor to define certain leg variables
        self.a_offset = a_offset
        self.b_offset = b_offset
        self.q_1 = q_1
        self.q_2 = q_2
        self.q_3 = q_3
        self.l_1 = l_1
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

        global l_2
        global l_3

        #origin_base_rot = np.matrix([[0, 0, 1, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
        # base_link to joint_0 transforms
        base_zero_trans = np.matrix([[1, 0, 0, self.a_offset],[0, 1, 0, self.b_offset],[0, 0, 1, 0], [0, 0, 0, 1]])
        #joint_0 to joint_1 transforms
        #l_1 translation will be -l_1 if it is the right side of the vehicle and l_1 if on the left
        zero_one_rot_z = np.matrix([[math.cos(self.q_1), -1*math.sin(self.q_1), 0, 0], [math.sin(self.q_1), math.cos(self.q_1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        zero_one_trans = np.matrix([[1, 0, 0, self.l_1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
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
        #origin_ee = origin_base_rot* base_zero * zero_one * one_two * two_ee
        base_ee = base_zero * zero_one * one_two * two_ee
        #print(origin_ee)
        position_matrix = np.matrix([[base_ee.item(0, 3)], [-base_ee.item(1, 3)], [-base_ee.item(2, 3)]])
        return position_matrix

    def get_delta_q(self, z, x, y):
        #OK THIS IS SOME JANKY SHIT, BUUUUUT YOU HAVE TO INPUT (xyz) & FOR REASONS UNKNOWN, THE INDEXING GETS FUCKY
        #X RESULTS IN CHANGING Y
        #Y RESULTS IN CHANGING Z
        #Z RESULTS IN CHANGING
        #NOT JUST THAT, BUT SOME BECOME NEGATIVE?????? HELLLO?
        delta_x = np.matrix([[-x],[-y],[z]])
        dx_dq_1 = l_3*math.cos(self.q_1)*math.sin(self.q_2)*math.sin(self.q_3) - l_2*math.cos(self.q_1)*math.cos(self.q_2) - self.l_1*math.sin(self.q_1)
        dx_dq_2 = l_3*(math.cos(self.q_2)*math.sin(self.q_1)*math.sin(self.q_3) + math.cos(self.q_3)*math.sin(self.q_1)*math.sin(self.q_2)) + l_2*math.sin(self.q_1)*math.sin(self.q_2)
        dx_dq_3 = l_3*(math.cos(self.q_2)*math.sin(self.q_1)*math.sin(self.q_3) + math.cos(self.q_3)*math.sin(self.q_1)*math.sin(self.q_2))
        dy_dq_1 = l_3*(math.sin(self.q_1)*math.sin(self.q_2)*math.sin(self.q_3) - math.cos(self.q_2)*math.cos(self.q_3)*math.sin(self.q_1)) + self.l_1*math.cos(self.q_1) - l_2*math.cos(self.q_2)*math.sin(self.q_1)
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

feet = [0, 1, 2, 3]
i = 0

y_move = .1
x_move = .2
step_height = .1

if feet[i] == 0:
  #move foot i in the z axis:
  rf.get_delta_q(0, 0, step_height)
  #move other three feet, so that base_link is inside of triangle:
  lf.get_delta_q(-x, y)
  rb.get_delta_q(-x, y)
  lb.get_delta_q(-x, y)
  #and return the step back down to og position:
  rf.get_delta_q(0, 0, -step_height)
  i = i + 1

elif feet[i] == 1:
  #move foot i in the z axis:
  lf.get_delta_q(0, 0, step_height)
  #move other three feet, so that base_link is inside of triangle
  rf.get_delta_q(-x, -y)
  rb.get_delta_q(-x, -y)
  lb.get_delta_q(-x, -y)
  #and return the step back down to og position:
  lf.get_delta_q(0, 0, -step_height)
  i = i + 1

elif feet[i] == 2:
  #move foot i in the z axis:
  rb.get_delta_q(0, 0, step_height)
  #move other three feet, so that base_link is inside of triangle
  rf.get_delta_q(x, y)
  lf.get_delta_q(x, y)
  lb.get_delta_q(x, y)
  #and return the step back down to og position:
  rb.get_delta_q(0, 0, -step_height)
  i = i + 1

elif feet[i] == 3:
  #move foot i in the z axis:
  lb.get_delta_q(0, 0, step_height)
  #move other three feet, so that base_link is inside of triangle
  rf.get_delta_q(x, -y)
  lf.get_delta_q(x, -y)
  rb.get_delta_q(x, -y)
  #and return the step back down to og position:
  lb.get_delta_q(0, 0, -step_height)
  i = 0
