""" 
Created on Wednesday 8 00:43 2017
@author: Cesar Hernandez

"""
def grayscale(R=None, G=None, B=None):
    average =(0.2126 * float(R) + (0.2126 * float(G)) + (0.2126 * float(B)))
    return average

rgb = []

list_values = []

output = []

file = open('4x4.ppm')

i = 0
while i < 3:
    line = file.readline().strip()
    print(line)
    i += 1
values = file.readerline().strip().split()

for v in values:
    list_values.append(v)

for value in list_values:
    rgb.append(value)
    if len(rgb) == 3:
        gray = grayscale(rgb[0], rgb[1], rgb[2])
        output.append(gray)
print(output)