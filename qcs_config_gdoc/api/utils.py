import frappe
import json

@frappe.whitelist()
def getFields(doctype):
    meta = frappe.get_meta(doctype)
    fields = []
    # Extract the fieldnames from the metadata
    metafields = meta.fields
    for metafield in metafields:
        metafieldDict = metafield.as_dict()
        if metafieldDict.fieldtype not in ['Column Break','Section Break','Tab Break']:
            fields.append({'label':metafieldDict.label,'fieldname':metafieldDict.fieldname})
    return fields

@frappe.whitelist()
def getFieldsByInstance(instance):
    instance = frappe.get_doc("Gdoc Processor Instance",instance)
    doctype = instance.reference_doctype
    data = getFields(doctype)
    #Return reference doctype embedded within Processor Instance Doctype
    final = {
        'fields': data,
        'reference': doctype
    }
    return final

@frappe.whitelist()
def getProcessorInstances():
    instances = frappe.get_all("Gdoc Processor Instance",fields=["*"])
    return instances

