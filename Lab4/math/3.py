import math
number_of_sides = float(input("Input number of sides: "))
lenght_of_side = float(input("Input the length a side: "))
# площадь правильного многоугольника равна произведению радиуса вписанной окружности и полупериметра
angle_of_polygon = (number_of_sides - 2) / number_of_sides * 180 # находим угол многоугольника
radius_of_inner_circle = math.tan(math.radians(angle_of_polygon / 2)) * lenght_of_side / 2 
# радиус вписанной окружности внутри многоугольника
semi_perimeter = number_of_sides * lenght_of_side / 2
area = radius_of_inner_circle * semi_perimeter
print("The area of the polygon is", round(area, 3))