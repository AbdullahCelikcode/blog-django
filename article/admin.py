from django.contrib import admin

# Register your models here.

from .models import Article,Comment

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title" , "author" , "created_date"]
    #article sayfasında bunların gözükmesini istediğimiz için böle yapabiliriz.
    list_display_links = ["title" , "created_date"]
    #üstüne link koyarız ve bastığımızda sayfayı değişir
    search_fields = ["title"]
    #Başlığa göre bir arama çubuğu koyar
    list_filter = ["created_date"]
    #bir süzgeç yaparız admin sayfasında yükleme sıralarına göre daha rahat arama yapabiliriz
    class Meta:
        #ArticleAdmin ile Article birbirine bağlamak için Djangonun bize sunduğu bir özellik class içi class
        model = Article