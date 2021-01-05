from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


from core.models import sdacha_Otcheta_tech_Nadzora, Talon_Cmp, Zakazchik, Generalnyi_podryadchik, Subpodryadnye_org, General_proek, Org_avtor, Gotovnost_obj, calendar_graphic, \
    sostoyanie_ispolnitelno, soderzhanie, ITR_sostav, izmenenie_v_proekte, vydannie_zamechanie, expert_tech, primichanie



class UserSerializer(ModelSerializer):
    sdacha = serializers.PrimaryKeyRelatedField(many=True, queryset = sdacha_Otcheta_tech_Nadzora.objects.all)
    talon = serializers.PrimaryKeyRelatedField(many=True, queryset = Talon_Cmp.objects.all)
    zakazchik = serializers.PrimaryKeyRelatedField(many=True, queryset = Zakazchik.objects.all)
    generalnyi_podryadchik = serializers.PrimaryKeyRelatedField(many=True, queryset = Generalnyi_podryadchik.objects.all)
    subpodryadnye_org = serializers.PrimaryKeyRelatedField(many=True, queryset = Subpodryadnye_org.objects.all)
    general_proek = serializers.PrimaryKeyRelatedField(many=True, queryset = General_proek.objects.all)
    org_avtor = serializers.PrimaryKeyRelatedField(many=True, queryset = Org_avtor.objects.all)
    gotovnost_obj = serializers.PrimaryKeyRelatedField(many=True, queryset = Gotovnost_obj.objects.all)
    calendar_graphic = serializers.PrimaryKeyRelatedField(many=True, queryset = calendar_graphic.objects.all)
    sostoyanie_ispolnitelno = serializers.PrimaryKeyRelatedField(many=True, queryset = sostoyanie_ispolnitelno.objects.all)
    soderzhanie = serializers.PrimaryKeyRelatedField(many=True, queryset = soderzhanie.objects.all)
    itr_sostav = serializers.PrimaryKeyRelatedField(many=True, queryset = ITR_sostav.objects.all)
    izmenenie_v_proekte = serializers.PrimaryKeyRelatedField(many=True, queryset = izmenenie_v_proekte.objects.all)
    vydannie_zamechanie = serializers.PrimaryKeyRelatedField(many=True, queryset = vydannie_zamechanie.objects.all)
    expert_tech = serializers.PrimaryKeyRelatedField(many=True, queryset = expert_tech.objects.all)
    primichanie = serializers.PrimaryKeyRelatedField(many=True, queryset = primichanie.objects.all)
    
    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = "__all__"


class SdachaSerializer(serializers.ModelSerializer):
    class Meta:
        model = sdacha_Otcheta_tech_Nadzora
        fields = ['otchetnyi_organ', 'raion', 'Nazvanie_obj', 'Address']


class TalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talon_Cmp
        fields = ['Nomer_uvedomlenye', 'data_uvedomlenye', 'uroven_otvetstvennosti', 'istochnik_finansirovanya']
        

class ZakazchikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zakazchik
        fields = ['BIN', 'Name']

class GeneralnyiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generalnyi_podryadchik
        fields = ['BIN', 'Name']

class SubpodryadnyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subpodryadnye_org
        fields = ['BIN', 'Name']

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General_proek
        fields = ['BIN', 'Name']

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org_avtor
        fields = ['BIN', 'Name']


class GotovnostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gotovnost_obj
        fields = ['common', 'fundament', 'carcas', 'crovlya', 'ingener_net', 'otdel', 'salbotochnye', 'blagoustr']

class calendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = calendar_graphic
        fields = ['attending']
        


class sostoyanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = sostoyanie_ispolnitelno
        fields = ['attending']

        
class soderzhanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = soderzhanie
        fields = ['passport', 'ograzhdenie', 'moika', 'bunker', 'tverdie', 'ohrana']

class ITRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITR_sostav
        fields = ['IIN', 'familya', 'name', 'otchestvo', 'specializacia', 'nomer_attestata', 'data_attestata', 'attestacionnyi_center', 'BIN', 'name_org']

class izmenenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = izmenenie_v_proekte
        fields = ['sut_izmenenie', 'osnovanie', 'data_soglasovaine', 'result_sogl']


class vydannieSerializer(serializers.ModelSerializer):
    class Meta:
        model = vydannie_zamechanie
        fields = fields = ['zamechanie', 'date_vydachi', 'date_ustranenie', 'neobhodimie_mery', 'status', 'photo']


class expertSerializer(serializers.ModelSerializer):
    class Meta:
        model = expert_tech
        fields = fields = ['IIN', 'FIO']


class primichanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = primichanie
        fields = fields = ['primichanie', 'image']

