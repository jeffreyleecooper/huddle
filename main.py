#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import db
from AsanaFeed import ClientTaskFeeder


JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))

approved_user_list=['jeffreyleecooper@gmail.com',
                    'jeff.cooper@threeshipsmedia.com',
                    'test@example.com',
                    'tedbaxa@gmail.com'
                    ]

class MainHandler(webapp2.RequestHandler):
   def get(self):
        if users.get_current_user():
            url = '/huddle'
            url_linktext='Huddle'
#            url2=users.create_logout_url(self.request.uri)
            url2=None
            current_user=users.get_current_user().email()
        else:
            url = users.create_login_url('/huddle')
            url2 = None
            url_linktext = 'Login'
            current_user = None

        template_values = {
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user,
            'url2':url2
        }
        template = JINJA_ENVIRONMENT.get_template('base.html')
        self.response.write(template.render(template_values))

class HuddleHandler(webapp2.RequestHandler):
   def get(self):
        if users.get_current_user().email().lower() not in approved_user_list:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = None
            template_values = {
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
            template = JINJA_ENVIRONMENT.get_template('denied.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_logout_url(self.request.uri)
            url_linktext='Logout'
            current_user=users.get_current_user().email()
            template_values = {
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
            template = JINJA_ENVIRONMENT.get_template('huddle.html')
            self.response.write(template.render(template_values))
class AsanaFeedClient(webapp2.RequestHandler):
   def get(self):
        if users.get_current_user().email().lower() not in approved_user_list:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = None
            template_values = {
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
            template = JINJA_ENVIRONMENT.get_template('denied.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_logout_url(self.request.uri)
            url_linktext='Logout'
            current_user=users.get_current_user().email()
            template_values = {
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
            json=ClientTaskFeeder()
            self.response.headers.add_header('content-type','application/json',charset='utf-8')
            self.response.out.write(json)
        
class AsanaFeedStaff(webapp2.RequestHandler):
   def get(self):
        if users.get_current_user().email().lower() not in approved_user_list:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = None
            template_values = {
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
            template = JINJA_ENVIRONMENT.get_template('denied.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_logout_url(self.request.uri)
            url_linktext='Logout'
            current_user=users.get_current_user().email()
            template_values = {
            'login_url':url,
            'login_text':url_linktext,
            'user':current_user
        }
            json=ShipmateTaskFeeder()
            self.response.headers.add_header('content-type','application/json',charset='utf-8')
            self.response.out.write(json)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/huddle', HuddleHandler),
    ('/asanafeed-client', AsanaFeedClient),
    ('/asanafeed-staff', AsanaFeedStaff)
], debug=True)
