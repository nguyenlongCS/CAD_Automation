# Module 2.5 - Offset / Trim
# Nhiem vu:
# - Trim: cat bo doan co do dai = trim o 2 dau (mui/got) doc truc Length
# - Offset: offset surface theo phap tuyen, khoang cach = offset (am = vao trong)
# - Nhan surface tu Module 2.4, tra ve surface da xu ly

def compute_offset_trim(length, width, height, offset, trim):
    """Tinh khoang x con lai va kich thuoc sau offset - dung de test doc lap, khong can Rhino."""
    x_start = trim
    x_end = length - trim
    new_width = width + 2 * offset
    new_height = height + 2 * offset
    valid = x_end > x_start and new_width > 0 and new_height > 0
    return x_start, x_end, new_width, new_height, valid


if __name__ == "__main__":
    x_start, x_end, new_width, new_height, valid = compute_offset_trim(
        length=280, width=90, height=30, offset=-2, trim=1
    )

    print("Khoang x con lai:", x_start, "->", x_end)
    print("Width sau offset:", new_width)
    print("Height sau offset:", new_height)
    print("Valid:", valid)


# ============================================================
# CODE TRONG GRASSHOPPER (GHPYTHON / SCRIPT COMPONENT)
# ============================================================
# import Rhino.Geometry as rg
# import scriptcontext as sc
#
# tol = sc.doc.ModelAbsoluteTolerance
# bbox = brep.GetBoundingBox(True)
#
# cut_start = rg.Plane(rg.Point3d(bbox.Min.X + trim, 0, 0), rg.Vector3d(-1, 0, 0))
# cut_end = rg.Plane(rg.Point3d(bbox.Max.X - trim, 0, 0), rg.Vector3d(1, 0, 0))
#
# result = brep
#
# if trim > 0:
#     for plane in (cut_start, cut_end):
#         parts = result.Trim(plane, tol) if result else None
#         result = parts[0] if parts else None
#
# if result and offset != 0:
#     off = rg.Brep.CreateOffsetBrep(result, offset, False, True, tol)
#     result = off[0][0] if off[0] else None
#
# T = result

# ============================================================
# HUONG DAN GRASSHOPPER - RHINO 7 / GHPYTHON
# ============================================================
# 1. DUNG LAI 2 NUMBER SLIDER TU MODULE 2.1
# Chi can: offset, trim.
#
# 2. TAO PYTHON SCRIPT COMPONENT MOI
# Double-click canvas -> go "GHPython".
# Trong component:
#   - Tao 3 INPUT dat ten dung: brep, offset, trim
#       Right-click input "brep" -> Type hint: Brep
#       Right-click input "brep" -> Access: Item Access
#   - Tao 1 OUTPUT dat ten: T
#
# 3. NOI DAY
# Noi output L cua component Module 2.4 vao input brep.
# Noi slider offset va trim vao 2 input tuong ung.
#
# 4. XEM KET QUA
# T la Brep that nen hien thi truc tiep trong Rhino viewport, khong can Panel.
#
# 5. TEST
# Gia tri: Offset = -2, Trim = 1
# Ket qua: surface ngan di 1 o moi dau (x tu 1 den 279), thu nho vao trong 2 theo phap tuyen.
# Offset = 0 va Trim = 0: T giong surface cua Module 2.4.
