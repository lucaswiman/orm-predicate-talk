from django.db import models

class Order(models.Model):
    pass

class InsuranceClaim(models.Model):
    order = models.OneToOneField('app.Order', null=True,
                                 related_name='claim')
    payer = models.ForeignKey('app.InsurancePayer',
                              on_delete=models.CASCADE)
    services = models.ManyToManyField('app.BillableService')

class BillableService(models.Model):
    pass

class InsurancePayer(models.Model):
    name = models.TextField()


class Node(models.Model):
    m2m = models.ManyToManyField('self', related_name='reverse_m2m')
    fk = models.ManyToManyField('self', related_name='reverse_fk')
    one_to_one = models.OneToOneField(
        'self', null=True, related_name='reverse_one_to_one')
    attr1 = models.TextField(null=True, default=None)
    attr2 = models.TextField(null=True, default=None)
    def __repr__(self):
        return 'Node(pk=%s)' % self.pk
    __str__ = __repr__
