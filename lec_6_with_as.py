with open("myfile.txt", "r") as file:
    '''
    myfile.txt
    mama
    wash
    frame
    '''
    lines = file.readlines()
    for line in lines:
	    print(line.strip())