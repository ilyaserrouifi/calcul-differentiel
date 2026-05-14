
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# Configuration des figures
fig = plt.figure(figsize=(18, 12))

# ==================== SCHÉMA 1: LA DÉFINITION GÉOMÉTRIQUE ====================
ax1 = fig.add_subplot(2, 3, 1, projection='3d')

# Espace E (domaine) - plan horizontal
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Dessiner le plan E
ax1.plot_surface(X, Y, Z, alpha=0.2, color='blue', label='E')

# Point x dans E
x0, y0 = 1, 0.5
ax1.scatter([x0], [y0], [0], color='blue', s=100, label='x')
ax1.text(x0, y0, 0.2, 'x', fontsize=12, color='blue', fontweight='bold')

# Vecteur h (petit déplacement)
h_x, h_y = 0.3, 0.4
ax1.quiver(x0, y0, 0, h_x, h_y, 0, color='green', arrow_length_ratio=0.3, linewidth=2)
ax1.text(x0+h_x/2, y0+h_y/2, 0.1, 'h', fontsize=12, color='green', fontweight='bold')

# Boule ouverte autour de x (petit rayon)
theta = np.linspace(0, 2*np.pi, 50)
r = 0.6
ax1.plot(x0 + r*np.cos(theta), y0 + r*np.sin(theta), np.zeros_like(theta), 
         'b--', linewidth=2, alpha=0.7, label='U (ouvert)')

# Espace F (but) - plan vertical à droite
ax1.plot_surface(np.full_like(X, 3), Y, X, alpha=0.2, color='red')

# Point f(x) dans F
fx, fy, fz = 3, 1.5, 2
ax1.scatter([fx], [fy], [fz], color='red', s=100)
ax1.text(fx, fy, fz+0.2, 'f(x)', fontsize=12, color='red', fontweight='bold')

# Application f (flèche courbe)
t = np.linspace(0, 1, 50)
fx_curve = 3 * np.ones_like(t)
fy_curve = y0 + (fy - y0) * t + 0.5 * np.sin(np.pi * t)
fz_curve = 0 + (fz - 0) * t
ax1.plot(fx_curve, fy_curve, fz_curve, 'purple', linewidth=3, alpha=0.8)
ax1.text(3.1, 0.8, 1, 'f', fontsize=14, color='purple', fontweight='bold')

# df(x)(h) - approximation linéaire
ax1.quiver(fx, fy, fz, 0.5, 0.3, 0.8, color='orange', arrow_length_ratio=0.3, linewidth=2)
ax1.text(fx+0.5, fy+0.3, fz+0.9, 'df(x)(h)', fontsize=11, color='orange', fontweight='bold')

# f(x+h) - vraie valeur
ax1.scatter([fx], [fy+0.35], [fz+0.85], color='darkred', s=50)
ax1.text(fx, fy+0.5, fz+1, 'f(x+h)', fontsize=10, color='darkred')

# Petit o(||h||) - l'erreur
ax1.quiver(fx+0.5, fy+0.3, fz+0.8, 0, 0.05, 0.05, color='gray', 
           arrow_length_ratio=0.3, linewidth=1, linestyle='--')
ax1.text(fx+0.5, fy+0.4, fz+0.95, 'o(||h||)', fontsize=9, color='gray')

ax1.set_xlabel('E (domaine)', fontsize=10)
ax1.set_ylabel('y', fontsize=10)
ax1.set_zlabel('z', fontsize=10)
ax1.set_title('1. Définition Géométrique\nf(x+h) ≈ f(x) + df(x)(h)', fontsize=12, fontweight='bold')
ax1.set_xlim(-2.5, 4)
ax1.set_ylim(-2.5, 2.5)
ax1.set_zlim(-0.5, 3)

# ==================== SCHÉMA 2: L'APPLICATION LINÉAIRE df(x) ====================
ax2 = fig.add_subplot(2, 3, 2, projection='3d')

# Espace E
ax2.plot_surface(X, Y, Z, alpha=0.15, color='cyan')

# Sphère unité dans E
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 50)
THETA, PHI = np.meshgrid(theta, phi)
R = 1
X_sphere = R * np.sin(PHI) * np.cos(THETA)
Y_sphere = R * np.sin(PHI) * np.sin(THETA)
Z_sphere = R * np.cos(PHI)
ax2.plot_surface(X_sphere, Y_sphere, Z_sphere, alpha=0.2, color='blue')

# Quelques vecteurs sur la sphère unité
vectors_e = [(1,0,0), (0,1,0), (0,0,1), (0.707, 0.707, 0), (-0.707, 0.707, 0)]
for v in vectors_e:
    ax2.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', arrow_length_ratio=0.1, linewidth=2)

ax2.text(1.2, 0, 0, 'E', fontsize=12, color='blue', fontweight='bold')

