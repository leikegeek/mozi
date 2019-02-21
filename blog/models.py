from django.db import models


# 作者
class User(models.Model):
    user_id = models.CharField(max_length=16),  # 作者iD
    user_name = models.CharField(max_length=32),  # 作者昵称
    register_dt = models.DateTimeField(auto_now_add=True),  # 注册时间
    login_dt = models.DateTimeField(),  # 登陆时间
    author_sign = models.CharField(max_length=120),  # 签名
    sex = models.IntegerField(default=0),  # 性别默认0【男】
    birthday = models.DateField(),  # 生日
    user_level = models.IntegerField(default=1)  # 等级默认1
    user_status = models.IntegerField(default=1)  # 用户状态 1 正常状态 0 已删除 2 被锁定
    active_dt = models.DateTimeField()  # 解锁时间
    create_by = models.CharField(max_length=16)  # 创建人
    update_by = models.CharField(max_length=16)  # 最后更新人
    create_dt = models.DateTimeField(auto_now_add=True),  # 创建时间
    update_dt = models.DateTimeField(auto_now=True),  # 更新时间


# 文章
class Article(models.Model):
    article_tile = models.CharField(max_length=120)  # 标题
    article_content = models.TextField()  # 文章内容
    author = models.ForeignKey("User")  # 作者
    tags = models.CharField(max_length=120)  # 标签
    create_by = models.CharField(max_length=16)  # 创建人
    update_by = models.CharField(max_length=16)  # 最后更新人
    create_dt = models.DateTimeField(auto_now_add=True),  # 创建时间
    update_dt = models.DateTimeField(auto_now=True),  # 更新时间
    likes = models.IntegerField(default=0)  # 点赞数
    view_count = models.IntegerField(default=0)  # 阅读量
    article_status = models.IntegerField(default=0)  # 文章状态0默认草稿 1已发布


# comment 评论
class Comment(models.Model):
    author = models.ForeignKey("User")  # 作者
    comment_content = models.CharField(max_length=4000)  # 评论内容
    parent_id = models.IntegerField(default=0)  # 父评论ID
    comment_status = models.IntegerField(default=1)  # 1正常 0 已删除
    create_by = models.CharField(max_length=16)  # 创建人
    update_by = models.CharField(max_length=16)  # 最后更新人
    create_dt = models.DateTimeField(auto_now_add=True),  # 创建时间
    update_dt = models.DateTimeField(auto_now=True),  # 更新时间


class Tag(models.Model):
    tag_name = models.CharField(max_length=360)  # 标签名
    tag_description = models.CharField(max_length=360)  # 标签描述
    create_by = models.CharField(max_length=16)  # 创建人
    update_by = models.CharField(max_length=16)  # 最后更新人
    create_dt = models.DateTimeField(auto_now_add=True),  # 创建时间
    update_dt = models.DateTimeField(auto_now=True),  # 更新时间


