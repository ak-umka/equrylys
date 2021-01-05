from django.contrib import admin

from core.models import sdacha_Otcheta_tech_Nadzora, Talon_Cmp, Zakazchik, Generalnyi_podryadchik, Subpodryadnye_org, General_proek, Org_avtor, Gotovnost_obj, calendar_graphic, \
    sostoyanie_ispolnitelno, soderzhanie, ITR_sostav, izmenenie_v_proekte, vydannie_zamechanie, expert_tech, primichanie


@admin.register(sdacha_Otcheta_tech_Nadzora)
class SdachaCategory(admin.ModelAdmin):
    list_display = ('otchetnyi_organ', 'raion', 'Nazvanie_obj', 'Address')
    list_display_links = ('otchetnyi_organ', 'raion', 'Nazvanie_obj', 'Address')

@admin.register(Talon_Cmp)
class TalonCategory(admin.ModelAdmin):
    list_display = ('Nomer_uvedomlenye', 'data_uvedomlenye', 'uroven_otvetstvennosti', 'istochnik_finansirovanya')
    list_display_links = ('Nomer_uvedomlenye', 'data_uvedomlenye', 'uroven_otvetstvennosti', 'istochnik_finansirovanya')

@admin.register(Zakazchik)
class ZakazchikCategory(admin.ModelAdmin):
    list_display = ('BIN', 'Name')
    list_display_links = ('BIN', 'Name')

@admin.register(Generalnyi_podryadchik)
class GeneralnyiCategory(admin.ModelAdmin):
    list_display = ('BIN', 'Name')
    list_display_links  = ('BIN', 'Name')

@admin.register(Subpodryadnye_org)
class SubpodryadnyeCategory(admin.ModelAdmin):
    list_display = ('BIN', 'Name')
    list_display_links  = ('BIN', 'Name')

@admin.register(General_proek)
class GeneralCategory(admin.ModelAdmin):
    list_display = ('BIN', 'Name')
    list_display_links  = ('BIN', 'Name')
    

@admin.register(Org_avtor)
class OrgCategory(admin.ModelAdmin):
    list_display = ('BIN', 'Name')
    list_display_links  = ('BIN', 'Name')
    
@admin.register(Gotovnost_obj)
class GotovnostCategory(admin.ModelAdmin):
    list_display = ('common', 'fundament', 'carcas', 'crovlya', 'ingener_net', 'otdel', 'salbotochnye', 'blagoustr')
    list_display_links = ('common', 'fundament', 'carcas', 'crovlya', 'ingener_net', 'otdel', 'salbotochnye', 'blagoustr')

@admin.register(calendar_graphic)
class calendarCategory(admin.ModelAdmin):
    list_display_list = ('attending')
    list_display_list_links = ('attending')

@admin.register(sostoyanie_ispolnitelno)
class sostoyanieCategory(admin.ModelAdmin):
    list_display_list = ('attending')
    list_display_list_links = ('attending')

@admin.register(soderzhanie)
class soderzhanieCategory(admin.ModelAdmin):
    list_display = ('passport', 'ograzhdenie', 'moika', 'bunker', 'tverdie', 'ohrana')
    list_display_links = ('passport', 'ograzhdenie', 'moika', 'bunker', 'tverdie', 'ohrana')

@admin.register(ITR_sostav)
class ITR_Category(admin.ModelAdmin):
    list_display = ('IIN', 'familya', 'name', 'otchestvo', 'specializacia', 'nomer_attestata', 'data_attestata', 'attestacionnyi_center', 'BIN', 'name_org')
    list_display_links = ('IIN', 'familya', 'name', 'otchestvo', 'specializacia', 'nomer_attestata', 'data_attestata', 'attestacionnyi_center', 'BIN', 'name_org')

@admin.register(izmenenie_v_proekte)
class izmenenieCategory(admin.ModelAdmin):
    list_display = ('sut_izmenenie', 'osnovanie', 'data_soglasovaine', 'result_sogl')
    list_display_links = ('sut_izmenenie', 'osnovanie', 'data_soglasovaine', 'result_sogl')

@admin.register(vydannie_zamechanie)
class vydannieCategory(admin.ModelAdmin):
    list_display = ('zamechanie', 'date_vydachi', 'date_ustranenie', 'neobhodimie_mery', 'status', 'photo')
    list_display_links = ('zamechanie', 'date_vydachi', 'date_ustranenie', 'neobhodimie_mery', 'status', 'photo')

@admin.register(expert_tech)
class expertCategory(admin.ModelAdmin):
    list_display = ('IIN', 'FIO')
    list_display_links = ('IIN', 'FIO')
    
@admin.register(primichanie)
class primichanieCategory(admin.ModelAdmin):
    list_display = ('primichanie', 'image')
    list_display_links = ('primichanie', 'image')
    




    

    

    

