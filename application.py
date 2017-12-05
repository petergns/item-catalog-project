from flask import (Flask,
                   render_template,
                   url_for,
                   request,
                   redirect,
                   jsonify,
                   make_response,
                   flash)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatChar, User
from flask import session as login_session
import random
import string
import json
import httplib2
import requests
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())[
    'web']['client_id']

# Connect to Database
engine = create_engine('sqlite:///charcatalog.db')
Base.metadata.bind = engine

# Create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# User Helper Functions


def createUser(login_session):
    newUser = User(
        name=login_session['username'],
        email=login_session['email'],
        picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except BaseException:
        return None


@app.route('/')
@app.route('/catalog')
def showCategories():
    # Get all categories
    categories = session.query(Category).all()
    # Get latest category characters added
    catChars = session.query(CatChar).all()
    # Check if user is logged in
    if 'username' not in login_session:
        return render_template('publicCategories.html',
                               categories=categories,
                               catChars=catChars)
    else:
        return render_template(
            'categories.html',
            categories=categories,
            catChars=catChars)


@app.route('/catalog/<int:catalog_id>')
@app.route('/catalog/<int:catalog_id>/chars')
def showCategory(catalog_id):
    # Get all categories
    categories = session.query(Category).all()
    # Get category
    category = session.query(Category).filter_by(id=catalog_id).first()
    # Get name of category
    categoryName = category.name
    # Get all characters of a specific category
    catChars = session.query(CatChar).filter_by(category_id=catalog_id).all()
    # Get count of category characters
    catCharsCount = session.query(CatChar).filter_by(
        category_id=catalog_id).count()
    # Check if user is logged in
    if 'username' not in login_session:
        return render_template('publicCategory.html',
                               categories=categories,
                               catChars=catChars,
                               categoryName=categoryName,
                               catCharsCount=catCharsCount)
    else:
        return render_template(
            'category.html',
            categories=categories,
            catChars=catChars,
            categoryName=categoryName,
            catCharsCount=catCharsCount)


@app.route('/catalog/<int:catalog_id>/chars/<int:char_id>')
def showCatChar(catalog_id, char_id):
    # Get category character
    catChar = session.query(CatChar).filter_by(id=char_id).first()
    # Get creator of character
    creator = getUserInfo(catChar.user_id)
    # Check if user is logged in
    if 'username' not in login_session:
        return render_template('publicCategoryChar.html',
                               catChar=catChar,
                               creator=creator)
    else:
        return render_template('catChar.html',
                               catChar=catChar,
                               creator=creator)


@app.route('/catalog/add', methods=['GET', 'POST'])
def addCatChar():
    # Check if user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        # TODO: Retain data when there is an error
        if not request.form['name']:
            flash('Please add character/s name')
            return redirect(url_for('addCatChar'))

        if not request.form['description']:
            flash('Please add a description')
            return redirect(url_for('addCatChar'))
        # Add category char
        newCatChar = CatChar(
            name=request.form['name'],
            description=request.form['description'],
            category_id=request.form['category'],
            user_id=login_session['user_id'])
        session.add(newCatChar)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        # Get all categories
        categories = session.query(Category).all()
        return render_template('addCatChar.html', categories=categories)


@app.route(
    '/catalog/<int:catalog_id>/chars/<int:char_id>/edit',
    methods=[
        'GET',
        'POST'])
def editCatChar(catalog_id, char_id):
    # Check if user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # Get category character
    catChar = session.query(CatChar).filter_by(id=char_id).first()
    # Get creator of character
    creator = getUserInfo(catChar.user_id)
    # Session query for edited character content
    editedChar = session.query(CatChar).filter_by(id=char_id).first()
    # Check if logged in user is creator of category character
    if creator.id != login_session['user_id']:
        return redirect(url_for('showCategories'))
    # Get all categories Edit This Udacity
    categories = session.query(Category).all()
    if request.method == 'POST':
        if request.form['name']:
            editedChar.name = request.form['name']
        if request.form['description']:
            editedChar.description = request.form['description']
        if request.form['category']:
            editedChar.category_id = request.form['category']
        session.add(editedChar)
        session.commit()
        return redirect(
            url_for(
                'showCatChar',
                catalog_id=catChar.category_id,
                char_id=catChar.id))
    else:
        return render_template(
            'editCatChar.html',
            categories=categories,
            catChar=catChar, char=editedChar)


@app.route(
    '/catalog/<int:catalog_id>/chars/<int:char_id>/delete',
    methods=[
        'GET',
        'POST'])
def deleteCatChar(catalog_id, char_id):
    # Check if user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # Get category character
    catChar = session.query(CatChar).filter_by(id=char_id).first()
    # Get creator of character
    creator = getUserInfo(catChar.user_id)
    # Check if logged in user is creator of category character
    if creator.id != login_session['user_id']:
        return redirect(url_for('showCategories'))

    if request.method == 'POST':
        session.delete(catChar)
        session.commit()
        return redirect(
            url_for(
                'showCategory',
                catalog_id=catChar.category_id))
    else:
        return render_template('deleteCatChar.html', catChar=catChar)


@app.route('/login')
def login():
    # Create anti-forgery state token
    state = ''.join(
        random.choice(
            string.ascii_uppercase +
            string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/logout')
def logout():
    if login_session['provider'] == 'facebook':
        fbdisconnect()
        del login_session['facebook_id']

    if login_session['provider'] == 'google':
        gdisconnect()
        del login_session['gplus_id']
        del login_session['access_token']

    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['user_id']
    del login_session['provider']

    return redirect(url_for('showCategories'))

# 1 Create anti-forgery state token


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


# Connect to Facebook
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token
    # 3 Gets info from fb clients secrets
    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?' \
          'grant_type=fb_exchange_token&client_id=%s&' \
          'client_secret=%s&fb_exchange_token=%s' % (
              app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # 4 Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.8/me?' \
          'access_token=%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token
    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?' \
          'access_token=%s&redirect=0&' \
          'height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]
    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 200px; height: 200px;border-radius:' \
        ' 150px;-webkit-border-radius: 150px;' \
        ' -moz-border-radius: 150px;"> '
    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (
        facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"
    # End Facebook


@app.route('/gconnect', methods=['POST'])
def gconnect():
        # Validate anti-forgery state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check that the access token is valid.
    access_token = credentials.access_token
    url = (
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' %
        access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id
    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'
    # See if user exists
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    return "Login Successful"


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')

    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/catalog/JSON')
def showCategoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[category.serialize for category in categories])


@app.route('/catalog/<int:catalog_id>/JSON')
@app.route('/catalog/<int:catalog_id>/chars/JSON')
def showCategoryJSON(catalog_id):
    catChars = session.query(CatChar).filter_by(category_id=catalog_id).all()
    return jsonify(CatChars=[catChar.serialize for catChar in catChars])


@app.route('/catalog/<int:catalog_id>/chars/<int:char_id>/JSON')
def showCatCharJSON(catalog_id, char_id):
    catChar = session.query(CatChar).filter_by(id=char_id).first()
    return jsonify(atChar=[catChar.serialize])


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000)
