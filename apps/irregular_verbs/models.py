from django.db import models

class IrregularVerb(models.Model):
    uz_translate = models.CharField(max_length=50)
    ru_translate = models.CharField(max_length=50)
    
    infinitive = models.CharField(max_length=50)
    past_simple = models.CharField(max_length=50)
    past_participle = models.CharField(max_length=50)

    def __str__(self):
        return self.infinitive
