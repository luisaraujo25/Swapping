# Week 3

## Anchors in Django

`href = "{ % url 'view name' % }"`

## Class Meta

Model Meta is basically the inner class of your model class. Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name and lot of other options. It's completely optional to add Meta class in your model.

<code>

    class MyTable(models.Model):
    class Meta:
        unique_together = (('key1', 'key2'),)

    key1 = models.IntegerField(primary_key=True)
    key2 = models.IntegerField()</code>