from flask import Flask
from flask import render_template,redirect,request,url_for
import datetime
import jsondtb
'''importing required modules'''


date=datetime.date.today()
time=datetime.datetime.today()
'''seting time to use in the html'''

app = Flask(__name__)
db = jsondtb.json_database(['title','content','date_posted','img_link','author'],'post_.json',id = True)


@app.route('/')
def home():
    return redirect(url_for('post'))

@app.route('/json' ,methods=['GET'])
def post():

    posts = db.view_data()[:10]

    return render_template('index.html',posts = posts, offset = 10)
"""returning the page with all the required data"""


@app.route('/get_posts' ,methods=['GET'])
def get_posts():
    offset = int(request.args.get('offset'))
    posts = db.view_data()[ offset: offset + 10]

    return render_template('partial/post.html', posts = posts, offset = offset + 10)
"""returning the page with all the required data"""


@app.route('/json/edit/<string:id>' ,methods=['GET','POST'])
def edit(id):
    if request.method == 'GET':

        data = db.get_row_elements('id',id)
        title = data["title"]
        content = data["content"]
        author = data.get("author")
        author = author if author else ''
        print(data)        
        
        return render_template('edit.html',title=title,
        content=content, author = author, id=id)
    
    else:
        
        new_title = request.form['title']
        new_content = request.form['content']

        print(id,new_content,new_title)
        
        db.update_row_element('id',id,'title',new_title)
        db.update_row_element('id',id,'content',new_content)

        return redirect('/json')

    
""" route to delete post"""
@app.route('/json/delete/<string:id>')
def delete(id):

    db.delete_row('id',id)

    return redirect('/json')
    # '''simply redirecting back to the main page'''

@app.route('/post/new', methods=["POST","GET"])
def new_post():
    if request.method == 'POST':
        title=request.form["title"]
        content=request.form["content"]
        author = request.form['author']
        date_posted = datetime.date.today().strftime(' %d %B, %y')
        db.add_row([title, content, date_posted,'img/LMLD.jpg', author])

        return redirect("/json")
    else:
        return render_template('new_post.html')


if __name__ == '__main__':
    app.run(debug=True)   
