print('''Remove Duplicate Files''')
import os
def remove_file():
	MainFolder = r'{0}'.format(input("Copy & Paste the path of folder containing duplicate files")) #Main folder where all files some of them were duplicate
	duplicatfiles = os.listdir(MainFolder)

	ChosenFolder =r'{0}'.format(input("Copy paste the path of folder those were may be common in target folder")) #Folder contains files make be common files in Main Folder 
	files= os.listdir(ChosenFolder)

	for file in duplicatfiles:
		if file in files:
			commonfiles = os.path.join(MainFolder, file) #It detect common files
			print(commonfiles)
			os.remove(commonfiles)# remove common files from main folder
	print("All the similiar files were deleted from " + MainFolder)

remove_file()