#!/usr/bin/python3
"""

"""

import json

class FileStorage:
	"""
	
	"""
	__file_path = "file.json"
	__objects = {}
	def all(self):
		"""
		
		"""
		return FileStorage.__objects
	
	def new(self, obj):
		"""
		
		"""
		key = f"{type(obj).__name__}.{obj.id}"
		FileStorage.__objects[key] = obj.to_dict()

	def save(self):
		"""

		"""
		with open(FileStorage.__file_path, "a", encoding="utf-8") as file:
			json.dump(FileStorage.__objects, file)
	
	def reload(self):
		"""
		
		"""
		try:
			with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
				json.load(file)
		except Exception:
			pass
