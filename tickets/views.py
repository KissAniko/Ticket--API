from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer

# Create your views here.


@api_view(['GET'])
def getAllTickets(request):
                allTicket = Ticket.objects.all()
                serializedTickets = TicketSerializer(allTicket, many = True)

                return Response(serializedTickets.data)

@api_view(['POST'])
def createNewTicket(request):
       
       serializer =  TicketSerializer(data = request.data)

       if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
       else:
               return Response({serializer.errors})
