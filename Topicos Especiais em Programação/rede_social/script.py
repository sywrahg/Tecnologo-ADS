import json
import os
import django

def main():
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rede_social.settings")
	django.setup()
	from core.models import Profile,Address,Comment,Post

	file = open('./db.json')
	data = json.load(file)
	for user in data['users']:
		if not Profile.objects.filter(pk= user['id']).exists():
			Profile.objects.create(pk=user['id'],
				name=user['name'],
				email=user['email'],
				address=Address.objects.create(street=user['address']['street'],suite=user['address']['suite'],city=user['address']['city'],zipcode=user['address']['zipcode']))

	print('Usuario criados\n')

	for post in data['posts']:
		if not Post.objects.filter(pk=post['id']).exists():
			Post.objects.create(pk=post['id'],
				title = post['title'],
				body = post['body'],
				profile = Profile.objects.get(pk=post['userId']))

	print('Posts criados\n')	

	for comment in data['comments']:
		if not Comment.objects.filter(pk=comment['id']).exists():
			Comment.objects.create(pk=comment['id'],
				name=comment['name'],
				email=comment['email'],
				body=comment['body'],
				post=Post.objects.get(pk=comment['postId']))

	print('Comentarios criados\n')

if __name__ == '__main__':
	main()