import matplotlib.pyplot as p
import matplotlib.ticker as mticker 
from hand_series import HandSeries

def plot_speeds(sorted_hand_series, window_title="Speeds"):
	times = []

	hand_position_differences = []
	wrist_angle_differences = []

	thumb_configuration_differences = []
	index_configuration_differences = []
	middle_configuration_differences = []
	ring_configuration_differences = []
	pinky_configuration_differences = []

	# list of tuples of form (timestamp, Hand object), sorted by increasing time
	start_time = sorted_hand_series[0][0]/10.**4

	for i in range(1, len(sorted_hand_series)):
		current_time = sorted_hand_series[i][0]/10.**4 #convert from 100ns to ms
		current_hand = sorted_hand_series[i][1]
		previous_time = sorted_hand_series[i-1][0]/10.**4
		previous_hand = sorted_hand_series[i-1][1]

		times.append(current_time-start_time)

		time_diff = current_time - previous_time
		hand_position_diff = current_hand.get_position_difference(previous_hand)/time_diff
		wrist_angle_diff = current_hand.get_wrist_angle_difference(previous_hand)/time_diff

		thumb_configuration_diff = current_hand.get_thumb_configuration_distance(previous_hand)/time_diff
		index_configuration_diff = current_hand.get_index_configuration_distance(previous_hand)/time_diff
		middle_configuration_diff = current_hand.get_middle_configuration_distance(previous_hand)/time_diff
		ring_configuration_diff = current_hand.get_ring_configuration_distance(previous_hand)/time_diff
		pinky_configuration_diff = current_hand.get_pinky_configuration_distance(previous_hand)/time_diff

		wrist_angle_differences.append(wrist_angle_diff)
		hand_position_differences.append(hand_position_diff)

		thumb_configuration_differences.append(thumb_configuration_diff)
		index_configuration_differences.append(index_configuration_diff)
		middle_configuration_differences.append(middle_configuration_diff)
		ring_configuration_differences.append(ring_configuration_diff)
		pinky_configuration_differences.append(pinky_configuration_diff)

	# Basic Differences
	fig = p.figure(1)
	p.title("Differences in Position/Wrist Angle")
	num_x_bins = 5
	num_y_bins = 4

	p.subplot(2,1,1)
	p.title("Differences in Hand Position")
	p.plot(times, hand_position_differences)
	p.locator_params(axis='x',nbins=num_x_bins)
	p.locator_params(axis='y',nbins=num_y_bins)
	p.xlabel("Timestamp (ms)")
	p.ylabel(r'$\frac{\Delta Distance}{\Delta Time}$')
	p.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d ms'))
	p.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d cm/ms'))

	p.subplot(2,1,2)
	p.title("Differences in Wrist Angle")
	p.plot(times, wrist_angle_differences)
	p.locator_params(axis='x',nbins=num_x_bins)
	p.locator_params(axis='y',nbins=num_y_bins)
	p.xlabel("Timestamp (ms)")
	p.ylabel(r'$\frac{\Delta Angle}{\Delta Time}$')
	p.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d ms'))
	p.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d rad/ms'))

	p.tight_layout()
	fig.canvas.set_window_title(window_title)
	fig.suptitle('Speeds', fontsize=20)
	fig.subplots_adjust(top=.85)
	p.show()

	# Differences in Each Finger
	fig = p.figure(2)
	p.title("Differences is Finger Configurations")
	num_x_bins = 4
	num_y_bins = 2

	p.subplot(3,2,1)
	p.plot(times, thumb_configuration_differences)
	p.locator_params(axis='x',nbins=num_x_bins)
	p.locator_params(axis='y',nbins=num_y_bins)
	p.xlabel("Timestamp")
	p.ylabel(r'$\frac{\Delta Angle}{\Delta Time}$')
	p.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d ms'))
	p.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d rad/ms'))

	p.subplot(3,2,2)
	p.plot(times, index_configuration_differences)
	p.locator_params(axis='x',nbins=num_x_bins)
	p.locator_params(axis='y',nbins=num_y_bins)
	p.xlabel("Timestamp")
	p.ylabel(r'$\frac{\Delta Angle}{\Delta Time}$')
	p.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d ms'))
	p.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d rad/ms'))

	p.subplot(3,2,3)
	p.plot(times, middle_configuration_differences)
	p.xlabel("Timestamp")
	p.ylabel(r'$\frac{\Delta Angle}{\Delta Time}$')
	p.locator_params(axis='x',nbins=num_x_bins)
	p.locator_params(axis='y',nbins=num_y_bins)
	p.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d ms'))
	p.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d rad/ms'))

	p.subplot(3,2,4)
	p.plot(times, ring_configuration_differences)
	p.xlabel("Timestamp")
	p.ylabel(r'$\frac{\Delta Angle}{\Delta Time}$')
	p.locator_params(axis='x',nbins=num_x_bins)
	p.locator_params(axis='y',nbins=num_y_bins)
	p.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d ms'))
	p.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d rad/ms'))

	p.subplot(3,2,5)
	p.plot(times, pinky_configuration_differences)
	p.xlabel("Timestamp")
	p.ylabel(r'$\frac{\Delta Angle}{\Delta Time}$')
	p.locator_params(axis='x',nbins=num_x_bins)
	p.locator_params(axis='y',nbins=num_y_bins)
	p.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d ms'))
	p.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d rad/ms'))

	p.tight_layout()
	fig.canvas.set_window_title(window_title)
	fig.suptitle('Speeds', fontsize=20)
	fig.subplots_adjust(top=1)
	p.get_current_fig_manager().window.showMaximized()
	p.show()

