# Tron
### Install requirnments
```
sudo apt-get install python3-tk
pip3 install --user http://bit.ly/csc161graphics
```

### Protocol
UDP, connecting and game starting messages acked but all other messages will just be sent out 5 times and dropped if non reach the destination.
All 1 byte unless stated otherwise.

* Connecting: client connects to the server [ 0 ]
* Connected: server sends client it's client number [ 1 | client number ]
* State: containes last n position up to 6 [ 2 | num positions | client number 1 | x1 (2 bytes) | y1 (2 bytes) | ... | client number n | .. x6 (2 bytes) | y6 (2 bytes)]
* Direction: [ 3 | 0 = left, 1 = up, 2 = right, 3 = down]
* Dead: [ 4 | client number]
* Winner: [ 5 | cilent number]
* Game Starting: [ 6 | { same data as game states } ]
* Ack Game Starting: [ 7 ]