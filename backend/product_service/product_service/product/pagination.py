from rest_framework.pagination import PageNumberPagination

class SmallPagePagination(PageNumberPagination):
    page_size = 4

class MediumPagePagination(PageNumberPagination):
    page_size = 10

class LargePagePagination(PageNumberPagination):
    page_size = 20
