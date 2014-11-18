from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import DistributionRequestForm

@api_view(['POST'])
def handle_post(request):
    response = {'status': 'error'}
    status_code = 400
    data = request.DATA
    data.update({
        'name': request.user.get_full_name(),
        'email': request.user.email,
        'username': request.user.username,
    })
    data.setdefault('vidzios', None)
    vidzios = data['vidzios']
    del data['vidzios']

    form = DistributionRequestForm(data=data)
    if form.is_valid():
        dr = form.save()
        response['status'] = 'success'
        status_code = 200

        if vidzios:
            ct = ContentType.objects.get_by_natural_key(app_label=settings.COLLECTFORM_RELATED_MODEL[0], model=settings.COLLECTFORM_RELATED_MODEL[1])
            for vidzio_id in vidzios:
                dr.vidzios.create(**{
                    'content_type': ct,
                    'object_id': vidzio_id,
                })
    else:
        response['errors'] = form.errors
    return Response(response, status=status_code)
