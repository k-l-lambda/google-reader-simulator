
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import users


class TestHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        path = os.path.join(os.path.dirname(__file__), 'templates/View.html')
        self.response.out.write(template.render(path, {
            'user':                 user,
            'logout_url':           users.create_logout_url(self.request.uri),
        }))


def main():
    application = webapp.WSGIApplication([
        ('/view/',                          TestHandler),
        ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
