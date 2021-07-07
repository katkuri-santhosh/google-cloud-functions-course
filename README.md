# Google Cloud Functions Course
## Starting a Project

To start a project in Google cloud, we can go to the 
[Firebase Console](htts://console.firebase.google.com) or create it from [Google Cloud Platform Consloe](htts://console.cloud.google.com)
## Creating a virtual environment
First we have to install 'python3.venv' with the following command
```
Linux/Ubuntu:
sudo apt install python.venv
Windows:
pip install virtualenv
```

Then we execute below command
```
python -m virtualenv virtualenv
```

Activate Virtual environment use the below command
```.\virtualenv\scripts\activate.bat```

In order to add new packages to our virtual environment we create a file called 
'requirements.txt' and execute the following command

```
pip install -r requirement.txt
```

Go to the File --> Settings --> Click on Project --> python interpreter --> Click on settings Icon and click Add --> Select Virtual environment--> Existing Environment --> Apply

# Deploying our function
First, we have to set our project ID with the following command
```
gcloud config set project [YOUR PROJECT ID]
```

Then we deploy our function with  this command
```
gcloud functions deploy [FUNCTION NAME] --runtime python37 --trigger-http
```

