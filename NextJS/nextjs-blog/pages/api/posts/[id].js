import { getAllPostIds, getPostData } from '../../../lib/posts'

export async function getStaticPaths() {
  const paths = getAllPostIds()
  return {
    paths,
    fallback: false
  }
}

export default async function handler(req, res) {
	const {query: { id }} = req
	const post = await getPostData(id)
	post.id ? res.json({'post': {'id': post.id, 'title': post.title, 'author': post.author, 'date': post.date}}) : res.json({'error-404': 'Page not found'})
}