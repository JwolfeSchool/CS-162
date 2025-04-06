#Function 1
# Returns Area of Rectangle
#Written by Jaden Wolfe
def rect_area(length, width):
 return length * width
#Function 2
# Returns Surface Area of Rectangular Solid
#Written by Asher Knowles
def rect_surface_area(length,width,height):
    return 2*((length*width)+(height*length)+(width*height))
# Request the dimension of a solid rectangular object

length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))

