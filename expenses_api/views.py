from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .seriliazers import ExpenseTableSerializer
from .models import ExpenseTable

# Create your views here.
class Expenses(viewsets.ViewSet):
    def list(self,request):
        exp = ExpenseTable.objects.all()
        serializer = ExpenseTableSerializer(exp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = ExpenseTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Record inserted'}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors)

    def retrieve(self,request,pk):
        try:
            exp = ExpenseTable.objects.get(pk=pk)
        except ExpenseTable.DoesNotExist:
            return Response({'msg':'Record not found...'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseTableSerializer(exp)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self,request,pk):
        exp = ExpenseTable.objects.get(pk=pk)
        serializer = ExpenseTableSerializer(exp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(serializer.errors)

    def destroy(self,request,pk):
        try:
            exp = ExpenseTable.objects.get(pk=pk)
        except ExpenseTable.DoesNotExist:
            return Response({'msg':'Record not found...'}, status=status.HTTP_404_NOT_FOUND)

        exp.delete()
        return Response({'msg':'Record deleted'}, status=status.HTTP_204_NO_CONTENT)


# class AllExpenses(ListCreateAPIView):
#     queryset = ExpenseTable.objects.using('expenses')
#     serializer_class = ExpenseTableSerializer
#
#
# class SingleExpense(RetrieveUpdateDestroyAPIView):
#     queryset = ExpenseTable.objects.using('expenses')
#     serializer_class = ExpenseTableSerializer

