from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator

class sdacha_Otcheta_tech_Nadzora(models.Model):
    organ_choices = (
        ('Nur-Sultan', 'Nur-Sultan'),
        ('Almaty', 'Almaty'),
        ('Akmolinskaya oblast', 'Akmolinskaya oblast'),
        ('Aktubinskaya oblast', 'Aktubinskaya oblast'),
        ('Almatinskaya oblast', 'Almatinskaya oblast'),
        ('Atyrauskaya oblast', 'Atyrauskaya oblast'),
        ('ZKO', 'ZKO'),
        ('Zhambylskaya oblast','Zhambylskaya oblast'), 
        ('Karagandinskaya oblast', 'Karagandinskaya oblast'),
        ('Kostanaiskaya oblast', 'Kostanaiskaya oblast'),
    )
    otchetnyi_organ = models.CharField(max_length=100, choices=organ_choices)

    raion_choices = (
        ('Almatinski raion', 'Almatinski raion'),
        ('Baikonurski raion', 'Baikonurski raion'),
        ('Esilski raion', 'Esilski raion'),
        ('Saryarkinski raion', 'Saryarkinski raion'),
        ('Alatauski raion', 'Alatauski raion'),
        ('Almatinski raion', 'Almatinski raion'),
        ('Auzovski raion', 'Auzovski raion'),
        ('Bostandykski raion', 'Bostandykski raion'),
        ('Zhetysuiski raion', 'Zhetysuiski raion'),
        ('Medeuski raion', 'Medeuski raion'),
        ('Naurizbayski raion', 'Naurizbayski raion')
    )
    raion = models.CharField(max_length=100, choices=raion_choices) 

    Nazvanie_obj = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='sdacha', on_delete=models.CASCADE, default=None)

class Talon_Cmp(models.Model):
    Nomer_uvedomlenye = models.IntegerField(null=False)
    data_uvedomlenye = models.DateField(auto_now=False, auto_now_add=False)
    uroven_choices = (
        ('I(povyshennogo) urovnya', '1(povyshennogo) urovnya'),
        ('II (norm) urovnya otvetstvennosty', 'II (norm) urovnya otvetstvennosty'),
        ('III (norm) urovnya otvetstvennosty, ne otnosyashyeasya k tech slozhnym', 'III (norm) urovnya otvetstvennosty, ne otnosyashyeasya k tech slozhnym'),
        ('IV (norm) urovnya otvetstvennosty', 'IV (norm) urovnya otvetstvennosty'),
    )
    uroven_otvetstvennosti = models.CharField(max_length=120, choices=uroven_choices)
    istochnik_choices = (
        ('Respublicansky byudzhet', 'Respublicansky byudzhet'),
        ('Mestny byudzhet', 'Mestny byudzhet'),
        ('Kvazhigos sector', 'Kvazhigos sector'),
        ('Chastnye inves', 'Chastnye inves'),
        ('Inostrannye inves', 'Inostrannye inves'),
    )
    istochnik_finansirovanya = models.CharField(max_length=100, choices=istochnik_choices)
    owner = models.ForeignKey('auth.User', related_name='talon', on_delete=models.CASCADE, default=None)

class Zakazchik(models.Model):
    BIN = models.IntegerField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    Name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='zakazchik', on_delete=models.CASCADE, default=None)

class Generalnyi_podryadchik(models.Model):
    BIN = models.IntegerField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    Name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='generalnyi_podryadchik', on_delete=models.CASCADE, default=None)

class Subpodryadnye_org(models.Model):
    BIN = models.IntegerField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    Name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='subpodryadnye_org', on_delete=models.CASCADE, default=None)

class General_proek(models.Model):
    BIN = models.IntegerField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    Name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='general_proek', on_delete=models.CASCADE, default=None)

class Org_avtor(models.Model):
    BIN = models.IntegerField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    Name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='org_avtor', on_delete=models.CASCADE, default=None)

class Gotovnost_obj(models.Model):
    common = models.BooleanField(default=False)
    fundament = models.BooleanField(default=False)
    carcas = models.BooleanField(default=False)
    crovlya = models.BooleanField(default=False)
    ingener_net = models.BooleanField(default=False)
    otdel = models.BooleanField(default=False)
    salbotochnye = models.BooleanField(default=False)
    blagoustr = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='gotovnost_obj', on_delete=models.CASCADE, default=None)

