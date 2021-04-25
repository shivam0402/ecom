

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

from ..models import OrderItem,Order,ShippingAddress,Product

from ..serializers import OrderSerializer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user=request.user
    data=request.data

    orderItems=data['orderItems']

    print(user)
    print(data)

    if orderItems and len(orderItems) == 0:
        return Response({'details : No order items'},status=status.HTTP_400_BAD_REQUEST)
    else :
        order=Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice']
        )


        shippingAddress=ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city =data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['postalcode'],
            country=data['shippingAddress']['country'],

        )


        for i in orderItems :
            print(i)
            product=Product.objects.get(_id=i['product'])

            item=OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                image=product.image,
                qty=i['qty'],
                price=i['price']


            )

            product.countInStock -= item.qty
            product.save()

        serializer=OrderSerializer(order,many=False)

        return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrder(request,pk):
    user=request.user

    try:
        order = Order.objects.get(_id=pk)
        # print(order)
        # print(order.user)
        # print(user.is_staff)
        if user.is_staff or order.user == user :
            serializer = OrderSerializer(order,many=False)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response({'details ':'Not Authorized to view this Order'},status.HTTP_400_BAD_REQUEST)
    except:
        return  Response({'details ':'Order Does not exist'},status.HTTP_400_BAD_REQUEST)