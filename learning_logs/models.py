from django.db import models


class Topic(models.Model):
    '''Topic wchich user already learned'''

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Returns model representation as a string'''

        return self.text
