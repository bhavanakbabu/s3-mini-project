from django.db import models

# Create your models here.


class userreg(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    def __str__(self):
        return self.username
    
class Notification(models.Model):
    user = models.ForeignKey(userreg, on_delete=models.CASCADE)  # Link to userreg model
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:30]}"



class bin(models.Model):
    area=models.CharField(max_length=25)
    landmark=models.CharField(max_length=25,null=True)
    dmail=models.CharField(max_length=25)
    period=models.CharField(max_length=25)
    complaint = models.ForeignKey('regcomp',null=True, on_delete=models.CASCADE, related_name='bins')


class driver(models.Model):
    dname=models.CharField(max_length=25)
    dpassword=models.CharField(max_length=25)
    demail=models.CharField(max_length=25)
    darea=models.CharField(max_length=25)
class regcomp(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('declained','Declained'),
    ]
    rarea=models.CharField(max_length=25)
    remail=models.CharField(max_length=25)
    username=models.CharField(max_length=25,default="username")
    raddress=models.CharField(max_length=50,null=True)
    rcomp=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
class drivstatus(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('complited','Complited'),
        ('declained','Declained'),
    ]
    drivername=models.CharField(max_length=25,default='default')
    area=models.CharField(max_length=25,default='default')
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')

