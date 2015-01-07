from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    allContent = models.CharField(max_length=500)
    publication_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title


class Center(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    urlButton = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=30)
    allContent = models.CharField(max_length=500)


class RContent(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    allContent = models.CharField(max_length=500)
    publication_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30)


class JoinMe(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    myclass = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    describe = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['-project']

    def __unicode__(self):
        return self.project


class Activities(models.Model):
    title = models.CharField(max_length=50)
    describe = models.CharField(max_length=300, null=True)
    author = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30)
    create_time = models.DateField(max_length=50)


class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    num = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    describe = models.CharField(max_length=300)
    myactivities = models.ForeignKey(JoinMe)





