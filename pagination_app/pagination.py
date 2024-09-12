from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# Generate custom class pagination.
class MyPagination(PageNumberPagination):
    page_size = 5   # only show 5 records at a time. override global variable with local variable.
    page_query_param = 'mypage' # to customize query parameter. default parameter is page.
    page_size_query_param = 'page_size'   # query parameter that allows the client to set the page size.
    max_page_size = 15  # only valid if page_size_query_param is also set
    last_page_strings = ('endpage', ) # page_query_param to request the final page in the set. Default value is ('last',)

class MyPagination2(LimitOffsetPagination):
    default_limit = 5  # default limit of records.
    limit_query_param = 'mylimit'  # to customize query parameter. default parameter is limit.
    offset_query_param = 'myoffset' # # to customize query parameter. default parameter is offset.
    max_limit = 20  # maximum 20 records showing. 

class MyPagination3(CursorPagination):
    ordering = 'vsal'   # asending order by vsal, if you want in desending order just pass - only like '-vsal'.
    page_size = 5 # get 5 records per page.

    