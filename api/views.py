from os.path import exists

from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from api.forms import LoginForm, NewUserForm
from backend.settings import BASE_DIR
from .models import Data1, Data2
from django.contrib import auth
import os
import glob
from django.views.decorators.csrf import csrf_exempt


def table_first():
    path_file = os.path.join('/media/sf_Storage/Project')
    dirfiles = os.listdir(path_file)
    fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
    dirs = []
    for file in fullpaths:
        if os.path.isdir(file): dirs.append(file)
        os.getcwd()
    x = list(dirs)
    for i in x:
        project_path = os.listdir(i)
        folder_project = map(lambda name: os.path.join(i, name), project_path)
        fll = []
        for profolder in folder_project:
            if os.path.isdir(profolder): fll.append(profolder)
            os.getcwd()
        y1 = list(fll)
        path_list_all = []
        for j in y1:
            prounder_path = os.listdir(j)
            pro_folder = map(lambda name: os.path.join(j, name), prounder_path)
            path = []
            for f in pro_folder:
                if os.path.isdir(f): path.append(f)
                os.getcwd()
            y2 = list(path)
            for k in y2:
                path_list_all.append(k)
        y3 = list(path_list_all)
        fastqc_path = []
        for k in y3:
            fqc_path = os.listdir(k)
            fqc_fol = map(lambda name: os.path.join(k, name), fqc_path)
            path1 = []
            for k1 in fqc_fol:
                if os.path.isdir(k1): path1.append(k1)
                os.getcwd()
            for s in path1:
                fastqc_path.append(s)
        y4 = list(fastqc_path)
        for l in y4:
            fast_qc = os.listdir(l)
            fast_fol = map(lambda name: os.path.join(l, name), fast_qc)
            path2 = []
            for l1 in fast_fol:
                if os.path.isdir(l1): path2.append(l1.split('/'))
                os.getcwd()
            for s1 in path2:
                main_path = s1.index('sf_Storage')
                new_path = s1[main_path:]
                project = new_path[2]
                patient = new_path[3]
                sequence = new_path[4]
                fastqcfol = new_path[5]
                samplename = new_path[6]
                sample = new_path[6][4:]
                if Data1.objects.filter(Q(Patient=patient) & Q(Sequence=sequence) &
                                        Q(Samplename=samplename) & Q(Sample=sample)).exists():
                    pass
                else:
                    insert = Data1(Project=project, Patient=patient, Sequence=sequence, Fastqcfol=fastqcfol,
                                   Samplename=samplename, Sample=sample)
                    insert.save()


def null_value():
    path_file = os.path.join('/media/sf_Storage/Project')
    dirfiles = os.listdir(path_file)
    fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
    dirs = []
    for file in fullpaths:
        if os.path.isdir(file): dirs.append(file)
        os.getcwd()
    x = list(dirs)
    for i in x:
        project_path = os.listdir(i)
        folder_project = map(lambda name: os.path.join(i, name), project_path)
        fll = []
        for profolder in folder_project:
            if os.path.isdir(profolder): fll.append(profolder)
            os.getcwd()
        y1 = list(fll)
        for j in y1:
            pat_path = j.split('/')
            mdd = pat_path.index('sf_Storage')
            now_pat = pat_path[mdd:]
            project = now_pat[2]
            pat = now_pat[3]

            if Data1.objects.filter(Q(Project=project) & Q(Patient=pat) & Q(Sequence='DNA')).exists():
                pass
            else:
                entry = Data1(Project=project, Patient=pat, Sequence='DNA', Fastqcfol='FASTQC_REPORTS',
                              Samplename='null', Sample='null')
                entry.save()
            if Data1.objects.filter(Q(Project=project) & Q(Patient=pat) & Q(Sequence='RNA')).exists():
                pass
            else:
                entry = Data1(Project=project, Patient=pat, Sequence='RNA', Fastqcfol='FASTQC_REPORTS',
                              Samplename='null', Sample='null')
                entry.save()
            if Data1.objects.filter(Q(Project=project) & Q(Patient=pat) & Q(Sequence='FFPE')).exists():
                pass
            else:
                entry = Data1(Project=project, Patient=pat, Sequence='FFPE', Fastqcfol='FASTQC_REPORTS',
                              Samplename='null', Sample='null')
                entry.save()


