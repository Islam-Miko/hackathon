from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['POST'])
def student_registration(request):
    pass
    # if request.method == 'POST':
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True)
