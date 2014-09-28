#!/usr/bin/env python
# conding: utf-8

pre_fix = 'controllers'

urls = (
        '/',                    pre_fix + '.todo.Index',
        '/todo/new',            pre_fix + '.todo.New',
        '/todo/(\d+)',          pre_fix + '.todo.View',
        '/todo/(\d+)/edit',     pre_fix + '.todo.New',
        '/todo/(\d+)/delete',   pre_fix + '.todo.Delete',
        '/todo/(\d+)/finish',   pre_fix + '.todo.Finish',
       )
