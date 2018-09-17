# Postmortem

## Issue Summary 6:45 - 6:48 UTC
At approximately 6:45 UTC on September 10th 2018 one of our load balancers went offline leading to unbalanced traffic to our web servers and poor performance for our customers for four minutes. During this time some users would have trouble connecting to our web services. This incident occurred outside of peak traffic hours and as such only affected 10% of total users.

## Timeline

**6:45 UTC**: Monitoring software alerts that loadBalancer01 has gone offline

**6:46 UTC**: Issue is escalated to devops team

**6:48 UTC**: Two new load balancers are deployed while an investigation into loadBalancer01 begins

**6:49 UTC**: Investigation into why loadBalancer01 suddenly went offline begins

**7:00 UTC**: Investigation team begins running diagnostics on affected server

**7:15 UTC**: Diagnostics complete

**7:20 UTC**: Investigatory team determines that sudden spike of traffic caused loadBalancer01 to overload

## Root Cause
The primary cause was an unexpected influx of incoming traffic. The load balancer setup at the time was not ready for any sudden traffic spikes higher than the average peak usage from current metrics. In order to combat the issue, the devops team brought up two new load balancers to take the place of the affected loadBalancer01.

## Corrective and Preventative Measures
A third permanent load balancer has been brought online in addition to implementing a new system to auto-deploy additional servers and load balancers as traffic begins to spike on the network. Furthermore, the current load balancer setup does not handle failure of a load balancer very well, as a result, the devops team will begin implementing failover procedures for our load balancers so that in the case of a failure, another server can step in immeadiately. Additionally, the investigation team found the nginx install on the load balancer was out of date and will begin a new software update procedure for all servers going forward.
