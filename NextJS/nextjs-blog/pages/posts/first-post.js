import Link from 'next/link'

export default function FirstPost() {
	return (
	<>
	<h1>Hello world!</h1>
	<h2>
	    <Link href="/">
	        <a>Back to the homepage</a>
	    </Link>
    </h2>
    </>
    )
}