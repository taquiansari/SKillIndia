# Introduction
SKillIndia is an innovative online platform designed to address the general problems of locality by connecting skilled workers with the local community in need of their services. The platform serves as a bridge between skilled workers, such as sanitation workers, electricians, plumbers, and the general public seeking assistance with various tasks.

## Features

- **Dual Login System:** Separate logins for workers and the general public.
- **User-Friendly Dashboard:** Intuitive interface for easy navigation.
- **Detailed Worker Profiles:** Showcase skills, experience, and ratings.
- **Job Posting:** Public users can post job requests.
- **Job History and Reviews:** Transparent feedback and ratings.
- **Verified Profiles:** Workers can undergo verification for added trust.
- **Customer Support:** Dedicated support for inquiries and assistance.

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
