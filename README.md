# hand-analysis
modules to import hand data from specially formatted files and perform basic analysis

Required libraries: matplotlib

Modules:
  - Quaternion: basic quaternion operations. Used as angle representations in Hand.
  - Hand: stores position of the hand in 3D space, angle of the wrist in 3D space, and
      angles of 22 joints (wrist, palm, and 4 joints for each finger) with respect to wrist
  - HandSeries: stores map from timestamps to Hands. Contains methods to load data from properly formatted
      csv files (examples in testData folder), to save the hand series, and to access hand at given time.
  - helper: utility functions. Currently only has function to create hand series from folder containing all
      necessary files.

Contact: csquires@mit.edu
