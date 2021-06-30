from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from customUsers.models import User
from .manager import CommentManager, ManagerCustom

class Post(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = RichTextUploadingField()
    tag = models.CharField(max_length=50, null=True, blank=True)
    in_archive = models.BooleanField(default=False)

    objects = ManagerCustom()

    def __str__(self) -> str:
        return self.title

    class Meta():
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    objects = CommentManager()

    def __str__(self) -> str:
        return f"Comment by {self.author}"
    
    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментраии"

class ReplyToComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)

    objects = CommentManager()

    def __str__(self) -> str:
        return f"Comment by {self.author}"
    
    class Meta:
        db_table = 'ReplyToComment'
        verbose_name = 'Отвеченный Комментарий'
        verbose_name_plural = "Отвеченные Комментраии"

class ReplyToReply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    replied_comment = models.ForeignKey(ReplyToComment, on_delete=models.CASCADE)

    objects = CommentManager()

    def __str__(self) -> str:
        return f"Comment by {self.author}"
    
    class Meta:
        db_table = 'ReplyToReply'
        verbose_name = 'Комментарий на отвеченный комментарий'
        verbose_name_plural = "Комментарии на отвеченные комментарий"