from PIL import Image

# TODO: Add command line argument file input
def main():
    img = Image.open("index.png").convert("LA")
    print_characters(img)


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

            x += 1  # Add 1 to X for each pixel looped through

            if x == (img.size[0]):  # If loop reaches width of image
                y += 1
                x = 0
                f.write('\n')
        f.close()


if __name__ == "__main__":
    main()
