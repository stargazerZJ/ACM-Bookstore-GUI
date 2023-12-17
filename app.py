from flask import (Blueprint, Flask, abort, make_response, redirect,
                   render_template, request, send_from_directory)
import bookstore

web = Flask(__name__)

store = bookstore.BookStore("db/")
store.initialize(force_reset=True)
store.login("root", "sjtu") # for test

def returnCode(code):
    return {"e": code, "msg": bookstore.exceptionTypeToString(code)}

@web.route('/')
def index():
    # ret = store.login("root", "sjtu")
    # return bookstore.exceptionTypeToString(ret)
    return render_template(
        'index.html',
        friendlyName = store.getUserName(),
        is_Admin = store.getPrivilege() >= 3,
    )

@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        nxt = request.args.get('next')
        return render_template('register.html', Next=nxt, friendlyName= store.getUserName(),
                               is_Admin=store.getPrivilege() >= 3)
    username = request.form.get('username')
    password = request.form.get('password')
    friendly_name = request.form.get('friendly_name')
    privilege = request.form.get('privilege') or 1
    try:
        privilege = int(privilege)
    except:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    if privilege == 1:
        code = store.customerUseradd(username, password, friendly_name)
    else:
        code = store.useradd(username, password, friendly_name, privilege)
    return returnCode(code)

@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        nxt = request.args.get('next')
        nxt = '/' if nxt is None else nxt
        return render_template('login.html', Next=nxt, friendlyName= store.getUserName(),
                               is_Admin=store.getPrivilege() >= 3)
    username = request.form.get('username')
    password = request.form.get('password')
    code = store.login(username, password)
    return returnCode(code)

@web.route('/logout')
def logout():
    store.logout()
    return redirect('/')

@web.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        if not store.getUserId():
            return redirect('/OnlineJudge/login?next=' + request.full_path)
        return render_template('profile.html', friendlyName= store.getUserName(),
                               is_Admin=store.getPrivilege() >= 3)
    else:
        user_id = store.getUserId()
        if not user_id:
            return returnCode(bookstore.kExceptionType_K_NO_LOGIN_USER)
        form = request.json
        try:
            code = store.passwd(user_id, form.get('password'), form.get('old_password'))
            return returnCode(code)

        except KeyError:
            return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
        except TypeError:
            return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)

@web.route('/admin')
def admin():
    if not store.getUserId() or store.getPrivilege() < 3:
        abort(404)
    return render_template('admin.html', friendlyName= store.getUserName(),
                           is_Admin=store.getPrivilege() >= 3, privilege=store.getPrivilege())

@web.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if not store.getUserId() or store.getPrivilege() < 3:
        abort(404)
    if request.method == 'GET':
        nxt = request.args.get('next') or '/add-book'
        return render_template('add-book.html', Next=nxt, friendlyName= store.getUserName(),
                               is_Admin=store.getPrivilege() >= 3)
    form = request.json
    try:
        code = store.select(form.get('ISBN'))
        if code != bookstore.kExceptionType_K_SUCCESS:
            return returnCode(code)
        price = form.get('price')
        price = int(float(price) * 100)
        book = bookstore.Book("", form.get('title'), form.get('author'), form.get('keywords'), price)
        code = store.modify(book)
        return returnCode(code)
    except KeyError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except TypeError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except ValueError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)

if __name__ == '__main__':
    web.run()
