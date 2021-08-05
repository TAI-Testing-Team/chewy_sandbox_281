'''
This script swipes up until a label is found for a default max of 10 swipes, you can modify as needed.
Available swipe actions are: swipe_up, swipe_down, swipe_left, swipe_right.
Replace 4 labeled_element and 3 lnk_about items wit your values.
You can set the start_x, start_y, end_x, end_y values.
The duration is how long the swipe will take from the start to the end point, larger number is a slower swipe.
'''

import logging
import time
import os

log = logging.getLogger(__name__)

MAX_SWIPES = 10


def run(context):
    labeled_element = False
    attempts = 0

    labeled_element = element_exists(context, 'lnk_about')
    
    while not labeled_element and attempts <= MAX_SWIPES:
        attempts += 1
        context.perform_gesture('swipe_up', '')
        labeled_element = element_exists(context, 'lnk_about')

    context.verify(['lnk_about'])


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0

