from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize > 100000000000000 or filesize < 1000000 :
        raise ValidationError('your file does not meet the file size standards')

def file_sizes(value):
    filesize=value.size
    if filesize > 100000000000000 or filesize < 1000000 :
        raise ValidationError('your file does not meet the file size standards')