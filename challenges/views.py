from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Come frutas y verduras",
    "february": "Haz ejercicio",
    "march": "Lavate los dientes",
    "april": "Haz ejercicio",
    "may": "Come frutas y verduras",
    "june": "Lavate los dientes",
    "july": "Haz ejercicio",
    "august": "Lavate los dientes",
    "september": "Come frutas y verduras",
    "october": "Lavate los dientes",
    "november": "Lavate los dientes",
    "december": "Come frutas y verduras",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}<a/></li>"

    response_data = f"""
    <ul>
        {list_items}
    </ul>
    """
    return HttpResponse(response_data)


# Create your views here.
def monthly_challenge_by_number(request, month: int):
    months = list(monthly_challenges.keys())

    if month > len(months) or month <= 0:
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str):
    try:
        challengue_text = monthly_challenges[month]
        response_data = f"<h1>{challengue_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    return HttpResponse(response_data)
