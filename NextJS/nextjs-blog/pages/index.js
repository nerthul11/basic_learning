import Head from 'next/head'
import Layout, { site } from '../components/layout'
import utilStyles from '../styles/utils.module.css'

export default function Home() {
  return (
    <Layout home>
      <Head>
        <title>{site}</title>
      </Head>
      <section className={utilStyles.headingMd}>
        <p>Junior Web developer, creating my first NextJS website! You can also check my <a href="https://github.com/nerthul11">GitHub</a> profile</p>
      </section>
    </Layout>
  )
}