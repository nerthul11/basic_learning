var stdin = process.stdin,
    stdout = process.stdout,
    person = {'name': null, 'age': 0}

function saveAge(age) {
    person.age = age
    var underage = true
    if (age >= 18) {underage = false}
    stdout.write(`Hello ${person.name}, your age is ${person.age}, so the fact that you are underage is ${underage}`)
    process.exit()
}

function saveName(name) {
    person.name = name
    quiz(`Hello ${name}, input your age: `, saveAge)
}

function quiz(question, callback) {
    stdin.resume()
    stdout.write(question)
    stdin.once('data', (res) => {
        callback(res.toString().trim())
    })
}

stdin.setEncoding('utf8')
quiz('Input name: ', saveName)