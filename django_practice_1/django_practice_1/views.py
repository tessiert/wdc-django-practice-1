from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    response = HttpResponse('Hello World')
    return response


# Use /date URL
def current_date(request):
    """
        Return a string with current date.
        e.g.: 'Today is 5, January 2018'
    """
    date_string = 'Today is {}'.format(datetime.strftime(datetime.now(), '%d, %B %Y'))
    response = HttpResponse(date_string)
    return response


def _zero_pad(in_string):
    if len(in_string) == 1:
        return '0' + in_string
    else:
        return in_string


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        e.g.: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    birth_date = datetime.strptime(str(year) + _zero_pad(str(month)) + _zero_pad(str(day)), '%Y%m%d')
    elapsed_days = (datetime.now() - birth_date).days 
    age_in_years = str(elapsed_days // 365)  # Use floor division to find age in years
    age_string = 'Your age is {age} years old'.format(age=age_in_years)
    return HttpResponse(age_string)


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    birth_month_and_day = birthday[5:]  #MM-DD
    current_year = str(datetime.now().year)
    next_birthday = datetime.strptime(current_year + birth_month_and_day, '%Y%m-%d')

    days_remaining = (next_birthday - datetime.now()).days

    if days_remaining < 0:
        days_remaining += 365

    return HttpResponse('Days until next birthday: {}'.format(days_remaining))


# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    pass



"""
    The goal for next task is to practice routing between two URLs.
    You will have:
        - /authors --> contains a list of Authors (template is provided to you)
        - /author/<authors_last_name> --> contains the detail for given author,
        using the AUTHORS_INFO provided below.

    First view just have to render the given 'authors.html' template sending the
    AUTHORS_INFO as context.

    Second view has to take the authors_last_name provided in the URL, look for
    for the proper author info in the dictionary, and send it as context while
    rendering the 'author.html' template. Make sure to complete the given
    'author.html' template with the data that you send.
"""
AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
    }
}

# Use provided URLs, don't change them
def authors(request):
    pass


def author(request, authors_last_name):
    pass
