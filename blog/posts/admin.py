from django.contrib import admin
from django import forms

from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        fields = ('__all__')

        model = Post
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
# Register your models here.
