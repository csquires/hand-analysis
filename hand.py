from quaternion import Quaternion
from enum import Enum
from math import sqrt

class Hand:
    
    def __init__(self, joint_angles_dict=None, position_in_space=None, wrist_angle=None):
        self._joint_angles_dict = joint_angles_dict
        self._position_in_space = position_in_space
        self._wrist_angle = wrist_angle

    def __str__(self):
        string_rep = "-----------------------------------------------------\n"
        string_rep += "Joint Angles: {\n" + ",\n".join("%s: %s" % (joint,angle) for (joint, angle) in self._joint_angles_dict.iteritems()) + "}\n"
        string_rep += "Position in Space: " + str(self._position_in_space) + "\n"
        string_rep += "Wrist Angle: " + str(self._wrist_angle) + "\n"
        string_rep += "-----------------------------------------------------"
        return string_rep

    def get_configuration_distance(self, other):
        """
        Returns total angular distance between joints in this hand and joints in other
        """
        #TODO possibly weigh joint angles differently? may require ML
        distance = 0.
        for joint in self._joint_angles_dict:
            self_joint_angle = self._joint_angles_dict[joint]
            other_joint_angle = other._joint_angles_dict[joint]
            distance += self_joint_angle.angle_diff(other_joint_angle)
        return distance

    def get_thumb_configuration_distance(self, other):
        """
        Returns total angular distance between joints in this hand's thumb and joints in other's thumb
        """
        distance = 0.
        for i in range(Joint.thumb_b.value, Joint.thumb_tip.value+1):
            self_angles = self._joint_angles_dict[Joint(i)]
            other_angles = other._joint_angles_dict[Joint(i)]
            distance += self_angles.angle_diff(other_angles)
        return distance

    def get_index_configuration_distance(self, other):
        """
        Returns total angular distance between joints in this hand's index finger and joints in other's index finger
        """
        distance = 0.
        for i in range(Joint.index_b.value, Joint.index_tip.value+1):
            self_angles = self._joint_angles_dict[Joint(i)]
            other_angles = other._joint_angles_dict[Joint(i)]
            distance += self_angles.angle_diff(other_angles)
        return distance

    def get_middle_configuration_distance(self, other):
        """
        Returns total angular distance between joints in this hand's middle finger and joints in other's middle finger
        """
        distance = 0.
        for i in range(Joint.middle_b.value, Joint.middle_tip.value+1):
            self_angles = self._joint_angles_dict[Joint(i)]
            other_angles = other._joint_angles_dict[Joint(i)]
            distance += self_angles.angle_diff(other_angles)
        return distance

    def get_ring_configuration_distance(self, other):
        """
        Returns total angular distance between joints in this hand's ring finger and joints in other's ring finger
        """
        distance = 0.
        for i in range(Joint.ring_b.value, Joint.ring_tip.value+1):
            self_angles = self._joint_angles_dict[Joint(i)]
            other_angles = other._joint_angles_dict[Joint(i)]
            distance += self_angles.angle_diff(other_angles)
        return distance

    def get_pinky_configuration_distance(self, other):
        """
        Returns total angular distance between joints in this hand's pinky finger and joints in other's pinky finger
        """
        distance = 0.
        for i in range(Joint.pinky_b.value, Joint.pinky_tip.value+1):
            self_angles = self._joint_angles_dict[Joint(i)]
            other_angles = other._joint_angles_dict[Joint(i)]
            distance += self_angles.angle_diff(other_angles)
        return distance

    def get_position_difference(self, other):
        """
        Returns Euclidean distance between the position of each hand (measured at wrist)
        """
        x_diff = self._position_in_space[0] - other._position_in_space[0]
        y_diff = self._position_in_space[1] - other._position_in_space[1]
        z_diff = self._position_in_space[2] - other._position_in_space[2]
        return sqrt(x_diff**2 + y_diff**2 + z_diff**2)

    def get_wrist_angle_difference(self, other):
        """
        Returns angular distance between this hand's wrist and other's wrist
        """
        return self._wrist_angle.angle_diff(other._wrist_angle)

    def get_joint_angles(self):
        return self._joint_angles_dict

    def get_wrist_angle(self):
        return self._wrist_angle

    def get_position_in_space(self):
        return self._position_in_space

    def set_joint_angles(self, joint_angles_dict):
        self._joint_angles_dict = joint_angles_dict

    def set_position_in_space(self, position):
        self._position_in_space = position

    def set_wrist_angle(self, wrist_angle):
        self._wrist_angle = wrist_angle

    def pickle_save(self, filename):
        """
        Utility method to save this hand into file
        """
        output = open(filename, 'wb')
        pickle.dump(self, output)
        output.close()

    @staticmethod   
    def pickle_load(filename):
        """
        Utility method to load a hand from a file
        """
        pickle_file = open(filename, 'rb')
        pickled_hand = pickle.load(pickle_file)
        pickle_file.close()
        return pickled_hand

class Joint(Enum):
    wrist = 0
    palm = 1
    thumb_a = 2
    thumb_b = 3
    thumb_c = 4
    thumb_tip = 5
    index_a = 6
    index_b = 7
    index_c = 8
    index_tip = 9
    middle_a = 10
    middle_b = 11
    middle_c = 12
    middle_tip = 13
    ring_a = 14
    ring_b = 15
    ring_c = 16
    ring_tip = 17
    pinky_a = 18
    pinky_b = 19
    pinky_c = 20
    pinky_tip = 21