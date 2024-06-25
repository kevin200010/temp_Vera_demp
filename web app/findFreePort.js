const net = require('net');

function findFreePort(startPort = 3000, callback) {
  const port = startPort;
  const server = net.createServer();

  server.listen(port, () => {
    server.once('close', () => {
      callback(null, port);
    });
    server.close();
  });

  server.on('error', () => {
    findFreePort(port + 1, callback);
  });
}

module.exports = findFreePort;
