from django.db import models


class Band(models.Model):
    """A model of a rock band."""

    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)


class Member(models.Model):
    """A model of a rock band member."""

    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(
        choices=(
            ("g", "Guitar"),
            ("b", "Bass"),
            ("d", "Drums"),
        ),
        max_length=1,
    )
    band = models.ForeignKey("Band",on_delete=models.CASCADE)