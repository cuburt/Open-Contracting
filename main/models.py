from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import datetime
import pandas as pd
from django.utils.functional import lazy


# Create your models here.

class Database(models.Model):
    frequencies = (('daily','Daily'),
                  ('monthly','Monthly'),
                  ('yearly','Yearly'))
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    frequency = models.CharField(choices=frequencies, max_length=10)
    is_favorite = models.BooleanField(default=False)
    group_by_column = models.BooleanField(default=False)
    columns = models.CharField(max_length=10, default=None)
    file = models.FileField()

    def __init(self, *args, **kwargs):
        super(Database, self).__init__(*args, **kwargs)
        self.columns.choices = self.filtered_columns()

    def get_df(self, file):
        df = pd.read_csv(str(file))
        return df

    def group_df(self,df):
        groups = []
        column = str(self.columns)
        for value in df[column].values:
            df = df.loc[df[column] == value]
            groups.append(df)
        return groups

    def export_to_csv(self, df):
        file = df.to_csv(index=False)
        return file

    def filtered_columns(self):
        choices = []
        if self.group_by_column:
            for column in list(self.get_df(self.file).columns):
                choices.append((column,column))
            return choices

    def save(self, *args, **kwargs):
        if self.group_by_column:
            groups = [self.group_df(self.get_df(self.file))]
            for df in groups:
                self.file =  self.export_to_csv(df)
                super(Database, self).save(*args, **kwargs)

    def get_file(self):
        return self.file

    def __str__(self):
        return self.title

class Dataset(models.Model):
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_updated = models.DateTimeField(default=datetime.datetime.today())
    frequency = models.CharField(max_length=50, default='Daily')

    def __str__(self):
        return self.title

