from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Post, Tag


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 配置列表页面展示的内容
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')

    # 匿名用户的存储
    def save_model(self, request, obj, form, change):
        # obj是当前要保存的用户对象，form是页面提交过来之后的对象，change是用于标记本次保存的数据是新增的还是更新的
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title','category','status',
        'created_time','operator'
    ]
    # list_display_links用来配置那些字段可以作为链接，点击他们，可以进入编辑页面
    list_display_links = []

    # search_field是用来配置搜索
    search_fields = ['title','category__name']
    # list_filter用来配置页面过滤器，需要通过哪些字段的值来过滤列表页。
    list_filter = ['category',]

    # 编辑页面
    # save_on_top 保存、编辑、编辑并新建按钮是否在顶部展示
    # actions_on_top 动作相关的配置，是否展示在底部
    # actions_on_bottom 动作相关的配置，是否展示在底部
    save_on_top = True

    fields = (
        ('category','title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    # operator自定义方法，在list_display中，如果想要展示自定义字段，如何处理？
    # -自定义函数可以返回HTML，但是需要通过format_html函数处理，reverse是根据名称解析出URL地址，
    # operator.short_description的作用就是指定头的展示文案
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request,obj,form,change)
