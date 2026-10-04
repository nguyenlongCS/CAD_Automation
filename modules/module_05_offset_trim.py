# Module 2.5 - Offset / Trim
# Nhiem vu:
# - Trim: cat bo doan co do dai = trim o 2 dau (mui/got) doc truc Length,
#   bang cach tao lai section tai 2 vi tri cat va bo cac section nam ngoai
# - Offset: mo rong / thu nho tung section theo offset (am = vao trong)
# - Loft lai cac section da xu ly thanh surface
# - Nhan danh sach section tu Module 2.3, tra ve surface da xu ly

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
#
# rects = []
# for c in sections:
#     bb = c.GetBoundingBox(True)
#     rects.append((bb.Min.X, bb.Min.Y, bb.Max.Y, bb.Min.Z, bb.Max.Z))
#
# if trim > 0:
#     base = rg.Brep.CreateFromLoft(
#         sections, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False
#     )[0]
#     bbox = base.GetBoundingBox(True)
#     xa = bbox.Min.X + trim
#     xb = bbox.Max.X - trim
#     ends = []
#     for x in (xa, xb):
#         cut = rg.Brep.CreateContourCurves(base, rg.Plane(rg.Point3d(x, 0, 0), rg.Vector3d.XAxis))
#         bb = rg.Curve.JoinCurves(cut)[0].GetBoundingBox(True)
#         ends.append((x, bb.Min.Y, bb.Max.Y, bb.Min.Z, bb.Max.Z))
#     rects = [ends[0]] + [r for r in rects if xa < r[0] < xb] + [ends[1]]
#
# curves = []
# for x, y0, y1, z0, z1 in rects:
#     y0, y1, z0, z1 = y0 - offset, y1 + offset, z0 - offset, z1 + offset
#     pts = [
#         rg.Point3d(x, y0, z0),
#         rg.Point3d(x, y1, z0),
#         rg.Point3d(x, y1, z1),
#         rg.Point3d(x, y0, z1),
#         rg.Point3d(x, y0, z0)
#     ]
#     curves.append(rg.Polyline(pts).ToNurbsCurve())
#
# loft = rg.Brep.CreateFromLoft(
#     curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False
# )
#
# T = loft[0] if loft else None

# ============================================================
# HUONG DAN GRASSHOPPER - RHINO 7 / GHPYTHON
# ============================================================
# 1. DUNG LAI 2 NUMBER SLIDER TU MODULE 2.1
# Chi can: offset, trim.
#
# 2. PYTHON SCRIPT COMPONENT MODULE 2.5
# Trong component:
#   - 3 INPUT dat ten dung: sections, offset, trim
#       Right-click input "sections" -> Type hint: Curve
#       Right-click input "sections" -> Access: List Access
#   - 1 OUTPUT dat ten: T
#
# 3. NOI DAY
# Noi output S cua component Module 2.3 vao input sections.
# Noi slider offset va trim vao 2 input tuong ung.
#
# 4. XEM KET QUA
# T la Brep that nen hien thi truc tiep trong Rhino viewport, khong can Panel.
#
# 5. TEST
# Gia tri: Offset = -2, Trim = 1
# Ket qua: surface ngan di 1 o moi dau (x tu 1 den 279), thu nho vao trong 2 moi phia,
# van gom 6 section, 2 dau phang de Module 2.6 dong nap.