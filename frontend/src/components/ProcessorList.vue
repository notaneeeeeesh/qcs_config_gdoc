<template>
    <div>
        <Select v-if="instanceLabels.length != 0" :options=instanceLabels v-model="selectedInstance" placeholder="Select a Processor Instance" />
    </div>
</template>

<script setup>
import { ref, watchEffect, watch, reactive } from 'vue'
import { createResource, Button, Select, Spinner, Textarea } from 'frappe-ui'
const props = defineProps(['testRef'])
const selectedInstance = props.testRef
const instanceLabels = ref([])
const instanceList = createResource({
    url: 'qcs_config_gdoc.api.utils.getProcessorInstances',
    auto: true
})
instanceList.promise.then(() => setInstanceLabels())
const setInstanceLabels = () => {
    console.log(instanceList.data)
    instanceList.data.map((instance) => {
        instanceLabels.value.push({
            'label': instance.instance_name,
            'value': instance.name
        })
    })
    console.log(instanceLabels.value)
}
watch(selectedInstance, () => console.log(selectedInstance.value))
</script>