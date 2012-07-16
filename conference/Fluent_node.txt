/*

Node.js talk tom@jetpacksfordinosaurs.com 

- email him for slides & ebay contact
- http://ofps.oreilly.com/titles/9781449398583/
- example arch

user <-> node (front-end) <-> db
                          <-> node (logging) <-> disk

- move non user-facing work outside of the main loop
- cluster (multi cpu use) is a must use eg. require('cluster');
- unbundle SSL (stud) could speed up
- apache traffic server (not sure what this is? some type of proxy/lb)
- npm (eg. npm install express) - node package management
- node-inspector debugger - run along side of the node process
- upstart or forever - a wrapper command that will run the node process

** sublime editor 
http://www.sublimetext.com/blog/articles/sublime-text-2-beta


*/
// Helloworld

var http = require('http');

http.createServer(function (request, response) {
    response.writeHead(200, {'Content-Type': 'text/html'});

    if (request.headers['user-agent']) {
        response.write('I\'m Learning Node\n' 
            + request.headers['user-agent']);
    }
    response.end('');
    
}).listen(8000);

console.log('Server running at http://127.0.0.1:8000/');

// Simple app

var express = require('express');
var app = express.createServer();
app.use(express.cookieParser());

app.get('/', function(req, res) {
    var page = '';
    if (req.query.page) {
        page = req.query.page;
    }
    res.send('root ' + page);
});

app.get('/products/:page', function(req, res) {
    res.send('products ' + req.params.page);
});

app.get('/old/?', function(req, res) {
    res.redirect('/new/');
});

app.get('/new/?', function(req, res) {
    res.cookie('rememberme', 'yes');
    res.send('new');
});

app.listen(3000);

// Simple chat server

var net = require('net');

var server = net.createServer();

server.listen(8001);

var connections = [];

server.on('connection', function(socket) {
    socket.write('Hello');
    console.log('new connection');
    
    connections.push(socket);
    
    socket.on('data', function(data) {
        for (var i=0; i<connections.length;i++) {
            // if( connections[i].writable) {
            connections[i].write(data);
            //}
        }
    });
    
    socket.on('close', function() {
        connections.splice(connections.indexOf(socket),1));
    });
});

