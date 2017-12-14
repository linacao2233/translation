from django.db import models

# Create your models here.

class Chapter(models.Model):
	order = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.order)


class Sentence(models.Model):
	Chinese = models.TextField(null=True, blank=True)
	English = models.TextField(null=True, blank=True)
	googletranslate = models.TextField(null=True, blank=True)

	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	order = models.FloatField(default=1.0)

	def __str__(self):
		return str(self.chapter.order)+' '+str(self.order)





