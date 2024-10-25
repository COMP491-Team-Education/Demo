import web
import json
import plugin_online

urls = (
    '/', 'Index',
    '/search', 'Search'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.search()

class Search:
    def GET(self):
        user_data = web.input()
        query = user_data.query

        results = plugin_online.get_books_info(query)

        return render.search(results=results)

if __name__ == "__main__":
    app.run()
