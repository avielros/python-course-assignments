import sys

def main():
    
    try:
        with open('colors.txt') as fh:
            colors = [line.strip() for line in fh if line.strip()]
    except IOError:
        print("Could not open colors.txt")
        exit()

    
    if not colors:
        print("No colors found in file.")
        exit()

    
    for i, color in enumerate(colors):
        print(f"{i}) {color}")

    
    if len(sys.argv) == 2:
        selection = sys.argv[1]
    else:
        selection = input("Select color by number or name: ")

    
    try:
        index = int(selection)
        if 0 <= index < len(colors):
            print(f"Selected color: {colors[index]}")
        else:
            print("Invalid index")
    except ValueError:
        
        normalized = selection.strip().lower()
        matched = [c for c in colors if c.lower() == normalized]
        if matched:
            print(f"Selected color: {matched[0]}")
        else:
            print("Color not found in list")

if __name__ == "__main__":
    main()
