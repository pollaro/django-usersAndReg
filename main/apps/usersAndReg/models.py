from __future__ import unicode_literals
from django.db import models
import re

nameRegex = r'^\w{1,}'
emailRegex = r'^\w+@\w+\.[a-zA-Z]{3}'
nameRegex = re.compile(nameRegex)
emailRegex = re.compile(emailRegex)

class UsersManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if not nameRegex.match(postData['firstName']):
            errors['firstName'] = 'Please enter a valid first name'
        if not nameRegex.match(postData['lastName']):
            errors['lastName'] = 'Please enter a valid last name'
        if not emailRegex.match(postData['email']):
            errors['email'] = 'Please enter a valid email address'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        if postData['password'] != postData['confirmPW']:
            errors['confirmPW'] = 'Password and confirm password must match'
        return errors

class Users(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirmPW = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()
