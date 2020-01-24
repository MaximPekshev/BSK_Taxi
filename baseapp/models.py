from django.db import models

import uuid

def get_uuid():
	return str(uuid.uuid4().fields[0])

class Driver(models.Model):

	first_name		= models.CharField(max_length = 30, verbose_name = 'Имя')
	second_name		= models.CharField(max_length = 30, verbose_name = 'Фамилия')
	third_name		= models.CharField(max_length = 30, verbose_name = 'Отчество', blank=True, null=True)

	slug 			= models.SlugField(max_length=10, verbose_name='Url', blank=True, null=True, db_index=True)
	
	debt			= models.DecimalField(verbose_name = 'Долг', max_digits=15, decimal_places=2)



	def __str__(self):

		return self.second_name

	def save(self, *args, **kwargs):

		if self.slug == "":
			self.slug = get_uuid()
		super(Driver, self).save(*args, **kwargs)
			
	
	class Meta:
		verbose_name = 'Водитель'
		verbose_name_plural = 'Водители'



class  Working_day(models.Model):

	
	driver 		= models.ForeignKey(Driver, on_delete=models.PROTECT)

	date 		= models.DateField('Дата рабочего дня', auto_now_add = False)

	rate		= models.DecimalField(verbose_name = 'Ставка', max_digits=15, decimal_places=2)
	fuel		= models.DecimalField(verbose_name = 'ГСМ', max_digits=15, decimal_places=2)
	penalties	= models.DecimalField(verbose_name = 'Штрафы', max_digits=15, decimal_places=2)

	cash		= models.DecimalField(verbose_name = 'Наличные', max_digits=15, decimal_places=2)
	cashless	= models.DecimalField(verbose_name = 'Безналичные', max_digits=15, decimal_places=2)

	debt_of_day	= models.DecimalField(verbose_name = 'Долг дня', max_digits=15, decimal_places=2)

	slug 		= models.SlugField(max_length=10, verbose_name='Url', blank=True, null=True, db_index=True)


	def __str__(self):
		
		return self.slug


	def save(self, *args, **kwargs):
		
		if self.slug == "":
			self.slug = get_uuid()
		super(Working_day, self).save(*args, **kwargs)


	class Meta:
		
		verbose_name = 'Рабочий день'
		verbose_name_plural = 'Рабочие дни'