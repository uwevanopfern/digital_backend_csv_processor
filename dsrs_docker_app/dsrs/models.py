from django.db import models


class Territory(models.Model):
    name = models.CharField(max_length=48, default="Spain")
    code_2 = models.CharField(max_length=2, default="ES")
    code_3 = models.CharField(max_length=3)
    local_currency = models.ForeignKey(
        "Currency", related_name="territories", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "territory"
        verbose_name = "territory"
        verbose_name_plural = "territories"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=48, default="Euro")
    symbol = models.CharField(max_length=4)
    code = models.CharField(max_length=3, default="EUR")

    class Meta:
        db_table = "currency"
        verbose_name = "currency"
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.name


class DSR(models.Model):
    class Meta:
        db_table = "dsr"

    STATUS_ALL = (
        ("failed", "FAILED"),
        ("ingested", "INGESTED"),
    )

    path = models.CharField(max_length=256, default="/path/to/dsr.csv")
    period_start = models.DateTimeField(null=False)
    period_end = models.DateTimeField(null=False)

    status = models.CharField(
        choices=STATUS_ALL, default=STATUS_ALL[1][0], max_length=48
    )

    territory = models.ForeignKey(
        Territory, related_name="dsrs", on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        Currency, related_name="dsrs", on_delete=models.CASCADE
    )


class Resource(models.Model):
    class Meta:
        db_table = "resource"

    dsp_id = models.CharField(max_length=256)
    title = models.CharField(max_length=50, null=True)
    artists = models.CharField(max_length=200, null=True)
    isrc = models.CharField(max_length=50, null=True)
    usages = models.IntegerField(null=True)
    revenue = models.FloatField()
    dsrs = models.ManyToManyField(DSR)

    class Meta:
        ordering = ("-revenue",)
