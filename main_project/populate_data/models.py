from django.db import models

# Create your models here.
# class customer_data(models.Model):
#     uid = models.IntegerField(unique=True)
#     name = models.CharField(max_length=100)
#     dob = models.DateField()
#     def __str__(self):
#             return str(self.uid)

# class txn_data(models.Model):
#     name = models.CharField(max_length=100)
#     item = models.CharField(max_length=100)
#     value = models.CharField(max_length=100)
#     def __str__(self):
#             return str(self.name)
class customer_list(models.Model):
    uid = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=250)
    dob = models.DateField(max_length=250)
    loan = models.IntegerField(default=0)
    email = models.CharField(max_length=250)
    mobile = models.IntegerField(default=0)
    def __str__(self):
        return str(self.uid)


class customer_values(models.Model):
    uid = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=250)
    ubill_value = models.IntegerField(default=0)
    tchallan_value = models.IntegerField(default=0)
    ecar_value = models.IntegerField(default=0)
    penalty_value = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)
    
 

class rules(models.Model):
    rule_id = models.IntegerField(default=1)
    ubill_value = models.IntegerField(default=0)
    tchallan_value = models.IntegerField(default=0)
    ecar_value = models.IntegerField(default=0)
    penalty_value = models.IntegerField(default=0)
    threshold_value = models.IntegerField(default=0)
    ubill_wt = models.FloatField(default=0)    
    tchallan_wt = models.FloatField(default=0)    
    ecar_wt = models.FloatField(default=0)    
    penalty_wt = models.FloatField(default=0)    
    threshold_wt = models.FloatField(default=0)    
    def __str__(self):
        return str("Rules")


class decision(models.Model):
    uid = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
    def __str__(self):
        return str(self.uid)