extends Node2D

# Propriétés
var radius = 50  # Rayon du cercle
var color = Color(1, 0, 0)  # Couleur du cercle (rouge)
var center = Vector2(0, 0)  # Centre du cercle, calculé dynamiquement

func _ready():
	# Calculer le centre de l'écran
	center = get_viewport_rect().size / 2
	# Demander un redessin
	queue_redraw()

func _draw():
	# Dessiner un cercle centré à l'écran
	draw_circle(center, radius, color)
