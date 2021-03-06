import os
import sys

path1 = ''

def parse_line(line, line_parsed):
	tline = line.replace("RECIPE: ", "")
	if (len(line_parsed) != 13):
		print("Error! This line does not have a length of 13 - {}".format(tline))
		return ""
	else:
		otype=line_parsed[0].replace("/material/","")
		otype=otype.replace("/","")
		CSONstring = '{}:\n'.format(line_parsed[1])
		CSONstring += '	template_name: "{}"\n'.format(line_parsed[1])
		CSONstring += '	name: "{}"\n'.format(line_parsed[1])
		CSONstring += '	cost: {}\n'.format(line_parsed[3])
		CSONstring += '	res_amount: {}\n'.format(line_parsed[3])
		CSONstring += '	time: {}{}\n'.format(line_parsed[4], "00") # deciseconds to miliseconds
		CSONstring += "	on_floor: true\n"
		CSONstring += '	category: "{}"\n'.format(line_parsed[7])
		CSONstring += '	age1: {}\n'.format(line_parsed[8])
		CSONstring += '	age2: {}\n'.format(line_parsed[9])
		CSONstring += '	age3: {}\n'.format(line_parsed[10])
		CSONstring += '	last_age: {}\n'.format(line_parsed[11])
		CSONstring += "	material: {}\n".format(otype)
		CSONstring += '	opath: "{}"\n'.format(line_parsed[0])
		CSONstring += "END: true\n"
		return CSONstring

if (__name__ == "__main__"):
	masterdir = os.path.normpath(os.getcwd() + os.sep + os.pardir).replace("\\","/")
	outputdir = masterdir+"/recipe-converter/"
	currdir = os.getcwd()

	file = open("{}/config.txt".format(masterdir), 'r')
	lines = file.readlines()
	path1 = lines[1].replace("\\","/").replace("\n","") # civ folder
	file.close()

	if path1 == '':
		print("Error! No configs found.")
		sys.exit()
	
	fullCSON = ""
	material_list = []
	rfile = open("{}/config/material_recipes.txt".format(path1), 'r')
	rlines = rfile.readlines()
	print("Reading recipe list...")
	for line in rlines:
		line = line.replace("\n","")
		if line.find("RECIPE: ", 0, 10) != -1:
			if line != "":
				tline = line.replace("RECIPE: ", "")
				line_parsed = tline.split(",")
				fullCSON += parse_line(line, line_parsed)
				if line_parsed[0].find("/material/") != -1:
					otype=line_parsed[0].replace("/material/","")
					otype=otype.replace("/","")
					if not (otype in material_list):
						material_list.append(otype)
						print("Added new material {}".format(otype))

	print("	done")
	splitfullCSON = fullCSON.split("END: true\n")
	for material in material_list:
		print("Writing {} recipes...".format(material))
		crafting_file = open("{}recipes/{}.crafting".format(outputdir,material), "w")
		for rec in splitfullCSON:
			if rec.find("	material: {}\n".format(material)) != -1:
				crafting_file.write(rec)
		crafting_file.close()
	print("All finished.")
	sys.exit()


