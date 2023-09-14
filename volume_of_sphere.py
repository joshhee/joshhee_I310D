import math

def calculate_volume_of_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius_1 = 30.0
radius_2 = 40.0

volume_1 = calculate_volume_of_sphere(radius_1)
volume_2 = calculate_volume_of_sphere(radius_2)

print(f"The volume of the sphere with radius {radius_1} is {volume_1}")
print(f"The volume of the sphere with radius {radius_2} is {volume_2}")