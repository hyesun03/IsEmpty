from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class BookingChartView(TemplateView):
    template_name = "booking_chart.html"
