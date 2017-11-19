from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponseRedirect

from booking.models import Booking
from booking.forms import BookingCreateForm


class HomeView(TemplateView):
    template_name = "home.html"


class BookingChartView(View):
    template_name = "booking_chart.html"

    def get(self, request, *args, **kwargs):
        queryset = Booking.alive_objects.all()
        date = self.request.GET.get('datepick')

        if date:
            data = queryset.filter(Q(book_date=date))
        else:
            data = queryset.filter(Q(book_date=str(timezone.now().date())))

        booking_list = []

        # 해당 호수에 예약이 없어도 row는 존재해야 하기 때문에 빈 값을 넣어준다.
        booking_list.append(['310호', '', '', 'new Date(0,0,0,9,0)', 'new Date(0,0,0,9,0)'])
        booking_list.append(['311호', '', '', 'new Date(0,0,0,9,0)', 'new Date(0,0,0,9,0)'])
        booking_list.append(['312호', '', '', 'new Date(0,0,0,9,0)', 'new Date(0,0,0,9,0)'])
        booking_list.append(['313호', '', '', 'new Date(0,0,0,9,0)', 'new Date(0,0,0,9,0)'])
        booking_list.append(['314호', '', '', 'new Date(0,0,0,9,0)', 'new Date(0,0,0,9,0)'])
        booking_list.append(['315호', '', '', 'new Date(0,0,0,9,0)', 'new Date(0,0,0,9,0)'])
        booking_list.append(['316호', '', '', 'new Date(0,0,0,9,0)', 'new Date(0,0,0,9,0)'])

        for i in data:
            start = "new Date(0,0,0," + str(i.start_hour) + "," + str(i.start_min) + ")"
            end = "new Date(0,0,0," + str(i.end_hour) + "," + str(i.end_min) + ")"
            booking_list.append([i.room.room_number+"호", i.user.name, '', start, end])

        return render(request, self.template_name, {'booking_list': booking_list})


class BookingCreateView(FormView, LoginRequiredMixin):
    form_class = BookingCreateForm
    template_name = "booking_add.html"
    success_url = "/booking/charts/"

    def form_valid(self, form):
        new_booking = form.save(commit=False)
        new_booking.save()

        return super(BookingCreateView, self).form_valid(form)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'booking_delete.html'

    def get_object(self, queryset=None):
        return Booking.alive_objects.get(id=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        if 'cancel' not in request.POST.keys():
            delete_booking = Booking.alive_objects.get(id=self.kwargs['pk'])
            delete_booking.is_delete = True
            delete_booking.delete_date = timezone.now()
            delete_booking.save()

        # 마이페이지로 redirect하려고 했는데 없어서 임시로 보냄
        return HttpResponseRedirect('/booking/charts/')


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BookingCreateForm
    template_name = 'booking_update.html'
    success_url = '/booking/charts/'  # 임시

    def get_object(self, queryset=None):
        return Booking.alive_objects.get(id=self.kwargs['pk'])

    def form_valid(self, form):
        update_digger = form.save(commit=False)
        update_digger.save()

        return super(BookingUpdateView, self).form_valid(form)
