# Module 2.6 - 3D Sole Generation
# Nhiem vu:
# - Dong nap 2 dau (mui/got) cua surface tu Module 2.5 thanh 1 solid kin
# - Dam bao solid co huong dung (khong bi lon nguoc)

import math


def compute_sole_stats(length, width, height, offset, trim, steps=200):
    """Tinh kich thuoc 2 nap dau va the tich xap xi - dung de test doc lap, khong can Rhino."""
    x_start = trim
    x_end = length - trim

    def cross_section(x):
        t = x / float(length)
        w = width * (0.5 + 0.5 * math.sin(math.pi * t)) + 2 * offset
        h = height + 2 * offset
        return w, h

    caps = [(x_start,) + cross_section(x_start), (x_end,) + cross_section(x_end)]

    volume = 0.0
    dx = (x_end - x_start) / float(steps)
    for i in range(steps):
        w0, h0 = cross_section(x_start + i * dx)
        w1, h1 = cross_section(x_start + (i + 1) * dx)
        volume += (w0 * h0 + w1 * h1) / 2.0 * dx

    return caps, volume


if __name__ == "__main__":
    caps, volume = compute_sole_stats(
        length=280, width=90, height=30, offset=-2, trim=1
    )

    print("Nap dau (x, width, height):")
    for c in caps:
        print(" ", c)
    print("The tich xap xi:", round(volume, 1))


# ============================================================
# CODE TRONG GRASSHOPPER (GHPYTHON / SCRIPT COMPONENT)
# ============================================================
# import Rhino.Geometry as rg
# import scriptcontext as sc
#
# tol = sc.doc.ModelAbsoluteTolerance
# solid = brep.CapPlanarHoles(tol)
#
# if solid and solid.SolidOrientation == rg.BrepSolidOrientation.Inward:
#     solid.Flip()
#
# M = solid

# ============================================================
# HUONG DAN GRASSHOPPER - RHINO 7 / GHPYTHON
# ============================================================
# 1. TAO PYTHON SCRIPT COMPONENT MOI
# Double-click canvas -> go "GHPython".
# Trong component:
#   - Tao 1 INPUT dat ten dung: brep
#       Right-click input "brep" -> Type hint: Brep
#       Right-click input "brep" -> Access: Item Access
#   - Tao 1 OUTPUT dat ten: M
#
# 2. NOI DAY
# Noi output T cua component Module 2.5 vao input brep.
# Khong can slider moi.
#
# 3. XEM KET QUA
# M la Brep that nen hien thi truc tiep trong Rhino viewport, khong can Panel.
#
# 4. TEST
# Gia tri: Length = 280, Width = 90, Height = 30, Offset = -2, Trim = 1
# Ket qua: 1 solid kin, 2 dau co nap phang; the tich xap xi khop voi phan test ngoai Rhino.
