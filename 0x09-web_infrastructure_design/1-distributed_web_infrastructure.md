Explanation
This is a distributed web infrastructure, this has three server and hosts the website www.foobar.com, in this infrastructure there are two major servers, the primary and the replica and the load balancer, this infrastructure has no security but it has redundancy in check.

Specifics:
Two servers were added to this infrastructure so s to be able to increase the amount of traffic coming to www.foobar.com, herby increasing the scalability, help reduce down-time so when the primary server needs to be deployed with new code, the replica serves, and vice versa. Also if the network to one is down the other serves pending the error is rectified.

Load-balancer is added so as to distribute traffic between the two servers either using the active-active method or the active-passive method, this also helps in diversion of traffic to the server that is running if the other is being upgraded.

The distribution algorithm the load balancer is configured with and how it works?
The load balancer is configured with the Round Robin distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.

The load-balancer(HAproxy) is enabling an Active-Active setup rather than an Active-Active setup.
In an Active-Active setup, the load balancer distributes workloads across all the servers evenly as this with increase the response time and also make sure that traffice with some specific requests like the write request goes to the primary server and others go to the replica evenly thereby increasing the throughput.
In an Active-Passive setup, not all the server will be active, in the case of two servers, one will be active and recieves all the traffic while the other serves as backup to the main server should in case anything happens to the active server, the passive one switche to active mode and serves as the primary server while the other swithes to passive mode.

How a database Primary-Replica (Master-Slave) cluster works?
The database Primary-Replica cluster setup configures the primary server as the master while the replica as the slave. The Primary server performs read/write requests while the replica server performs only read requests. However, Data is synchronized between the Primary and Replica servers whenever the primary server gets a written operation done to it.

Difference between the Primary node and the Replica node in regard to the application?
The Primary node is responsible for all the write operations the site needs whilst the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.

BOTTLENECK OF THIS INFRASTRUCTURE
Where are SPOFs?
The load balancer is a SPOF, because when it is down both servers cannot serve the request of the client
The Primary MySQL database server is also a SPOF, because if the database is down and a write request is sent, it will not be able to make these changes except when the load balancer is in active-passive mode when one server serves the request of the client.

Security issues?
There is no security on this infrastructure, there is no firewall on the servers to enable the network filter out any danger or any security bridges on the network, also there is no SSL installed, this means that the information being recieved by the client cannot be trusted as there is no security handshake between the client and the server.

No monitoring?
There is no monitoring client installed on the server and no data collector that analyzes the data as such theres no way for this infrastructure to be monitored.
