from django.db import migrations

def crear_peliculas(apps, schema_editor):
    Movie = apps.get_model('movies', 'Movie')

    Movie.objects.create(
        Título="Los Minions",
        Año=2015,
        Director="Kyle Balda, Pierre Coffin",
        Categoría="Animación / Comedia",
        Sinapsis=(
            "Los minions buscan al villano más malvado a quien servir. "
            "En su aventura conocen a Scarlet Overkill, quien los recluta "
            "para ayudarla a conquistar el mundo."
        )
    )

    Movie.objects.create(
        Título="Rápidos y Furiosos",
        Año=2001,
        Director="Rob Cohen",
        Categoría="Acción",
        Sinapsis=(
            "Brian O'Conner se infiltra en las carreras callejeras lideradas "
            "por Dominic Toretto, mientras investiga una serie de robos "
            "relacionados con autos modificados."
        )
    )

    Movie.objects.create(
        Título="Alicia en el País de las Maravillas",
        Año=2010,
        Director="Tim Burton",
        Categoría="Fantasía",
        Sinapsis=(
            'Alicia regresa al País de las Maravillas, donde criaturas mágicas '
            'le revelan que debe derrotar al Jabberwocky y salvar el reino.'
        )
    )

def borrar_peliculas(apps, schema_editor):
    Movie = apps.get_model('movies', 'Movie')
    Movie.objects.filter(Título__in=[
        "Los Minions",
        "Rápidos y Furiosos",
        "Alicia en el País de las Maravillas"
    ]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_peliculas, borrar_peliculas),
    ]
