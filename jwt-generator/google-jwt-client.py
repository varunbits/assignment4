#!/usr/bin/env python

import argparse
import time
import google.auth.crypt
import google.auth.jwt
import os

def generate_jwt(audience,
                 sa_email,
                 expiry_length):

    """Generates a signed JSON Web Token using a Google API Service Account."""
    sa_keyfile = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    now = int(time.time())

    payload = {
        'iat': now,
        # expires after 'expiry_length' seconds.
        "exp": now + int(expiry_length),
        # iss must match 'issuer' in the security configuration in your
        # swagger spec (e.g. service account email). It can be any string.
        'iss': sa_email,
        # aud must be either your Endpoints service name, or match the value
        'aud': audience,
        # sub and email should match the service account's email address
        'sub': sa_email,
        'email': sa_email
    }
    signer = google.auth.crypt.RSASigner.from_service_account_file(sa_keyfile)
    jwt = google.auth.jwt.encode(signer, payload)

    return jwt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--audience', help='The audience entry for the JWT')
    parser.add_argument(
        '--sa_email',
        help='The email address for the service account.')
    parser.add_argument(
        '--expiry_length',
        default=86400,
        help='The email address for the service account.')    

    args = parser.parse_args()

    keyfile_jwt = generate_jwt(args.audience,
                               args.sa_email,
                               args.expiry_length)
    print(keyfile_jwt)