# Espace F (décalé)
offset_x = 4
ax2.plot_surface(np.full_like(X, offset_x), Y, X, alpha=0.15, color='magenta')

# Image de la sphère par df(x) - ellipsoïde
# Supposons df(x) = matrice diag(2, 1, 1.5)
A = np.array([[2, 0, 0], [0, 1, 0], [0, 0, 1.5]])
X_ell = offset_x + 2*X_sphere
Y_ell = 1*Y_sphere
Z_ell = 1.5*Z_sphere
ax2.plot_surface(X_ell, Y_ell, Z_ell, alpha=0.3, color='red')

# Vecteurs images
for v in vectors_e:
    v_arr = np.array(v)
    w = A @ v_arr
    ax2.quiver(offset_x, 0, 0, w[0], w[1], w[2], color='red', arrow_length_ratio=0.1, linewidth=2)

ax2.text(offset_x+2.2, 0, 0, 'F', fontsize=12, color='red', fontweight='bold')

# Flèche df(x)
ax2.quiver(2, 0, 0, 1.5, 0, 0, color='purple', arrow_length_ratio=0.2, linewidth=3)
ax2.text(2.5, 0, 0.3, 'df(x)', fontsize=14, color='purple', fontweight='bold')

ax2.set_xlabel('x', fontsize=10)
ax2.set_ylabel('y', fontsize=10)
ax2.set_zlabel('z', fontsize=10)
ax2.set_title('2. df(x) ∈ L_c(E,F)\nSphère unité → Ellipsoïde', fontsize=12, fontweight='bold')
ax2.set_xlim(-2, 7)
ax2.set_ylim(-2.5, 2.5)
ax2.set_zlim(-2, 2)

# ==================== SCHÉMA 3: L'APPROXIMATION ====================
ax3 = fig.add_subplot(2, 3, 3)

# Courbe f(x) en 1D pour simplifier
x_1d = np.linspace(-2, 2, 200)
f_1d = x_1d**3  # f(x) = x^3

# Tangente en x=1
x_tangent = 1
f_tangent = x_tangent**3
df_tangent = 3 * x_tangent**2  # f'(1) = 3
tangent_line = f_tangent + df_tangent * (x_1d - x_tangent)

ax3.plot(x_1d, f_1d, 'b-', linewidth=3, label='f(x) = x³')
ax3.plot(x_1d, tangent_line, 'r--', linewidth=2, label='Tangente: f(1)+f\'(1)(x-1)')

# Point x=1
ax3.scatter([x_tangent], [f_tangent], color='blue', s=150, zorder=5)
ax3.text(x_tangent, f_tangent+0.5, 'x', fontsize=12, color='blue', fontweight='bold')

# Point x+h
h = 0.8
x_h = x_tangent + h
f_xh = x_h**3
ax3.scatter([x_h], [f_xh], color='green', s=100, zorder=5)
ax3.text(x_h, f_xh+0.5, 'x+h', fontsize=12, color='green', fontweight='bold')

# Valeur approchée
f_approx = f_tangent + df_tangent * h
ax3.scatter([x_h], [f_approx], color='orange', s=100, zorder=5)
ax3.text(x_h, f_approx-1.5, 'f(x)+df(x)(h)', fontsize=11, color='orange', fontweight='bold')

# Erreur o(||h||)
ax3.plot([x_h, x_h], [f_approx, f_xh], 'gray', linewidth=2, linestyle=':')
ax3.text(x_h+0.1, (f_approx+f_xh)/2, 'o(||h||)', fontsize=10, color='gray')

# Vecteur h
ax3.annotate('', xy=(x_h, f_tangent), xytext=(x_tangent, f_tangent),
            arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax3.text(x_tangent+h/2, f_tangent-1, 'h', fontsize=12, color='green', fontweight='bold')

ax3.set_xlabel('x', fontsize=12)
ax3.set_ylabel('f(x)', fontsize=12)
ax3.set_title('3. Approximation Locale\nf(x+h) = f(x) + df(x)(h) + o(||h||)', fontsize=12, fontweight='bold')
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)
ax3.set_xlim(-2, 2.5)
ax3.set_ylim(-5, 10)

# ==================== SCHÉMA 4: INVARIANCE PAR NORMES ÉQUIVALENTES ====================
ax4 = fig.add_subplot(2, 3, 4)

# Deux normes équivalentes sur R²
# Norme 1: euclidienne (cercle)
theta = np.linspace(0, 2*np.pi, 100)
r1 = 1
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)

# Norme 2: ||(x,y)|| = max(|x|,|y|) (carré)
x2 = [1, 1, -1, -1, 1]
y2 = [1, -1, -1, 1, 1]

# Norme 3: ||(x,y)|| = |x| + |y| (losange)
x3 = [1, 0, -1, 0, 1]
y3 = [0, 1, 0, -1, 0]

