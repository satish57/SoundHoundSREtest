# SoundHoundSREtest
SoundHound SRE Take-Home Assignment

Task 1: Containerization

Step 1: Build the Docker Image Navigate to the directory containing your Dockerfile and app.py, and run the following command to build the Docker image:
docker build -t python-web-app .
Step 2: Run the Docker Container To run the Docker container with the default message, execute:
docker run -p 5000:5000 python-web-app
To run the Docker container with a custom message, you can override the MESSAGE environment variable like this:
docker run -p 5000:5000 -e MESSAGE="Your Custom Message" python-web-app
Step 3: Access the API You can access the REST API by navigating to http://localhost:5000/api/message in your web browser or by using curl: curl http://localhost:5000/api/message

Orchestration 

Step 1: Build the deployment YAML file
Step 2: Build the Service YAML file
Step 3: Build the Ingress YAML file
Accessing the Application, once everything is set up:

The application will be accessible within the cluster through the service at http://python-web-app-service.
The Ingress will expose the application externally at http://sretest.com/. 

Task 2: Observability

Step 1: Setting Up Prometheus on Kubernetes
1.1 Create a prometheus-config.yaml file
1.2 Create a prometheus-deployment.yaml file
1.3 Create a prometheus-service.yaml file

Apply the configuration
kubectl apply -f prometheus-deployment.yaml

Step 2: Setting Up a Python Application with a Custom Metric
2.1 Create a Simple Python Application
pip install Flask prometheus_client
2.2 Create a Dockerfile
Build the Docker image and run the Dockercontainer
2.3 Deploy the Python Application to Kubernetes
kubectl apply -f python-app-deployment.yaml
kubectl apply -f python-app-service.yaml
Step 3: Verifying Prometheus Setup
Access the Prometheus UI using the NodePort defined earlier (http://<node-ip>:30090).
In the Prometheus UI, go to the "Targets" page (Status > Targets) to verify that the Python application's metrics endpoint is being scraped.
You can also query the request_count metric in the "Graph" tab to see the number of requests.
This setup ensures that Prometheus is correctly configured to scrape metrics from your Python application deployed on Kubernetes.
