# Module 2.4 - Surface Generation
# Nhiem vu:
# - Loft cac section tu Module 2.3 thanh 1 surface (polysurface) lien
# - Surface chay doc truc Length, hai dau con ho (se duoc dong nap o Module 2.6)

from module_03_section_generation import compute_section_corners


def compute_loft_rails(sections):
    """Gom cac goc tuong ung cua moi section thanh rail - dung de test doc lap, khong can Rhino."""
    if len(sections) < 2:
        return [], 0
    rails = []
    for j in range(4):
        rails.append([s[j] for s in sections])
    face_count = 4 * (len(sections) - 1)
    return rails, face_count


if __name__ == "__main__":
    sections = compute_section_corners(length=280, width=90, height=30, num_sections=6)
    rails, face_count = compute_loft_rails(sections)

    print("So rail:", len(rails))
    for j, r in enumerate(rails):
        print("Rail", j, ":", r)
    print("So face du kien:", face_count)


# ============================================================
# CODE TRONG GRASSHOPPER (GHPYTHON / SCRIPT COMPONENT)
# ============================================================
# import Rhino.Geometry as rg
#
# loft = rg.Brep.CreateFromLoft(
#     sections, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False
# )
#
# L = loft[0] if loft else None

# ============================================================
# HUONG DAN GRASSHOPPER - RHINO 7 / GHPYTHON
# ============================================================
# 1. TAO PYTHON SCRIPT COMPONENT MOI
# Double-click canvas -> go "GHPython".
# Trong component:
#   - Tao 1 INPUT dat ten dung: sections
#       Right-click input "sections" -> Type hint: Curve
#       Right-click input "sections" -> Access: List Access
#   - Tao 1 OUTPUT dat ten: L
#
# 2. NOI DAY
# Noi output S cua component Module 2.3 vao input sections.
# Khong can slider moi: moi thay doi o slider length / width / height /
# num_sections se tu dong cap nhat surface.
#
# 3. XEM KET QUA
# L la Brep that nen hien thi truc tiep trong Rhino viewport, khong can Panel.
#
# 4. TEST
# Gia tri: Length = 280, Width = 90, Height = 30, num_sections = 6
# Ket qua: 1 polysurface gom 20 face (4 face x 5 doan), thon dan o 2 dau,
# rong o giua, hai dau ho.
