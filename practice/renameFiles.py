import os
# Function to rename multiple files
def main():
	i = 0
	path="F:\NEWFolder"
	for filename in os.listdir(path):
		if filename.startswith("_") == True:
			my_dest = filename[1:5] + "_" + filename[5:]

		#my_dest ="new" + str(i) + ".jpg"
		my_source =path + filename
		my_dest =path + my_dest
		# rename() function will
		# rename all the files
		os.rename(my_source, my_dest)
		i += 1
	print(i)
# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()