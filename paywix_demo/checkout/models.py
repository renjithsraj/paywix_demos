from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.



class Transaction(models.Model):
	txn_id = models.CharField(_("transaction id"), max_length=120, unique=True)
	txn_status = models.CharField(_("trabsaction status"), choices=(), max_length=2)

