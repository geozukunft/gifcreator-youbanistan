from PIL import Image, ImageDraw
import imageio

# Set the size of the image and the font size for the text
width, height = 400, 200
font_size = 16

# Define the colors
bg_color = (0, 0, 0)  # black
fg_color = (255, 255, 255)  # white
highlight_color = (255, 0, 0)  # red

# Define the flight information
airport_name = "Youbanistan (BAN)"
departure_time = "Now"
flight_status = "Boarding Now"

flights = [
    {
        "flight_number": "ABC123",
        "destination": "Youbanistan (BAN)",
        "departure_time": "Now",
        "status": "Boarding Now",
    },
    {
        "flight_number": "DEF456",
        "destination": "Aeroville (ARV)",
        "departure_time": "12:30",
        "status": "On Time",
    },
    {
        "flight_number": "GHI789",
        "destination": "Foggy City (FOG)",
        "departure_time": "13:00",
        "status": "Delayed",
    },
]

# Define the grid properties
num_rows = 8
row_height = height // num_rows
col_widths = [80, 120, 80, 80]

# Create a list of frames
frames = []
for i in range(20):
    # Create a new image with the black background
    im = Image.new('RGB', (width, height), bg_color)

    # Add the flight information to the image
    draw = ImageDraw.Draw(im)

    # Draw the column headers
    draw.text((10, 5), "Flight", fill=fg_color)
    draw.text((90, 5), "Destination", fill=fg_color)
    draw.text((210, 5), "Departure", fill=fg_color)
    draw.text((290, 5), "Status", fill=fg_color)

    # Draw the rows
    for j in range(num_rows):
        # Determine the background color for this row
        row_color = fg_color if j % 2 == 0 else bg_color

        # Draw the row background
        draw.rectangle((0, row_height * j + font_size + 5, width, row_height * (j + 1)), fill=row_color)

        # Draw the flight information in each column
        flight = flights[j % len(flights)]
        draw.text((10, row_height * j + font_size * 2 + 5), flight["flight_number"], fill=fg_color)
        draw.text((90, row_height * j + font_size * 2 + 5), flight["destination"], fill=fg_color)
        draw.text((210, row_height * j + font_size * 2 + 5), flight["departure_time"], fill=fg_color)

        # Highlight the row for the flight to Youbanistan (BAN)
        if airport_name.startswith("Youbanistan"):
            draw.rectangle((0, row_height * j + font_size + 5, width, row_height * (j + 1)), outline=highlight_color)
            draw.rectangle((1, row_height * j + font_size + 6, width - 1, row_height * (j + 1) - 1),
                           outline=highlight_color)

        # Draw the flight status in the last column
        if airport_name.startswith("Youbanistan") and i % 2 == 0:
            draw.text((290, row_height * j + font_size * 2 + 5), flight["status"], fill=highlight_color)
        else:
            draw.text((290, row_height * j + font_size * 2 + 5), flight["status"], fill=fg_color)

    # Add the image to the list of frames
    frames.append(im)

# Save the frames as a gif
imageio.mimsave('departure_table.gif', frames, duration=0.5)