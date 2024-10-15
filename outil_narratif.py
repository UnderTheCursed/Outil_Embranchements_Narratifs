import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Créer la fenêtre principale
window = tk.Tk()
window.title("Outil d'Embranchements Narratifs")
window.geometry("600x700")

# Ajouter un label d'introduction
label = tk.Label(window, text="Bienvenue dans l'outil d'embranchements narratifs !", font=("Arial", 14))
label.pack(pady=20)

# Variables globales pour stocker l'image et son affichage
img_label = None
img_canvas = None

# Fonction pour ajouter un nœud
def ajouter_noeud():
    noeud_nom = noeud_input.get()  # Récupère le nom du nœud
    noeuds_listbox.insert(tk.END, noeud_nom)  # Ajoute le nœud à la liste

# Fonction pour ajouter une branche
def ajouter_branche():
    noeud_selectionne = noeuds_listbox.get(tk.ACTIVE)  # Récupère le nœud sélectionné
    branche_nom = branche_input.get()  # Récupère le nom de la branche
    branches_listbox.insert(tk.END, f"{noeud_selectionne} -> {branche_nom}")  # Ajoute la branche

# Fonction pour charger et afficher une image
def charger_image():
    global img_label, img_canvas
    # Ouvre une boîte de dialogue pour sélectionner une image
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if img_path:
        # Charger l'image avec PIL
        img = Image.open(img_path)
        img = img.resize((150, 150), Image.ANTIALIAS)  # Redimensionner l'image

        # Convertir l'image pour Tkinter
        img_tk = ImageTk.PhotoImage(img)

        # Si une image était déjà affichée, la retirer
        if img_label:
            img_label.destroy()

        # Créer un label pour afficher l'image
        img_label = tk.Label(window, image=img_tk)
        img_label.image = img_tk  # Pour éviter que l'image ne soit effacée par le garbage collector
        img_label.pack(pady=10)

        # Optionnel : Dessiner l'image sur un canvas si tu veux plus de contrôle
        if img_canvas:
            img_canvas.delete("all")
        else:
            img_canvas = tk.Canvas(window, width=150, height=150)
            img_canvas.pack(pady=10)

        img_canvas.create_image(75, 75, image=img_tk)

# Fonction pour sauvegarder l'arbre
def sauvegarder_arbre():
    with open("arbre_narratif.txt", "w") as file:
        file.write("Nœuds et branches :\n")
        for branche in branches_listbox.get(0, tk.END):
            file.write(f"{branche}\n")

# Fonction pour importer un fichier d'arbre narratif
def importer_arbre():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            lines = file.readlines()

        noeuds_listbox.delete(0, tk.END)  # Effacer les anciens nœuds
        branches_listbox.delete(0, tk.END)  # Effacer les anciennes branches

        # Parcourir le fichier et séparer nœuds et branches
        for line in lines:
            if "->" in line:
                branches_listbox.insert(tk.END, line.strip())
            else:
                noeuds_listbox.insert(tk.END, line.strip())

# Créer une zone de saisie pour ajouter un nœud
noeud_input = tk.Entry(window, width=40)
noeud_input.pack(pady=10)

# Bouton pour ajouter un nœud
bouton_ajouter = tk.Button(window, text="Ajouter un nœud", command=ajouter_noeud)
bouton_ajouter.pack()

# Liste des nœuds ajoutés
noeuds_listbox = tk.Listbox(window, width=50, height=10)
noeuds_listbox.pack(pady=10)

# Créer une zone de saisie pour ajouter une branche
branche_input = tk.Entry(window, width=40)
branche_input.pack(pady=10)

# Bouton pour ajouter une branche
bouton_ajouter_branche = tk.Button(window, text="Ajouter une branche", command=ajouter_branche)
bouton_ajouter_branche.pack()

# Liste des branches ajoutées
branches_listbox = tk.Listbox(window, width=50, height=10)
branches_listbox.pack(pady=10)

# Bouton pour charger une image
bouton_image = tk.Button(window, text="Ajouter une image", command=charger_image)
bouton_image.pack(pady=10)

# Bouton pour sauvegarder l'arbre
bouton_sauvegarder = tk.Button(window, text="Sauvegarder l'arbre", command=sauvegarder_arbre)
bouton_sauvegarder.pack(pady=10)

# Bouton pour importer un arbre
bouton_importer = tk.Button(window, text="Importer un fichier d'arbre", command=importer_arbre)
bouton_importer.pack(pady=10)

# Afficher la fenêtre
window.mainloop()
