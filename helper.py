from hand_series import HandSeries
import os

def load_hand_series_from_folder(folder_name,hand_side):
	"""
	Returns a hand series from properly formatted folder for hand_side
	Args:
		folder_name: relative path to folder containing RelativeAngleData, AbsolutePositionData, and AbsoluteAngleData files
		hand_side: "L" for left, "R" for right
	Returns:
		hand_series object derived from the files
	"""
	assert hand_side == "L" or hand_side == "R"
	rel_angle_filename = folder_name + "/RelativeAngleData_" + hand_side + ".csv"
	abs_pos_filename = folder_name + "/AbsolutePositionData_" + hand_side + ".csv"
	abs_angle_filename = folder_name + "/AbsoluteAngleData_" + hand_side + ".csv"
	
	h = HandSeries()
	h.add_joint_angles_from_csv(rel_angle_filename)
	h.add_hand_positions_from_csv(abs_pos_filename)
	h.add_wrist_angles_from_csv(abs_angle_filename)

	return h