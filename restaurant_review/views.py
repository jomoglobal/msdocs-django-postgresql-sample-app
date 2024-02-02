#ORIGINAL CODE:
# from django.db.models import Avg, Count
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.utils import timezone
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.cache import cache_page

# from restaurant_review.models import Restaurant, Review

# # Create your views here.

# def index(request):
#     print('Request for index page received')
#     restaurants = Restaurant.objects.annotate(avg_rating=Avg('review__rating')).annotate(review_count=Count('review'))
#     lastViewedRestaurant = request.session.get("lastViewedRestaurant", False)
#     return render(request, 'restaurant_review/index.html', {'LastViewedRestaurant': lastViewedRestaurant, 'restaurants': restaurants})

# @cache_page(60)
# def details(request, id):
#     print('Request for restaurant details page received')
#     restaurant = get_object_or_404(Restaurant, pk=id)
#     request.session["lastViewedRestaurant"] = restaurant.name
#     return render(request, 'restaurant_review/details.html', {'restaurant': restaurant})


# def create_restaurant(request):
#     print('Request for add restaurant page received')
#     return render(request, 'restaurant_review/create_restaurant.html')


# @csrf_exempt
# def add_restaurant(request):
#     try:
#         name = request.POST['restaurant_name']
#         street_address = request.POST['street_address']
#         description = request.POST['description']
#     except (KeyError):
#         # Redisplay the form
#         return render(request, 'restaurant_review/add_restaurant.html', {
#             'error_message': "You must include a restaurant name, address, and description",
#         })
#     else:
#         restaurant = Restaurant()
#         restaurant.name = name
#         restaurant.street_address = street_address
#         restaurant.description = description
#         Restaurant.save(restaurant)

#         return HttpResponseRedirect(reverse('details', args=(restaurant.id,)))


# @csrf_exempt
# def add_review(request, id):
#     restaurant = get_object_or_404(Restaurant, pk=id)
#     try:
#         user_name = request.POST['user_name']
#         rating = request.POST['rating']
#         review_text = request.POST['review_text']
#     except (KeyError):
#         # Redisplay the form.
#         return render(request, 'restaurant_review/add_review.html', {
#             'error_message': "Error adding review",
#         })
#     else:
#         review = Review()
#         review.restaurant = restaurant
#         review.review_date = timezone.now()
#         review.user_name = user_name
#         review.rating = rating
#         review.review_text = review_text
#         Review.save(review)

#     return HttpResponseRedirect(reverse('details', args=(id,)))




# #UPDATE#1 - UPDATED CODE:
# from django.shortcuts import render
# from .models import AzurePricing

# # Create your views here.

# def index(request):
#     # For example, you might want to display all AzurePricing entries on the index page
#     pricing_data = AzurePricing.objects.all()
#     return render(request, 'restaurant_review/index.html', {'pricing_data': pricing_data})

# # You can create additional views that pertain to your AzurePricing model as needed




# #UPDATE#2 - ADDING LOGGING
# import logging
# from django.shortcuts import render
# from .models import AzurePricing

# # Get an instance of a logger
# logger = logging.getLogger(__name__)

# def index(request):
#     logger.debug('Request for index page received')
#     pricing_data = AzurePricing.objects.all()
#     logger.debug(f'Loaded {pricing_data.count()} AzurePricing records')
#     return render(request, 'restaurant_review/index.html', {'pricing_data': pricing_data})



#UPDATE#3 - ADDED EXCEPTION HANDLING
import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import AzurePricing

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    try:
        logger.debug('Request for index page received')
        pricing_data = AzurePricing.objects.all()
        logger.debug(f'Loaded {pricing_data.count()} AzurePricing records')
        return render(request, 'restaurant_review/index.html', {'pricing_data': pricing_data})
    except Exception as e:
        # Log the error and return an error message
        logger.error('Error in index view: %s', str(e), exc_info=True)
        # If DEBUG is True, you'll see the traceback of the error in your browser
        # Otherwise, you'll see a generic 500 error page
        return HttpResponse(f'Error in index view: {e}', status=500)
