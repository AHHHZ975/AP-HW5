import os

def create_dir(name, address):
	directory = str(address) + '/' + str(name)
	if not os.path.exists(directory):
		os.makedirs(directory)


def create_file(name, address):
	directory = str(address)
	if not os.path.exists(directory):
		os.makedirs(directory)
	with open(os.path.join(directory, str(name)), 'w'):
		pass

create_dir('ahz', 'ahz')
create_file('ahz.txt', 'ahz')