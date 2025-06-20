<template>
    <div>
        <div class="p-5">
            <div v-if="!flags.disableButtons">
                <Select class="max-w-60" v-if="instanceLabels.length != 0" :options=instanceLabels
                    v-model="selectedInstance" placeholder="Select a Processor Instance" />
            </div>
            <div>
                <div class="file-container">
                    <h1>Please select an image</h1>
                    <form>
                        <input type="file" id="media" accept="image/png, image/jpeg"
                            @change="(event) => handleFileUpload(event)" />
                    </form>
                </div>
                <div class="m-1">
                    <img class="max-h-64" v-if="renderImage" :src="renderImage">
                </div>
                <div>
                    <Button v-if="(selectedInstance != 'None' && imageData.content) && !flags.disableButtons"
                        :loading="(sendImageToProcessor.loading || sendImageToClassifier.loading)" :variant="'subtle'"
                        theme="gray" size="md" label="Button" @click="handleSend">Upload Image</Button>
                    <Button v-if="(imageData.content && selectedInstance == 'None') && !flags.disableButtons"
                        :loading="(sendImageToProcessor.loading || sendImageToClassifier.loading)" :variant="'subtle'"
                        theme="gray" size="md" label="Button" @click="handleSend">Upload Image</Button>
                    <!-- <button class="bg-gray-500 rounded-2xl px-5 mt-2" @click="printData">Print</button> -->
                    <Checkbox class="m-1" v-if="!flags.disableButtons" size="md" :value="false"
                        v-model="flags.submitDirect" label="Create Appropriate Document directly?" />
                </div>
                <div>
                    <div v-if="unsavedProcessedData" class="flex flex-wrap gap-5">
                        <div v-for="(value, field) in unsavedProcessedData" :key="field">
                            <p>{{ field }}</p>
                            <input class="rounded-lg" v-model="unsavedProcessedData[field]" type="text" />
                        </div>
                    </div>
                    <Button class="m-1" v-if="processedData && !flags.submitDirect" :variant="'subtle'" theme="red"
                        size="md" @click="saveEntries">Save?</Button>
                    <Button class="m-1" v-if="processedData && !flags.submitDirect" :variant="'subtle'" theme="red"
                        size="md" @click="handleSubmit">Submit?</Button>
                </div>
            </div>
        </div>
        <div>
            <Dialog :options="{
                title: 'Confirm',
                message: 'Document Created Successfully!',
                size: 'xl',
                actions: [
                    {
                        label: 'Done',
                        variant: 'solid',
                        onClick: () => {
                            reloadPage()
                        },
                    },
                ],
            }" v-model="flags.showDialog" />
        </div>
    </div>
</template>

<script setup>

import { ref, watch, reactive } from "vue";
import { fileToBase64, createResource, createListResource, Select, Checkbox, Dialog } from 'frappe-ui'

const imageData = ref({
    mime: "",
    content: ""
});

const flags = reactive({
    mismatch: false,
    doctype: "doctype",
    disableButtons: false,
    submitDirect: false,
    showDialog: false
})

const selectedDoctype = ref("DocType")

const instanceLabels = ref([{
    'label': "None",
    'value': null
}])
const instanceList = createResource({
    url: 'qcs_config_gdoc.api.utils.getProcessorInstances',
    auto: true
})

const processorLabels = ref()

instanceList.promise.then(() => setInstanceLabels())

const setInstanceLabels = () => {
    instanceList.data.map((instance) => {
        instanceLabels.value.push({
            'label': instance.instance_name,
            'value': instance.name
        })
    })
}

const processedDataKeys = ref()

const unsavedProcessedDataKeys = ref()

const renderImage = ref()

const unsavedProcessedData = ref({})

const processedData = ref()

const selectedInstance = ref("None")

const handleFileUpload = (e) => {
    var file = e.target.files[0]
    if (!file) return;
    fileToBase64(file).then((data) => {
        data = data.split(",")
        renderImage.value = data
        imageData.value.mime = data[0]
        imageData.value.content = data[1]
    })
};

const handleSend = () => {
    if (selectedInstance.value != "None") {
        sendImageToProcessor.submit({
            str: imageData.value,
            instanceName: selectedInstance.value
        },).then((data) => {
            flags.disableButtons = true
            flags.mismatch = false
            processedData.value = data
            processedDataKeys.value = Object.keys(processedData.value)
            unsavedProcessedDataKeys.value = Object.keys(unsavedProcessedData.value)
            if (JSON.stringify(processedDataKeys.value) !== JSON.stringify(unsavedProcessedDataKeys.value)) {
                flags.mismatch = true
            }
            processedDataKeys.value.map((key) => {
                unsavedProcessedData.value[key] = processedData.value[key]
            })

        })
    }
    else {
        sendImageToClassifier.submit({
            str: imageData.value
        },).then((returnData) => {
            flags.disableButtons = true
            flags.mismatch = false
            console.log(returnData)
            selectedDoctype.value = returnData.doctype
            docResource.update({ doctype: selectedDoctype.value })
            docResource.reload()
            console.log(selectedDoctype.value)
            processedData.value = returnData.data
            processedDataKeys.value = Object.keys(processedData.value)
            unsavedProcessedDataKeys.value = Object.keys(unsavedProcessedData.value)
            if (JSON.stringify(processedDataKeys.value) !== JSON.stringify(unsavedProcessedDataKeys.value)) {
                flags.mismatch = true
            }
            processedDataKeys.value.map((key) => {
                unsavedProcessedData.value[key] = processedData.value[key]
            })
        }).then(() => {
            if (flags.submitDirect) {
                handleSubmit()
            }
        })
    }
}

const handleSubmit = () => {
    if (!unsavedProcessedData.value) {
        console.log("empty");
        return
    }
    console.log(selectedDoctype.value)
    docResource.insert.submit(unsavedProcessedData.value).then((d) => {
        console.log(d)
        console.log("Submitted!")
        // window.location.reload();
        flags.showDialog = true
    })
}

// const printData = () => {
//     console.log("Image Data:")
//     console.log(imageData.value)
//     console.log("Receive Data:")
//     console.log(processedData.value)
//     console.log("Unsaved Data:")
//     console.log(unsavedProcessedData.value)
// }

const saveEntries = () => {
    console.log("Saved!")
}

const sendImageToProcessor = createResource({
    url: 'qcs_config_gdoc.api.processors.getProc'
})

const sendImageToClassifier = createResource({
    url: 'qcs_config_gdoc.api.processors.getClassifier'
})

const fieldsResource = createResource({
    url: 'qcs_config_gdoc.api.utils.getFieldsByInstance'
})

watch(selectedInstance, () => {
    console.log(selectedInstance.value)
    if (selectedInstance.value != "None") {
        fieldsResource.submit({ 'instance': selectedInstance.value }).then(() => {
            // unsavedProcessedData.value = {}
            // processorLabels.value = fieldsResource.data.fields
            // processorLabels.value.map((label) => {
            //     unsavedProcessedData.value[label.fieldname] = ""
            // })

            selectedDoctype.value = fieldsResource.data.reference
            docResource.update({ doctype: selectedDoctype.value })
            docResource.reload()
        })
    }
})

const docResource = createListResource({
    doctype: selectedDoctype.value,
    fields: ["*"],
    auto: false
})

const reloadPage = () => window.location.reload()

</script>