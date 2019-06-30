from flask import Blueprint, render_template, session, request, redirect, url_for
from App.models import *

blue = Blueprint('blog', __name__)


# 首页
@blue.route('/')
def index():
    cate=Catalog.query.all()
    data={
        "cate":cate
    }
    return render_template('home/index.html',data=data)

@blue.route('/index/<int:cid>/')
def index_cate(cid):
    article=Article.query.filter_by(catalogid=cid)
    cate = Catalog.query.all()
    # catalogs=Catalog.query.get(cid)
    data={
        'article':article,
        'cate':cate
    }

    return render_template('home/index.html',data=data)



# 后台
#首页
@blue.route('/admin/')
def admin_index():
    return render_template('admin/index.html')

#登录
@blue.route('/admin/login/',methods=['GET','POST'])
def admin_login():
    if request.method =="GET":
        if session.get('username'):
            return render_template('admin/index.html')
        else:
            return render_template('admin/login.html')





    else:
        usernames = request.form.get('username')
        passwords = request.form.get('userpwd')

        users=User.query.filter_by(
            username = usernames,
            password = passwords
        )
        if users.count() >0 :
            session['username']=usernames
            return redirect(url_for('blog.admin_index'))

        return '登陆错误'



#文章首页
@blue.route('/admin/article/',methods=['POST','GET'])
def admin_article():
    article_list=Article.query.all()
    return render_template('admin/article.html',article_list=article_list)

#增加文章
@blue.route('/admin/addarticle/',methods=['POST','GET'])
def add_article():
    if request.method =='POST':
        title = request.form.get('title')
        detail = request.form.get('content')

        art=Article()
        art.title = title
        art.detail = detail

        try:
            db.session.add(art)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
            return '错误'
        return redirect(url_for('blog.admin_article'))
    article_list = Article.query.all()
    return render_template('admin/add-article.html')

#修改首页
@blue.route('/admin/updateart/<int:id>')
def update_art(id):
    a = Article.query.get(id)
    return render_template('admin/update-article.html',a=a)
#修改文章
@blue.route('/admin/updatearticle/',methods=['GET','POST'])
def update_article():
    if request.method=='POST':
        title=request.form.get('title')
        detail = request.form.get('content')

        id = request.form.get('visibility')

        arts=Article.query.get(id)
        arts.title=title
        arts.detail=detail

        db.session.commit()
        return redirect(url_for('blog.admin_article'))

    return render_template('admin/article.html')



#删除文章
@blue.route('/admin/delarticle/<int:arid>',methods=['GET','POST'])
def del_article(arid):
    if request.method =='GET':
        srtid=Article.query.filter_by(id=arid).first()

        db.session.delete(srtid)
        db.session.commit()
        # return redirect(url_for('blog'))
    article_list = Article.query.all()
    return render_template('admin/article.html',article_list=article_list)


#获取栏目数据库
@blue.route('/admin/category')
def admin_category():
    cate = Catalog.query.all()
    return render_template('admin/category.html',cate=cate)


# @blue.route('/admin/addcategory')
# def get_category():
#     cate = Catalog.query.all()
#     # print(cate)
#     return render_template('admin/category.html',cate=cate)
#添加栏目
@blue.route('/admin/addcategory',methods=['POST','GET'])
def add_category():
    cate = Catalog.query.all()
    if request.method=='POST':
        category = request.form.get('name')
        catname = request.form.get('alias')
        keypassword = request.form.get('keywords')
        said = request.form.get('describe')

        cat = Catalog()
        cat.category = category
        cat.catename = catname
        cat.keypassword = keypassword
        cat.said = said

        try:
            db.session.add(cat)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
            return '错误'
        return redirect(url_for('blog.add_category'))
    cate = Catalog.query.all()
    return render_template('admin/category.html',cate=cate)

#修改栏目主页
@blue.route('/modifycategory/<int:cid>/')
def update_category(cid):
    cid=Catalog.query.get(cid)
    print(cid.id)
    return render_template('admin/update-category.html',cid=cid)

# #修改栏目
@blue.route('/updatecategory/',methods=['GET','POST'])
def uppdate_category():
    cate = Catalog.query.all()
    if request.method == 'POST':
        category = request.form.get('name')
        catname = request.form.get('alias')
        keypassword = request.form.get('keywords')
        said = request.form.get('describe')
        id =request.form.get('fid')

        cate=Catalog.query.filter_by(id=id).first()
        cate.category = category
        cate.catename = catname
        cate.keypassword = keypassword
        cate.said = said

        db.session.commit()

        cate = Catalog.query.all()
    return render_template('admin/category.html',cate=cate)

#删除栏目
@blue.route('/deletecatalog/<int:did>',methods = ['GET','POST'])
def delete_catalog(did):
    cata = Catalog.query.all()
    did = Catalog.query.filter_by(id=did).first()
    if request.method == 'GET':
        db.session.delete(did)
        db.session.commit()
        return redirect(url_for('blog.admin_category'))
    return render_template('admin/update-category.html',cata=cata)


