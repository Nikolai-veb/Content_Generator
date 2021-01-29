from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify


class Categories(models.Model):
    """ Model Categories """
    name = models.CharField("Название", max_length=200,)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('site_category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.id)
        super(Categories, self).save(*args, **kwargs)



class Under_Categories(models.Model):
    """ Under Categories """
    category = models.ForeignKey(Categories, verbose_name="Категория", on_delete=models.CASCADE, related_name="under_category")
    name = models.CharField("Название под категории", max_length=200,)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('site_under_cotegories', kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Под категория"
        verbose_name_plural = "Под категории"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.id)
        super(Under_Categories, self).save(*args, **kwargs)



class Sites(models.Model):
    """ Sites """
    under_category = models.ForeignKey(Under_Categories, verbose_name="Под категория", on_delete=models.CASCADE, related_name="sites")
    name = models.CharField("Название сайта", max_length=200,)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    
    def get_absolute_url(self):
        return reverse('site_detail', kwargs={"pk": self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сайт"
        verbose_name_plural = "Сайты"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.id)
        super(Sites, self).save(*args, **kwargs)



class Articles(models.Model):
    """ Articles """
    site = models.ForeignKey(Sites, verbose_name="Сайт", on_delete=models.CASCADE, related_name="article")
    name = models.CharField("Название статьи", max_length=200,)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"pk": self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.id)
        super(Articles, self).save(*args, **kwargs)

