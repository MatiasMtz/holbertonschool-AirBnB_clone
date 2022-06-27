#!/usr/bin/python3
"""

"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
	"""

	"""

	def __init__(self, *args, **kwargs):
		"""

		"""
		if kwargs is not None and len(kwargs) is not 0:
			for key, value in kwargs.items():
				if key != "__class__":
					if key == "created_at" or key == "updated_at":
						value = datetime.fromisoformat(value)
					setattr(self, key, value)
		else:
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()

	def __str__(self):
		"""

		"""

		class_name = type(self).__name__
		return f"[{class_name}] ({self.id}) {self.__dict__}"

	def save(self):
		"""

		"""

		self.updated_at = datetime.now()

	def to_dict(self):
		"""

		"""

		to_dict = {}
		for key, value in self.__dict__.items():
			if key == "created_at" or key == "updated_at":
				value = value.isoformat()
			to_dict[key] = value
		to_dict["__class__"] = type(self).__name__

		return (to_dict)
