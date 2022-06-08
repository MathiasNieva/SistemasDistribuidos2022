var mqtt = require('mqtt');
const dockerIpTools = require("docker-ip-get");
const host = process.env.THEHOST;
const topic = process.env.THETOPIC;
var client  = mqtt.connect(host);
const os = require('os');

ip = '127.0.0.1';

dockerIpTools
   .getContainerIp()
   .then((containerIp) => ip=containerIp)
   .catch((err) => console.error(err));

client.on('connect', () =>
{
  console.log('Connected');
  client.subscribe(topic, (err) =>
  {
      console.log("subscribed")
        if (!err)
        {
          publish();
        }
  });
});

async function publish() {
  while(true)
  {
    let message = `"Time": ${''+new Date}, "Container" :  ${os.hostname()}, "IP": ${''+ip}`;
    client.publish(topic, message);
    await sleep(5000);
  }
}

client.on('message', (topic, message) => 
{

  console.log(message.toString());

});
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}