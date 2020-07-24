from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# Create your models here.

SERVER_STATUS = (
    ("SIN", "Server Side Initiated")
)

TRANSACTION_STATUS = (
    ('NS', 'Not Started'),
    ('IN', 'Initiated'),
    ('MP', 'Money With PayUMoney'),
    ('UD', 'Under Dispute')
    ('RF', 'Refunded'),
    ('PR', 'Partially Refunded'),
    ('BD', 'Bounced'),
    ('FD', 'Failed'),
    ('SP', 'Settlement in Process'),
    ('CP', 'Completed')
)
TRANSACTION_STATUS = TRANSACTION_STATUS + SERVER_STATUS
DETAILS = {
    "NS": "The transaction has not been started yet.",
    "IN": "The transaction has been started but not completed.",
    "MP": "The transaction was successful and the transaction amount is with PayUMoney.",
    "UD": "A dispute for the transaction has been raised.",
    "RF": "The entire amount of the transaction has been refunded.",
    "PR": "A part of the amount of the transaction has been refunded.",
    "BD": "Incomplete or no details provided at PayUMoney payment page.",
    "FD": "The transaction didn’t complete due to a failure.",
    "SP": "Settlement for the transaction is in process.",
    "CP": "The transaction is settled and complete.",
}


class TimeStampModel(models.Model):
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date'), auto_now=True)

    class Meta:
        """Meta definition for TimeStampModel."""
        abstract = True


class Transaction(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL)
    txn_id = models.CharField(_("transaction id"), max_length=120, unique=True)
    txn_status = models.CharField(
        _("trabsaction status"), choices=(TRANSACTION_STATUS), max_length=3, default='SIN')
    amount = models.DecimalField(_('amount'), max_digits=19, decimal_places=4)
    request_data = models.TextField(
        _('Requested Data'), null=True, blank=True)
    requested_hash = models.TextField(
        _('Requested Hash'), null=True, blank=True)
    # response
    response_data = models.TextField(
        _('Response Data'), null=True, blank=True)
    reponse_hash = models.TextField(
        _('Response Hash'), null=True, blank=True)
    payumoney_id = models.CharField(_('payuMoneyId'), editable=False)
    transaction_mode = models.CharField(
        _('Mode'), max_length=2, null=True, blank=True)

    def __str__(self):
        return f"{self.txnid} : {self.created_date} : {self.txn_status}"
