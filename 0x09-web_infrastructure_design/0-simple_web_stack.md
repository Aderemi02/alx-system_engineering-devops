Explanation
This is a simple web stack, this has just a single channel access to the website without any load balancing which means if the main server is down the network will be interrupted. this has no security and no monitoring. JUST A SIMPLE WEB STACK.

What a server?
A server can be defined as a computer hardware or software which provides services(attending to requests) of other computers(clients). this can either be physical or virtual and for the physical ones, the are mostly locatded at data centres which collection of servers are stacked in racks. servers runs on Operating systems depending on the type of Operating System you want to use. wehen we use Windows then we have WAMP(Windows/Apache/MySQL/Perl,Python,Php) and when we use Linux we have LAMP(Linux/Apache/MySQL/Perl,Python,Php) and then we have XAMP. the server communicates with the client using an IP address and also transmission of data can either be through TCP or UDP.  

we have the web server and app server.

The role of the web server?
The web server is a software that accepts requests through HTTP/HTTPS and responds with the content of the request with the resource(static content) in a HTML format or returns an error messsage.

The role of the application server?
The application server is a software that accepts requests business-oriented and responds with dynamic content to the client as the requests are not in a specific format or returns an error messsage.

The role of the domain name?
The primary role of a domain name is to make the address of a particular website on the internet become human readable and for us to easily remember how to locate the website on the internet. with this domain name and the help of a DNS, the domain name can be easily converted to the IP address of the website using A, AAAA, DNAME, CNAME record in achieving this.

We have different type of DNS records.
The type of DNS record www is in www.foobar.com is called the A record, this resolves the address to 8.8.8.8 IPv4 address.

The role of the database?
To maintain a collection of organized information that can easily be accessed, managed and updated, the database provides a form of storage for the server where requests from the client can be retrieved and provided to the client. 

What the server uses to communicate with the client?
Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite and when we request from a app server we can also use UDP/IP.

BOTTLENECKS OF THIS INFRASTRUCTURE
There are many SPOFs in this infrastructure.
If the database server is down, the entire site would be down.
If the app server is down, an app request cannot be responded to.
If the web server is down, any HTTP(s) request canno be responded to.
If the network to the server is down no other channel to get information from

Downtime when maintenance needed.
When we need to run some maintenance checks on any component or a new code is to be deployed and web server needs to be restarted, the whole network and traffic to and from the server will be down thereby leading to a very high downtime.

Scalability for too much incoming traffic.
There is little or no scalability in this infrastructure because the size of the server can only accomodate the highest amount of traffic limit it is capable of if too many traffic starts piling this can lead to other clients getting error messages and very slow response from the server.
