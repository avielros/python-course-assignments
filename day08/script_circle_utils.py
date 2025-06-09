from circle_utils import circle_area, circle_circumference

def main():
    radius = float(input("What is the circle's radius? "))
    area = circle_area(radius)
    circumference = circle_circumference(radius)
    print(f"The circle's area is: {area}")
    print(f"The circumference is: {circumference}")

if __name__ == "__main__":
    main()
