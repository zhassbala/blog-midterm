from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse 
from django.urls import reverse
from .models import Article, Comment
from django.utils import timezone 


# /articles/		главная страница где отображается список статей
def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:10]
	site_title = "Последние статьи"
	return render(request, 'articles/list.html', 
		{'latest_articles_list': latest_articles_list, 
		'label': "Последние новости:", 
		'site_title': site_title})

# /aricles/new_post {form info}
def new_post(request):		
	a = Article(
		article_title = request.POST['title'], 
		article_text = request.POST['text'], 
		pub_date = timezone.now(), 
		# image = request.POST['image']
		)
	a.save()
	return HttpResponseRedirect(reverse('articles:index'))


#----------//------------ 
# /articles/article_id  	переходишь  на страницу статьи и смотришь информацию о нем
def detail(request, article_id):
	try:
		a = Article.objects.get( id= article_id)
	except:
		raise Http404('Статья не найдена! Сорян')

	latest_comments_list = a.comment_set.order_by('-id')[:10]
	return render(	request, 'articles/detail.html', 
					{'article': a, 'latest_comments_list': latest_comments_list})


# articles/article_id/leave_comment  {form info} 
def leave_comment(request, article_id):
	try:
		a = Article.objects.get( id= article_id)
	except:
		raise Http404('Статья не найдена! Сорян')

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
	return HttpResponseRedirect(reverse('articles:detail', args=(a.id, )))


def search(request):
	articles_list = Article.objects.filter(article_title__icontains=request.GET['searchword'].capitalize())
	label = "Поиск по запросу \"" + str(request.GET['searchword']) + "\""
	return render(	request, 'articles/list.html', 
					{'latest_articles_list': articles_list, 
					'label': label, 
					'site_title': label})
