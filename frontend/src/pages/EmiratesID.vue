<template>
    <div>
        <div class="p-5">
            <div class="w-fit">
                <Select v-if="instanceLabels.length != 0" :options=instanceLabels v-model="selectedInstance"
                    placeholder="Select a Processor Instance" />
            </div>
            <h1 class="container">Upload Image</h1>
            <div>
                <div class="file-container">
                    <div>
                        <form>
                            <input type="file" id="media" accept="image/png"
                                @change="(event) => handleFileUpload(event)" />
                        </form>
                    </div>
                </div>
                <div>
                    <img v-if="renderImage" :src="renderImage">
                </div>
                <button v-if="selectedInstance" class="bg-gray-500 rounded-2xl px-5 mt-2"
                    @click="handleSend">Send?</button>
                <!-- <button class="bg-gray-500 rounded-2xl px-5 mt-2" @click="printData">Print</button> -->
                <div>
                    <!-- <h1 v-if="flags.mismatch" class="bg-red-600">WARNING: MISMATCHING FIELD NAMES BETWEEN DOCTYPE AND PROCESSOR FIELDS</h1> -->
                    <div v-if="unsavedProcessedData" class="flex flex-wrap gap-5">
                        <div v-for="(value, field) in unsavedProcessedData" :key="field">
                            <p>{{ field }}</p>
                            <input v-model="unsavedProcessedData[field]" type="text" />
                        </div>
                    </div>
                    <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="processedData"
                        @click="saveEntries">Save?</button>
                    <!-- <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="processedData && !flags.mismatch"
                        @click="handleSubmit">Submit?</button> -->
                    <button class="bg-red-300 rounded-2xl px-5 mt-5" v-if="processedData"
                        @click="handleSubmit">Submit?</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import { ref, watch, reactive } from "vue";
import { fileToBase64, createResource, createListResource, Select } from 'frappe-ui'

const imageData = ref({
    mime: "",
    content: ""
});

const flags = reactive({
    mismatch: false,
    doctype: "doctype"
})

const selectedDoctype = ref("DocType")

const instanceLabels = ref([])
const instanceList = createResource({
    url: 'qcs_config_gdoc.api.utils.getProcessorInstances',
    auto: true
})

const processorLabels = ref()

instanceList.promise.then(() => setInstanceLabels())

const setInstanceLabels = () => {
    // console.log(instanceList.data)
    instanceList.data.map((instance) => {
        instanceLabels.value.push({
            'label': instance.instance_name,
            'value': instance.name
        })
    })
    // console.log(instanceLabels.value)
}

const processedDataKeys = ref()

const unsavedProcessedDataKeys = ref()

const renderImage = ref()

const unsavedProcessedData = ref({})

const processedData = ref()

const selectedInstance = ref()

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
    sendImage.submit({
        str: imageData.value,
        instanceName: selectedInstance.value
    },).then((data) => {
        flags.mismatch = false
        processedData.value = data
        processedDataKeys.value = Object.keys(processedData.value)
        // console.log(processedDataKeys.value.sort())
        unsavedProcessedDataKeys.value = Object.keys(unsavedProcessedData.value)
        // console.log(unsavedProcessedDataKeys.value.sort())
        if (JSON.stringify(processedDataKeys.value) !== JSON.stringify(unsavedProcessedDataKeys.value)) {
            flags.mismatch = true
        }
        processedDataKeys.value.map((key) => {
            unsavedProcessedData.value[key] = processedData.value[key]
        })
        // console.log(unsavedProcessedData.value)
    })
}

const handleSubmit = () => {
    if (!unsavedProcessedData.value) {
        console.log("empty");
        return
    }
    docResource.insert.submit(unsavedProcessedData.value).then((d) => {
        console.log(d)
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

const sendImage = createResource({
    url: 'qcs_config_gdoc.api.processors.getProc'
})

// const testResource = createResource({
//     url: 'qcs_config_gdoc.api.utils.test',
//     auto: true
// })

const fieldsResource = createResource({
    url: 'qcs_config_gdoc.api.utils.getFieldsByInstance'
})

watch(selectedInstance, () => {
    fieldsResource.submit({ 'instance': selectedInstance.value }).then(() => {
        unsavedProcessedData.value = {}
        processorLabels.value = fieldsResource.data.fields
        processorLabels.value.map((label) => {
            unsavedProcessedData.value[label.fieldname] = ""
            // console.log(label.fieldname)
        })

        selectedDoctype.value = fieldsResource.data.reference
        docResource.update({ doctype: selectedDoctype.value })
        docResource.reload()
        // console.log(unsavedProcessedData.value)
    })
})

const docResource = createListResource({
    doctype: selectedDoctype.value,
    fields: ["*"],
    auto: false
})

</script>