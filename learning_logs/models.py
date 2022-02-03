from django.db import models


class Topic(models.Model):
    '''Topic wchich user already learned'''

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Returns model representation as a string'''

        return self.text

class Entry(models.Model):
    '''Particular information about learning progress'''
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        '''return representaion of the model as a string'''
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
