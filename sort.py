import sys


def sort(width, height, length, mass):
    if (width > 0 and height > 0 and length > 0 and mass > 0) is False:
        raise ValueError("Dimensions and mass must be greater then 0")
    
    bulky = False
    heavy = False
    if width * height * length > 1000000:
        bulky = True
    elif width > 150 or height > 150 or length > 150:
        bulky = True
    if mass > 20:
        heavy = True
    
    if bulky and heavy:
        return "REJECTED"
    
    if bulky or heavy:
        return "SPECIAL"
    
    return "STANDARD"


if __name__ == "__main__":
    if len(sys.argv) == 5:
        try:
            width = int(sys.argv[1])
            height = int(sys.argv[2])
            length = int(sys.argv[3])
            mass = int(sys.argv[4])
        except Exception as e:
            raise ValueError("All values must be integer")
        print(sort(width, height, length, mass))
    else:
        print("Missing arguments")