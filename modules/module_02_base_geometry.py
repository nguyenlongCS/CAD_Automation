# Module 2.2 - Base Geometry Generation
# Nhiem vu:
# - Tao geometry co ban (Rectangle + Box) tu Length, Width, Height da validate
# - Lam nen cho cac module Section / Surface phia sau

try:
    import Rhino.Geometry as rg
except ImportError:
    rg = None  # Cho phep chay test doc lap khong can Rhino


class BaseGeometry(object):

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.base_rectangle = None
        self.base_box = None

    def generate(self):

        L = self.length
        W = self.width
        H = self.height

        if rg is None:
            # Khong co Rhino -> tra ve toa do 4 goc de test doc lap
            self.base_rectangle = [
                (0, -W / 2.0, 0),
                (L, -W / 2.0, 0),
                (L, W / 2.0, 0),
                (0, W / 2.0, 0)
            ]
            self.base_box = None
            return self.base_rectangle, self.base_box

        # Rectangle nam tren mat phang XY, goc tai (0,0), tam theo chieu rong
        plane = rg.Plane.WorldXY
        self.base_rectangle = rg.Rectangle3d(
            plane, rg.Interval(0, L), rg.Interval(-W / 2.0, W / 2.0)
        )

        # Box lam khung tham chieu (chua phai hinh dang cuoi cung cua de giay)
        self.base_box = rg.Box(
            plane, rg.Interval(0, L), rg.Interval(-W / 2.0, W / 2.0), rg.Interval(0, H)
        )

        return self.base_rectangle, self.base_box


# --------------------------------------------------
# TEST (chay doc lap, khong can Grasshopper)
# --------------------------------------------------
if __name__ == "__main__":
    geo = BaseGeometry(length=280, width=90, height=30)
    rect, box = geo.generate()

    print("Base rectangle (4 goc):")
    for p in rect:
        print(" ", p)
    print("Base box:", box)


# ============================================================
# CODE TRONG GRASSHOPPER (GHPYTHON / SCRIPT COMPONENT)
# ============================================================
# import Rhino.Geometry as rg
#
# class BaseGeometry(object):
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height
#     def generate(self):
#         plane = rg.Plane.WorldXY
#         rect = rg.Rectangle3d(
#             plane, rg.Interval(0, self.length),
#             rg.Interval(-self.width / 2.0, self.width / 2.0)
#         )
#         box = rg.Box(
#             plane, rg.Interval(0, self.length),
#             rg.Interval(-self.width / 2.0, self.width / 2.0),
#             rg.Interval(0, self.height)
#         )
#         return rect, box
#
# geo = BaseGeometry(length, width, height)
# rect, box = geo.generate()
# R = rect
# X = box

# ============================================================
# HUONG DAN GRASSHOPPER - RHINO 7 / GHPYTHON
# ============================================================
# 1. DUNG LAI 3 NUMBER SLIDER TU MODULE 2.1
# Chi can: length, width, height (section_position/offset/trim chua dung o module nay).
#
# 2. TAO PYTHON SCRIPT COMPONENT MOI
# Double-click vao canvas -> go "GHPython".
# Trong component:
#   - Tao 3 INPUT dat ten dung: length, width, height
#   - Tao 2 OUTPUT dat ten: R (rectangle), X (box)
# Noi 3 slider (length, width, height) vao 3 input tuong ung.
#
# 3. CODE GHPYTHON
# Paste toan bo class BaseGeometry + doan code o muc
# "CODE DUNG TRONG GRASSHOPPER" o tren vao component.
#
# 4. XEM KET QUA
# Khac voi Module 2.1 (chi ra text), o day R va X la geometry that
# nen Grasshopper se tu dong hien thi Rectangle va Box ngay trong
# Rhino viewport - khong can Panel.
# Neu khong thay gi: bam phim "P" tren component de bat/tat preview.
#
# 5. TEST
# Gia tri:
#   Length = 280
#   Width  = 90
#   Height = 30
#
# Ket qua:
#   - R: hinh chu nhat 280 x 90, tam theo truc doc, dat tai goc (0,0)
#   - X: khoi hop 280 x 90 x 30 dung lam khung tham chieu cho Module 2.3 (Section)
