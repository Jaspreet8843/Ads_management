## Ads Management System
Hosted on https://ads-management.herokuapp.com/ <br/>
Username: admin <br/>
Password: adminadmin <br/>
> This project is totally built on Desktop View, so rendering on responsive screen will generate random positioning of elements.

## Overview
This project helps you in managing the advertisement records of an agency. It allows you to add customer and their advertisement. This website also generates the scheduled advertisements for the day and over a period of time. This also generates a bill for a customer for their advertisements as specified by the organisation.

## Project Flow
* Admin adds customer
* Admin add advertisement for the customer
* Accept the advertisement for a specified date
* Generate bill for the advertisement
* Clears the bill after payment

## Project
The project is built with
* Django Framework
* HTML CSS JS
* ORM Model Django

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Jaspreet8843/Ads_management.git
$ cd Ads_management
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m virtualenv myenv
$ myenv\Scripts\activate
```

Then install the dependencies:

```sh
(myenv)$ pip install -r requirements.txt
```
Note the `(myenv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(myenv)$ py manage.py runserver
```
And navigate to `http://127.0.0.1:8000/Ads_management/`.

## Walkthrough
The project has only admin side. It allows 
1. Login
2. Add/View Customer/s
3. Add/View/Accept Advertisements
4. Generate/View Bills
5. View Schedule

## Snapshots
Column 1 | Column 2
------------ | -------------
![](https://user-images.githubusercontent.com/46393531/124586586-3d3e5580-de74-11eb-81fa-9f22436d1ff5.png) | ![](https://user-images.githubusercontent.com/46393531/124586810-89899580-de74-11eb-9252-483c4edef17a.png)
Login | Home Page
![](https://user-images.githubusercontent.com/46393531/124586979-bfc71500-de74-11eb-86d2-8581686de79a.png) | ![](https://user-images.githubusercontent.com/46393531/124587022-cb1a4080-de74-11eb-80ff-f1c45e1e4461.png)
View Customers | View Advertisements
![](https://user-images.githubusercontent.com/46393531/124587121-e5ecb500-de74-11eb-87a6-85e5dae3b110.png) | ![](https://user-images.githubusercontent.com/46393531/124587162-f13fe080-de74-11eb-9e55-39343849a9d9.png)
View Bills | Show Schedule



