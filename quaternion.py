from math import sqrt, atan2, acos

#immutable class representing a quaternion
class Quaternion:

	def __init__(self,x,y,z,w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w

	@classmethod
	def fromarray(cls,array):
		return cls(array[0],array[1],array[2],array[3])

	def __str__(self):
		string_array = [str(self.x),str(self.y),str(self.z),str(self.w)]
		string_rep = "[" + ", ".join(string_array) + "]"
		return string_rep

	def __repr__(self):
		string_array = [str(self.x),str(self.y),str(self.z),str(self.w)]
		string_rep = "[" + ", ".join(string_array) + "]"
		return string_rep

	def __add__(self,other):
		new_x = self.x + other.x
		new_y = self.y + other.y
		new_z = self.z + other.z
		new_w = self.w + other.w
		return Quaternion(new_x, new_y, new_z, new_w)

	def __sub__(self,other):
		new_x = self.x - other.x
		new_y = self.y - other.y
		new_z = self.z - other.z
		new_w = self.w - other.w
		return Quaternion(new_x, new_y, new_z, new_w)

	def __mul__(self,other):
		new_x = self.w*other.x + self.x*other.w + self.y*other.z - self.z*other.y
		new_y = self.w*other.y + self.y*other.w + self.z*other.x - self.x*other.z
		new_z = self.w*other.z + self.z*other.w + self.x*other.y - self.y*other.x
		new_w = self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z
		return Quaternion(new_x, new_y, new_z, new_w)

	def __div__(self,other):
		return self*other.inverse()

	def is_zeroes(self):
		"""
		Returns whether or not this quaternion has x=y=z=w=0
		"""
		if self.x == 0 and self.y == 0 and self.z == 0 and self.w == 0:
			return True
		return False

	def norm(self):
		"""
		Returns norm of this quaternion
		"""
		return sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

	def normalized(self):
		"""
		Returns normalized version of this quaternion
		"""
		if self.is_zeroes():
			return Quaternion(self.x, self,y, self.z, self.w)
		norm = self.norm()
		new_x = self.x/norm
		new_y = self.y/norm
		new_z = self.z/norm
		new_w = self.w/norm
		return Quaternion(new_x, new_y, new_z, new_w)

	def conjugate(self):
		"""
		Returns normalized version of this quaternion
		"""
		return Quaternion(-self.x, -self.y, -self.z, self.w)

	def dot(self,other):
		"""
		Returns dot product of this quaternion with other
		"""
		return self.w*other.w + self.x*other.x + self.y*other.y + self.z*other.z

	def angle_diff(self,other):
		"""
		Returns difference in angle between this quaternion and other
		"""
		arg = self.dot(other)/(self.norm()*other.norm())
		# for small discrepancies with float values
		if arg > 1:
			arg = 1
		if arg < -1:
			arg = -1
		return acos(arg)
		
	def inverse(self):
		"""
		Returns inverse of this quaternion
		"""
		d = self.norm()
		new_x = -self.x/d
		new_y = -self.y/d
		new_z = -self.z/d
		new_w = self.w/d
		return Quaternion(new_x, new_y, new_z, new_w)
