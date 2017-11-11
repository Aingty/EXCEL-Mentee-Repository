     
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:56:03 2017

@author: Cesar Hernandez

HW 3: Modifying PPM images
"""
import os

def read_first_three_lines(infile, outfile):
   val_first_threelines = []
   i = 0
   while i < 3: 
       line = infile.readline().strip()
       val_first_threelines.append(line)
       i += 1
       
   return val_first_threelines
    
def process_header(infile=None, outfile=None):        
    commands = {
            'negate' : 'negate',
            'contrast' : 'increase_contrast',
            'grayscale' : 'get_grayscale',
            'remove color' :'remove_color'
            }
#    for key in commands:
#        print(key + '\n')
    values_of_lines = read_first_three_lines(infile, outfile)
    #print(values_of_lines)
    if values_of_lines[0] != 'P3':
        print ("Sorry, this file doesn't meet the specifications of it being P3.")
        return    
    outfile.write(str(values_of_lines[0]))
    #print(line)
    
    outfile.write(str('\n' + values_of_lines[1]))
    #print(line)
    
    if values_of_lines[2] != '255':
        print ("Sorry this file doesn't meet the specification of max 255 value.")
        return
    outfile.write(str('\n' + values_of_lines[2] + '\n'))
    
    #this for loop goes through the dictionary to give the user directions on how to call the functions
    for command in commands:
        print(command)
    modification_question = input("\nWhat would you like to do with file? (P.S. remove_color and modify third are under construction): ")
#    i = 3
#    while i > 0:  
#        if modification_question != commands:
#            print("What you typed in isn't a command!")
#            print('You have %d attempts left to put in a correct command\n' % (i))
#            for command in commands:
#                print (command)
#            modification_question = input("\nWhat would you like to do with file? (P.S. remove_color and modify third are under construction): ")
#        i -= 1
#        if i == 0:
#            return print('You have failed to put in a correct command! You have dishonered your Family!!!')
        
    modification = commands[modification_question]
    print (modification)
    process_body(infile, outfile, modification)

def process_body(infile=None, outfile=None, modification=None):
    for line in infile:
        line = line.strip().split()
        #print("Reading Line: ", line)
        rgb = []
        values_of_a_line = []
        for values in line:
            values_of_a_line.append(values)
        for values in values_of_a_line:
            rgb.append(values)
            if len(rgb) == 3:
                if modification == "get_grayscale":
                    gray = get_grayscale(rgb[0], rgb[1], rgb[2]) + ' '
                    outfile.write(gray * 3)
                    rgb = []
                elif modification == "negate":
                    colors = negate(rgb[0], rgb[1], rgb[2]) 
                    for x in colors:
                        r = colors[0]
                        g = colors[1]
                        b = colors[2]
                    #print ('this is the output of: ', r , g, b)
                    #print('values of rgb:', rgb)
                    #print("output of colors", rgb)
                    colors = str(r) + ' ' + str(g) + ' ' + str(b) + ' ' 
                    outfile.write(colors)
                    rgb = []
                elif modification == "increase_contrast":
                    for x in rgb:
                        contrast = increase_contrast(int(x))
                        outfile.write(str(contrast) + ' ')
                        #print (contrast)
                        rgb = []
                elif modification == "remove_color":
                    pass
                    color_removed = input("What color do you want removed? ")
                    remove_colors = remove_color(rgb[0], rgb[1], rgb[2], color_removed)
                    print (remove_colors)
                    outfile.write(str(remove_colors))
                    rgb = []
                elif modification == 'modify_thirds':
                    pass
        

#negate is done but not in a way that it meets requirement
def negate(red, green, blue):
    #to negate what I thought I could do is make get the number for the rgb and then subtract it from 255    
    r = 255 - int(red)
    g = 255 - int(green)
    b = 255 - int(blue)
    values = [r, g, b]
    return values
#grayscale is done too 
def get_grayscale(r, g, b):
    average = ((0.2126 * float(r)) + (0.7152 * float(g)) + (0.0722 * float(b))) #equation for grayscale
    return str(int(average))

#in progress
def increase_contrast(num):
    if 0 < num < 255:
        if num >= 127:
            num = 255
        else:
            num = 0
    return num

#in progress
def remove_color(R, G, B, user_input):
    pass
    if (0 < int(R) < 255) and (0 < int(G) < 255) and (0 < int(B) < 255):   
        if (user_input == "Red") or (user_input == "red"):
            R = 0
            return R and G and B
        elif (user_input == "Red") or (user_input == "red") and (user_input == "Green") or (user_input == "green"):
            R = 0
            G = 0
            return R, G
        elif (user_input == "Red") or (user_input == "red") and (user_input == "Blue") or (user_input == "blue"):
            R = 0
            B = 0
            return R, B
        elif (user_input == "Green") or (user_input == "green"):
            G = 0
            return G
        elif (user_input == "Green") or (user_input == "green") and (user_input == "Red") or (user_input == "red"):
            R = 0
            G = 0
            return R, G  
        elif (user_input == "Green") or (user_input == "green") and (user_input == "Blue") or (user_input == "Blue"):
            G = 0
            B = 0
            return G, B
        elif (user_input == "Blue") or (user_input == "blue"):
            B = 0
            return B
        elif (user_input == "Blue") or (user_input == "blue") and (user_input == "Green") or (user_input == "green"):
            G = 0
            B = 0
            return G, B
        elif (user_input == "Blue") or (user_input == "blue") and (user_input == "Red") or (user_input == "red"):
            R = 0
            B = 0
            return R, B

def modify_thirds(R, G, B, pixels):
    #this makes the program split the pixels into thirds and then modifies them
    """just a thought but floor division the area of the picture"""
    pixels = dimensions
    pass 

#this is where all the functions should be put together
def main():
    #actual main script
#    file_name = input('Please enter in a ppm file name (please be sure to add .ppm at the end): ')  #you need to check if this file exists
#    checking_file_name = os.path.isfile(file_name)
#    if checking_file_name == False:
#        return print("Sorry this file doesn't exist.")
    #print(checking_file_name)
    #infile = open(file_name)  
    infile = open('2x1.ppm') #this is just to check the the output of the program
     
    #gets the users input then checks to see if there is a file named what the user input
    #output_file_name = input("Please enter in an output ppm file name that doesn't exist (please be sure to add .ppm at the end): ")
    #checking_output_file = os.path.isfile(output_file_name)
#    if checking_output_file == True:
#        return print("Sorry this file already exists.")
    #outfile = open(output_file_name, 'w')        # opens file for writing
    outfile = open('2x1copy.ppm', 'w') #this is just to check the the output of the program
   
    process_header(infile, outfile) #if this is correct this should open the file and then send the file to the function as the arguement and then modify it
    #read_line(infile, outfile)

if __name__ == '__main__':
    main()

"""this code is still in progress"""
