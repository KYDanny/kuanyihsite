from datetime import datetime

def current_time_context(request):
    current_time = datetime.now()
    return {'current_time': current_time}
