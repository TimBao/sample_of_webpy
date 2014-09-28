#!/usr/bin/env python
# conding: utf-8

import web

db = web.database(dbn='sqlite', db='static/sql/todo.db')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email     = 'ddd@gmail.com',
    site_name = 'Todo',
    site_desc = '',
    static    = '/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
