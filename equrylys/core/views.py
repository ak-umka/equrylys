from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import generics, filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from core.models import sdacha_Otcheta_tech_Nadzora, Talon_Cmp, Zakazchik, Generalnyi_podryadchik, Subpodryadnye_org, General_proek, Org_avtor, Gotovnost_obj, calendar_graphic, \
    sostoyanie_ispolnitelno, soderzhanie, ITR_sostav, izmenenie_v_proekte, vydannie_zamechanie, expert_tech, primichanie

from core.serializers import SdachaSerializer, TalonSerializer, ZakazchikSerializer, GeneralnyiSerializer,  SubpodryadnyeSerializer, GeneralSerializer, \
    OrgSerializer, GotovnostSerializer, calendarSerializer, sostoyanieSerializer, soderzhanieSerializer, ITRSerializer, izmenenieSerializer, vydannieSerializer, \
    expertSerializer, primichanieSerializer, UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer


### SdachaViewSet в этом сериалайзере у каждого пользователя будет свой API и они могут просматривать только свои данные
class SdachaViewSet(ModelViewSet):
    serializer_class = SdachaSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return sdacha_Otcheta_tech_Nadzora.objects.filter(owner=self.request.user)

###serializer.save(owner=self.request.user) АВТОМАТИЧЕСКИ ПОЛУЧАЕТ owner

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(SdachaViewSet, self).perform_create(serializer)

 
    
class TalonViewSet(ModelViewSet):
    serializer_class = TalonSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return Talon_Cmp.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(TalonViewSet, self).perform_create(serializer)

class ZakazchikViewSet(ModelViewSet):
    serializer_class = ZakazchikSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return Zakazchik.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(ZakazchikViewSet, self).perform_create(serializer)

class GeneralnyiViewSet(ModelViewSet):
    serializer_class = GeneralnyiSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return Generalnyi_podryadchik.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(GeneralnyiViewSet, self).perform_create(serializer)

class SubpodryadnyeViewSet(ModelViewSet):
    serializer_class = SubpodryadnyeSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return Subpodryadnye_org.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(SubpodryadnyeViewSet, self).perform_create(serializer)

class GeneralViewSet(ModelViewSet):
    serializer_class = GeneralSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return General_proek.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(GeneralViewSet, self).perform_create(serializer)

class OrgViewSet(ModelViewSet):
    serializer_class = OrgSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return Org_avtor.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(OrgViewSet, self).perform_create(serializer)

class GotovnostViewSet(ModelViewSet):
    serializer_class = GotovnostSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return Gotovnost_obj.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(GotovnostViewSet, self).perform_create(serializer)

class calendarViewSet(ModelViewSet):
    serializer_class = calendarSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return calendar_graphic.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(calendarViewSet, self).perform_create(serializer)

class sostoyanieViewSet(ModelViewSet):
    serializer_class = sostoyanieSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return sostoyanie_ispolnitelno.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(sostoyanieViewSet, self).perform_create(serializer)

class soderzhanieViewSet(ModelViewSet):
    serializer_class = soderzhanieSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return soderzhanie.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(soderzhanieViewSet, self).perform_create(serializer)

class ITRViewSet(ModelViewSet):
    serializer_class = ITRSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return ITR_sostav.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(ITRViewSet, self).perform_create(serializer)

class izmenenieViewSet(ModelViewSet):
    serializer_class = izmenenieSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return izmenenie_v_proekte.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(izmenenieViewSet, self).perform_create(serializer)

class vydannieViewSet(ModelViewSet):
    serializer_class = vydannieSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return vydannie_zamechanie.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(vydannieViewSet, self).perform_create(serializer)

class expertViewSet(ModelViewSet):
    serializer_class = expertSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return expert_tech.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(expertViewSet, self).perform_create(serializer)

class primichanieViewSet(ModelViewSet):
    serializer_class = primichanieSerializer
    permission_classes=[IsAuthenticated, ]


    def get_queryset(self):
        return primichanie.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.validated_data.owner = self.request.user
        super(primichanieViewSet, self).perform_create(serializer)