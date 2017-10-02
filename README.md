# Fusion maps

# maps_and_addresses

This is a single page with a full viewport map on top and a list of addresses below based on Django 1.9, Django Rest Framework and
AngularJS 1.6.4.

Installation
Fork this repo, download as zip or clone it. Create a virtualenv on your machine and install required packages listed in the
requirements.txt.

## Setup

First before running the project you need to-do :-):
1. edit the `settings.py` file to setup your **GOOGLE_API_KEY
and GOOGLE_FUSIONTABLE_ID**.
2. create a new **google api service account** for the api dashboard:
<https://console.developers.google.com/apis/credentials/serviceaccountkey> and place the downloaded json file in the root folder of this
project, and replace content of file named `client_secrets.json` with downloaded data.
3. create a new fusion table <https://fusiontables.google.com> and share it with the newly created service account.
4. prepare the env and run it:

Then open up your browser and go to <http://localhost:8000/addresses>
