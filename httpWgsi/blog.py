from __future__ import unicode_literals

from flask import Flask
from flask import render_template, redirect, request
from kanado import kanado
import run_app
app = kanado.Kanado(__name__)


class Blog:
    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text


blogs = []
b1 = Blog(1, 'hello1', 'zhangsan')
b2 = Blog(2, 'hello2', 'lisi')
blogs.append(b1)
blogs.append(b2)


@app.route('/')
def home():
    ''' 主页'''
    # 渲染首页HTML模板文件
    return render_template('home.html')


@app.route('/blogs')
def list_notes():
    ''' 查询博文列表 '''
    # 渲染博文列表页面目标文件，传入blogs参数
    return render_template('list_blogs.html', blogs=blogs)

# @app.route('/blog/<id>',methods=['GET'])
@app.route('/blog/<id>')
def query_note(id):
    ''' 查询博文详情、删除博文 '''
    if request.method=='GET':
        blog = None  # 到数据库查询博文详情
        for b in blogs:
            if b.id == int(id):
                blog = b  # 渲染博文详情页面
        return render_template('query_blog.html', blog=blog)
if __name__ == '__main__':
    # 以debug模式启动程序
    run_app.run()
