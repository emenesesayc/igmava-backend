import sys

sys.path.insert(0, 'var/www/igmava/application')

from app import app

if __name__ == '__main__':
	app.run(port=8009)
