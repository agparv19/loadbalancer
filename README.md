This is a basic load balancer which can route traffic to multiple backend servers using round robin. This load balancer takes care of checking server health periodically and removes/adds server when they go down/come back up.

Motivation: [this coding challenge](https://codingchallenges.fyi/challenges/challenge-load-balancer)

Before starting the load balancer, you need to start backend servers. You can do this using:
```
./start_async_server -p <port>
```

This will start a backend server on `127.0.0.1:<port>`. You need to start at least two such servers to see load balancer in action.

Once few backend servers are started, start the load balancer using:
```
./start_loadbalance -lp 8080 -sp [2000, 2001, 2002] -ht 10
```

`8080` is the port at which loadbalacer will start.
`[2000, 2001, 2002]` is the list of ports on which three backend servers are listening on.
`10` seconds is the time period for running health check on these servers.

Now as a client you can send requests to the load balancer using:
```
curl http://127.0.0.1:8080 
```

Sending the above request multiple times, you will not the request gets routed to one of the servers mentioned in the server port list at the time of start.

For checking server health, load balancer sends a command similar to:
```
curl http://127.0.0.1:2000/health
```

You can experiment the load balancer working by killing a server of choice and bringing it back up.

Note that if a server goes down between two health checks, load balancer will request you to try again and will not send any further requests to that dead server until it succeeds an upcoming health check.