class calendar_graphic(models.Model):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
    )
    attending = models.BooleanField(choices=TRUE_FALSE_CHOICES)
    owner = models.ForeignKey('auth.User', related_name='calendar_graphic', on_delete=models.CASCADE, default=None)


"""from django import forms
class Form(forms.Form):
    field = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                   choices=((False, 'No'), (True, 'Yes')))

---------------OROROROROROROROR--------------

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        widgets = {
            'yes_or_no': forms.RadioSelect
        }
"""

class sostoyanie_ispolnitelno(models.Model):
    NOT_CHOICES = (
        (True, 'Vedetsya v polnom obyeme'),
        (False, 'Ne vedetsya v polnom obyeme'),
    )
    attending = models.BooleanField(choices=NOT_CHOICES)
    owner = models.ForeignKey('auth.User', related_name='sostoyanie_ispolnitelno', on_delete=models.CASCADE, default=None)


class soderzhanie(models.Model):
    PASS_CHOICES = (
        (True, 'passport sootvetstvuet'),
        (False, 'passport ne ootvetstvuet'),
    )
    passport = models.BooleanField(choices=PASS_CHOICES)

    OGRAZH_CHOICES = (
        (True, 'ograzhdenie sootvetstvuet'),
        (False, 'ograzhdenie ne ootvetstvuet'),
    )
    ograzhdenie = models.BooleanField(choices=OGRAZH_CHOICES)

    MOIKA_KOLES__CHOICES = (
        (True, 'imeetsya punkt moika koles'),
        (False, 'ootvetstvuet punkt moika koles'),
    )
    moika = models.BooleanField(choices=MOIKA_KOLES__CHOICES)

    BUNKER_CHOICES = (
        (True, 'imeetsya ustroistvo ili bunker'),
        (False, 'ootvetstvuet ustroistvo ili bunker'),
    )
    bunker = models.BooleanField(choices=BUNKER_CHOICES)

    TVERDIE_CHOICES = (
        (True, 'imeetsya tverdie pokritie'),
        (False, 'ootvetstvuet tverdie pokritie'),
    )
    tverdie = models.BooleanField(choices=TVERDIE_CHOICES)

    OHRANA_CHOICES = (
        (True, 'sobludaetsa trebovaine po ohrane truda '),
        (False, 'ne sobludaetsa trebovaine po ohrane truda'),
    )
    ohrana = models.BooleanField(choices=OHRANA_CHOICES)
    owner = models.ForeignKey('auth.User', related_name='soderzhanie', on_delete=models.CASCADE, default=None)


class ITR_sostav(models.Model):
    IIN = models.IntegerField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    familya = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otchestvo = models.CharField(max_length=50)
    specializacia = models.CharField(max_length=50)
    nomer_attestata = models.CharField(max_length=50)
    data_attestata = models.DateField(auto_now=False, auto_now_add=False)
    attestacionnyi_center = models.CharField(max_length=50)
    BIN = models.IntegerField()
    name_org = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='itr_sostav', on_delete=models.CASCADE, default=None)


class izmenenie_v_proekte(models.Model):
    sut_izmenenie = models.TextField()
    osnovanie = models.TextField()
    data_soglasovaine = models.DateField(auto_now=False, auto_now_add=False)
    result_sogl = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='izmenenie_v_proekte', on_delete=models.CASCADE, default=None)


class vydannie_zamechanie(models.Model):
    zamechanie = models.TextField()
    date_vydachi = models.DateField(auto_now=False, auto_now_add=False)
    date_ustranenie = models.DateField(auto_now=False, auto_now_add=False)
    neobhodimie_mery = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    owner = models.ForeignKey('auth.User', related_name='vydannie_zamechanie', on_delete=models.CASCADE, default=None)

class expert_tech(models.Model):
    IIN = models.IntegerField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    FIO = models.CharField(max_length=80)
    owner = models.ForeignKey('auth.User', related_name='expert_tech', on_delete=models.CASCADE, default=None)

class primichanie(models.Model):
    primichanie = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    owner = models.ForeignKey('auth.User', related_name='primichanie', on_delete=models.CASCADE, default=None)


