"""
Django settings for metaverse project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# 用于绑定当前项目所在的绝对路径，项目中所有文件都需要依赖此路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 这是一个加密的盐，一般配合加密算法Hash、MD5一起用
SECRET_KEY = 'django-insecure-i7--w@)ve2nr*82v(-2@!&@dyrsxmqpqus92plxa2&otqg2n2e'

# 用于配置Django项目的启动方式
# True：用于开发环境，属于调试模式，会显示报错信息用于调试
# False：用于线上环境，不启用调试模式
DEBUG = True

# 当 DEBUG = False 时需要填写，用于配置能够访问当前站点的域名（IP地址）
# 如果是空列表[*]，表示只有 localhost 可以访问本项目
# 如果是[*]，表示访问不设限
# 如果是像['192.168.1.3', '192.168.3.3'] 表示只有当前两个主机能访问当前项目
ALLOWED_HOSTS = []

# 这个参数指当前项目中安装的APP列表，Django 把默认自带的应用放在这个列表里，比如 Admin 后台应用、Auth 用户管理系统等
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
    'import_export'
]

# 这个参数用于注册中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 这个参数表示当前项目的根 URL，是 Django 路由系统的入口
ROOT_URLCONF = 'metaverse.urls'

# 这个参数用于指定模板的配置信息，列表中每一元素都是一个字典
# DjangoTemplates 是 Django自带默认模板
TEMPLATES = [
    {
        # Django默认设置，指定了要是用的模板引擎的 Python 路径
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 一个目录列表，指定模板文件的存放路径，可以是一个或者多个。模板引擎将按照列表中定义的顺序查找模板文件
        # 我们需要先在根目录下创建templates文件夹，然后在 DIRS 变量里添加路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': ["%s/%s" % (BASE_DIR, 'templates')],
        # 一个布尔值，默认为 True，表示会在安装应用中的 templates 目录中搜索所有模板文件
        'APP_DIRS': True,
        # 指定额外的选项，不同的模板引擎有着不同的可选参数
        # 例如 context_processors 用于配置模板上下文处理器，在使 RequestContext 时将看到它们的作用。
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 项目部署时，Django 的内置服务器将使用的 WSGI 应用程序对象的完整 Python 路径
WSGI_APPLICATION = 'metaverse.wsgi.application'

# 用于指定数据库配置信息，默认使用Django自带的sqllite3
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'metaverse',
        'USER': 'root',
        'PASSWORD': '54213TAT',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# 这是一个支持插拔的密码验证器，且可以一次性配置多个，Django 通过这些内置组件来避免用户设置的密码等级不足的问题。
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 语言配置项
# 英语：en-us 中文：zh-Hans
LANGUAGE_CODE = 'zh-Hans'

# 当前服务端时区的配置项
# 世界时区：UTC  中国时区：Asia/Shanghai
TIME_ZONE = 'Asia/Shanghai'

# 项目开发完成后，可以选择向不同国家的用户提供服务，那么就需要支持国际化和本地化
# USE_118N 和 USE_L10N 这两个变量值表示是否需要开启国际化和本地化功能。默认开启的状态
USE_I18N = True

# 它指对时区的处理方式，当设置为 True 的时候，存储到数据库的时间是世界时间  'UTC'
# 如果设置为False，表示对时区不敏感，使用本地时间
USE_TZ = False

# 指的是静态资源的存放位置，静态资源包括 CSS、JS、Images
# 比如我们要在项目中添加一些图片，通常这些静态图片被存放在新建的 static 目录下，这样就实现了通过 STATIC_URL= '/static/' 路径对静态资源的访问。
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_ROOT, 'css')),
    ('images', os.path.join(STATIC_ROOT, 'images')),
    ('js', os.path.join(STATIC_ROOT, 'js'))
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
