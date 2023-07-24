# Strip-The-Text - Frontend

---

## Setting up and Using the Project

Before you can run the project, some preparations need to be made first. These are described in the following.

### Cloning the Project

To open the project yourself in any IDE, the project must first be cloned. To do this, enter the following command in a
terminal:

```shell
git https://github.com/StripTheText/TextStrip-Backend.git
```

### Setting Up the Project

After successfully cloning the project, a folder named **TextStrip - Frontend** should now be located in the current
terminal directory. The project is now located in this folder. The structure of the project is as follows:

```text
|- TextStrip-Backend
|  |- api
|  |  |- classifier
|  |  |  |- __init__.py
|  |  |  |- api_models.py
|  |  |- summarizer
|  |  |  |- __init__.py
|  |  |  |- api_models.py
|  |  |- __init__.py
|  |  |- .gitkeep
|  |- models
|  |  |- classifier
|  |  |  |- classification_rnn_2.0
|  |  |  |  |- assets
|  |  |  |  |- variables
|  |  |  |  |  |- variables.data-00000-of-00001
|  |  |  |  |  |- variables.index
|  |  |  |  |- fingerprint.pb
|  |  |  |  |- keras_metadata.pb
|  |  |  |  |- saved_model.pb
|  |  |  |- .gitkeep
|  |  |- summarizer
|  |  |  |- .gitkeep
|  |- .gitignore
|  |- Dockerfile
|  |- environment.yml
|  |- LICENSE
|  |- main.py
|  |- README.md
|  |- requirements.txt
```

The **functions** folder contains all supporting functions that arise during the execution of the project. The **models** folder contains all trained models, which are needed on the different pages (**pages**). A detailed guide on how to
use it can be found on the Pages - Handbook page once the app is running.

### Installing the Project Dependencies