def table_second():
    path_file = os.path.join('/media/sf_Storage/Project')
    dirfiles = os.listdir(path_file)
    fullpaths = map(lambda name: os.path.join(path_file, name), dirfiles)
    dirs = []
    for file in fullpaths:
        if os.path.isdir(file): dirs.append(file)
        os.getcwd()
    x = list(dirs)
    for i in x:
        project_path = os.listdir(i)
        folder_project = map(lambda name: os.path.join(i, name), project_path)
        fll = []
        for profolder in folder_project:
            if os.path.isdir(profolder): fll.append(profolder)
            os.getcwd()
        y1 = list(fll)
        path_list_all = []
        for j in y1:
            prounder_path = os.listdir(j)
            pro_folder = map(lambda name: os.path.join(j, name), prounder_path)
            path = []
            for f in pro_folder:
                if os.path.isdir(f): path.append(f)
                os.getcwd()
            y2 = list(path)
            for k in y2:
                path_list_all.append(k)
        y3 = list(path_list_all)
        fastqc_path = []
        for k in y3:
            fqc_path = os.listdir(k)
            fqc_fol = map(lambda name: os.path.join(k, name), fqc_path)
            path1 = []
            for k1 in fqc_fol:
                if os.path.isdir(k1): path1.append(k1)
                os.getcwd()
            for s in path1:
                fastqc_path.append(s)
        y4 = list(fastqc_path)
        last_path = []
        for l in y4:
            fast_qc = os.listdir(l)
            fast_fol = map(lambda name: os.path.join(l, name), fast_qc)
            path2 = []
            for l1 in fast_fol:
                if os.path.isdir(l1): path2.append(l1)
                os.getcwd()
            for s1 in path2:
                last_path.append(s1)
        y5 = list(last_path)
        sample_path = []
        for r in y5:
            sam = os.listdir(r)
            samp_fol = map(lambda name: os.path.join(r, name), sam)
            for r1 in samp_fol:
                if os.path.isdir(r1): sample_path.append(r1)
                os.getcwd()
        y6 = list(sample_path)
        for o in y6:
            if(not o.split('/')[-1] == 'multiqc_data'):
                print(o)
                os.chdir(o)
                text_file = glob.glob('*.txt')
                image_path = o.split('/')
                md = image_path.index('sf_Storage')
                new_root = image_path[md:]
                new_split = new_root[7].split('_')
                new_root.append(new_split[0])
                new_root.append(new_split[1])
                new_root.append(new_split[2])
                new_root.append(new_split[3])
                new_root.append(new_split[4])
                new_root.append(new_split[5])
                with open(text_file[0], 'r') as f1, open(text_file[1], 'r') as f2:
                    read_file = f2.read().split()
                    fastqc_file = f1.read().split()
                new_root.append(read_file[0])
                new_root.append(read_file[4])
                new_root.append(read_file[10])
                new_root.append(read_file[16])
                new_root.append(read_file[22])
                new_root.append(read_file[28])
                new_root.append(read_file[34])
                new_root.append(read_file[40])
                new_root.append(read_file[45])
                new_root.append(read_file[50])
                new_root.append(read_file[54])
                new_root.append(fastqc_file[21])
                new_root.append(fastqc_file[30])
                new_root.append(fastqc_file[32])
                sequence = new_root[4]
                fastqc = new_root[5]
                samplename = new_root[6]
                pathname = new_root[7]
                trusqc = new_root[9]
                flowcell = new_root[10]
                lane = new_root[11]
                row = new_root[12]
                bs = new_root[14]
                pbsq = new_root[15]
                ptsq = new_root[16]
                psqs = new_root[17]
                pbsc = new_root[18]
                psgc = new_root[19]
                pbnc = new_root[20]
                sld = new_root[21]
                sdl = new_root[22]
                oss = new_root[23]
                ac = new_root[24]
                tsqc = new_root[25]
                sqclth = new_root[26]
                gc = new_root[27]
                if Data2.objects.filter(Q(Sequence=sequence) & Q(Sample_name=samplename) &
                                        Q(Lane=lane) & Q(Row=row)).exists():
                    pass
                else:
                    st = Data2(Sequence=sequence, FastQc=fastqc, Sample_name=samplename, Path_name=pathname,
                               Tru_Sequence=trusqc, Flowcell=flowcell, Lane=lane, Row=row, BS=bs, PBSQ=pbsq,
                               PTSQ=ptsq, PSQS=psqs, PBSC=pbsc, PSGC=psgc, PBNC=pbnc, SLD=sld, SDL=sdl, OS=oss,
                               AC=ac, Total_Sequence=tsqc, Sequence_length=sqclth, GC=gc)
                    st.save()


