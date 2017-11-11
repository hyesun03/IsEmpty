from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.http import HttpResponse
from booking.models import Booking


class HomeView(TemplateView):
    template_name = "home.html"


class BookingChartView(TemplateView):
    template_name = "booking_chart.html"

