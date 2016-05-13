import csv
import pickle
from hand import Hand, Joint
from quaternion import Quaternion

class JointsAlreadySetError(Exception):
	def __init__(self, value):
		self.value = value

class PositionAlreadySetError(Exception):
	def __init__(self, value):
		self.value = value

class WristAngleAlreadySetError(Exception):
	def __init__(self, value):
		self.value = value


#mutable class representing mapping from times to hand configurations/locations
class HandSeries:
	def __init__(self):
		self.hands = {}

	def __str__(self):
		stringRep = "{"
		for time, hand in self.get_sorted_hand_series():
			stringRep += str(time) + ": " + str(hand) + "\n"
		stringRep += "}"
		return stringRep

	def __repr__(self):
		stringRep = "{"
		for time, hand in self.get_sorted_hand_series():
			stringRep += str(time) + ": " + str(hand) + "\n"
		stringRep += "}"
		return stringRep

	def add_joint_angles_from_csv(self, csvfile):
		"""
		Adds Hand configurations to this HandSeries from a properly formatted csv file
		"""
		with open(csvfile) as csvfile:
			csvfile.readline() #get rid of header row
			reader = csv.reader(csvfile)
			for row in reader:
				timestamp = int(row[0])
				joint_angles_dict = self.get_joint_angles_from_csvrow(row)
				if joint_angles_dict is None:
					continue
				if timestamp not in self.hands:
					self.hands[timestamp] = Hand(joint_angles_dict)
				else:
					current_hand = self.hands[timestamp]
					if current_hand.get_joint_angles() is None:
						current_hand.set_joint_angles(joint_angles_dict)
					else:
						raise JointsAlreadySetError('current value of joints: ' + str(current_hand.get_joint_angles()))

	# helper method for get_joint_angles_from_csv
	# special value of None if the line was all 0s
	# (indicates hand was not read at this time - possibly fix in exporter?)
	def get_joint_angles_from_csvrow(self, csvrow):
		joint_angles_dict = {}
		angles = [Quaternion( \
			float(csvrow[i]), \
			float(csvrow[i+1]),\
			float(csvrow[i+2]), \
			float(csvrow[i+3])) \
			for i in range(1,len(csvrow),4)]

		if all(angle.is_zeroes() for angle in angles):
			return None

		for i, angle in enumerate(angles):
			joint_angles_dict[Joint(i)] = angle

		return joint_angles_dict

	def add_hand_positions_from_csv(self, csvfile):
		"""
		Adds position of hands to this HandSeries from a properly formatted csv file
		"""
		with open(csvfile) as csvfile:
			csvfile.readline() #get rid of header row
			reader = csv.reader(csvfile)
			for row in reader:
				timestamp = int(row[0])
				hand_position = (float(row[1]), float(row[2]), float(row[3]))
				if all(x==0 for x in hand_position):
					continue
				if timestamp not in self.hands:
					self.hands[timestamp] = Hand(position_in_space=hand_position)
				else:
					current_hand = self.hands[timestamp]
					if current_hand.get_position_in_space() is None:
						current_hand.set_position_in_space(hand_position)
					else:
						raise PositionAlreadySetError('current position of hand: ' + str(current_hand.get_position_in_space()))

	def add_wrist_angles_from_csv(self, csvfile):
		"""
		Adds wrist angles of hands to this HandSeries from a properly formatted csv file
		"""
		with open(csvfile) as csvfile:
			csvfile.readline() #get rid of header row
			reader = csv.reader(csvfile)
			for row in reader:
				timestamp = int(row[0])
				wrist_angle = Quaternion(float(row[1]), float(row[2]), float(row[3]), float(row[4]))
				# all-zero wrist angle is invalid, don't add
				if wrist_angle.is_zeroes():
					continue
				if timestamp not in self.hands:
					self.hands[timestamp] = Hand(wrist_angle=wrist_angle)
				else:
					current_hand = self.hands[timestamp]
					if current_hand.get_wrist_angle() is None:
						current_hand.set_wrist_angle(wrist_angle)
					else:
						raise WristAngleAlreadySetError('current wrist angle: ' + str(current_hand.get_wrist_angle()))

	def get_sorted_hand_series(self):
		"""
		Returns hand series as list in increasing order of time
		"""
		return sorted(self.hands.items())

	def get_hand_at_time(self,time):
		"""
		Returns hand at certain time if it exists, otherwise None
		"""
		if time in self.hands:
			return self.hands[time]
		else:
			return None

	def pickle_save(self, filename):
		"""
		Utility method to save this hand series into file
		"""
		output = open(filename, 'wb')
		pickle.dump(self, output)
		output.close()

	@staticmethod	
	def pickle_load(filename):
		"""
		Utility method to load a hand series from a file
		"""
		pickle_file = open(filename, 'rb')
		pickled_hand_series = pickle.load(pickle_file)
		pickle_file.close()
		return pickled_hand_series