# Main Code
@csrf_exempt
def update_data(request):
    if request.user.is_authenticated:
        user = request.user
        table_first()
        null_value()
        table_second()
        messages.success(request, f"Data Refresh Successfully. {user}")
        return redirect('home')
    else:
        user = request.user
        messages.error(request, f"Sorry {user} You are not authorized")
        return redirect('home')


class CustomerRegView(View):
    @csrf_exempt
    def get(self, request):
        form1 = LoginForm()
        form2 = NewUserForm()
        return render(request, 'index.html', {'login_form': form1, 'register_form': form2})

    @csrf_exempt
    def post(self, request):
        if request.method == "POST":
            if request.POST.get('signup'):
                form = NewUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    user = user
                    messages.success(request, f"Registration successfully. {user}")
                    return redirect('login', )
                else:
                    messages.error(request, "Sorry Unsuccessful registration. Please Type valid information")
                    form1 = LoginForm()
                    form2 = NewUserForm()
                    return render(request, 'index.html', {'login_form': form1, 'register_form': form2})

            if request.POST.get('signin'):
                form = LoginForm(request, data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, f"Welcome you are logging succesfully. {user}")
                        return redirect('home')
                    else:
                        messages.error(request, "Sorry Invalid username or password.")
                else:
                    messages.error(request, "Sorry Invalid username or password.")
                form1 = LoginForm()
                form2 = NewUserForm()
                return render(request, 'index.html', {'login_form': form1, 'register_form': form2})


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request, pt=None):
        if pt is None:
            prodata = Data1.objects.values('Project').distinct()
            return render(request, 'profile.html', {'prodata': prodata})

        if pt is not None:
            patient = Data1.objects.filter(Project=pt).values('Patient').distinct()
            ptd_dat = patient.values('Project', 'Patient', 'Sequence', 'Samplename', 'Sample').distinct()
            newptd = patient.values('Sequence').distinct()  # Sequence Send
            prodata = Data1.objects.values('Project').distinct()
            fast = Data1.objects.values('Fastqcfol').distinct()
            return render(request, 'profile.html', {'prodata': prodata, 'patient': patient, 'fast': fast,
                                                    'sqt': ptd_dat, 'smp': newptd, 'sqc': pt, 'active': 'is-danger'})


def logout_request(request):
    user = request.user
    auth.logout(request)
    messages.success(request, f" {user} You are logout successfully")
    return redirect('login')


@csrf_exempt
def show_data(request, dt=None, pt=None, data=None, data1=None):
    if dt is None and data is None and data1 is None:
        prodata = Data2.objects.values('Project').distinct()
        return render(request, {'prodata': prodata})

    if dt is not None and data is not None and data1 is not None:
        sample = Data2.objects.filter(Q(Sequence=data) & Q(Sample_name=data1))
        prodata = Data1.objects.values('Project').distinct()
        path = 'profile.html'
        return render(request, path, {'prodata': prodata, 'sample': sample, 'pro': dt, 'pt': pt,
                                      'sqc': data, 'spp': data1})


@csrf_exempt
def multiqc(request, pro=None, ptt=None, st=None, smmp=None):
    if request.method == 'GET':
        if pro is not None and ptt is not None and st is not None and smmp is not None:
            path_name = 'Project/' + pro + '/' + ptt + '/' + st + \
                        '/FASTQC_REPORTS' + '/' + smmp + '/multiqc_report.html'
            if path_name:
                return render(request, path_name)
            else:
                return render(request, '500.html')


def handler404(request, exception):
    messages.error("Sorry Page Not Found")
    return render(request, '404.html')


def handler500(request):
    messages.error("Sorry Page Not Found")
    return render(request, '500.html')
