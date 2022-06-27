#!/usr/bin/python3
"""

"""

import json

class FileStorage:
	"""
	
	"""
	__file_path = open("file.json", "w", encoding="utf-8")
	__objects = {}
	def all(self):
		"""
		
		"""
		return FileStorage.__objects
	
	def new(self, obj):
		"""
		
		"""

		FileStorage.__objects = f"{type(obj).__name__}.{obj.id}"

	def save(self):
		"""

		"""
		with open("file.json", "w", encoding="utf-8") as file:
			json.dump(FileStorage.__objects, file)
	
	def reload(self):
		"""
		
		"""
		if FileStorage.__file_path:
			with open("file.json", "r", encoding="utf-8") as file:
				json.load(file)

