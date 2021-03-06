import os
import sys

masterdir = os.path.normpath(os.getcwd() + os.sep + os.pardir).replace("\\","/")
currdir = os.getcwd()
path = ''

file = open("{}/config.txt".format(masterdir), 'r')
lines = file.readlines()
path = lines[3].replace("\\","/").replace("\n","") # typespess folder
file.close()

if (__name__ == "__main__"):
	print("Listing files...")
	with open("imglist.txt", "w", encoding="utf-8") as writing:
		with open("jslist.txt", "w", encoding="utf-8") as writing2:
			for root, dirs, files in os.walk(path): # checks all files and folders in the base folder
				for file in files:
					filesp = file.replace("\n","") # removes the paragraph at the end of the string
					if(file.endswith(".png") or file.endswith(".gif") or file.endswith(".jpg") or file.endswith(".ogg")):
						# if it has one of the extensions, split it so we get the filename without dirs
						filesp = str(root)+"\\"+str(file) # get the absolute directory
						if filesp.find("node_modules") == -1: #exclude the dependency folders
							filesp = file.split("\\") # if it has one of the extensions, split it so we get the filename without dirs
							final_path = filesp[len(filesp)-1]
							if(file.endswith(".png") or file.endswith(".gif") or file.endswith(".jpg")):
								final_path = final_path.replace(".png","")
								final_path = final_path.replace(".gif","")
								final_path = final_path.replace(".jpg","")
								final_path = final_path.replace("-dir1","")
								final_path = final_path.replace("-dir2","")
								final_path = final_path.replace("-dir3","")
								final_path = final_path.replace("-dir4","")
								final_path = "icon_state = \""+final_path+"\""+"\n"
							else:
								final_path = final_path+"\n"
							writing.write(final_path) # return the last value of the splitted array and write to the file
					#moving on to the code file listing...
					elif(file.endswith(".js") or file.endswith(".ts") or file.endswith(".coffee") or file.endswith(".atom")): #search code files
						filesp = str(root)+"\\"+str(file) # get the absolute directory
						if filesp.find("node_modules") == -1: #exclude the dependency folders
							writing2.write(filesp+"\n")
	writing.close()
	writing2.close()

	#all listed, now lets pair
	print("Finished listing the files.")
	print("Checking files...")
	with open("unused.txt","w") as unusedfile: # this is where we will list all the orphaned files
		with open("imglist.txt", "r") as reading3:
			for imgline in reading3:
				found = False
				imgline_parsed = imgline.replace("\n","") # remove the paragraph
				imgline_parsed = imgline_parsed.replace('\\',"/")
				imgline_parsed = imgline_parsed.replace("../../resources/","")
				print("Checking {}".format(imgline_parsed))
				with open("jslist.txt", "r") as reading:
					for jsline in reading:
						jsline_parsed = jsline.replace("\n","")
						imgline_parsed2 = imgline_parsed.replace(".png","")
						imgline_parsed2 = imgline_parsed2.replace(".jpg","")
						imgline_parsed2 = imgline_parsed2.replace(".gif","")
						imgline_parsed2 = imgline_parsed2.replace(".ogg","")
						for x in range(0,10):
							imgline_parsed2 = imgline_parsed2.replace(str(x),"")
						with open(jsline_parsed, "r", encoding="utf-8") as reading2: # opening the files in jslist.txt...
							print("    Checking in {}".format(jsline_parsed))
							for line in reading2: # checking each line
								if line.find(imgline_parsed) != -1 or line.find(imgline_parsed2) != -1: #if either of the img names found
									found = True
									print("        Found! {}".format(line)) # break out of the condition (no need to search the rest of the files)
									break
						if found == True:
							break
				if found == False:
					print("    Not found.")
					#if not found, write to list
					unusedfile.write(imgline)

	unusedfile.close()
	reading.close()
	reading2.close()
	reading3.close()
	print("All done. Check unused.txt for results.")
	print(" ")
	print("Do you want to remove these files? Y/N")
	text = input() 
	if (text == "y" or text == "Y"):
		with open("unused.txt","r") as unusedfile:
			for files in unusedfile:
				files_parsed = files.replace("\n","")
				if (os.path.isfile(files_parsed)):
					os.remove(files_parsed)
					print("Removed {}".format(files_parsed))
				if (os.path.isfile(files_parsed+".json")):
					os.remove(files_parsed+".json")
					print("Removed {}".format(files_parsed+".json"))
	else:
		print("Exiting.")
		sys.exit()