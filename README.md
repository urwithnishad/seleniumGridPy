# Python Dockerized-selenium

   Python script to execute by taking the input of URL and runnning headless browser with selenium hub by linking the chrome and firefox. Launching the container and taking the screenshot and pushing the screenshot 
   into s3 bucket.
   
   
  ## Requirements:
  
 1. Python 3.8
 2. Docker
 3. Selenium
 4. webdriver-manager
 5. Aws account to execute s3 Bucket.
 
 #### How To Run 
1. Launch the Container by running docker-compose up command.
2. Run the Python Script and provide the url of running container with port 4444.
3. While running Python scipt it will automatically take the screenshot for given URL.
4. Create a S3 bucket with all the permisssions required to execute the script successfully.
5. Create a AWS IAM user credentials to provide the Access and Secret Key to execute S3 in Python script.

### Note.

1. I have run this on my local machine and I have used Docker-Desktop to run docker command.
2. But it can also run on EC2 instance. While doing so we need to create an instance-AMI where it already contain docker-compose which is already available in Marketplace.
