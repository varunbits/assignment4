## JWT Generator

This repository contains script built on Python to generate a JWT token signed by Google Service Account in order to authenticate incoming requests from interfacing systems.

Whenever the external service wants to access to protected route or resource, it should send the JWT in the Authorization header using Bearer schema.

The content of the header should look like the following:

```bash
Authorization: Bearer <token>
```

## How to Use

Assuming you have Docker installed

First step, clone this repo and creates a file called service_account.json then copy secret key into it and finally build docker image locally

```bash
docker build -t jwt-generator .
```

Second step, run docker container using previous image with the following parameters:

- sa_keyfile: The local path to the service account's private key file.
- audience: Identifies the recipient that the JWT is intended.
- sa_email: The service account's email address.

```bash
docker run -e GOOGLE_APPLICATION_CREDENTIALS=service_account.json -v <sa_keyfile>:/service_account.json --rm jwt-generator --audience=<your-audience> --sa_email=<2020mt93070@wilp.bits-pilani.ac.in>
```