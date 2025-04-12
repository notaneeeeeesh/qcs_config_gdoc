# Copyright (c) 2025, QCS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GdocProcessorInstance(Document):
    def on_update(self):
        if(self.reference_doctype):
            print("Entered False")
            from qcs_config_gdoc.api.utils import getFields
            # Get the metadata for the "Emirates ID" doctype            
            fields = getFields(self.reference_doctype)                   
            self.sample = f'''import frappe
import json
import base64
from google.api_core.client_options import ClientOptions
from google.cloud import documentai 
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".{self.authentication_file_path}"
opts = ClientOptions(api_endpoint="{self.region}-documentai.googleapis.com")
client = documentai.DocumentProcessorServiceClient(client_options=opts)      
name = client.processor_path("{self.project_id}", "{self.region}", "{self.processor_id}")
image_path = ""  #Add image path 
mime_type = "" #Mention mime type
with open(image_path, "rb") as image:
	image_content = image.read()	
raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type) 
request = documentai.ProcessRequest(
    name=name,
    raw_document=raw_document                
)
result = client.process_document(request=request)
document = result.document 
"""
Contains the fields of the reference doctype
{fields}
"""
'''
             
        else:
            print("Entered True")
            self.sample = f'''import frappe
import json
import base64
from google.api_core.client_options import ClientOptions
from google.cloud import documentai 
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".{self.authentication_file_path}"
opts = ClientOptions(api_endpoint="{self.region}-documentai.googleapis.com")
client = documentai.DocumentProcessorServiceClient(client_options=opts)      
name = client.processor_path("{self.project_id}", "{self.region}", "{self.processor_id}")
image_path = ""  #Add image path 
mime_type = "" #Mention mime type
with open(image_path, "rb") as image:
	image_content = image.read()	
raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type) 
request = documentai.ProcessRequest(
    name=name,
    raw_document=raw_document                
)
result = client.process_document(request=request)
document = result.document 
'''
        
        pass
