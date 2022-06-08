var mqtt = require('mqtt')
const host = process.env.THEHOST
const topic = process.env.THETOPIC
var client  = mqtt.connect(host)

client.on('connect', () => {
  console.log('Connected to host');
  client.subscribe(topic, (err) => {
      console.log("Subscribed to topic")
        /*if (!err) {
        client.publish(topic, 'Hello mqtt')
        }*/
  })
})

client.on('message', (topic, message) => {

  console.log(message.toString())

})