#!/bin/bash
for i in {1..5}
do
   docker run --network ds-net -d --name pub$i node-mqtt
done