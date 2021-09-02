from django.db import models

# Create your models here.

TITLE_CLASSES = (
    ('biology', 'BIOLOGY'),
    ('math','MATH'),
    ('african History','AFRICAN HISTORY'),
    ('computer science', 'COMPUTER SCIENCE')
)

class DjangoClasses(models.Model):
    title = models.CharField(max_length=100, choices=TITLE_CLASSES)
    courseNumber = models.IntegerField(default=0)
    instructorName = models.CharField(max_length=100)
    duration = models.FloatField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.
