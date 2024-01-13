from rest_framework import status
from django.http import JsonResponse
from .models import ShopModel,CoupounModel
from .serializers import ShopSerializer,CoupounSerializer
from rest_framework.decorators import api_view
from rest_framework import response

@api_view(['GET','POST'])
def shop_list(request):
    if(request.method =='GET'):
        shops= ShopModel.objects.all()
        serializer = ShopSerializer(shops,many=True)
        responseData={'success':True,'count':len(shops),'data':serializer.data}
        return response.Response(responseData)
    elif(request.method =='POST'):
        try:
            serializer = ShopSerializer(data=request.data)         
            if(serializer.is_valid()):               
                serializer.save()
                return response.Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           
            return response.Response({'success':False,'message':e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET','PUT','DELETE'])
def shop_detail(request,id):
    try:
        shop = ShopModel.objects.get(pk=id)
    except Exception as e:
        return response.Response({'success':False,'message':e},status=status.HTTP_404_NOT_FOUND)
    if(request.method =='GET'):
        try:
            serializer = ShopSerializer(shop)
            responseData={'success':True,'data':serializer.data}
            return response.Response(responseData)
        except Exception as e:
            return response.Response({'success':False,'message':e},status=status.HTTP_500_INTERNAL_SERVER_ERROR,)
    elif(request.method =='PUT'):
        try:
            serializer = ShopSerializer(shop,data=request.data)         
            if(serializer.is_valid()):               
                serializer.save()
                return response.Response({'success':False,'message':"created"},serializer.data,status=status.HTTP_201_CREATED)
            else:
                return response.Response({'success':False,'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_message = {'error': str(e)}
            return response.Response({'success':False,'message':serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif(request.method=='DELETE'):
        shop.delete()
        return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        
         
@api_view(['GET','POST'])
def coupoun_list(request):
    if(request.method =='GET'):
        coupouns= CoupounModel.objects.all()
        serializer = CoupounSerializer(coupouns,many=True)
        responseData={'success':True,'count':len(coupouns),'data':serializer.data}
        return response.Response(responseData)
    elif(request.method =='POST'):
        try:
            serializer = CoupounSerializer.CoupounCreateSerializer(data=request.data)     
            if(serializer.is_valid()):             
                serializer.save()
                return response.Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_message = {'error': str(e)}
            return response.Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)