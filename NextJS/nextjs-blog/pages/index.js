import Head from 'next/head'
import Link from 'next/link'
import Layout, { site } from '../components/layout'
import utilStyles from '../styles/utils.module.css'
import {getSortedPostsData} from '../lib/posts'
import Date from '../components/date'

export async function getStaticProps() {
	const allPostsData = getSortedPostsData()
	return {
		props: {
			allPostsData
		}
	}
}

export default function Home({allPostsData}) {
  return (
    <Layout home>
		<Head>
			<title>{site}</title>
		</Head>
		<section className={utilStyles.headingMd}>
			<p>Junior Web developer, creating my first NextJS website!</p>
			<p>You can also check my <a href="https://github.com/nerthul11">GitHub</a> profile</p>
        </section>
	    <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
		<h2 className={utilStyles.headingLg}>Blog</h2>
		<ul className={utilStyles.list}>
			{allPostsData.map(({id, date, title}) => (
			<li className={utilStyles.listItem} key={id}>
				<Link href={`/posts/${id}`}><a>{title}</a></Link>
				<br />
				<small>
					<Date dateString={date} />
				</small>
			</li>
			))}
		</ul>
		</section>
    </Layout>
  )
}