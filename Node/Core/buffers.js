var buf = new Buffer.alloc(26)

console.log(buf)

for (i=0; i<buf.length; i++)
{
    buf[i] = i + 97;
}

console.log(buf.toString('ascii'))