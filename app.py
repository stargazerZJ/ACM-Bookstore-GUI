from flask import (Blueprint, Flask, abort, make_response, redirect,
                   render_template, request, send_from_directory)
import bookstore
import csv
import os

web = Flask(__name__)

db_path = "db/"
store = bookstore.BookStore(db_path)
store.initialize(force_reset=True)

class Log:
    """! CSV log file"""
    class LogFile:
        def __init__(self, path):
            self.path = path
            self.row_len = 0

        def write_head(self, head):
            self.row_len = len(head)
            if os.path.exists(self.path):
                return
            with open(self.path, "w") as f:
                writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                writer.writerow(head)
        def write(self, *args):
            if len(args) != self.row_len:
                raise ValueError("Invalid number of arguments")
            with open(self.path, "a") as f:
                writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                writer.writerow(args)
        def read(self):
            with open(self.path, "r") as f:
                reader = csv.reader(f, quoting=csv.QUOTE_MINIMAL)
                return list(reader)
    def __init__(self, path):
        self.user_log_path = path + "user.log"
        self.finance_log_path = path + "finance.log"
        self.user_log = self.LogFile(self.user_log_path)
        self.user_log.write_head(["who", "did_what", "to_whom"]) # did_what: register, change_password, delete
        self.finance_log = self.LogFile(self.finance_log_path)
        self.finance_log.write_head(["who", "did_what", "ISBN", "quantity", "cost"]) # did_what: purchase, import

    def add_user_log(self, who, did_what, to_whom):
        self.user_log.write(who, did_what, to_whom)

    def add_finance_log(self, who, did_what, ISBN, quantity, cost):
        self.finance_log.write(who, did_what, ISBN, quantity, cost)

    def get_user_log(self):
        return self.user_log.read()

    def get_finance_log(self):
        return self.finance_log.read()

log = Log(db_path)

def test():
    store.login("root", "sjtu")
    # book1 = bookstore.Book("978-7-302-32998-2", "C++_Primer", "Stanley_B._Lippman", "C++", 9999)
    # book2 = bookstore.Book("978-7-115-38899-6", "C++_Primer_Plus", "Stephen_Prata", "C++", 9999)
    book1 = bookstore.Book("1", "a", "a", "a", 9999)
    book2 = bookstore.Book("2", "b", "a", "a|b", 9999)
    store.select("0")
    store.modify(book1)
    store.import_(100, 100)
    store.select("0")
    store.modify(book2)
    store.useradd("user1", "password", "customer_1", 1)
    store.useradd("user2", "password", "employee_1", 3)
    store.logout()
    # store.login("username", "password")
    store.login("root", "sjtu")

test()

def returnCode(code):
    return {"e": -code, "msg": bookstore.exceptionTypeToString(code)}


@web.route('/')
def index():
    return render_template(
        'index.html',
        user_id=store.getUserId(),
        friendlyName=store.getUserName(),
        is_Admin=store.getPrivilege() >= 3,
    )


@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        nxt = request.args.get('next')
        return render_template('register.html', Next=nxt,user_id=store.getUserId(), friendlyName=store.getUserName(),
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
    if code == bookstore.kExceptionType_K_SUCCESS:
        log.add_user_log(store.getUserId(), "register", username)
    return returnCode(code)


@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        nxt = request.args.get('next')
        nxt = '/' if nxt is None else nxt
        return render_template('login.html', Next=nxt,user_id=store.getUserId(), friendlyName=store.getUserName(),
                               is_Admin=store.getPrivilege() >= 3)
    username = request.form.get('username')
    password = request.form.get('password')
    code = store.login(username, password)
    return returnCode(code)


@web.route('/logout')
def logout():
    store.logout()
    return redirect('/')


@web.route('/profile/<user_id>', methods=['GET', 'POST'])
def profile(user_id):
    if store.getUserId() and store.getUserId() != user_id and store.getPrivilege() < 3:
        abort(404)
    if request.method == 'GET':
        if not store.getUserId():
            return redirect('/login?next=' + request.full_path)
        return render_template('profile.html',user_id=store.getUserId(), friendlyName=store.getUserName(),
                               is_Admin=store.getPrivilege() >= 3)
    else:
        form = request.json
        try:
            code = store.passwd(user_id, form.get('password'), form.get('old_password'))
            if code == bookstore.kExceptionType_K_SUCCESS:
                log.add_user_log(store.getUserId(), "change_password", user_id)
            return returnCode(code)
        except KeyError:
            return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
        except TypeError:
            return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)

