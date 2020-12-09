var fs = require('fs'),
    readStream = fs.createReadStream('Assets/names.txt'),
    writeStream = fs.createWriteStream('Assets/names_copy.txt');

readStream.pipe(writeStream)
readStream.on('data', (chunk) => {
    console.log(chunk.length + ' characters read')
})

readStream.on('end', () => {
    console.log('Finished reading file')
})