from django.shortcuts import render
from django.views.generic.base import View

# 网站首页
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")
