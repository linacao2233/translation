# functions to call for file processing
from .models import *


def fileoutput(filename):
	"""
	write all the translated sentences in an English file
	"""

	chapters = Chapter.objects.all().order_by('order')

	file = open(filename,'w')

	for chapter in chapters:
		sentences = Sentence.objects.filter(chapter=chapter).order_by('order')
		file.write('\n')

		for sentence in sentences:
			if sentence.English:
				file.write(sentence.English + '\n')

		file.write('\n')

	file.close()


def readfile(filename):
	file = open(filename,'r')

	
