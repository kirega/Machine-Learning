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
		
		# load the data
		with open("data.json", "r") as f:
			for line in f:
				sample = line.strip('\n').split(' ')
				one_sample = []
				for x in sample:
					one_sample.append(int(x))
				self.data.append(one_sample)
		
	pass
	
knn = KNN()
print knn.data
