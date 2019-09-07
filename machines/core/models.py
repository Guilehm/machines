from django.db import models


class Machine:
    code = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    on_sale = models.BooleanField(default=False, db_index=True)
    pictures = models.ManyToManyField('core.Picture', related_name='machines')
    picture_list = models.ForeignKey(
        'core.Picture',
        null=True,
        blank=True,
        related_name='machines',
        on_delete=models.CASCADE,
    )
    modules = models.ManyToManyField('core.Module')
    price = models.DecimalField(max_digits=9, decimal_places=2)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.code}) {self.name}'


class Module:
    code = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    pictures = models.ManyToManyField('core.Picture', related_name='modules')
    picture_list = models.ForeignKey(
        'core.Picture', null=True, blank=True, on_delete=models.CASCADE
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class ModuleVariation:
    module = models.ForeignKey(
        'core.Module',
        related_name='variations',
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    pictures = models.ManyToManyField('core.Picture', related_name='variations')
    stock = models.PositiveIntegerField(default=0, db_index=True)
    on_sale = models.BooleanField(default=False, db_index=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.code}) {self.name}'


class Picture(models.Model):
    original_file_name = models.CharField(max_length=1024, null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to='core/picture/image')

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '#{id}{title}'.format(
            id=self.pk,
            title=f' ({self.title})' if self.title else '',
        )
