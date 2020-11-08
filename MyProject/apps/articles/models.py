from django.db import models


class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField("Дата публикации", auto_now=False, auto_now_add=False)

    def __str__(self):
        return 'Article title: ' + self.article_title + '\nArticle text: ' + self.article_text
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name="", on_delete=models.CASCADE)
    author_name = models.CharField('author name', max_length=50)
    comment_text = models.CharField('comment text', max_length=50)
    
    def __str__(self):
        return 'Author name: ' + self.author_name + ', Comment text: ' + self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
