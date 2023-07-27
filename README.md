# Bitespeed Backend Task: Identity Reconciliation 

Bitespeed needs a way to identify and keep track of a customer's identity across multiple purchases.

We know that orders on FluxKart.com will always have either an **`email`** or **`phoneNumber`** in the checkout event.

Bitespeed keeps track of the collected contact information in a relational database table named **`Contact`.**

## Steps to run the project

In the project directory, you can run:

### git clone <repo-name>

This clones the project

### docker-compose build

Builds the project on docker

### docker-compose up

Runs the project on the development server and the exposed endpoint is
``/identity``

Resume link : https://drive.google.com/file/d/1GbWdjxdOsHAsEIJHSzaUwbhEibBjo2X_/view?usp=sharing