Before you can run the project, the project's dependencies must first be installed. There are the following options for
this: **[pip](https://pip.pypa.io/en/stable/)**, **[conda](https://docs.conda.io/en/latest/)** and **[venv](https://docs.python.org/3/library/venv.html)**. All three options are described below, but require an installed
version of Python (This project was developed with Python 3.11.*). If there is no suitable version of Python installed,
yet, it can be downloaded from the official **[Python website](https://www.python.org/downloads/)**.

**Note:** In addition to the project's dependencies, there are other dependencies defined by the operating system.
Please pay attention to the corresponding error messages.

#### Installation with pip

To install the dependencies with pip, the following command must be entered into a terminal:

```shell
pip install -r requirements.txt
```

**Note:** This method installs the packages globally. If this is not desired, one of the other methods should be used.

#### Installation with conda

Before you can install the individual dependencies, conda must first be installed and active. Please refer to the
official documentation of **[conda](https://docs.conda.io/en/latest/)**. After conda has been set up, it makes sense to
create a separate environment for this project, where only the required libraries are installed. To do this, follow
these steps:

```shell
conda create --name <Name of the Environment> python=3.11
```

After creating the environment, it must first be activated by the following step.

```shell
conda activate <Name of the Environment>
```

**Note:** If the environment is no longer needed, it can be deactivated again with the following command. It may also be
necessary to reactivate the environment at each new session.

```shell
conda deactivate
```

After the environment has been activated, the dependencies can now be installed. To do this, the following command must
be entered into a terminal (with activated environment):

```shell
conda install --file requirements.txt
```

#### Installation with venv

To install the dependencies with venv, a new environment must also be created by the following command in a terminal:

```shell
python -m venv <Name of the Environment>
```

After the environment has been created, it must first be activated by the following step.

```shell
<Name of the Environment>\Scripts\activate.bat
```

**Note:** If the environment is no longer needed, it can be deactivated again with the following command. It may also be
necessary to reactivate the environment at each new session.

```shell
deactivate
```

After the environment has been activated, the dependencies can now be installed. To do this, the following command must
be entered into a terminal (with activated environment):

```shell
pip install -r requirements.txt
```

With that, all dependencies are now installed and the project can be executed.

Natürlich, hier ist ein zusätzlicher Abschnitt, der beschreibt, wie man das Projekt über ein Docker-Image ausführt.

### Running the Project Using a Docker Image

If you want to run this project using a Docker container, you can do so using the provided Docker image. This can be
particularly useful as it abstracts away dependency management and provides a self-contained environment for running the
application.

First, you need to have Docker installed on your machine. If you don't, you can download it from the official Docker
website: **[Docker](https://www.docker.com/get-started)**.

Once Docker is installed and running, you can pull the Docker image for this project using the following command in your
terminal:

```shell
docker pull tkister/strip_the_text_backend
```

After successfully pulling the image, you can run the container with the following command:

```shell
docker run -p 8080:8080 tkister/strip_the_text_backend
```

The `-p` option maps the port 8501 in the container to port 8501 on your local machine, which is the default port for
Streamlit applications.

Now, you should be able to access the Streamlit application in your web browser at `http://localhost:8080`.

Remember, any changes made inside the container will not be persistent. If you want to modify the application code or
add your own files, consider building your own Docker image or directly running the application on your local machine.

### Running the Project

To run the project, the environment in which the dependencies have been installed must first be activated. The project
can then be run with the following command:

```shell
uvicorn main:app --host localhost --port 8080 --reload
```

The project is now running and can be accessed in the browser at `http://localhost:8080`.
For Information on how to use the project, refer to the Information provided on the web-page.

# [StripTheText 2.0 - Backend](https://app.tango.us/app/workflow/a5fb78da-563c-4d75-8a72-67f904588f16?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)

These are the Steps how to perform the different Tasks through the Backend of the Application.

__Creation Date:__ July 24, 2023  
__Created By:__ Tobias Kister  
[View most recent version on Tango.us](https://app.tango.us/app/workflow/a5fb78da-563c-4d75-8a72-67f904588f16?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)



***




## # [StripTheText 2.0: Classification](http://localhost:8080/#/)
As the first Step it is required to open the Webpage of the Application: [localhost/8080](localhost:8080)


### 1. Select the API-Entpoint
For the Task of the Classification, please select the API-Entpoint "/api/classifier"
![Step 1 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/a02a33d4-2f70-4abb-9164-203ab5e4a686/ebcdcec5-af27-4989-8e2a-d711da276456.png?crop=focalpoint&fit=crop&fp-x=0.4777&fp-y=0.4388&fp-z=1.0281&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=34&mark-y=343&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTExJmg9NDEmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 2. For testing the API please press the Button "Try it Out"
![Step 2 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/7aeec2ca-fdca-4a10-ab8f-9629f33f2598/68098500-7335-4173-87ff-c71ec11ddd26.png?crop=focalpoint&fit=crop&fp-x=0.7439&fp-y=0.6073&fp-z=2.8624&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=383&mark-y=346&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz00MzMmaD0xMTQmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 3. Inserting of Data
In the Textfield change the Value "String" to your requested text, please Note Line Breaks are not supported, caused by the JSON-Format.
![Step 3 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/9bbe6d7a-f1c0-456f-9468-5d6030ef16ab/093b8d1f-528d-4dc3-8a92-3c1c0c4fb690.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.4560&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=221&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9MzI0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 4. Example Values
![Step 4 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/37368560-2e85-4d94-8510-f0f9c95c002e/d40c0cb5-471b-4d57-bbd0-57f484b89aa0.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.5901&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=299&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9MzI0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 5. Click on Execute
![Step 5 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/3be9f607-c1c2-4b99-a6d8-2bc4591849d2/cfdc17cd-b677-4c8c-84c7-ce9e1d5dfcc1.png?crop=focalpoint&fit=crop&fp-x=0.2731&fp-y=0.8734&fp-z=1.3393&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=80&mark-y=643&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz03MTgmaD01MyZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 6. Results
When you scroll down, you will see your result in JSON-Format at the position of the StatusCode 200.
![Step 6 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/8cb71a1c-250e-4a87-a226-e6f693d06e82/350cb5ba-358a-4449-8334-10351aba67b7.png?crop=focalpoint&fit=crop&fp-x=0.5303&fp-y=0.4453&fp-z=1.1312&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=38&mark-y=354&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTI1Jmg9OTgmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


## # [StripTheText 2.0: Compression](http://localhost:8080/#/)


### 7. Selcet your API-Endpoint
Both summarizer Entpoints will work, the one with "/compress", will also include the Compression Rate.
![Step 7 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/d7445cd9-3314-467a-954e-09d39b9983d1/3b40ffa8-b3da-4677-aa9d-f948749b4a1f.png?crop=focalpoint&fit=crop&fp-x=0.1751&fp-y=0.2162&fp-z=2.3041&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=299&mark-y=369&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNzEmaD02NiZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)


### 8. Click on Try it out
![Step 8 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/08803c8c-9fbd-4b92-9e10-3de44f93243f/d28fdcea-2772-4bc4-9542-04082e82c863.png?crop=focalpoint&fit=crop&fp-x=0.8916&fp-y=0.1148&fp-z=2.8624&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=648&mark-y=208&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zNTkmaD0xMTQmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 9. Change your Requested Data
![Step 9 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/1651ba95-4af7-47e5-88bb-c03db0703923/252563d7-1ee8-4383-a7af-da930ef242d1.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.3659&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=145&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9MzI0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)


### 10. Click on Execute
![Step 10 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/5a102442-3f01-4397-aa1b-f3a9336cadd2/104815bd-9be0-4fc5-9106-9a38bd047c85.png?crop=focalpoint&fit=crop&fp-x=0.4924&fp-y=0.6406&fp-z=1.0420&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=35&mark-y=480&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTMxJmg9NDkmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)


### 11. View your Results.
![Step 11 screenshot](https://images.tango.us/workflows/a5fb78da-563c-4d75-8a72-67f904588f16/steps/4b32d291-9d07-4deb-9666-d61aae0d82b1/3324801c-cb85-4caf-9a52-a7082d75e474.png?crop=focalpoint&fit=crop&fp-x=0.5303&fp-y=0.7124&fp-z=1.1312&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=38&mark-y=452&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTI1Jmg9MTg0JmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)

<br/>

***
Created with [Tango.us](https://tango.us?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)

---

### License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.
