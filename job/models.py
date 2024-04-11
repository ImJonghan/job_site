from django.db import models

# Create your models here.
# Person - 이름, 전문분야, 증명사진

class Person(models.Model):    
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)    
    image = models.ImageField(upload_to='images/') # 이 부분이 이미지 저장
