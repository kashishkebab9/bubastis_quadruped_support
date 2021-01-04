#!/usr/bin/python
import math
q_0 = 0
q_1 = 0
q_2 = 0
q_3 = 0
q_4 = 0
q_5 = 0
q_6 = 0

a_offset = .1
l_1 = .1
l_2 = .1
l_3 = .1
l_4 = .1
l_5 = .1
l_6 = .1
l_7 = .1

#x needs to be reviewed
#x = math.cos(q_0) * l_2 * math.sin(q_1) - math.cos(q_5) * l_6 * (math.sin(q_3) * (math.sin(q_0)* math.sin(q_2) - math.cos(q_0) * math.cos(q_1) * math.cos(q_2)) - math.cos(q_0) * math.cos(q_3) * math.sin(q_1)) - l_6 * math.sin(q_5) * (math.sin(q_4))*(math.cos(q_2) * math.sin(q_0) + math.cos(q_0)*math.cos(q_1) * math.sin(q_2)) + math.cos(q_4)*(math.cos(q_3) * (math.sin(q_0) * math.sin(q_2) - math.cos(q_0) * math.cos(q_1) * math.cos(q_2)) + math.cos(q_0) * math.sin(q_1) * math.sin(q_3)) - l_4 * math.sin(q_3) * (math.sin(q_0) * math.sin(q_2) - math.cos(q_0) * math.cos(q_1) * math.cos(q_2)) - l_5 * (math.sin(q_3) * (math.sin(q_0) * math.sin(q_2) - math.cos(q_0) * math.cos(q_1) * math.cos(q_2)) - math.cos(q_0) * math.cos(q_3) * math.sin(q_1)) + math.cos(q_0) * l_3 * math.sin(q_1) + math.cos(q_0) * math.cos(q_3) * l_4 * math.sin(q_1)
y = l_6 * math.sin(q_5) * (math.cos(q_4) * (math.cos(q_1) * math.sin(q_3) + math.cos(q_2) * math.cos(q_3) * math.sin(q_1)) - math.sin(q_1) * math.sin(q_2) * math.sin(q_4)) - l_1 - math.cos(q_1) * l_2 - math.cos(q_1) * l_3 - l_5 * (math.cos(q_1) * math.cos(q_3) - math.cos(q_2) * math.sin(q_1) * math.sin(q_3)) - a_offset - math.cos(q_5) * l_6 * (math.cos(q_1) * math.cos(q_3) - math.cos(q_2) * math.sin(q_1) * math.sin(q_3)) - math.cos(q_1) * math.cos(q_3) * l_4 + math.cos(q_2) * l_4 * math.sin(q_1) * math.sin(q_3)
z = l_5 * (math.sin(q_3) * (math.cos(q_0) * math.sin(q_2) + math.cos(q_1) * math.cos(q_2) * math.sin(q_0)) + math.cos(q_3) * math.sin(q_0) * math.sin(q_1)) + math.cos(q_5) * l_6 * (math.sin(q_3) * (math.cos(q_0) * math.sin(q_2) + math.cos(q_1) * math.cos(q_2) * math.sin(q_0)) + math.cos(q_3) * math.sin(q_0) * math.sin(q_1)) + l_6 * math.sin(q_5) * (math.sin(q_4) * (math.cos(q_0) * math.cos(q_2) - math.cos(q_1) * math.sin(q_0) * math.sin(q_2)) + math.cos(q_4) * (math.cos(q_3) * (math.cos(q_0) * math.sin(q_2) + math.cos(q_1) * math.cos(q_2) * math.sin(q_0)) - math.sin(q_0) * math.sin(q_1) * math.sin(q_3))) + l_4 * math.sin(q_3) * (math.cos(q_0) * math.sin(q_2) + math.cos(q_1) * math.cos(q_2) * math.sin(q_0)) + l_2 * math.sin(q_0) * math.sin(q_1) + l_3 * math.sin(q_0) * math.sin(q_1) + math.cos(q_3) * l_4 * math.sin(q_0) * math.sin(q_1)

print(x)
print(y)
print(z)
