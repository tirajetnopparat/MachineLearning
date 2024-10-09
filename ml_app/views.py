from django.shortcuts import render
from .model import model

def predict(request):
    prediction_text = None  # Initialize prediction_text as None

    if request.method == 'POST':
        input_data = {
            'Age': int(request.POST.get('Age')),
            'Gender': int(request.POST.get('Gender')),
            'self_employed': int(request.POST.get('self_employed')),
            'family_history': int(request.POST.get('family_history')),
            'work_interfere': int(request.POST.get('work_interfere')),
            'remote_work': int(request.POST.get('remote_work')),
            'benefits': int(request.POST.get('benefits')),
            'wellness_program': int(request.POST.get('wellness_program')),
            'seek_help': int(request.POST.get('seek_help')),
            'mental_health_consequence': int(request.POST.get('mental_health_consequence')),
            'phys_health_consequence': int(request.POST.get('phys_health_consequence')),
            'coworkers': int(request.POST.get('coworkers')),
            'supervisor': int(request.POST.get('supervisor')),
        }

        input_values = [
            input_data['Age'],
            input_data['Gender'],
            input_data['self_employed'],
            input_data['family_history'],
            input_data['work_interfere'],
            input_data['remote_work'],
            input_data['benefits'],
            input_data['wellness_program'],
            input_data['seek_help'],
            input_data['mental_health_consequence'],
            input_data['phys_health_consequence'],
            input_data['coworkers'],
            input_data['supervisor'],
        ]

        prediction = model.predict([input_values])
        prediction_result = int(prediction[0])

        # Convert the prediction result to "Yes" or "No"
        prediction_text = "ควรเข้ารับการรักษา" if prediction_result == 1 else "ไม่จำเป็น"

    # Render the form and pass the prediction result to the template
    return render(request, 'predict.html', {'prediction': prediction_text})
