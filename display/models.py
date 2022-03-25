from django.db import models


# Create your models here.


# 海域
class Sea(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name


# CRISPR序列
class Sequence(models.Model):
    sea = models.ForeignKey(Sea, on_delete=models.CASCADE) # 该序列所属的海域
    excel_id = models.CharField(unique=True, max_length=50)
    seq_id = models.CharField(unique=True, max_length=100)
    CRISPR_start = models.PositiveBigIntegerField()
    CRISPR_end = models.PositiveBigIntegerField()


# 蛋白
class Protein(models.Model):
    crispr = models.ForeignKey(Sequence, on_delete=models.CASCADE) # 该蛋白所属的序列
    protein_id = models.CharField(max_length=100)
    faa_id = models.CharField(max_length=100)
    protein_start = models.PositiveBigIntegerField()
    protein_end = models.PositiveBigIntegerField()
    E_value = models.FloatField()
    distace_between_CRISPR_pro = models.BigIntegerField() # 可以是负数
    length = models.PositiveBigIntegerField()
    anno_name = models.CharField(max_length=200)
    pfam_anno_name = models.CharField(max_length=200)
    function = models.CharField(max_length=1000)
