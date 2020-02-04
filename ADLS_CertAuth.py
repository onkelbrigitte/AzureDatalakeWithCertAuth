import adal
import json
from azure.datalake.store import core, lib
import time

#import config file
config = json.loads(open('config.json','r').read())

#App details
client_id       = config["client_id"]
cert_thumbprint = config["cert_thumbprint"]
authority       = config["authority"]
tenant_id       = config["tenant_id"]
resource        = config["resource"]
pem_file        = config["pem_file"]

#ADL-S details
adls_name       = config["adls_name"]

#read private key in .PEM format from local filesystem
private_key= open(pem_file,'rb').read()
client_credential= {"thumbprint": cert_thumbprint, "private_key": private_key}

#authentificate with certificate
context = adal.AuthenticationContext(authority=authority)
result = context.acquire_token_with_client_certificate(resource=resource,client_id=client_id, certificate=private_key, thumbprint=cert_thumbprint)

#update attributes of dict to be complaint with DataLakeCredential
result.update({'access': result['accessToken'], 'resource': resource,
                'refresh': result.get('refreshToken', False),
                'time': time.time(), 'tenant':tenant_id , 'client': client_id})

adls_creds = lib.DataLakeCredential(result)

#Create a filesystem client object
adlsFileSystemClient = core.AzureDLFileSystem(token=adls_creds, store_name=adls_name)

print(adlsFileSystemClient.ls('/', detail=True))