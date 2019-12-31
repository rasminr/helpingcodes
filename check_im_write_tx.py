#python code that reads a text file, compares files in another folder and copies
#all the files annotated in the text file to a newfolder
import os,shutil


im_list=os.listdir("train_images")

#fo = open("annotate.txt", "r")

#result = line.find('.png') 

fo = open("annotatenew.txt", "a")
with open("annotate.txt") as f:
	
	for line in f:
		end = line.find('.png')
		start=line.find('train_images/')
		filename=line[start+13:end+4]
		#print(filename)
		path="train_images/"
		filepath=path+str(filename)
		for image in im_list:
			#print(image)
			if image==filename:
				fo.write(line)
					
   
	   

