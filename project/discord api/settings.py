INSTALLED_APPS += [
    "rest_framework",
    "rest_framework_simplejwt",
    "api",
]

AUTH_USER_MODEL = "api.User"  # on crée un utilisateur custom simple



REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}
