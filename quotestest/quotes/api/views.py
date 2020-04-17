from rest_framework import generics
from quotes.api.serializers import QuoteSerializer
from rest_framework.permissions import IsAdminUser
from quotes.api.pagination import SmallSetPagination
from quotes.models import Quote


class QuoteCreateAPIView(generics.ListCreateAPIView):  # concrete classes which are abstracted.
    queryset = Quote.objects.all().order_by("id")
    serializer_class = QuoteSerializer
    pagination_class = SmallSetPagination


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUser]

