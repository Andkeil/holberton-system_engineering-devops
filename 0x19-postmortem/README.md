# Postmortem

## Issue Summary
At approximately 6:45 UTC on September 10th 2018 our primary load balancer went offline leading to unbalanced traffic to our web servers and poor performance for our customers

## Timeline

**6:45 UTC**: Monitoring software alerts that loadBalancer01 has gone offline

**6:46 UTC**: A new loadBalancer is one click deployed while an investigation into loadBalancer01 begins

**6:47 - 7:00 UTC**: Investigation into why loadBalancer01 suddenly went offline

## Root Cause
The primary cause was an unexpected influx of incoming traffic

## Corective and Preventative Measures
A third permanent load balancer has been brought online in addition to implementing a new system to auto-deploy additional servers and load balancers as traffic begins to spike on the network
