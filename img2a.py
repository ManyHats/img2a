import sys
from PIL import Image


def main():
    img = get_file()
    print_characters(img)

def get_file():
    if len(sys.argv) != 2:
        print("Usage: $ python img2a.py {Path/to/file}")
        sys.exit()
    else:
        return Image.open(sys.argv[1]).convert("LA")

def print_characters(img):
    x = 0
    y = 0
    with open("output.txt", 'w') as f:
        for px in range(img.size[0] * img.size[1]):
            pixel_color = img.getpixel((x, y))
            
            # TODO: Clean up this mess, and choose better characters
            if pixel_color[0] >= 0 and pixel_color[0] < 20:
                f.write('x')
                f.write('@')
            elif pixel_color[0] >= 20 and pixel_color[0] < 40:
                f.write('x')
                f.write('%')
            elif pixel_color[0] >= 40 and pixel_color[0] < 60:
                f.write('x')
                f.write('&')
            elif pixel_color[0] >= 60 and pixel_color[0] < 80:
                f.write('x')
                f.write('#')
            elif pixel_color[0] >= 80 and pixel_color[0] < 100:
                f.write('x')
                f.write('$')
            elif pixel_color[0] >= 100 and pixel_color[0] < 120:
                f.write('x')
                f.write('W')
            elif pixel_color[0] >= 120 and pixel_color[0] < 140:
                f.write('x')
                f.write('T')
            elif pixel_color[0] >= 140 and pixel_color[0] < 160:
                f.write('x')
                f.write('O')
            elif pixel_color[0] >= 160 and pixel_color[0] < 180:
                f.write('x')
                f.write('G')
            elif pixel_color[0] >= 180 and pixel_color[0] < 200:
                f.write('x')
                f.write('L')
            elif pixel_color[0] >= 200 and pixel_color[0] < 240:
                f.write('x')
                f.write('V')
            elif pixel_color[0] <= 255:
                f.write(' ')
                f.write(' ')

            x += 1

            if x == (img.size[0]):
                y += 1
                x = 0
                f.write('\n')
        f.close()


if __name__ == "__main__":
    main()
