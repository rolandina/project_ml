# **TITANIC** 
![](https://github.com/rolandina/titanic/blob/master/front-end/img/1.jpeg)

Project Titanic is a responsive site based on FastApi deployd on Azure Cloud for prediction of the survaval of the passanger of Titanic. 
We took our data with passangers from [seaborn dataset 'titanic'](https://seaborn.pydata.org/generated/seaborn.load_dataset.html).

### Structure of the Project

**Folders:**

[**titanic**](https://github.com/rolandina/titanic/tree/master/titanic) it is a module with two classes Data and Model both used data set Titanic. Class Model will be used in FastApi: 

- [data.py](https://github.com/rolandina/titanic/blob/master/titanic/data.py) - file with class Data
- [model.py](https://github.com/rolandina/titanic/blob/master/titanic/model.py) - file with class Model 
  
[**api**](https://github.com/rolandina/titanic/tree/master/api) it is a folder with api realisation will be used to create image file with Docker:   

- [api](https://github.com/rolandina/titanic/blob/master/api/api.py)
  
[**front-end**](https://github.com/rolandina/titanic/tree/master/front-end) folder with files for creating responsive site:  

- [index.html](https://github.com/rolandina/titanic/blob/master/front-end/index.html) - static site stucture   
- [script.js](https://github.com/rolandina/titanic/blob/master/front-end/script.js) - jquery script for api integration   
- [style.css](https://github.com/rolandina/titanic/blob/master/front-end/style.css) - css file with the style of the site

[**notebooks**](https://github.com/rolandina/titanic/tree/master/notebooks) folder with the notebook for testing model and api:

* [frontend.ipynb](https://github.com/rolandina/titanic/blob/master/notebooks/frontend.ipynb) - notebook to test fast api   
* [model.ipynb](https://github.com/rolandina/titanic/blob/master/notebooks/model.ipynb) - notebook where we test the model

**Docker files**:

* [Dockerefile](https://github.com/rolandina/titanic/blob/master/Dockerfile)
* [docker-compose.yml](https://github.com/rolandina/titanic/blob/master/docker-compose.yml)
* [gunicorn_config.py](https://github.com/rolandina/titanic/blob/master/gunicorn_config.py)

**Other files**:

* [.gitignore](https://github.com/rolandina/titanic/blob/master/.gitignore)
* [README.md](https://github.com/rolandina/titanic/blob/master/README.md) current markdown ReadMe file
* [requirements.txt](https://github.com/rolandina/titanic/blob/master/requirements.txt)
* [Makefile](https://github.com/rolandina/titanic/blob/master/Makefile)
  
* [setup.py](https://github.com/rolandina/titanic/blob/master/setup.py) setup file to build pip project to use package on local machine.
To install package simply run `pip install .` from the root directory of the project.   

## Clone this repository and install package

```
git clone https://github.com/rolandina/titanic.git
cd titanic
pip install .
```

## Create Docker image and deploy api on Azure

To create docker image:

```
docker-compose build
```

To access to the azure registry:

```
docker login titanicfastapi.azurecr.io/titanicfastapi
docker push titanicfastapi.azurecr.io/titanicfastapi
```

To run container with fast api on the laptop:

```
docker run -d --name titanic-fastapi -p 8080:8000 titanicfastapi.azurecr.io/titanicfastapi
```

Address on local host to access fast api titanic after running docker container `0.0.0.0:8080`


## Links on API and Site

[Titanic FastAPI](https://titanicfastapi.azurewebsites.net/docs) - the link on webApp with FastApi deployed on Azure (which probably will not be working by the time you are reading it).


[Titanic Survaval Prediction](https://rolandina.github.io/site_titanic/) - the link on the site deployed on [GitHubPages](https://pages.github.com/) (the site uses the fast api above, so it will not be working as well once the project is finished).




## Contributing

To create this project we have used several libraries and services:
To run fast api we've used:

* [FastApi](https://fastapi.tiangolo.com/)
* [gunicorn](https://gunicorn.org/)
* [Docker](https://www.docker.com/)
  
To deploy fast api on cloud we've used [Azure Portal](https://portal.azure.com/#home).

To create a responsive site we've used [jQuery](https://gunicorn.org/).

## Contacts
If you have any questions you are welcome to contact us:

* [rolandina](https://github.com/rolandina)
* [hugofgry](https://github.com/hugofgry) 
* [AhmadNawzadi](https://github.com/AhmadNawzadi)

