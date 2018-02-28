# -*- coding: utf-8 -*-

import os.path

from configurations import values
from froide.settings import ThemeBase, Base, Production, Dev, rec

gettext = lambda s: s

def get_setting(setting):
    from froide.settings import Base
    return getattr(Base, setting)

class TietopyyntoBase(ThemeBase, Base):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'tietopyynto',
            'USER': 'tietopyynto',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            }
        }
    CONN_MAX_AGE = None

    SECRET_KEY = ('1d20oV9ZjfSLmQ7DE3W44c43/0hmr21LaV'
                  '70yVi3ZJAoRilr2w1XaPQuLm3w5Xm6PBM=')

    SITE_NAME = values.Value(u'Tietopyyntö')
    SITE_EMAIL = values.Value('tietopyynto@tietopyynto.fi')
    SITE_URL = values.Value('http://tietopyynto.fi')

    SITE_ID = values.IntegerValue(1)

    BROKER_URL = values.Value('amqp://tietopyynto:Sua49aZIDCm9@localhost:5672/tietopyynto')

#    CELERY_RESULT_BACKEND = values.Value('amqp://tietopyynto:tietopyynto@localhost:5672/tietopyynto')

    CELERY_EMAIL_TASK_CONFIG = {
        'max_retries': None,
        'ignore_result': False,
        'acks_late': True,
        'store_errors_even_if_ignored': True
    }

    ADMINS = (
         ('Leo Honkanen', 'leo@ponie.fi'),
    )

    MANAGERS = ADMINS

    INTERNAL_IPS = values.TupleValue(('127.0.0.1',))

    # XXX Social Auth is not set up on this repo yet

    SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
    SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

    CUSTOM_AUTH_USER_MODEL_DB = []

    GEOIP_PATH = None

    SOCIAL_AUTH_GITHUB_KEY = '92af0dc8697f140dc548'
    SOCIAL_AUTH_GITHUB_SECRET = '17c2f79970a4f722ef46a7398812987ad8e3f26a'
    SOCIAL_AUTH_GITHUB_SCOPE = ['email']

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '343221621424-vja05krudv99d2b2osgioei8c0ovn4cv.apps.googleusercontent.com'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'VjxfCK5ZceMJMlgfuy8JIfEP'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

    SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
    )

    SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]

    SOCIAL_AUTH_FACEBOOK_KEY     = '1511558542417882'
    SOCIAL_AUTH_FACEBOOK_SECRET  = 'dd353864b3139430b6cede88f19bef75'
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/tili/'
    SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/tili/'
    SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/tili/'
    SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/tili/'

    # -- end social auth things --

    TIME_ZONE = values.Value('Europe/Helsinki')
    USE_TZ = values.BooleanValue(True)
    LANGUAGE_CODE = values.Value('fi-fi')
    LANGUAGES = (
        ('fi-fi', gettext('Suomi')),
        ('sv-fi', gettext('Svenska')),
        ('en', gettext('English')),
    )


    CELERY_ROUTES = {
        'froide.foirequest.tasks.fetch_mail': {"queue": "emailfetch"},
    }
    CELERYD_HIJACK_ROOT_LOGGER = False

    FROIDE_CONFIG = dict(
        create_new_publicbody=True,
        publicbody_empty=True,
        user_can_hide_web=True,
        public_body_officials_public=True,
        public_body_officials_email_public=True,
        request_public_after_due_days=14,
        payment_possible=True,
        currency="Euro",
        default_law=1,
        search_engine_query="http://www.google.fi/search?as_q=%(query)s&as_epq=&as_oq=&as_eq=&hl=fi&lr=&cr=&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=%(domain)s&as_rights=&safe=images",
        greetings=[rec(u"Dear (?:Mr\.?|Ms\.? .*?)")],
        closings=[rec(u"Sincerely yours,?")],
        public_body_boosts={},
        dryrun=False,
        dryrun_domain="tietopyynto.fi",
        allow_pseudonym=False,
        doc_conversion_binary="/usr/bin/libreoffice",
    )

    # EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_SUBJECT_PREFIX = values.Value('[Tietopyynto] ')
    SERVER_EMAIL = values.Value('tietopyynto@tietopyynto.fi')
    DEFAULT_FROM_EMAIL = values.Value('tietopyynto@tietopyynto.fi')

    # Official Notification Mail goes through
    # the normal Django SMTP Backend
    EMAIL_HOST = values.Value("mail.kapsi.fi")
    EMAIL_PORT = values.IntegerValue(25)
    EMAIL_HOST_USER = values.Value("")
    EMAIL_HOST_PASSWORD = values.Value("")
    EMAIL_USE_TLS = values.BooleanValue(False)

    FOI_EMAIL_DOMAIN = "tietopyynto.fi"
    FOI_EMAIL_PORT_IMAP = values.IntegerValue(143)
    FOI_EMAIL_HOST_IMAP = values.Value("localhost")
    FOI_EMAIL_ACCOUNT_NAME = values.Value("tietopyynto-mail")
    FOI_EMAIL_ACCOUNT_PASSWORD = values.Value("PgtFsqqYXFW0")
    FOI_EMAIL_USE_SSL = values.BooleanValue(False)
    FOI_EMAIL_USE_TLS = values.BooleanValue(False)

    # SMTP settings for sending FoI mail
    FOI_EMAIL_HOST_USER = values.Value("")
    FOI_EMAIL_HOST_FROM = values.Value("tietopyynto@tietopyynto.fi")
    FOI_EMAIL_HOST_PASSWORD = values.Value("")
    FOI_EMAIL_HOST = values.Value("mail.kapsi.fi")
    FOI_EMAIL_PORT = values.IntegerValue(25)

    FOI_EMAIL_FIXED_FROM_ADDRESS = values.BooleanValue(True)

    ALLOWED_HOSTS = values.TupleValue((
        'www.tietopyynto.fi',
        'tietopyynto.fi',
        'beta.tietopyynto.fi',
    ))

    FROIDE_THEME = 'tietopyynto_fi.theme'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_URL = '/static/'
    STATIC_ROOT = values.Value(os.path.abspath(os.path.join(PROJECT_ROOT,
                                                            "..", "public")))
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, "static"),
    )
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
    )



