from django.core.exceptions import ValidationError

def validate_cuit(value):
    """
    Custom validator to ensure the cuit field has exactly 11 digits.
    """
    if len(value) != 11:
        raise ValidationError('El campo "cuit" debe tener exactamente 11 dígitos.')

    # You can add additional validation logic here, if needed (e.g., check for specific digit patterns)