ax4.plot(x1, y1, 'b-', linewidth=3, label='||·||₂ (euclidienne)')
ax4.plot(x2, y2, 'r--', linewidth=3, label='||·||∞ (max)')
ax4.plot(x3, y3, 'g:', linewidth=3, label='||·||₁ (somme)')

ax4.fill(x1, y1, alpha=0.1, color='blue')
ax4.fill(x2, y2, alpha=0.1, color='red')
ax4.fill(x3, y3, alpha=0.1, color='green')

ax4.scatter([0], [0], color='black', s=50)
ax4.text(0.1, 0.1, '0', fontsize=12)

# Montrer l'équivalence: α||x|| ≤ ||x||' ≤ β||x||
ax4.annotate('', xy=(1.4, 1.4), xytext=(0, 0),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
ax4.text(1.5, 1.5, 'α·||x|| ≤ ||x||\' ≤ β·||x||', fontsize=11, color='purple', fontweight='bold')

ax4.set_xlabel('x', fontsize=12)
ax4.set_ylabel('y', fontsize=12)
ax4.set_title('4. Normes Équivalentes\nBoules unité différentes mais équivalentes', fontsize=12, fontweight='bold')
ax4.legend(fontsize=10, loc='upper left')
ax4.grid(True, alpha=0.3)
ax4.set_xlim(-2, 2.5)
ax4.set_ylim(-2, 2.5)
ax4.set_aspect('equal')

# ==================== SCHÉMA 5: UNICITÉ DE LA DIFFÉRENTIELLE ====================
ax5 = fig.add_subplot(2, 3, 5)

# Représentation graphique de la preuve d'unicité
x_vals = np.linspace(-2, 2, 100)

# Deux applications linéaires différentes
L1 = 2 * x_vals
L2 = 2.5 * x_vals

ax5.plot(x_vals, L1, 'b-', linewidth=3, label='L₁(h) = 2h')
ax5.plot(x_vals, L2, 'r--', linewidth=3, label='L₂(h) = 2.5h')

# La différence
ax5.plot(x_vals, L2 - L1, 'g:', linewidth=3, label='(L₂-L₁)(h) = 0.5h')

# Montrer que ||L2(h) - L1(h)|| / ||h|| → 0 implique L1 = L2
h_test = 0.5
ax5.scatter([h_test], [2*h_test], color='blue', s=100, zorder=5)
ax5.scatter([h_test], [2.5*h_test], color='red', s=100, zorder=5)
ax5.plot([h_test, h_test], [2*h_test, 2.5*h_test], 'purple', linewidth=3)
ax5.text(h_test+0.1, 2.25*h_test, '||L₂(h)-L₁(h)||', fontsize=10, color='purple')

# Quand h→0, la différence doit être o(||h||)
ax5.annotate('', xy=(0.1, 0), xytext=(0.5, 0),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax5.text(0.25, -0.3, 'h → 0', fontsize=11)

ax5.set_xlabel('h', fontsize=12)
ax5.set_ylabel('L(h)', fontsize=12)
ax5.set_title('5. Unicité de df(x)\nSi (L₂-L₁)(h) = o(||h||) alors L₁ = L₂', fontsize=12, fontweight='bold')
ax5.legend(fontsize=10)
ax5.grid(True, alpha=0.3)
ax5.set_xlim(-2, 2)
ax5.set_ylim(-5, 5)

# ==================== SCHÉMA 6: RÉSUMÉ VISUEL ====================
ax6 = fig.add_subplot(2, 3, 6)
ax6.axis('off')

# Texte récapitulatif
text = """
RÉSUMÉ : LA DIFFÉRENCIELLE

📐 DÉFINITION :
f: U ⊂ E → F est différentiable en x
s'il existe L ∈ L_c(E,F) telle que :

f(x+h) = f(x) + L(h) + o(||h||)

quand h → 0

🎯 INTERPRÉTATION :
• f(x+h) : valeur exacte
• f(x) : valeur au point
• L(h) = df(x)(h) : partie linéaire (tangente)
• o(||h||) : erreur négligeable

📊 PROPRIÉTÉS :
1. Unicité : df(x) est unique
2. Continuité : f diff ⟹ f continue
3. Linéarité : df(x) ∈ L_c(E,F)
4. Invariance : indépendante des normes 
   équivalentes

🔧 EXEMPLE SIMPLE :
f: R → R, f(x) = x³
f(x+h) = (x+h)³ = x³ + 3x²h + 3xh² + h³
         = f(x) + f'(x)h + o(|h|)

df(x)(h) = 3x²·h
"""

ax6.text(0.05, 0.95, text, transform=ax6.transAxes, fontsize=11,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('/mnt/agents/output/differentielle_schemas.png', dpi=150, bbox_inches='tight')
plt.show()
print("Schémas sauvegardés!")
