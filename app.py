from flask import Flask, make_response
import requests
import io
import time
import yaml

app = Flask(__name__)
app.config["DEBUG"] = False

# Fetch config
with open('config.yml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

rotation_time = config['rotation_time']
image_urls = config['image_urls']

def fetch_image():
    # Get the current image index based on the current time
    current_index = int(time.time() / (rotation_time * 60)) % len(image_urls)

    # Fetch the image from the current index
    response = requests.get(image_urls[current_index])

    # Convert the image data to a byte stream
    image_stream = io.BytesIO(response.content)

    # Set the response headers to indicate that this is an image file
    headers = {
        'Content-Type': 'image/png'
    }

    # Return the image stream as the response
    return make_response(image_stream.getvalue(), 200, headers)

@app.route('/rotate_image')
def rotate_image():
    return fetch_image()


if __name__ == "__main__":
    app.run(debug=True)