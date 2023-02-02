from django.db import models





class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        abstract = True


class Home(TimeStampModel):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greeting_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    
    
    
    def __str__(self):
        return self.name

class About(TimeStampModel):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    
    def __str__(self):
        return self.career
    
    
class Profile(TimeStampModel):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)
    
    
class Category(TimeStampModel):
    name = models.CharField(max_length=20)
    
    
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        
    def __str__(self):
        return self.name
    
    
class Skills(TimeStampModel):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills_name = models.CharField(max_length=20)
    
    
class Photos(TimeStampModel):
    picture_1 = models.ImageField(upload_to='picture/',blank=True, null=True)
    
    
    
    
class Portfolio(TimeStampModel):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    
    
    def __str__(self):
        return f'portfolio {self.id}'
    
 
class Contact(TimeStampModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=200)
    message = models.TextField()
    
class Footer1(TimeStampModel):
    header = models.CharField(max_length=255)
    page = models.TextField(blank=False)
    
class Footer2(TimeStampModel):
    header = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
   
    
class Footer3(TimeStampModel):
    header = models.CharField(max_length=255)
    social_name = models.CharField(max_length=10, blank=True, null=True)
    link = models.URLField(max_length=255)
   
    