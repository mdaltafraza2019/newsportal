from django.db import models
CAT=(
    ('crime','crime'),
    ('education','education'),
    ('sports','sports'),
    ('entertenment','entertenment'),
    ('golbal','golbal'),
)
PLACE=(
    ('purnia','purnia'),
    ('katihar','katihar'),
    ('america','america'),
    ('delhi','delhi'),
    ('mumbai','mumbai'),
)

# Create your models here.
class Post(models.Model):
    title=models.CharField( max_length=100)
    author=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    content=models.TextField()
    catogary=models.CharField(max_length=100,choices=CAT,blank=True,null=True)
    place=models.CharField(max_length=100,choices=PLACE,blank=True,null=True)


    def __str__(self):
        return self.title+" "+str(self.date)
    
