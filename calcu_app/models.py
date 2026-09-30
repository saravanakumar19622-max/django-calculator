from django.db import models

# Create your models here.
class Calculation(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operator = models.CharField(max_length=1)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.num1} {self.operator} {self.num2} = {self.result}"

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email