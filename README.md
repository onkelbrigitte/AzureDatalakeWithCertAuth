# AzureDatalakeWithCertAuth
A sample script in Python how to access Azure Data Lake Store Gen1 with certificate based authentification using AAD service principal.

As the Python SDK for Azure Data Lake Store Gen1 (provided [here](https://github.com/Azure/azure-data-lake-store-python)) doesn't provide a convenient interface to authentificate with a SPN and a certificate, this script demonstrates how to leverage the Python ADAL library for certificate based authentification and pass the credential object to the Python SDK for ADL-S.

Free to use and copy but no warranty provided.
