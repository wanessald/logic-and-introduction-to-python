import os
import math
import platform

def input_data_coordinate():
    x0 = float(input("Enter the x0 coordinate: "))
    y0 = float(input("Enter the y0 coordinate: "))
    x1 = float(input("Enter the x1 coordinate: "))
    y1 = float(input("Enter the y1 coordinate: "))
    x2 = float(input("Enter the x2 coordinate: "))
    y2 = float(input("Enter the y2 coordinate: "))
    
    return [x0, y0, x1, y1, x2, y2]

def calculate_distance_between_two_points(coordinates):
    distance_ab = math.sqrt((coordinates[2] - coordinates[0])**2 + (coordinates[3] - coordinates[1])**2)
    distance_bc = math.sqrt((coordinates[4] - coordinates[2])**2 + (coordinates[5] - coordinates[3])**2)
    distance_ca = math.sqrt((coordinates[0] - coordinates[4])**2 + (coordinates[1] - coordinates[5])**2)
    
    semi_perimeter = (distance_ab + distance_bc + distance_ca) / 2

    area = math.sqrt(semi_perimeter*(semi_perimeter - distance_ab)*(semi_perimeter - distance_bc)*(semi_perimeter - distance_ca))
    return area
   
def main():
        system_name = platform.system()
        
        try:
            if system_name == 'Windows':
                os.system("cls")
            elif system_name in ['Linux', 'Darwin']:
                os.system("clear")
            else:
                print(f"Unsupported operating system: {system_name}")
        except Exception as e:
            print(f"An error occurred while trying to clear the terminal: {e}")    

        coordinates = input_data_coordinate()  
        calculate_distance_between_two_points(coordinates)
        area_of_triangle = calculate_distance_between_two_points(coordinates)
        
        print(f"\nA triangle with vertices {coordinates[0], coordinates[1]}, {coordinates[2], coordinates[3]}, and {coordinates[4], coordinates[5]} has an area of: {area_of_triangle:.2f}.\n")

main()
