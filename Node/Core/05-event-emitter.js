const EventEmitter = require('events').EventEmitter, pub = new EventEmitter

pub
    .on('myEvent', message => {console.log(message)})
    .once('myEvent', message => {console.log(`First message: ${message}`)})

pub.emit('myEvent', 'Hello world')
pub.emit('myEvent', 'Second message: Should not display the pub.once')
pub.removeAllListeners('myEvent') // Kills .on and .once