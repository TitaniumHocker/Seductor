
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'd05661c81df53f54e9973d8ccdbb0666cd91925d89b24abfad58a1073d3f0a2e' 

# Domains
# DOMAINS = ['sdct.ru']

# Production database
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://seductor_user:pass@localhost/seductor_db'

# Devepopment config
SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
DEBUG = True
DOMAINS = ['10.15.3.198']

