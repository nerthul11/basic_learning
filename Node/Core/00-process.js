function singleThread() {
	console.log('Node.JS Process')
	console.log('ID: ' + process.pid)
	console.log('Title: ' + process.title)
	console.log('Node directory: ' + process.execPath)
	console.log('Current directory: ' + process.cwd())
	console.log('Node version: ' + process.version)
	console.log('Dependencies versions: ' + process.versions)
	console.log('OS Platform: ' + process.platform)
	console.log('OS Arch: ' + process.arch)
	console.log('Active time: ' + process.uptime())
	console.log('Process arguments: ' + process.argv)
	}

singleThread()