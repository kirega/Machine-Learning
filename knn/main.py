import math

class KNN():
	"this is to demonstrate the use of KNN"
	def __init__(self):
		print """
		KNN - CSC 323 
		Rapando C Samson
		Kirega Joseph
		Adrian Wanderi
		"""
		
		self.data = []
		self.sample = []
		
		# load the data
		with open("data.json", "r") as f:
			for line in f:
				sample = line.strip('\n').split(' ')
				for x in sample:
					print int(x),
				print
			
		
		
	pass
	
knn = KNN()
