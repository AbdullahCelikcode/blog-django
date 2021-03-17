from django.db import models
from ckeditor.fields import RichTextField

# Create your models here. # Modellerinizi burada oluşturun. 

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE , verbose_name="Yazar")
    #author = yazar / ForeignKey = başka bir tabloyu göstermek için
    #on_delete = models.CASCADE = Eğer yazar silinirse ona ait olan makaleleride sil gibi
    
    #Tablo
    title = models.CharField(max_length=50 , verbose_name="Başlık")
    #title = Başlık kısmı
    #costent = models.TextField(verbose_name="İçerik")
    #content = içerik
    costent = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True , verbose_name="Oluşturulma Tarihi")
    #Created_date = oluşturma zamanı / auto_now_add=True = paylaşılan zamanı kaydet
    article_image = models.FileField(blank= True, null= True , verbose_name="Makaleye Fotoraf Ekleyin")
    def __str__(self):
        return self.title
        #Başlık kısmı article object 1 olarak gözükmesini engelliyip asıl başlığını göstermesini sağlar
    class Meta:
        ordering = ["-created_date"]
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE, verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length= 50,verbose_name="İsim")
    comment_content = models.CharField(max_length= 200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author
    class Meta:
        ordering = ["-comment_date"]
