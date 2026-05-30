from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from .models import Cafenea, Recenzie
from .forms import UtilizatorRegistrationForm, RecenzieForm


def register(request):
    if request.method == 'POST':
        form = UtilizatorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_cafenele')
    else:
        form = UtilizatorRegistrationForm()
    return render(request, 'cafespot/register.html', {'form': form})


def lista_cafenele(request):
    query = request.GET.get('q')
    cafenele = Cafenea.objects.annotate(rating_mediu=Avg('recenzii__rating'))
    if query:
        cafenele = cafenele.filter(Q(nume__icontains=query) | Q(adresa__icontains=query))

    # else:
    #     cafenele = Cafenea.objects.all()
    return render(request, 'cafespot/lista_cafenele.html', {'cafenele': cafenele, 'query': query})


def detalii_cafenea(request, cafe_id):
    cafenea = get_object_or_404(Cafenea, id=cafe_id)
    recenzii = cafenea.recenzii.all()

    if request.method == 'POST' and request.user.is_authenticated:
        form = RecenzieForm(request.POST)
        if form.is_valid():
            recenzie = form.save(commit=False)
            recenzie.cafe = cafenea
            recenzie.user = request.user
            recenzie.save()
            return redirect('detalii_cafenea', cafe_id=cafenea.id)
    else:
        form = RecenzieForm()

    este_favorita = False
    if request.user.is_authenticated:
        este_favorita = request.user.cafenele_favorite.filter(id=cafe_id).exists()

    return render(request, 'cafespot/detalii_cafenea.html', {
        'cafenea': cafenea,
        'recenzii': recenzii,
        'form': form,
        'este_favorita': este_favorita
    })


@login_required
def toggle_favorit(request, cafe_id):
    cafenea = get_object_or_404(Cafenea, id=cafe_id)
    if request.user.cafenele_favorite.filter(id=cafe_id).exists():
        request.user.cafenele_favorite.remove(cafenea)
    else:
        request.user.cafenele_favorite.add(cafenea)
    return redirect('detalii_cafenea', cafe_id=cafe_id)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def lista_favorite(request):
    favoritele_mele = request.user.cafenele_favorite.all()
    return render(request, 'cafespot/lista_favorite.html', {'cafenele': favoritele_mele})
