
# Flask Image Rotator

This is a Flask app that serves a list of images and rotates them every `rotation_time` minutes. The list of images is stored in a `config.yml` file, which can be easily edited to add or remove images.

### Installation

To run the Flask app, you will need Python 3.9 and the required Python packages. You can install the required packages by running the following command:

```shell
pip install -r requirements.txt
```

### Configuration

The list of images are configured in the `config.yml` file. Here's an example of what the `config.yml` file might look like:

```yaml
image_urls:
  - https://example.com/image1.png
  - https://example.com/image2.png
  - https://example.com/image3.png

image_files:
  - data/image1.png
  - data/image2.png
```

The `config.yml` file also allows you to configure the rotation time, which determines how frequently the images are rotated. Additionally, you have the option to select either URLs or local files as source.

```yaml
rotation_time: 1

use_urls: false
```

To start the Flask app, run the following command:

```shell
gunicorn app:app -b 0.0.0.0:8000
```
This will start the Flask app and make it available at `http://localhost:8000/rotate_image`. You can then access the app in a web browser. Images will rotate but you have to refresh the page to see the new ones.

## Docker

Alternatively, you can run the Flask app inside a Docker container. To do this, you will first need to build the Docker image by running the following command:

```shell
 docker build --tag  background_rotator .
 ```

 Once the image has been built, you can run the Flask app in a Docker container using the following command:

```shell
 docker run -d -p 8000:8000 --name background_rotator  background_rotator
```

This will start a new Docker container and map port 8000 inside the container to port 8000 on the host system. You can then access the app in a web browser at `http://localhost:8000/rotate_image`, images will rotate but you have to refresh the page to see the new ones.