def plot_distances_between_hands():
	pass


rel_angle_csv_L = "../StreamExports/test/RelativeAngleData_L.csv"
abs_position_csv_L = "../StreamExports/test/AbsolutePositionData_L.csv"
abs_angle_csv_L = "../StreamExports/test/AbsoluteAngleData_L.csv"
hand_series_L = HandSeries()
hand_series_L.add_joint_angles_from_csv(rel_angle_csv_L)
hand_series_L.add_hand_positions_from_csv(abs_position_csv_L)
hand_series_L.add_wrist_angles_from_csv(abs_angle_csv_L)

rel_angle_csv_R = "../StreamExports/test/RelativeAngleData_R.csv"
abs_position_csv_R = "../StreamExports/test/AbsolutePositionData_R.csv"
abs_angle_csv_R = "../StreamExports/test/AbsoluteAngleData_R.csv"
hand_series_R = HandSeries()
hand_series_R.add_joint_angles_from_csv(rel_angle_csv_R)
hand_series_R.add_hand_positions_from_csv(abs_position_csv_R)
hand_series_R.add_wrist_angles_from_csv(abs_angle_csv_R)

sorted_hand_series_L = hand_series_L.get_sorted_hand_series()
sorted_hand_series_R = hand_series_R.get_sorted_hand_series()
# plot_speeds(sorted_hand_series_L, window_title="Left Hand Differences")
print "------------------------------------"
plot_speeds(sorted_hand_series_R, window_title="Right Hand Differences")


print "Number of left hand observations: ", len(sorted_hand_series_L)
print "Number of right hand observations: ", len(sorted_hand_series_R)
# print "Total time (ms): ", sum(time_differences)
# print "Total time (s): ", sum(time_differences)/10.**3
# print "Maximum time difference (100ns)", max(time_differences)
# print "Maximum time difference (ms)", max(time_differences)
# print "Minimum time difference (100ns)", min(time_differences)
# print "Minimum time difference (ms)", min(time_differences)
# print "Average time difference (100ns)", sum(time_differences)/len(time_differences)
# print "Average time difference (ms)", sum(time_differences)/len(time_differences)