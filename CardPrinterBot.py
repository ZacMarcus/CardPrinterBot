import serial
import time
import re
from PIL import Image, ImageDraw, ImageFont
import os

def read_rfid(serial_port):
    tag_data = ""
    if serial_port.in_waiting > 0:
        try:
            raw_data = serial_port.readline().decode('ascii').strip()
            # Skip the first 2 bytes, read 10 bytes
            # https://www.aliexpress.com/i/4000052805959.html
            raw_data = raw_data[4:24]
            print (f"Raw: + {raw_data}")
            hex_data_match = re.search(r'[0-9A-Fa-f]+', raw_data)
            if hex_data_match:
                hex_data = hex_data_match.group(0)
                tag_data = int(hex_data, 16)  # Convert the hexadecimal string to a decimal integer
        except (UnicodeDecodeError, ValueError):
            pass  # Ignore non-ASCII characters or invalid data
    return tag_data

def write_string_on_image(text, font_path=None, image_size=(400, 200), bg_color=(255, 255, 255), text_color=(0, 0, 0), font_size=40):
    # Create a new image with the specified size and background color
    image = Image.new('RGB', image_size, bg_color)
    
    # Create a draw object to draw on the image
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("arial.ttf", font_size)

    # Get the size of the text
    text_size = draw.textbbox((0, 0), text, font=font)
    text_width = text_size[2]
    text_height = text_size[3]

    # Calculate the position to center the text on the image
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2
    
    # Write the text on the image
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the image to a file
    #image.save('output_image.png')

    return image

def print_image(image_path):
    os.startfile(image_path, "print")
    print(f"Image sent to the printer")

def main():
    # test printing
    # tag_data = "569267"
    # img = write_string_on_image(tag_data)
    # imageFileName = f"rfid_tag_{tag_data}.png"
    # img.save(imageFileName)
    # print_image(imageFileName)
    # return

    # Configure the serial connection
    serial_port = serial.Serial(
        port='COM3',  # '/dev/serial0' UART port on the Raspberry Pi
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1
    )

    print("RFID Reader Initialized.")
    try:
        while True:
            tag_data = read_rfid(serial_port)
            if tag_data:
                print(f"RFID Tag Detected: {tag_data}")
                img = write_string_on_image(f"{tag_data}")
                imageFileName = f"rfid_tag.png"
                img.save(imageFileName)
                print_image(imageFileName)
                os.remove(imageFileName)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        serial_port.close()

if __name__ == "__main__":
    main()