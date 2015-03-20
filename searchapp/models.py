from django.db import models



class MPattendence(models.Model):
    division_or_seat_num = models.IntegerField(default=0)
    member_name = models.CharField(max_length=200)
    lok_sabha = models.IntegerField(default=0)
    session = models.IntegerField(default=0)
    state = models.CharField(max_length=200, default=None)
    constituency = models.CharField(max_length=200, default=None)
    total_seats = models.IntegerField(default=0)
    num_of_days = models.IntegerField(default=0)
