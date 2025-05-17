# PRESORTING
print("=== SISTEM ANTREAN PUSKESMAS - PRESORTING ===")
pasien = []
n = int(input("Jumlah pasien (contoh: 3): "))
for i in range(n):
    nama = input(f"Nama pasien ke-{i+1} (contoh: Budi): ")
    prioritas = int(input("Skor prioritas (contoh: 1=terpenting): "))
    pasien.append((nama, prioritas))

terurut = sorted(pasien, key=lambda x: x[1])
print("\nDaftar pasien terurut:")
for nama, p in terurut:
    print(f"{nama} (Prioritas {p})")


# BST
print("\n=== SISTEM PENCATATAN ID PASIEN - BST ===")
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

data = list(map(int, input("Masukkan ID pasien (pisah spasi, contoh: 5 2 8 1): ").split()))
root = None
for d in data:
    root = insert(root, d)

print("ID pasien terurut (inorder): ", end="")
inorder(root)
print()


# HEAP SORT
print("\n=== SISTEM PEMANGGILAN KATEGORI PASIEN BERDASARKAN PRIORITAS - HEAP SORT ===")
import heapq
kategori = []
n = int(input("Jumlah kategori pasien (contoh: 3): "))
for i in range(n):
    prioritas = int(input(f"Prioritas kategori ke-{i+1} (contoh: 1): "))
    nama = input(f"Nama kategori ke-{i+1} (contoh: Lansia): ")
    kategori.append((prioritas, nama))

heapq.heapify(kategori)
print("\nUrutan panggilan kategori:")
while kategori:
    print("Dipanggil:", heapq.heappop(kategori)[1])


# GRAPH
print("\n=== SISTEM RUJUKAN ANTAR POLI DI PUSKESMAS - GRAPH ===")
graph = {}
jumlah = int(input("Jumlah poli (contoh: 3): "))
for _ in range(jumlah):
    poli = input("Nama poli (contoh: Poli Umum): ")
    tujuan = input(f"Rujukan dari '{poli}' (pisah koma, kosong jika tidak ada, contoh: Poli Gigi, Poli Anak): ")
    graph[poli] = [x.strip() for x in tujuan.split(",")] if tujuan else []

def dfs(visited, graph, node):
    if node not in visited:
        print("->", node)
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(visited, graph, neighbor)

awal = input("Mulai dari poli (contoh: Poli Umum): ")
print("\nJalur rujukan:")
visited = set()
dfs(visited, graph, awal)
