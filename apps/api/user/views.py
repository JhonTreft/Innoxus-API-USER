from .imports.index import *
# Create your views here.

@csrf_exempt
@require_POST
def login(request):
    try:
        data = json.loads(request.body.decode('utf-8'))

        if not data:
            return JsonResponse({'message': 'No se recibieron datos'}, status=status_codes["Bad_Request"])

        username = data.get('username')
        #email = data.get('email')
        password = data.get('password')

        # Validator
        validator = LoginValidator({'username': username, 'password': password})
        status_validation = validator.validate()
        
        print(status_validation)

        if status_validation:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                expiration_date = datetime.utcnow() + timedelta(days=15)
                
                instance_user = User.objects.get(username=username)
                # Crear el payload del token
                token_payload = {
                    'email': instance_user.email,
                    'exp': expiration_date
                }
                    
                # Codificar el token con la expiración
                token = jwt.encode(token_payload, str(os.getenv('SECRET_KEY')), algorithm='HS256')

                # Check token expiration
                try:
                    payload = jwt.decode(token, str(os.getenv('SECRET_KEY')), algorithms=['HS256'])
                except jwt.ExpiredSignatureError:
                    # If token has expired, refresh it
                    new_token = refresh_token(request)
                    return new_token
                
                return JsonResponse({'token': token, 'status_code': status_codes["OK"],'email':user.email,'username':user.username},status=status_codes["OK"])
            else:
                return JsonResponse({'error': 'Credenciales inválidas','status_code':status_codes["Unauthorized"]}, status=status_codes["Unauthorized"])
        else:
            return JsonResponse({'message': 'No pasó la validación', 'status': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])

    except json.decoder.JSONDecodeError as e:
        return JsonResponse({'error': 'Error al decodificar JSON', 'details': str(e),'status_code':status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])

    except Exception as e:
        return JsonResponse({'error': 'Ha ocurrido un error', 'details': str(e),'status_code':status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])



@csrf_exempt
@require_POST
def register(request):
    try:
        data = json.loads(request.body.decode('utf-8'))

        if data:
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            
            #validator
            validator = RegisterValidator({'username':username,'email': email, 'password': password})
            status_validation = validator.validate()
            
            if status_validation:
                # Verificar si el usuario ya existe
                existing_user = get_user_by_email(email)
                existing_username = get_user_by_username(username)
                
                print(existing_username)
                
                if existing_username is not None:
                    return JsonResponse({'error':'Username already exists','status_code':status_codes["Already"]}, status=status_codes["Already"])
                
                if existing_user is not None:
                    return JsonResponse({'error': 'Email already exists','status_code':status_codes["Already"]},  status=status_codes["Already"])
                else:
                    user = User.objects.create_user(username=username, password=password,email=email)

                    return JsonResponse({'message':'User registered successfully','status_code':status_codes["OK"]})
            else:
                return JsonResponse({'message': 'No pasó la validación', 'status': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])

    except ValidationError as e:
        # Manejar la validación fallida
        return JsonResponse({'message': str(e), 'status': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])

    except Exception as e:
        # Manejar otras excepciones no controladas
        return JsonResponse({'message': 'Ha ocurrido un error: ' + str(e), 'status': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])

@csrf_exempt
def refresh_token(request):
    token = request.META.get('HTTP_AUTHORIZATION')

    if not token or 'Bearer ' not in token:
        return JsonResponse({'error': 'Token not provided'}, status=status_codes["Unauthorized"])

    try:
        # Obtener el token real eliminando 'Bearer ' del encabezado
        token = token.split(' ')[1]

        # Decodificar el token existente para obtener los datos del payload
        payload = jwt.decode(token, str(os.getenv('SECRET_KEY')), algorithms=['HS256'])

        # Definir la fecha de expiración del nuevo token (1 día más desde ahora)
        expiration_date = datetime.utcnow() + timedelta(days=15)

        # Crear el payload del nuevo token
        token_payload = {
            'email': payload['email'],
            'exp': expiration_date.timestamp()
        }

        # Crear el nuevo token con el nuevo payload y devolverlo en la respuesta
        new_token = jwt.encode(token_payload, str(os.getenv('SECRET_KEY')), algorithm='HS256')
        
        return JsonResponse({'token': new_token})
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token expired'}, status=status_codes["Unauthorized"])
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Invalid token'}, status=status_codes["Unauthorized"])
    
