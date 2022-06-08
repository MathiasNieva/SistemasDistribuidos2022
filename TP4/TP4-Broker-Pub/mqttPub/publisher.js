const mqtt = require('mqtt');
const host = process.env.THEHOST;
const topic = process.env.THETOPIC;
var client  = mqtt.connect(host);

const dockerIpTools = require('docker-ip-get');
ip = '127.0.0.1';
dockerIpTools
    .getContainerIp()
    .then((containerIp) => ip=containerIp)
    .catch((err) => console.error(err));

client.on('connect', () =>
{
  console.log('Connected');
  client.subscribe(randomVal("topic"), (err) =>
  {
      console.log("subscribed to")
      console.log(randomVal("topic"))
        if (!err)
        {
          publish();
        }
  });
});
client.on('message', (topic, payload) => {
  console.log('Received Message:', topic, payload.toString())
});

function sleep(ms) 
{
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function publish()
{
    while(true)
    {
        let message = { "control" : randomVal("control"),  "forward" : randomVal("forward"), "ip" : ip }
        client.publish(randomVal("topic"), JSON.stringify(message));
        await sleep(3000);
    }

}
function randomVal(val)
{
    let rndNum = Math.floor(Math.random()*11);
    let value = "";
    if(val === "control")
    {
        if(rndNum % 2 == 0)
        {
            value = "ON";
        }
        else
        {
            value = "OFF";
        }
    }
    else if(val === "forward")
    {
        if(rndNum % 2 == 0)
        {
            value = "True";
        }
        else
        {
            value = "False";
        }
    }
    else
    {
        if(rndNum % 2 == 0)
        {
            value = "forward";
        }
        else
        {
            value = "control";
        }
    }
    return value;
}