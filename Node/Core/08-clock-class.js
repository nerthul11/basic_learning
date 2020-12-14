class Clock
{
    constructor()
    {
        setInterval(() => this.theTime(), 1000)
    }

    theTime() {
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

        const msg = `${hrs}:${min}:${sec}${ampm}`
        console.log(msg)
    }
}

module.exports = Clock