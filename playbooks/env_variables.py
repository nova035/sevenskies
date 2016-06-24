import os

login_user = os.environ.get('KEHIA_STAGING_PG_USER', 'kehia_staging_user')
login_password = os.environ.get('KEHIA_STAGING_PG_PASSWORD', 'kehia')
db_user = os.environ.get('KEHIA_STAGING_DB_USER', 'kehia')
db_pass = os.environ.get('KEHIA_STAGING_DB_PASSWORD', 'kehia')
db_name = os.environ.get('KEHIA_STAGING_DB_NAME', 'kehia')
secret_key = os.environ.get('secret_key', 'hjklhjh89789jhjh89907h')
front_end_url = os.environ.get('KEHIA_FRONTEND_URL', '')
libcloud_user = os.environ.get('KEHIA_LIBCLOUD_USER', '')
libcloud_key = os.environ.get('KEHIA_LIBCLOUD_KEY', '')
aws_key_id = os.environ.get('KEHIA_AWS_KEY_ID', '')
aws_secret = os.environ.get('KEHIA_AWS_SECRET', '')
libcloud_storage = os.environ.get('KEHIA_LIBCLOUD_PROVIDER', 'google')
libcloud_provider = os.environ.get(
    'KEHIA_LIBCLOUD_STORAGE', 'djlibcloud.storage.LibCloudStorage')
libcloud_type = os.environ.get(
    'KEHIA_LIBCLOUD_TYPE', 'libcloud.storage.types.Provider.GOOGLE_STORAGE')
libcloud_bucket = os.environ.get('KEHIA_LIBCLOUD_BUCKET', 'kehia-images')
