#!/usr/bin/env python -Wall

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import django_website.settings
from django.core.management import execute_manager
execute_manager(django_website.settings)