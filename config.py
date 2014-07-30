CSRF_ENABLED = True
SECRET_KEY = 'dad-hates-deer-eggs'
# Whoosh does not work on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None