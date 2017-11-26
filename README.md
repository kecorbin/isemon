# isemon - ISE Monitoring Portal


# Description

isemon is a self-service portal for accessing authorization information from
Cisco Identity Services Engine.

## Problem

ISE supports a finite number of concurrent user logins (20). There is a requirement
for large sets of users that will require information from ISE to enable support
and troubleshooting processes.

## Solution

Leverage ISE APIs to view required information without the need for the user to log in to ISE.
The proposed solution is to build a portal that will make the required API calls to ISE.
Support teams would have access to this portal, and will be enabled to query information from ISE as needed.



# Installation

## Environment

Prerequisites

* Docker

## Downloading

Provide instructions for how to obtain the software from this repository, if there are multiple options - please include
as many as possible

Option A:

If you have git installed, clone the repository

    git clone https://github.com/kecorbin/isemon


## Installing

After you've cloned the repo, build a docker container and run it!


*NOTE:* make sure to change the ISE settings to match your environment

cd isemon
docker build -t isemon .
docker run -d -p  8000:8000 -e ISE_SERVER=my-ise-server.company.com -e ISE_USERNAME=admin -e ISE_PASSWORD=password isemon


# Development

Provide any notes for other contributors.  This includes how to run tests / etc


## Linting

We use flake 8 to lint our code. Please keep the repository clean by running:

    flake8

## Testing

We should attempt to have unittests with  100% code coverage. An example test suite is contained
within the tests.py file for the boilerplate application

The tests are can be run in the following ways::

    python tests.py


When adding additional code or making changes to the project, please ensure that unit tests are added to cover the
new functionality and that the entire test suite is run against the project before submitting the code.
Minimal code coverage can be verified using tools such as coverage.py.

For instance, after installing coverage.py, the toolkit can be run with the command::

    coverage run tests.py

and an HTML report of the code coverage can be generated with the command::

    coverage html
