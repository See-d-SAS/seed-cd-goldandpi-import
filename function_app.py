import azure.functions as func
import logging
import os
from azure.storage.blob import BlobServiceClient, generate_blob_sas, AccountSasPermissions
from integrity_test import integrity_test

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

STORAGEACCOUNTURL=os.environ["STORAGEACCOUNTURL"]
STORAGEACCOUNTKEY=os.environ["STORAGEACCOUNTKEY"]
CONTAINERNAMESOURCE=os.environ["CONTAINERNAMESOURCE"]

@app.route(route="integritytrigger")
def integritytrigger(myblob: func.InputStream):
    logging.info('Python HTTP trigger function processed a request.')
    blob_service_client_instance = BlobServiceClient(
    account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
    BLOBNAME  =  myblob.name.split("/")[-1]
    blob_client_instance = blob_service_client_instance.get_blob_client(
    CONTAINERNAMESOURCE, BLOBNAME, snapshot=None) 
    blob_data = blob_client_instance.download_blob()
    data = blob_data.readall()
    integrity_test(data)