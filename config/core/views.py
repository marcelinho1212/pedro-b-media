from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from leads.forms import LeadForm
from .models import Portfolio, PortfolioPhoto


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def packages(request):
    return render(request, "packages.html")


def projects(request):
    return render(request, "custom_projects.html")


def portfolio(request):
    videos = Portfolio.objects.all().order_by("-created_at")
    photos = PortfolioPhoto.objects.all().order_by("-created_at")

    return render(request, "portfolio.html", {
        "videos": videos,
        "photos": photos
    })


def contact(request):
    form = LeadForm()
    success = False

    if request.method == "POST":
        form = LeadForm(request.POST)

        if form.is_valid():
            lead = form.save()

            subject = f"New service request from {lead.full_name}"
            message = (
                f"New service request received.\n\n"
                f"Full Name: {lead.full_name}\n"
                f"Email: {lead.email}\n"
                f"Service: {lead.service}\n"
                f"Message: {lead.message}\n"
            )

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )

            form = LeadForm()
            success = True

    return render(
        request,
        "contact.html",
        {
            "form": form,
            "success": success,
        },
    )