from PIL import Image, ImageDraw
import imageio

# Set the size of the image
width, height = 400, 200

# Define the colors
color1 = (0, 0, 255)  # blue
color2 = (255, 255, 255)  # white

# Create a list of frames
frames = []
for i in range(10):
    # Create a new image with the alternating colors
    im = Image.new('RGB', (width, height), color1 if i % 2 == 0 else color2)

    # Add the flight information to the image
    draw = ImageDraw.Draw(im)
    draw.text((10, 10), "Youbanistan (BAN)", fill=color2)
    draw.text((10, 30), "Departure Time: Now", fill=color2)

    # Add the image to the list of frames
    frames.append(im)

# Save the frames as a gif
imageio.mimsave('airport.gif', frames, duration=0.5)