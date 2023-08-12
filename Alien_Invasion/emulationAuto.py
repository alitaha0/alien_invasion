import time

from PIL import Image


 

def get_average_color(image, left, top, right, bottom):

    segment = image.crop((left, top, right, bottom))

    rgb_values = segment.getdata()

    total_pixels = len(rgb_values)

    total_red = total_green = total_blue = 0


 

    for r, g, b in rgb_values:

        total_red += r

        total_green += g

        total_blue += b


 

    avg_red = total_red // total_pixels

    avg_green = total_green // total_pixels

    avg_blue = total_blue // total_pixels


 

    return (avg_red, avg_green, avg_blue)


 

# Path to the image

image_path = r"C:\slotMachine\image.jpeg"


 

# Define the segment coordinates as a list of tuples

segment_coordinates = [

    (133, 2705, 363, 2882), # Segment 1

    (543, 2705, 773, 2882), # Segment 2

    (953, 2705, 1183, 2882), # Segment 3

    (1363, 2705, 1593, 2882), # Segment 4

    (1773, 2705, 2003, 2882), # Segment 5

    (133, 3044, 363, 3221), # Segment 6

    (543, 3044, 773, 3221), # Segment 7

    (953, 3044, 1183, 3221), # Segment 8

    (1363, 3044, 1593, 3221), # Segment 9

    (1773, 3044, 2003, 3221), # Segment 10

    (133, 3383, 363, 3561), # Segment 11

    (543, 3383, 773, 3561), # Segment 12

    (953, 3383, 1183, 3561), # Segment 13

    (1363, 3383, 1593, 3561), # Segment 14

    (1773, 3383, 2003, 3561) # Segment 15

]


 

# Open the image

image = Image.open(image_path)

image.show()

# Create a 2D array to store the results

result_array = [["          " for _ in range(5)] for _ in range(3)]


 

# Color threshold

threshold = 255

"""

# Iterate over the segment coordinates

for i, (left, top, right, bottom) in enumerate(segment_coordinates):

    average_color = get_average_color(image, left, top, right, bottom)

    r, g, b = average_color

   

    if (

        abs(r - 92) <= threshold and

        abs(g - 29) <= threshold and

        abs(b - 15) <= threshold

    ):

        result_array[i // 5][i % 5] = "Cherry    "

    if (

        abs(r - 79) <= threshold and

        abs(g - 52) <= threshold and

        abs(b - 24) <= threshold

    ):

        result_array[i // 5][i % 5] = "Watermelon"



 

    if (

        abs(r - 135) <= threshold and

        abs(g - 74) <= threshold and

        abs(b - 16) <= threshold

    ):

        result_array[i // 5][i % 5] = "Dollar    "

    if (

        abs(r - 130) <= threshold and

        abs(g - 90) <= threshold and

        abs(b - 12) <= threshold

    ):

        result_array[i // 5][i % 5] = "Lemon     "

    if (

        abs(r - 123) <= threshold and

        abs(g - 59) <= threshold and

        abs(b - 14) <= threshold

        and result_array[i // 5][i % 5] != "Dollar    "


 

    ):

        result_array[i // 5][i % 5] = "Orange    "


 

    if (

        abs(r - 120) <= threshold and

        abs(g - 39) <= threshold and

        abs(b - 15) <= threshold


 

    ):

        result_array[i // 5][i % 5] = "Seven     "


 

    if (

        abs(r - 88) <= threshold and

        abs(g - 59) <= threshold and

        abs(b - 47) <= threshold

    ):

        result_array[i // 5][i % 5] = "Star      "


 

    if (

        abs(r - 126) <= threshold and

        abs(g - 79) <= threshold and

        abs(b - 35) <= threshold

    ):

        result_array[i // 5][i % 5] = "Bell      "

   

    if (

        abs(r - 55) <= threshold and

        abs(g - 36) <= threshold and

        abs(b - 63) <= threshold

    ):

        result_array[i // 5][i % 5] = "Grapes    "

    if (

        abs(r - 96) <= threshold and

        abs(g - 25) <= threshold and

        abs(b - 61) <= threshold

    ):

        result_array[i // 5][i % 5] = "Plum      "

   

"""


 

color_mapping = {    


 

    (198, 151, 68):"Bell       ", #done

    (126, 72, 31): "Cherry     ", #done

    (94, 157, 27):"Green Hat  ",

    (195, 109, 32): "Orange     ", #done

    (200, 72, 31): "Seven      ", # done

    (209, 88, 47): "Seven      ",

    (152, 42, 148):"Plum       ", #done

    (214, 186, 37):"Lemon      ",  #done

    (147, 126, 72):"Watermelon ", #done

    (70, 67, 106):"Grapes     ", #Done

    (187, 87, 31):"Red Hat    ", #done


 

    (140, 94, 40):"Fireball   ",

    (158, 100, 45):"Fireball   ",

    (167, 110, 51):"Fireball   ",

    (147, 101, 45):"Fireball   ",

    (218, 137, 77):"Fireball   "


 

   

}


 

result_array = [[""] * 5 for _ in range(len(segment_coordinates) // 5)]

accuracy_array = [[threshold*3+1] * 5 for _ in range(len(segment_coordinates) // 5)]


 

for i, (left, top, right, bottom) in enumerate(segment_coordinates):

    average_color = get_average_color(image, left, top, right, bottom)

    r, g, b = average_color

   

    for color, label in color_mapping.items():


 

        if (

            abs(r - color[0]) <= threshold and

            abs(g - color[1]) <= threshold and

            abs(b - color[2]) <= threshold

        ):

            TotalDifference = abs(r - color[0]) + abs(g - color[1]) + abs(b - color[2])

            if TotalDifference < accuracy_array[i // 5][i % 5]:

                result_array[i // 5][i % 5] = label

                accuracy_array[i // 5][i % 5] = TotalDifference

               


 

# Print the result array

for row in result_array:

    print(row)


 

#for accRow in accuracy_array:

#    print(accRow)