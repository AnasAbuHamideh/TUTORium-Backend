from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , CreateAPIView 
# for sign up
from rest_framework import viewsets
from django.contrib.auth.models import User

from mainApp.models import (
                            MainCategory,
                            Course,
                            Visitor,
                            Student,
                            Tutor,
                            PrivateTutor,
                            ContractedTutor,
                            UnavailableSlot,
                            Transaction,

)
from .Serializers import (
                            MainCategorySerializer,
                            CourseSerializer,
                            VisitorSerializer,
                            StudentSerializer,
                            TutorSerializer,
                            PrivateTutorSerializer,
                            ContractedTutorSerializer,
                            UnavailableSlotSerializer,
                            TransactionSerializer,
                            SignupSerializer,
                            LoginSerializer,
                            ) 
from .permission import IsOwnerOrReadOnly , permissions
# Catergor for cards -> list view
# when teacher post a class should choose from caterorie

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
# or IsAuthenticatedOrReadOnly

class MainCategorylist(ListCreateAPIView):
     queryset = MainCategory.objects.all()
     serializer_class = MainCategorySerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class MainCategoryRUD(RetrieveUpdateDestroyAPIView):
     queryset = MainCategory.objects.all()
     serializer_class = MainCategorySerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )



# classes 
class Courselist(ListCreateAPIView):
     queryset =  Course.objects.all()
     serializer_class =CourseSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class CourseRUD(RetrieveUpdateDestroyAPIView):
     queryset =  Course.objects.all()
     serializer_class = CourseSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class CourseCreate(CreateAPIView):
     queryset =  Course.objects.all()
     serializer_class = CourseSerializer
     


# # Visitor
# class Visitorlist(ListCreateAPIView):
#      queryset = Visitor.objects.all()
#      serializer_class =VisitorSerializer
#      permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# class VisitorRUD(RetrieveUpdateDestroyAPIView):
#      queryset =  Visitor.objects.all()
#      serializer_class = VisitorSerializer
#      permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

# class VisitorCreate(CreateAPIView):
#      queryset =  Visitor.objects.all()
#      serializer_class = VisitorSerializer
#      permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# Student 
class Studentlist(ListCreateAPIView):
     queryset = Student.objects.all()
     serializer_class =StudentSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class StudentRUD(RetrieveUpdateDestroyAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class StudentCreate(CreateAPIView):
     queryset =  Student.objects.all()
     serializer_class = StudentSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# tutor
class Tutorlist(ListCreateAPIView):
     queryset = Tutor.objects.all()
     serializer_class =TutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class TutorRUD(RetrieveUpdateDestroyAPIView):
     queryset = Tutor.objects.all()
     serializer_class = TutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class TutorCreate(CreateAPIView):
     queryset =  Tutor.objects.all()
     serializer_class = TutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# PrivateTutor
class PrivateTutorlist(ListCreateAPIView):
     queryset = PrivateTutor.objects.all()
     serializer_class =PrivateTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class PrivateTutorRUD(RetrieveUpdateDestroyAPIView):
     queryset = PrivateTutor.objects.all()
     serializer_class = PrivateTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class PrivateTutorCreate(CreateAPIView):
     queryset =  PrivateTutor.objects.all()
     serializer_class = PrivateTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )



# ContractedTutor
class ContractedTutorlist(ListCreateAPIView):
     queryset = ContractedTutor.objects.all()
     serializer_class =ContractedTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class ContractedTutorRUD(RetrieveUpdateDestroyAPIView):
     queryset = ContractedTutor.objects.all()
     serializer_class = ContractedTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class ContractedTutorCreate(CreateAPIView):
     queryset =  ContractedTutor.objects.all()
     serializer_class = ContractedTutorSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )



# UnavailableSlot
class UnavailableSlotlist(ListCreateAPIView):
     queryset = UnavailableSlot.objects.all()
     serializer_class =UnavailableSlotSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class UnavailableSlotRUD(RetrieveUpdateDestroyAPIView):
     queryset = UnavailableSlot.objects.all()
     serializer_class = UnavailableSlotSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class UnavailableSlotCreate(CreateAPIView):
     queryset =  UnavailableSlot.objects.all()
     serializer_class = UnavailableSlotSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# Transaction
class Transactionlist(ListCreateAPIView):
     queryset = Transaction.objects.all()
     serializer_class =TransactionSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


class TransactionRUD(RetrieveUpdateDestroyAPIView):
     queryset = Transaction.objects.all()
     serializer_class = TransactionSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )

class TransactionCreate(CreateAPIView):
     queryset =  Transaction.objects.all()
     serializer_class = TransactionSerializer
     permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )


# sign up
class UserViewset(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = SignupSerializer


# login
# Creating private endpoint
