development = {
    #'ASSET_URL': '/static/',
    'DATABASE_URL': 'mysql+mysqldb://aereel.db',
    'BASE_URL': 'http://localhost:5000/',
    'DEBUG': True,
}

production = {
    'DATABASE_URL': 'mysql+mysqldb://aereel.db',
    'BASE_URL': 'http://localhost:5000/',
    'DEBUG': True,
}

test = {
    'DATABASE_URL': 'mysql+mysqldb://aereel_test.db',
    'BASE_URL': 'http://localhost:8000/',
    'TESTING': True,
}

config = {
    'development': development,
    'production': production,
    'test': test,
}
