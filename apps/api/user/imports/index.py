from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.http import JsonResponse
from ...helpers.status_code.index import status_codes
import os
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.contrib.auth import authenticate
from ...helpers.request_data.index import *
from django.core.exceptions import ValidationError
import json
from datetime import datetime, timedelta
from random import choices
from django.core.exceptions import ObjectDoesNotExist
from ...helpers.validations.email_username import *