# Module 2.3 - Section Generation
# Nhiem vu:
# - Tao nhieu mat cat (section) doc theo chieu dai de giay
# - Moi section la 1 hinh chu nhat (Width x Height) tai 1 vi tri x tren truc Length
# - Section hep dan o 2 dau (mui/got), rong nhat o giua
# - Cac section nay se duoc dung de Loft thanh Surface o Module 2.4

import math


def compute_section_corners(length, width, height, num_sections):
    """Tinh toa do 4 goc cua tung section - dung de test doc lap, khong can Rhino."""
    result = []
    n = int(num_sections)
    for i in range(n):
        t = float(i) / (n - 1)
        x = t * length
        w = width * (0.5 + 0.5 * math.sin(math.pi * t))
        corners = [
            (x, -w / 2, 0),
            (x,  w / 2, 0),
            (x,  w / 2, height),
            (x, -w / 2, height)
        ]
        result.append(corners)
    return result


if __name__ == "__main__":
    sections = compute_section_corners(length=280, width=90, height=30, num_sections=6)

    print("So section tao ra:", len(sections))
    for i, s in enumerate(sections):
        print("Section", i, ":", s)


# ============================================================
# CODE TRONG GRASSHOPPER (GHPYTHON / SCRIPT COMPONENT)
# ============================================================
# import Rhino.Geometry as rg
# import math
#
# sections = []
# n = int(num_sections)
#
# for i in range(n):
#     t = float(i) / (n - 1)
#     x = t * length
#     w = width * (0.5 + 0.5 * math.sin(math.pi * t))
#
#     pts = [
#         rg.Point3d(x, -w/2, 0),
#         rg.Point3d(x,  w/2, 0),
#         rg.Point3d(x,  w/2, height),
#         rg.Point3d(x, -w/2, height),
#         rg.Point3d(x, -w/2, 0)
#     ]
#
#     sections.append(rg.Polyline(pts).ToNurbsCurve())
#
# S = sections

# ============================================================
# HUONG DAN GRASSHOPPER - RHINO 7 / GHPYTHON
# ============================================================
# 1. THEM 1 SLIDER MOI: num_sections
# Double-click canvas -> "Number Slider" -> Rename thanh "num_sections".
# Double-click slider -> chinh:
#   Min = 2, Max = 20, Value = 6
#
# 2. TAO PYTHON SCRIPT COMPONENT MOI
# Double-click canvas -> go "GHPython".
# Trong component:
#   - Tao 4 INPUT dat ten dung: length, width, height, num_sections
#   - Tao 1 OUTPUT dat ten: S
# Noi 4 slider (length, width, height tu Module 2.1/2.2 va num_sections moi) vao 4 input.
#
# 3. XEM KET QUA
# S la danh sach cac duong cong section -> Grasshopper tu dong hien thi
# truc tiep trong Rhino viewport, khong can Panel.
#
# 4. TEST
# Gia tri: Length = 280, Width = 90, Height = 30, num_sections = 6
# Ket qua: 6 section xep doc truc X, hep o 2 dau (mui/got), rong o giua.