
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
 docker run -d -p 8001:80001-v /Path_to_config_file/config.yml:/app/config.yml --name background_rotator  background_rotator
```

Alternativily, you can use docker-compose to create the container. Create docker-compose.yml and use the `docker-compose_example.yml` as an example.

```shell
cp docker-compose_example.yml docker-compose.yml
```

Replace `/Path_to_config_file` with the path of the repo on the host machine and then run the compose file

```shell
docker-compose up -d
```

This will start a new Docker container and map port 8000 inside the container to port 8000 on the host system. You can then access the app in a web browser at `http://localhost:8001/rotate_image`, images will rotate but you have to refresh the page to see the new ones.
Since config.yml is mapped into the container, you can add and remove images from this file without having to restart the container.

The main objective of this programe is to be used in home dashboards for homelabs. ie. Hommer or flame dashboard.
After you runt he container and provide its link to the dashboarss to use it as beackground image, you will have a rotating background.

## Limitations

The rotation of images is not happening live. You must restart the browser to see the new image. But the main idea is that you have a diferrent background every time you refresh the app.