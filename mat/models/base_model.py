#!/usr/bin/python3
"""

"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
	"""

	"""

	def __init__(self, *args, **kwargs):
		"""

		"""
		if kwargs is not None and len(kwargs) != 0:
			for key, value in kwargs.items():
				if key != "__class__":
					if key == "created_at" or key == "updated_at":
						value = datetime.fromisoformat(value)
					setattr(self, key, value)
		else:
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)

	def __str__(self):
		"""

		"""

		class_name = self.__class__.__name__
		return f"[{class_name}] ({self.id}) {self.__dict__}"

	def save(self):
		"""

		"""

		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		"""

		"""

		new_dict = {}
		for key, value in self.__dict__.items():
			if key == "created_at" or key == "updated_at":
				value = value.isoformat()
			new_dict[key] = value
		new_dict["__class__"] = self.__class__.__name__

		return (new_dict)
