import math
from os import listdir
from os.path import isfile, join

class KNN():
	"this is to demonstrate the use of KNN"
	def __init__(self):
		print """
___________________________________________

			KNN - CSC 323 
			Rapando C Samson
			Kirega Joseph
			Adrian Wanderi
___________________________________________

		"""
		
		self.data = []
		self.no_samples = self.attributes =  0

		folder = "../files/"

		print "Choose a file from the ones below : \n"
		files = [f for f in listdir(folder) if isfile(join(folder, f))]
		for f in files:
			print f

		pass

	def load_data(self):
		pass

		
	# 	with open("../files/heart.data.txt", "r") as f:
	# 		for line in f:
	# 			sample = line.strip('\r\n').split(' ')
	# 			one_sample = []
	# 			for x in sample:
	# 				one_sample.append(x)
	# 			self.data.append(one_sample)
	# 	del self.data[-1]

	# 	self.no_samples = len(self.data)
	# 	self.attributes = len(self.data[-1]) - 1

	# 	print "The data has "

		
	# pass
	
knn = KNN()
