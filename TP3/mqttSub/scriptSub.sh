#!/bin/bash
for i in {1..5}
do
   docker run -d -e "THEHOST=mqtt://research.upb.edu:21132" -e "THETOPIC=ds" --name sub$i alpine-node-sub
done