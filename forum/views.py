from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolves import reverse
from django.views.decorators.http import require_POST
from django.db.models import F 
from django.core.cache improt cache

from  .models import ForumPost
from .forms import ForumPost

def post_index(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			form = ForumPostForm(request.POST)
			if form.is_valid():
				post = form.save(request.POST)
				post.creator = request.user
				post.save()
				#create_action(request.user, POST, post)
				return HttpResponseRedirect(reverse('forum:index'))
		else:
				return HttpResponseRedirect(reverse('forum:login'))
	else:
		order = request.GET.get('order','default')
		if not order in ('time', 'all'):
			order = 'default'
		cache_key = REDIS_POSTS_KEY.format(order)


def 
# Create your views here.
