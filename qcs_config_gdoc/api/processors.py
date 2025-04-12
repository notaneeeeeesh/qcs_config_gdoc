import frappe
import json
import os
from typing import Optional
from google.api_core.client_options import ClientOptions
from google.cloud import documentai  
from frappe import _

@frappe.whitelist()
def getProc(instanceName, str):
    instance = frappe.get_doc("Gdoc Processor Instance", instanceName)
    mime_type = str["mime"].split(":")[1].split(";")[0]
    call = callGdoc(location = instance.region, processor_id = instance.processor_id, project_id = instance.project_id, authentication = instance.authentication_file_path, mime = mime_type, image = str["content"])
    return call
       
    
@frappe.whitelist()
def callGdoc(project_id,location,processor_id,authentication,image,mime):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"./{frappe.local.site}{authentication}"
    content = image
    mime_type = mime
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    name = client.processor_path(project_id, location, processor_id)
    # Load binary data
    raw_document = documentai.RawDocument(content=content, mime_type=mime_type)

    # For more information: https://cloud.google.com/document-ai/docs/reference/rest/v1/ProcessOptions
    # Configure the process request
    request = documentai.ProcessRequest(
        name=name,
        raw_document=raw_document
    )
    
    result = client.process_document(request=request)

    # For a full list of `Document` object attributes, reference this page:
    # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document

    arr = []
    for entity in result.document.entities:
        # print(entity)
        arr.append(f'"{entity.type}":"{entity.mention_text}"')
    finalStr = '{' + ",".join(arr) + '}'
    data = json.loads(finalStr)
    return data
    
    # return {
    #     "card_number": "123456789",
    #     "date_expiry": "11/09/2024",
    #     "date_issue": "09/09/2022",
    #     "date_of_birth": "14/10/1974",
    #     "employer_ar": "\u0627\u0644\u062a\u0642\u0646\u064a\u0627\u062a \u0627\u0644\u0647\u0646\u062f\u0633\u064a\u0629 \u0644\u0644\u062e\u062f\u0645\u0627\u062a",
    #     "employer_en": "Engineering Tech. Services",
    #     "full_name_ar": "\u0647\u064a\u0645\u064a\u0646\u062a\u064a\u0631\u0627 \u0641\u0648\u064a\u0646\u062a\u064a\u0633",
    #     "full_name_en": "John Bush Travolta",
    #     "id": "xx4-xxxx-46xxxx7-0",
    #     "nationality_ar": "\u0627\u0644\u0641\u0644\u0628\u064a\u0646",
    #     "nationality_en": "Philippines",
    #     "occupation_ar": "\u0645\u0631\u0627\u0642\u0628 \u0627\u0644\u0645\u0628\u064a\u062f\u0627\u062a \u0627\u0644\u062d\u0634\u0631\u064a\u0629",
    #     "occupation_en": "Actor",
    #     "place_of_issue_ar": "\u0627\u0644\u0634\u0627\u0631\u0642\u0629",
    #     "place_of_issue_en": "Dubai",
    #     "scan_number": "2x0xxxx8xx"
    # }

