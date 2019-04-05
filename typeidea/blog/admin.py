from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from .models import Category, Post, Tag
from typeidea.base_admin import BaseOwnerAdmin


# import requests
# from django.contrib.auth import get_permission_codename

PERMISSION_API = "http://permission.sso.com/has_per?user={}&per_code={}"

# 对于PostAdmin、TagAdmin、CategoryAdmin类均继承抽象出来的BaseOwnerAdmin类，是为了让用户至看到
# 自己的分类、文章、标签，并且BaseOwnerAdmin类抽象出了save_model方法保存用户，get_queryset方法
# 让列表页只展示当前用户
# Register your models here.
class PostInline(admin.StackedInline):
    fields = ('title', 'desc')
    extra = 1  # 控制额外多个
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]
    # 配置列表页面展示的内容
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    # 匿名用户的存储
    # def save_model(self, request, obj, form, change):
    #     # obj是当前要保存的用户对象，form是页面提交过来之后的对象，change是用于标记本次保存的数据是新增的还是更新的
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    # def has_add_permission(self, request):
    #     opts = self.opts
    #     codename = get_permission_codename("add", opts)
    #     perm_code = "%s.%s" % (opts.app_label, codename)
    #     resp = requests.get(PERMISSION_API.format(request.user.username, perm_code))
    #     if resp.status_code == 200:
    #         return True
    #     else:
    #         return False

    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    # list_display_links用来配置那些字段可以作为链接，点击他们，可以进入编辑页面
    list_display_links = []

    # list_filter用来配置页面过滤器，需要通过哪些字段的值来过滤列表页。
    list_filter = [CategoryOwnerFilter]
    # search_field是用来配置搜索
    search_fields = ['title', 'category__name']
    save_on_top = True
    # 编辑页面
    # save_on_top 保存、编辑、编辑并新建按钮是否在顶部展示
    # actions_on_top 动作相关的配置，是否展示在底部
    # actions_on_bottom 动作相关的配置，是否展示在底部
    actions_on_top = True
    actions_on_bottom = True

    exclude = ['owner',]

    # fields配置的两个作用：1.限定要显示的字段 2.配置显示字段的顺序
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide',),
            'fields': ('tag',),

        })
    )

    # operator自定义方法，在list_display中，如果想要展示自定义字段，如何处理？
    # -自定义函数可以返回HTML，但是需要通过format_html函数处理，reverse是根据名称解析出URL地址，
    # operator.short_description的作用就是指定头的展示文案
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdm.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)
