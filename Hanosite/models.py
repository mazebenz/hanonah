from django.db import models

# Create your models here.


PRIORITY = [
	('L', 'Low'), #Tuple1
	('M', 'Medium'), #Tuple2
	('H', 'High'), #Tuple3
]

class Mission(models.Model):
	title					= models.CharField(max_length=60)
	mission					= models.TextField(max_length=400)
	priority				= models.CharField(max_length=1, choices=PRIORITY)

	def __str__(self):
		return self.title


