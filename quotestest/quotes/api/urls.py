from django.urls import path
from quotes.api.views import QuoteCreateAPIView, QuoteDetailAPIView

urlpatterns = [
    path("quotes/", QuoteCreateAPIView.as_view(), name="quote-list"),
    path("quotes/<int:pk>", QuoteDetailAPIView.as_view(), name="quote-detail")
]