@web.route('/profile/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if not store.getUserId() or store.getPrivilege() < 3:
        abort(404)
    code = store.deluser(user_id)
    if code == bookstore.kExceptionType_K_SUCCESS:
        log.add_user_log(store.getUserId(), "delete", user_id)
    return returnCode(code)

@web.route('/admin')
def admin():
    if not store.getUserId() or store.getPrivilege() < 3:
        abort(404)
    return render_template('admin.html',user_id=store.getUserId(), friendlyName=store.getUserName(),
                           is_Admin=store.getPrivilege() >= 3, privilege=store.getPrivilege())


@web.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if not store.getUserId() or store.getPrivilege() < 3:
        abort(404)
    if request.method == 'GET':
        nxt = request.args.get('next') or '/add-book'
        return render_template('add-book.html', Next=nxt,user_id=store.getUserId(), friendlyName=store.getUserName(),
                               is_Admin=store.getPrivilege() >= 3)
    isbn = request.form.get('ISBN')
    param = bookstore.Book(isbn)
    result = store.search(param)
    code, book = result.first, result.second
    if code != bookstore.kExceptionType_K_SUCCESS:
        return returnCode(code)
    if len(book) > 0:
        return returnCode(bookstore.kExceptionType_K_DUPLICATED_ISBN)
    return add_modify_book(isbn)

@web.route('/search')
def search():
    if not store.getUserId():
        return redirect('/login?next=' + request.full_path)
    typ = request.args.get('type')
    if typ:
        param = bookstore.Book()
        if typ == "All":
            pass
        elif typ == "ISBN":
            param.ISBN = request.args.get('parameter')
        elif typ == "Title":
            param.title = request.args.get('parameter')
        elif typ == "Author":
            param.author = request.args.get('parameter')
        elif typ == "Keyword":
            param.keywords = request.args.get('parameter')
        else:
            abort(403)
        result = store.search(param)
        code, books = result.first, result.second
    else:
        code, books = bookstore.kExceptionType_K_SUCCESS, []
    code = returnCode(code)
    return render_template('search.html',user_id=store.getUserId(), friendlyName=store.getUserName(),
                           is_Admin=store.getPrivilege() >= 3,
                           code=code, books=books,
                           args=dict(request.args.items()))


@web.route('/book/<ISBN>')
def manage_book(ISBN):
    if not store.getUserId():
        abort(404)
    param = bookstore.Book(ISBN)
    result = store.search(param)
    code, book = result.first, result.second
    if code != bookstore.kExceptionType_K_SUCCESS or len(book) == 0:
        abort(404)
    book = book[0]
    return render_template('book.html',user_id=store.getUserId(), friendlyName=store.getUserName(),
                           is_Admin=store.getPrivilege() >= 3,
                           book=book)

@web.route('/book/<ISBN>/modify', methods=['POST'])
def modify_book(ISBN):
    if not store.getUserId() or store.getPrivilege() < 3:
        abort(404)
    param = bookstore.Book(ISBN)
    result = store.search(param)
    code, book = result.first, result.second
    if code != bookstore.kExceptionType_K_SUCCESS or len(book) == 0:
        abort(404)
    return add_modify_book(ISBN)

@web.route('/book/<ISBN>/import', methods=['POST'])
def import_book(ISBN):
    if not store.getUserId() or store.getPrivilege() < 3:
        abort(404)
    param = bookstore.Book(ISBN)
    result = store.search(param)
    code, book = result.first, result.second
    if code != bookstore.kExceptionType_K_SUCCESS or len(book) == 0:
        abort(404)
    form = request.form
    try:
        store.select(ISBN)
        cost = form.get('cost')
        cost = int(float(cost) * 100)
        code = store.import_(int(form.get('quantity')), cost)
        if code == bookstore.kExceptionType_K_SUCCESS:
            log.add_finance_log(store.getUserId(), "import", ISBN, int(form.get('quantity')), -cost / 100)
        return returnCode(code)
    except KeyError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except TypeError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except ValueError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)

def add_modify_book(old_isbn):
    form = request.form
    try:
        code = store.select(old_isbn)
        if code != bookstore.kExceptionType_K_SUCCESS:
            return returnCode(code)
        price = form.get('price')
        price = int(float(price) * 100)
        new_isbn = form.get('ISBN')
        book = bookstore.Book(new_isbn, form.get('title'), form.get('author'), form.get('keywords'), price)
        if old_isbn == new_isbn:
            book.ISBN = ""
        code = store.modify(book)
        return returnCode(code)
    except KeyError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except TypeError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except ValueError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)

@web.route('/book/<ISBN>/buy', methods=['POST'])
def buy_book(ISBN):
    if not store.getUserId():
        return redirect('/login?next=' + request.full_path)
    param = bookstore.Book(ISBN)
    result = store.search(param)
    code, book = result.first, result.second
    if code != bookstore.kExceptionType_K_SUCCESS or len(book) == 0:
        abort(404)
    form = request.form
    try:
        result = store.purchase(ISBN, int(form.get('quantity')))
        code, cost = result.first, result.second
        if code == bookstore.kExceptionType_K_SUCCESS:
            log.add_finance_log(store.getUserId(), "purchase", ISBN, int(form.get('quantity')), cost / 100)
        code = returnCode(code)
        code["cost"] = float(cost) / 100
        return code
    except KeyError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except TypeError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)
    except ValueError:
        return returnCode(bookstore.kExceptionType_K_INVALID_PARAMETER)

@web.route('/log')
def show_log():
    if not store.getUserId() or store.getPrivilege() < 7:
        abort(404)
    user_log = log.get_user_log()
    user_log = user_log[1:]
    finance_log = log.get_finance_log()
    finance_log = finance_log[1:]
    return render_template('log.html',user_id=store.getUserId(), friendlyName=store.getUserName(),
                           is_Admin=store.getPrivilege() >= 3,
                           user_log=user_log,
                           finance_log=finance_log,
                           )



if __name__ == '__main__':
    web.run()
