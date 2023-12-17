# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _bookstore
else:
    import _bookstore

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _bookstore.delete_SwigPyIterator

    def value(self):
        return _bookstore.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _bookstore.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _bookstore.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _bookstore.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _bookstore.SwigPyIterator_equal(self, x)

    def copy(self):
        return _bookstore.SwigPyIterator_copy(self)

    def next(self):
        return _bookstore.SwigPyIterator_next(self)

    def __next__(self):
        return _bookstore.SwigPyIterator___next__(self)

    def previous(self):
        return _bookstore.SwigPyIterator_previous(self)

    def advance(self, n):
        return _bookstore.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _bookstore.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _bookstore.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _bookstore.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _bookstore.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _bookstore.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _bookstore.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _bookstore:
_bookstore.SwigPyIterator_swigregister(SwigPyIterator)
class BookStore(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _bookstore.BookStore_swiginit(self, _bookstore.new_BookStore(*args))
    __swig_destroy__ = _bookstore.delete_BookStore

    def initialize(self, force_reset=False):
        return _bookstore.BookStore_initialize(self, force_reset)

    def login(self, *args):
        return _bookstore.BookStore_login(self, *args)

    def logout(self):
        return _bookstore.BookStore_logout(self)

    def useradd(self, user_id, password, name, privilege):
        return _bookstore.BookStore_useradd(self, user_id, password, name, privilege)

    def customerUseradd(self, user_id, password, name):
        return _bookstore.BookStore_customerUseradd(self, user_id, password, name)

    def passwd(self, *args):
        return _bookstore.BookStore_passwd(self, *args)

    def deluser(self, user_id):
        return _bookstore.BookStore_deluser(self, user_id)

    def search(self, params):
        return _bookstore.BookStore_search(self, params)

    def select(self, ISBN):
        return _bookstore.BookStore_select(self, ISBN)

    def modify(self, new_book):
        return _bookstore.BookStore_modify(self, new_book)

    def import_(self, quantity, cost):
        return _bookstore.BookStore_import_(self, quantity, cost)

    def purchase(self, ISBN, quantity):
        return _bookstore.BookStore_purchase(self, ISBN, quantity)

    def showFinance(self, *args):
        return _bookstore.BookStore_showFinance(self, *args)

    def getUserId(self):
        return _bookstore.BookStore_getUserId(self)

    def getUserName(self):
        return _bookstore.BookStore_getUserName(self)

    def getPrivilege(self):
        return _bookstore.BookStore_getPrivilege(self)

# Register BookStore in _bookstore:
_bookstore.BookStore_swigregister(BookStore)
kExceptionType_K_SUCCESS = _bookstore.kExceptionType_K_SUCCESS
kExceptionType_K_INVALID_COMMAND = _bookstore.kExceptionType_K_INVALID_COMMAND
kExceptionType_K_INVALID_PARAMETER = _bookstore.kExceptionType_K_INVALID_PARAMETER
kExceptionType_K_USER_NOT_FOUND = _bookstore.kExceptionType_K_USER_NOT_FOUND
kExceptionType_K_WRONG_PASSWORD = _bookstore.kExceptionType_K_WRONG_PASSWORD
kExceptionType_K_PERMISSION_DENIED = _bookstore.kExceptionType_K_PERMISSION_DENIED
kExceptionType_K_NO_LOGIN_USER = _bookstore.kExceptionType_K_NO_LOGIN_USER
kExceptionType_K_USER_ALREADY_EXIST = _bookstore.kExceptionType_K_USER_ALREADY_EXIST
kExceptionType_K_USER_IS_LOGGED_IN = _bookstore.kExceptionType_K_USER_IS_LOGGED_IN
kExceptionType_K_BOOK_NOT_FOUND = _bookstore.kExceptionType_K_BOOK_NOT_FOUND
kExceptionType_K_NO_SELECTED_BOOK = _bookstore.kExceptionType_K_NO_SELECTED_BOOK
kExceptionType_K_NOT_ENOUGH_INVENTORY = _bookstore.kExceptionType_K_NOT_ENOUGH_INVENTORY
kExceptionType_K_SAME_ISBN = _bookstore.kExceptionType_K_SAME_ISBN
kExceptionType_K_DUPLICATED_ISBN = _bookstore.kExceptionType_K_DUPLICATED_ISBN
kExceptionType_K_DUPLICATED_KEYWORDS = _bookstore.kExceptionType_K_DUPLICATED_KEYWORDS
kExceptionType_K_NOT_ENOUGH_RECORDS = _bookstore.kExceptionType_K_NOT_ENOUGH_RECORDS

def exceptionTypeToString(exception_type):
    return _bookstore.exceptionTypeToString(exception_type)
class FinanceRecord(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    @staticmethod
    def byte_size():
        return _bookstore.FinanceRecord_byte_size()

    def toBytes(self, dest):
        return _bookstore.FinanceRecord_toBytes(self, dest)

    def fromBytes(self, src):
        return _bookstore.FinanceRecord_fromBytes(self, src)

    def __init__(self, *args):
        _bookstore.FinanceRecord_swiginit(self, _bookstore.new_FinanceRecord(*args))

    def income(self):
        return _bookstore.FinanceRecord_income(self)

    def expenditure(self):
        return _bookstore.FinanceRecord_expenditure(self)

    def balance(self):
        return _bookstore.FinanceRecord_balance(self)

    def __sub__(self, rhs):
        return _bookstore.FinanceRecord___sub__(self, rhs)

    def valid(self):
        return _bookstore.FinanceRecord_valid(self)

    def log(self, money):
        return _bookstore.FinanceRecord_log(self, money)
    __swig_destroy__ = _bookstore.delete_FinanceRecord

# Register FinanceRecord in _bookstore:
_bookstore.FinanceRecord_swigregister(FinanceRecord)
class FinanceLog(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _bookstore.FinanceLog_swiginit(self, _bookstore.new_FinanceLog(*args))

    def initialize(self, reset=False):
        return _bookstore.FinanceLog_initialize(self, reset)

    def log(self, money):
        return _bookstore.FinanceLog_log(self, money)

    def sum(self, *args):
        return _bookstore.FinanceLog_sum(self, *args)
    __swig_destroy__ = _bookstore.delete_FinanceLog

# Register FinanceLog in _bookstore:
_bookstore.FinanceLog_swigregister(FinanceLog)
class UserLog(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _bookstore.UserLog_swiginit(self, _bookstore.new_UserLog(*args))

    def initialize(self, reset=False):
        return _bookstore.UserLog_initialize(self, reset)
    __swig_destroy__ = _bookstore.delete_UserLog

# Register UserLog in _bookstore:
_bookstore.UserLog_swigregister(UserLog)
class Book(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ISBN = property(_bookstore.Book_ISBN_get, _bookstore.Book_ISBN_set)
    title = property(_bookstore.Book_title_get, _bookstore.Book_title_set)
    author = property(_bookstore.Book_author_get, _bookstore.Book_author_set)
    keywords = property(_bookstore.Book_keywords_get, _bookstore.Book_keywords_set)
    price = property(_bookstore.Book_price_get, _bookstore.Book_price_set)
    quantity = property(_bookstore.Book_quantity_get, _bookstore.Book_quantity_set)

    def __init__(self, *args):
        _bookstore.Book_swiginit(self, _bookstore.new_Book(*args))

    @staticmethod
    def byte_size():
        return _bookstore.Book_byte_size()

    def toBytes(self, dest):
        return _bookstore.Book_toBytes(self, dest)

    def fromBytes(self, src):
        return _bookstore.Book_fromBytes(self, src)

    @staticmethod
    def unpackKeywords(keywords):
        return _bookstore.Book_unpackKeywords(keywords)

    @staticmethod
    def regularizeKeywords(keywords):
        return _bookstore.Book_regularizeKeywords(keywords)

    @staticmethod
    def hasKeyword(keywords, keyword):
        return _bookstore.Book_hasKeyword(keywords, keyword)
    __swig_destroy__ = _bookstore.delete_Book

# Register Book in _bookstore:
_bookstore.Book_swigregister(Book)
class BookSystem(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, file_prefix, vectors):
        _bookstore.BookSystem_swiginit(self, _bookstore.new_BookSystem(file_prefix, vectors))
    __swig_destroy__ = _bookstore.delete_BookSystem

    def initialize(self, reset=False):
        return _bookstore.BookSystem_initialize(self, reset)

    def find(self, ISBN):
        return _bookstore.BookSystem_find(self, ISBN)

    def get(self, id):
        return _bookstore.BookSystem_get(self, id)

    def select(self, ISBN):
        return _bookstore.BookSystem_select(self, ISBN)

    def modify(self, id, old, new_book):
        return _bookstore.BookSystem_modify(self, id, old, new_book)

    def search(self, params):
        return _bookstore.BookSystem_search(self, params)

# Register BookSystem in _bookstore:
_bookstore.BookSystem_swigregister(BookSystem)
class PairExceptionULL(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _bookstore.PairExceptionULL_swiginit(self, _bookstore.new_PairExceptionULL(*args))
    first = property(_bookstore.PairExceptionULL_first_get, _bookstore.PairExceptionULL_first_set)
    second = property(_bookstore.PairExceptionULL_second_get, _bookstore.PairExceptionULL_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _bookstore.delete_PairExceptionULL

# Register PairExceptionULL in _bookstore:
_bookstore.PairExceptionULL_swigregister(PairExceptionULL)
class VectorBook(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _bookstore.VectorBook_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _bookstore.VectorBook___nonzero__(self)

    def __bool__(self):
        return _bookstore.VectorBook___bool__(self)

    def __len__(self):
        return _bookstore.VectorBook___len__(self)

    def __getslice__(self, i, j):
        return _bookstore.VectorBook___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _bookstore.VectorBook___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _bookstore.VectorBook___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _bookstore.VectorBook___delitem__(self, *args)

    def __getitem__(self, *args):
        return _bookstore.VectorBook___getitem__(self, *args)

    def __setitem__(self, *args):
        return _bookstore.VectorBook___setitem__(self, *args)

    def pop(self):
        return _bookstore.VectorBook_pop(self)

    def append(self, x):
        return _bookstore.VectorBook_append(self, x)

    def empty(self):
        return _bookstore.VectorBook_empty(self)

    def size(self):
        return _bookstore.VectorBook_size(self)

    def swap(self, v):
        return _bookstore.VectorBook_swap(self, v)

    def begin(self):
        return _bookstore.VectorBook_begin(self)

    def end(self):
        return _bookstore.VectorBook_end(self)

    def rbegin(self):
        return _bookstore.VectorBook_rbegin(self)

    def rend(self):
        return _bookstore.VectorBook_rend(self)

    def clear(self):
        return _bookstore.VectorBook_clear(self)

    def get_allocator(self):
        return _bookstore.VectorBook_get_allocator(self)

    def pop_back(self):
        return _bookstore.VectorBook_pop_back(self)

    def erase(self, *args):
        return _bookstore.VectorBook_erase(self, *args)

    def __init__(self, *args):
        _bookstore.VectorBook_swiginit(self, _bookstore.new_VectorBook(*args))

    def push_back(self, x):
        return _bookstore.VectorBook_push_back(self, x)

    def front(self):
        return _bookstore.VectorBook_front(self)

    def back(self):
        return _bookstore.VectorBook_back(self)

    def assign(self, n, x):
        return _bookstore.VectorBook_assign(self, n, x)

    def resize(self, *args):
        return _bookstore.VectorBook_resize(self, *args)

    def insert(self, *args):
        return _bookstore.VectorBook_insert(self, *args)

    def reserve(self, n):
        return _bookstore.VectorBook_reserve(self, n)

    def capacity(self):
        return _bookstore.VectorBook_capacity(self)
    __swig_destroy__ = _bookstore.delete_VectorBook

# Register VectorBook in _bookstore:
_bookstore.VectorBook_swigregister(VectorBook)
class PairExceptionVectorBook(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _bookstore.PairExceptionVectorBook_swiginit(self, _bookstore.new_PairExceptionVectorBook(*args))
    first = property(_bookstore.PairExceptionVectorBook_first_get, _bookstore.PairExceptionVectorBook_first_set)
    second = property(_bookstore.PairExceptionVectorBook_second_get, _bookstore.PairExceptionVectorBook_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _bookstore.delete_PairExceptionVectorBook

# Register PairExceptionVectorBook in _bookstore:
_bookstore.PairExceptionVectorBook_swigregister(PairExceptionVectorBook)
class PairExceptionFinanceRecord(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _bookstore.PairExceptionFinanceRecord_swiginit(self, _bookstore.new_PairExceptionFinanceRecord(*args))
    first = property(_bookstore.PairExceptionFinanceRecord_first_get, _bookstore.PairExceptionFinanceRecord_first_set)
    second = property(_bookstore.PairExceptionFinanceRecord_second_get, _bookstore.PairExceptionFinanceRecord_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _bookstore.delete_PairExceptionFinanceRecord

# Register PairExceptionFinanceRecord in _bookstore:
_bookstore.PairExceptionFinanceRecord_swigregister(PairExceptionFinanceRecord)

