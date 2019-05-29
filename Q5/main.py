import os

def create_dir(name, address):
	directory = str(address) + '/' + str(name)
	if not os.path.exists(directory):
		os.makedirs(directory)



create_dir('ahz', 'ahz')