import json
from channels import Group
from .models import Category

def connect_room(message, slug):
    print("Connected to room")
    category = Category.objects.get(slug=slug)
    message.reply_channel.send({"accept": True})
    Group(category.group_name).add(message.reply_channel)


def disconnect_room(message, slug):
    category = Category.objects.get(slug=slug)
    Group(category.group_name).discard(message.reply_channel)

def save_post(message, slug):
    post = json.loads(message['text'])['post']
    category = Category.objects.get(slug=slug)
    Category.objects.create(category=category, body=post)
