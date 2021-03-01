from superset_config import *
from celery.schedules import crontab
from cachelib import RedisCache
from superset.typing import CacheConfig
import os

FEATURE_FLAGS = {
    "ALERT_REPORTS": True
}

# slack API token (optional)
SLACK_API_TOKEN = "xoxb-"
SLACK_PROXY = None

POSTGRES_USER = "superset"
POSTGRES_PASS = "superset"
POSTGRES_HOST = "postgres"
POSTGRES_PORT = "5432"
POSTGRES_DATABASE = "superset"
REDIS_HOST = "redis-superset"
REDIS_PORT = "6379"
# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://%s:%s@%s:%s/%s?client_encoding=utf8' % (POSTGRES_USER,
                                                          POSTGRES_PASS,
                                                          POSTGRES_HOST,
                                                          POSTGRES_PORT,
                                                          POSTGRES_DATABASE)
CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 24*60*60, # 1 day
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://%s:%s/1' % (REDIS_HOST, REDIS_PORT)
}
DATA_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 24*60*60, # 1 day
    'CACHE_KEY_PREFIX': 'data_',
    'CACHE_REDIS_URL': 'redis://%s:%s/1' % (REDIS_HOST, REDIS_PORT)
}
THUMBNAIL_SELENIUM_USER = "admin"
THUMBNAIL_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 24*60*60*30,
    'CACHE_KEY_PREFIX': 'thumbnail_',
    'CACHE_NO_NULL_WARNING': True,
    'CACHE_REDIS_URL': 'redis://%s:%s/1' % (REDIS_HOST, REDIS_PORT)
}
SCREENSHOT_LOCATE_WAIT = 100
SCREENSHOT_LOAD_WAIT = 600
RESULTS_BACKEND = RedisCache(host=REDIS_HOST, port=REDIS_PORT, key_prefix='superset_results')
class CeleryConfig(object):
    BROKER_URL = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
    CELERY_IMPORTS = ('superset.sql_lab', "superset.tasks", "superset.tasks.thumbnails", )
    CELERY_RESULT_BACKEND = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True
    CELERY_ANNOTATIONS = {
        'sql_lab.get_sql_results': {
            'rate_limit': '100/s',
        },
        'email_reports.send': {
            'rate_limit': '1/s',
            'time_limit': 600,
            'soft_time_limit': 600,
            'ignore_result': True,
        },
    }
    CELERYBEAT_SCHEDULE = {
        'reports.scheduler': {
            'task': 'reports.scheduler',
            'schedule': crontab(minute='*', hour='*'),
        },
        'reports.prune_log': {
            'task': 'reports.prune_log',
            'schedule': crontab(minute=0, hour=0),
        },
        'cache-warmup-hourly': {
            'task': 'cache-warmup',
            'schedule': crontab(minute='*/30', hour='*'),
             'kwargs': {
                'strategy_name': 'top_n_dashboards',
                'top_n': 10,
                'since': '7 days ago',
            },
       },
    }
CELERY_CONFIG = CeleryConfig

# SMTP email configuration
EMAIL_REPORTS_USER="admin"
EMAIL_PAGE_RENDER_WAIT=300
EMAIL_NOTIFICATIONS = True

SMTP_HOST = "smtp.sendgrid.net"
SMTP_STARTTLS = True
SMTP_SSL = False
SMTP_USER = "your_user"
SMTP_PORT = 2525 # your port eg. 587
SMTP_PASSWORD = "your_password"
SMTP_MAIL_FROM = "noreply@youremail.com"

WEBDRIVER_TYPE= "chrome"
WEBDRIVER_OPTION_ARGS = [
        "--force-device-scale-factor=2.0",
        "--high-dpi-support=2.0",
        "--headless",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-extensions",
        ]

WEBDRIVER_BASEURL="http://superset:8088"
WEBDRIVER_BASEURL_USER_FRIENDLY="http://localhost:8088" # change to your domain eg. https://superset.mydomain.com - this is the link that is sent to the recipient
SUPERSET_WEBSERVER_ADDRESS = "localhost"
SUPERSET_WEBSERVER_PORT = 8088
SUPERSET_WEBSERVER_TIMEOUT=600



FEATURE_FLAGS = { "THUMBNAILS" : True, "LISTVIEWS_DEFAULT_CARD_VIEW" : True}
THUMBNAIL_SELENIUM_USER = "admin"
THUMBNAIL_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 24*60*60,
    'CACHE_KEY_PREFIX': 'thumbnail_',
    'CACHE_NO_NULL_WARNING': True,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'
}