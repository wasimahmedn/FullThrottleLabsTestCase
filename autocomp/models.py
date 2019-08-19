from django.db import models

# Create your models here.
class Word_TB(models.Model):
	word=models.CharField(max_length=264,unique=True)
	frequency=models.BigIntegerField()

	def __str__(self):
		return self.word
