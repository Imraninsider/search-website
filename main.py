import os
import  webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "template")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = "true")

class Handler(webapp2.RequestHandler):
		def write(self, *a, **kw):
			self.response.out.write(*a,**kw)
		def render_str(self,template, **params):
			t = jinja_env.get_template(template)
			return t.render(params)
		def render(self, template, **kw):
			self.write(self.render_str(template,**kw))

class MainPage(Handler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text'
        #self.response.write("html")
		self.render("front.html")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
