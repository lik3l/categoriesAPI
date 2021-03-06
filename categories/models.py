from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            help_text='Name of the category')
    parent = models.ForeignKey(to='categories.Category', related_name='children',
                               on_delete=models.SET_NULL, null=True,
                               help_text='Parent of the category')

    @property
    def siblings(self):
        if not self.parent:
            return []

        return self.parent.children.exclude(pk=self.pk)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
