from django.shortcuts import render
from joblib import load
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os
from django.shortcuts import render

model =load('./savedModels/model.joblib')

# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect(predictor)
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def predictor(request):
    return render(request, 'main.html')

def BytesToInt(b):
    return int.from_bytes(b, byteorder='big')

def formInfo(request):
    # Load the key for decryption
    with open('./Notebooks/encryption_key.txt', 'rb') as key_file:
        key = key_file.read()

    baseline_value = int(float(request.GET.get('baseline_value', 0.0)))
    baseline_value_bytes = baseline_value.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_baseline_value = BytesToInt(b64encode(cipher.encryptor().update(baseline_value_bytes)))

    accelerations = int(float(request.GET.get('fetal_movement', 0.0)))
    accelerations_bytes = accelerations.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_accelerations = BytesToInt(b64encode(cipher.encryptor().update(accelerations_bytes)))

    fetal_movement = int(float(request.GET.get('fetal_movement', 0.0)))
    fetal_movement_bytes = fetal_movement.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_fetal_movement = BytesToInt(b64encode(cipher.encryptor().update(fetal_movement_bytes)))

    uterine_contractions = int(float(request.GET.get('uterine_contractions', 0.0)))
    uterine_contractions_bytes = uterine_contractions.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_uterine_contractions = BytesToInt(b64encode(cipher.encryptor().update(uterine_contractions_bytes)))

    light_decelerations = int(float(request.GET.get('light_decelerations', 0.0)))
    light_decelerations_bytes = light_decelerations.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_light_decelerations = BytesToInt(b64encode(cipher.encryptor().update(light_decelerations_bytes)))

    severe_decelerations = int(float(request.GET.get('severe_decelerations', 0.0)))
    severe_decelerations_bytes = severe_decelerations.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_severe_decelerations = BytesToInt(b64encode(cipher.encryptor().update(severe_decelerations_bytes)))

    prolongued_decelerations = int(float(request.GET.get('prolongued_decelerations', 0.0)))
    prolongued_decelerations_bytes = prolongued_decelerations.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_prolongued_decelerations = BytesToInt(b64encode(cipher.encryptor().update(prolongued_decelerations_bytes)))

    abnormal_short_term_variability = int(float(request.GET.get('abnormal_short_term_variability', 0.0)))
    abnormal_short_term_variability_bytes = abnormal_short_term_variability.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_abnormal_short_term_variability = BytesToInt(b64encode(cipher.encryptor().update(abnormal_short_term_variability_bytes)))

    mean_value_of_short_term_variability = int(float(request.GET.get('mean_value_of_short_term_variability', 0.0)))
    mean_value_of_short_term_variability_bytes = mean_value_of_short_term_variability.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_mean_value_of_short_term_variability = BytesToInt(b64encode(cipher.encryptor().update(mean_value_of_short_term_variability_bytes)))

    percentage_of_time_with_abnormal_long_term_variability = int(float(request.GET.get('percentage_of_time_with_abnormal_long_term_variability', 0.0)))
    percentage_of_time_with_abnormal_long_term_variability_bytes = percentage_of_time_with_abnormal_long_term_variability.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_percentage_of_time_with_abnormal_long_term_variability = BytesToInt(b64encode(cipher.encryptor().update(percentage_of_time_with_abnormal_long_term_variability_bytes)))

    mean_value_of_long_term_variability = int(float(request.GET.get('mean_value_of_long_term_variability', 0.0)))
    mean_value_of_long_term_variability_bytes = mean_value_of_long_term_variability.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_mean_value_of_long_term_variability = BytesToInt(b64encode(cipher.encryptor().update(mean_value_of_long_term_variability_bytes)))

    histogram_width = int(float(request.GET.get('histogram_width', 0.0)))
    histogram_width_bytes = histogram_width.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_width = BytesToInt(b64encode(cipher.encryptor().update(histogram_width_bytes)))

    histogram_min = int(float(request.GET.get('histogram_min', 0.0)))
    histogram_min_bytes = histogram_min.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_min = BytesToInt(b64encode(cipher.encryptor().update(histogram_min_bytes)))

    histogram_max = int(float(request.GET.get('histogram_max', 0.0)))
    histogram_max_bytes = histogram_max.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_max = BytesToInt(b64encode(cipher.encryptor().update(histogram_max_bytes)))

    histogram_number_of_peaks = int(float(request.GET.get('histogram_number_of_peaks', 0.0)))
    histogram_number_of_peaks_bytes = histogram_number_of_peaks.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_number_of_peaks = BytesToInt(b64encode(cipher.encryptor().update(histogram_number_of_peaks_bytes)))

    histogram_number_of_zeroes = int(float(request.GET.get('histogram_number_of_zeroes', 0.0)))
    histogram_number_of_zeroes_bytes = histogram_number_of_zeroes.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_number_of_zeroes = BytesToInt(b64encode(cipher.encryptor().update(histogram_number_of_zeroes_bytes)))

    histogram_mode = int(float(request.GET.get('histogram_mode', 0.0)))
    histogram_mode_bytes = histogram_mode.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_mode = BytesToInt(b64encode(cipher.encryptor().update(histogram_mode_bytes)))

    histogram_mean = int(float(request.GET.get('histogram_mean', 0.0)))
    histogram_mean_bytes = histogram_mean.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_mean = BytesToInt(b64encode(cipher.encryptor().update(histogram_mean_bytes)))

    histogram_median = int(float(request.GET.get('histogram_median', 0.0)))
    histogram_median_bytes = histogram_median.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_median = BytesToInt(b64encode(cipher.encryptor().update(histogram_median_bytes)))

    histogram_variance = int(float(request.GET.get('histogram_variance', 0.0)))
    histogram_variance_bytes = histogram_variance.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_variance = BytesToInt(b64encode(cipher.encryptor().update(histogram_variance_bytes)))

    histogram_tendency = int(float(request.GET.get('histogram_tendency', 0.0)))
    histogram_tendency_bytes = histogram_tendency.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encrypted_histogram_tendency = BytesToInt(b64encode(cipher.encryptor().update(histogram_tendency_bytes)))

    y_pred = model.predict([[encrypted_baseline_value,encrypted_accelerations,encrypted_fetal_movement,encrypted_uterine_contractions,encrypted_light_decelerations,encrypted_severe_decelerations,encrypted_prolongued_decelerations,encrypted_abnormal_short_term_variability,encrypted_mean_value_of_short_term_variability,encrypted_percentage_of_time_with_abnormal_long_term_variability,encrypted_mean_value_of_long_term_variability,encrypted_histogram_width,encrypted_histogram_min,encrypted_histogram_max,encrypted_histogram_number_of_peaks,encrypted_histogram_number_of_zeroes,encrypted_histogram_mode,encrypted_histogram_mean,encrypted_histogram_median,encrypted_histogram_variance,encrypted_histogram_tendency]])
    # print(y_pred)
    return render(request, 'result.html',{'result' : y_pred})

