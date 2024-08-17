# python-web-app

Step 0: Install docker

Step 1: Build the Docker Image
Navigate to the directory containing your Dockerfile and app.py, and run the following command to build the Docker image:

docker build -t python-web-app .

Step 2: Run the Docker Container
To run the Docker container with the default message, execute:

docker run -p 5000:5000 python-web-app

To run the Docker container with a custom message, you can override the MESSAGE environment variable like this:

docker run -p 5000:5000 -e MESSAGE="Your Custom Message" python-web-app

Step 3: Access the API
You can access the REST API by navigating to http://localhost:5000/api/message in your web browser or by using curl:
