from django.db import models

class Gallery(models.Model):
  title = models.CharField('タイトル', max_length=100)
  text = models.TextField('テキスト')
  image = models.ImageField(null=True, upload_to='media/images/')
  created_date = models.DateTimeField('作成日',auto_now_add=True)
  updated_date = models.DateTimeField('更新日',auto_now=True)

  def __str__(self):
    return self.title
  
