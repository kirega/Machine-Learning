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

		self.folder = "../files/"

		print "LIST OF FILES AVAILABLE\n"
		self.files = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
		x = 1
		for f in self.files:
			print x, f
			x += 1
		print

		self.load_data()

	def load_data(self):
		chosen = int(raw_input("Choose the data file to load : ", ))
		chosen_file = self.files[chosen - 1]
		print "You have chosen ", chosen_file, "...\n"

		#load the data to the self.data variable
		with open(self.folder + chosen_file, "r") as f:
			for line in f:
				sample = line.strip('\r\n').split(' ')
				one_sample = []
				for x in sample:
					try:
						one_sample.append(float(x))
					except:
						one_sample.append(x)
				self.data.append(one_sample)
		print "The data has been loaded..."

		if len(self.data[-1]) == 1:
			del self.data[-1]

		for sample in self.data:
			sample[-1] = int(sample[-1])

		self.no_samples = len(self.data)
		self.attributes = len(self.data[-1]) - 1

		print "The data has ",self.no_samples, "samples and has ", self.attributes, " attributes."

		# for i in self.data:
		# 	print i

	def load_sample(self):
		attributes = self.attributes
		data = self.data
		no_samples = self.no_samples

		sample = []
		print
		for i in range(attributes):
			print "Enter Attribute ", i+1,
			x = raw_input()
			sample.append(x)

		print
	
knn = KNN()
knn.load_sample()