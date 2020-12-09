const EventEmitter = require('events').EventEmitter,
inherits = require('util').inherits,
clock = () => {
    // Constructor
    const Clock = function() {setInterval(() => this.emit('tick'), 1000)}
    inherits(Clock, EventEmitter)

    Clock.prototype.theTime = () => {
        function pad(num, size) {
            num = num.toString()
            while (num.length < size) num = "0" + num
            return num
        }
        var date = new Date(),
        hrs = pad(date.getHours(), 2),
        min = pad(date.getMinutes(), 2),
        sec = pad(date.getSeconds(), 2),
        ampm = hrs >= 12 ? 'PM' : 'AM'

        hrs = hrs > 12 ? pad(hrs - 12, 2) : hrs

        msg = `${hrs}:${min}:${sec}${ampm}`
        console.log(msg)
    }
    var timer = new Clock()

    timer.on('tick', () => {timer.theTime()})
}

module.exports.clock = clock // Exporta como clock