#    @property
#    def TEMPLATE_LOADERS(self):
#        old = super(Dev, self).TEMPLATE_LOADERS
#        if self.FROIDE_THEME is not None:
#            return (['froide.helper.theme_utils.ThemeLoader'] + old)
#        return old
#
#    @property
#    def INSTALLED_APPS(self):
#        installed = super(Dev, self).INSTALLED_APPS
#        if self.FROIDE_THEME is not None:
#            return installed.default + [self.FROIDE_THEME]
#        return installed.default

class TietopyyntoProd(TietopyyntoBase, Production):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    FACEBOOK_PAGE = "https://www.facebook.com/groups/tietopyynto"
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': [],
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },

            'standard': {
                'format': '%(asctime)s %(levelname)s [%(name)s: %(lineno)s] -- %(message)s',
                'datefmt': '%m-%d-%Y %H:%M:%S'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
            'celery_task_logger': {
                'level': 'DEBUG',
                'filters': None,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(PROJECT_ROOT, 'logs', 'celery_tasks.log'),
                'maxBytes': 1024*1024*5,
                'backupCount': 2,
                'formatter': 'standard'
            },
	    'logfile': {
		    'level':'DEBUG',
		    'class':'logging.handlers.RotatingFileHandler',
		    'filename': os.path.join(PROJECT_ROOT, 'logs', 'froide.log'),
		    'maxBytes': 50000,
		    'backupCount': 2,
		    'formatter': 'verbose',
	    },
        },
        'loggers': {
            'froide': {
                'handlers': ['console','logfile'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'django': {
                'handlers': ['logfile'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'celery.task': {
                'handlers': ['celery_task_logger'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }


class TietopyyntoDev(TietopyyntoBase, Dev):
    EMAIL_BACKEND = 'bandit.backends.smtp.HijackSMTPBackend'
    BANDIT_EMAIL = 'aleksi.knuutila@gmail.com'
    EMAIL_SUBJECT_PREFIX = values.Value('[Tietopyynto] ')
    SERVER_EMAIL = values.Value('tietopyynto@tietopyynto.fi')
    DEFAULT_FROM_EMAIL = values.Value('tietopyynto@tietopyynto.fi')

    ALLOWED_HOSTS = values.TupleValue((
        '91.232.156.222',
        'www.tietopyynto.fi',
        'tietopyynto.fi',
        'beta.tietopyynto.fi',
    ))


    INSTALLED_APPS = get_setting('INSTALLED_APPS')
    
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    FACEBOOK_PAGE = "https://www.facebook.com/groups/tietopyynto"
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'DEBUG',
            'handlers': [],
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },

            'standard': {
                'format': '%(asctime)s %(levelname)s [%(name)s: %(lineno)s] -- %(message)s',
                'datefmt': '%m-%d-%Y %H:%M:%S'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
            'celery_task_logger': {
                'level': 'DEBUG',
                'filters': None,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(PROJECT_ROOT, 'logs', 'celery_tasks.log'),
                'maxBytes': 1024*1024*5,
                'backupCount': 2,
                'formatter': 'standard'
            },
	    'logfile': {
		    'level':'DEBUG',
		    'class':'logging.handlers.RotatingFileHandler',
		    'filename': os.path.join(PROJECT_ROOT, 'logs', 'froide.log'),
		    'maxBytes': 50000,
		    'backupCount': 2,
		    'formatter': 'verbose',
	    },
        },
        'loggers': {
            'froide': {
                'handlers': ['console','logfile'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'django': {
                'handlers': ['logfile'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'celery.task': {
                'handlers': ['celery_task_logger'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }

