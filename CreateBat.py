
def exit():
	input("Press any key to continue...")

def createFiles():
	# Open File
	# fh = open("script.bat", "w")
	fileName = raw_input("Enter Filename: ")
	fh = open(fileName+".bat", "r")
	print(fileName+".bat")
	exit()

	# Edit File

	line1 = "C:/mingw/bin/gcc -c src/toRun.c -o obj/toRun.o"
	line2 = "\nC:/mingw/bin/gcc -o bin/runC.exe obj/toRun.o"
	line3 = "\npause"
	
	fh.write(line1)
	fh.write(line2)
	fh.write(line3)


	# Close File 
	fh.close()

	def runFiles():
		# Read Batch File 
		fh = open("script.bat", "r")
		print fh.readlines()
		
		# Read C Executable
		fh = open("\bin\runC.exe", "r")
		print fh.readLines()
	
	runFiles()
	
	
	
createFiles()
# runFiles()