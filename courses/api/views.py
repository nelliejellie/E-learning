from rest_framework import generics
from ..models import Subject, Course
from .serializers import SubjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
# importing authentication for a view
from rest_framework.authentication import BasicAuthentication

# view for all the subject fields
class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# view for all the subject detail
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# view for all students enrollment
class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled':True})