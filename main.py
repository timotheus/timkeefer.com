import webapp2

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+'/templates/style1')
)

TEMPLATE_DIR = 'templates/style1'

class Home(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/html'

      tvars = {}

      template = jinja_environment.get_template('home.html')
      self.response.out.write(template.render(tvars))

class Changes(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        tvars = {}
        template = jinja_environment.get_template('changes.html')
        self.response.out.write(template.render(tvars))

class Builds(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        tvars = {}
        template = jinja_environment.get_template('builds.html')
        self.response.out.write(template.render(tvars))

class OpenSource(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        tvars = {}
        template = jinja_environment.get_template('opensource.html')
        self.response.out.write(template.render(tvars))

class Shapes(webapp2.RequestHandler):
    def get(self, name):
        self.response.headers['Content-Type'] = 'text/html'
        tvars = {}
        if name == '':
            name = 'shapes'

        template = jinja_environment.get_template('%s.html' % name.replace('/', ''))
        self.response.out.write(template.render(tvars))
              
app = webapp2.WSGIApplication(
    [
        ('/', Home),
        ('/changes/?', Changes),
        ('/shapes/?(.*)/?', Shapes),
        ('/open-source/?', OpenSource),
        ('/builds/?', Builds),
    ],
    debug=True
)
