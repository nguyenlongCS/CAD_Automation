# Module 2.1 - Parameter Input & Validation
# Nhiem vu:
# - Luu thong so de giay
# - Kiem tra thong so co hop le hay khong


class SoleParameters(object):

    def __init__(self, length, width, height,
                 section_position, offset=0, trim=0):

        self.length = length
        self.width = width
        self.height = height
        self.section_position = section_position
        self.offset = offset
        self.trim = trim

    def validate(self):

        errors = []

        # 1. Kiem tra kich thuoc
        if self.length <= 0:
            errors.append("Length phai > 0")

        if self.width <= 0:
            errors.append("Width phai > 0")

        if self.height <= 0:
            errors.append("Height phai > 0")

        # 2. Section Position phai nam trong chieu dai
        if not (0 <= self.section_position <= self.length):
            errors.append("Section Position phai nam trong Length")

        # 3. Trim khong duoc am
        if self.trim < 0:
            errors.append("Trim khong duoc am")

        # 4. Offset khong duoc qua lon
        if abs(self.offset) >= self.width / 2:
            errors.append("Offset qua lon")

        # Ket qua
        if len(errors) == 0:
            return True, errors
        else:
            return False, errors


# --------------------------------------------------
# TEST
# --------------------------------------------------

params = SoleParameters(
    length=280,
    width=90,
    height=30,
    section_position=140,
    offset=-2,
    trim=1
)

valid, errors = params.validate()

print("Valid:", valid)

if not valid:
    for error in errors:
        print("Error:", error)

# ============================================================
# HUONG DAN GRASSHOPPER - RHINO 7 / GHPYTHON
# ============================================================
# 1. TAO 6 NUMBER SLIDER
# Double-click vao canvas Grasshopper -> go "Number Slider".
# Tao 6 slider va Right-click vao slider -> Rename:
#   length
#   width
#   height
#   section_position
#   offset
#   trim
# Double-click vao moi slider de chinh:
#   - Min
#   - Max
#   - Value
# Vi du:
#   Length:
#       Min = 100
#       Max = 400
#       Value = 280
#   Width:
#       Min = 50
#       Max = 150
#       Value = 90
#   Height:
#       Min = 10
#       Max = 60
#       Value = 30
#   Section Position:
#       Min = 0
#       Max = 280
#       Value = 140
#   Offset:
#       Min = -40
#       Max = 40
#       Value = -2
#   Trim:
#       Min = 0
#       Max = 20
#       Value = 1
#
# 2. TAO GHPYTHON
# Double-click vao canvas -> go "GHPython".
# Right-click vao cac input cua GHPython -> Rename thanh:
#   len
#   width
#   height
#   section_postion
#   offset
#   trim
# Noi 6 Number Slider vao 6 input tuong ung.
#
# 3. CODE GHPYTHON
# Copy class SoleParameters va ham validate() vao GHPython.
#
# Cuoi code them:
#     params = SoleParameters(Len, Width, Height, Section_Postion, Offset, Trim)
#     valid, errors = params.validate()
#     A = valid
#     B = errors
#
# 4. TAO PANEL
# Double-click vao canvas -> go "Panel".
# Noi output A vao Panel de xem:
#     True / False
# Tao Panel thu hai va noi output B vao Panel
# de xem danh sach loi.
#
# 5. TEST
# Gia tri ban dau:
#   Length           = 280
#   Width            = 90
#   Height           = 30
#   Section Position = 140
#   Offset           = -2
#   Trim             = 1
#
# Ket qua:
#   Valid = True
# Thu thay doi Trim = -5:
#   Valid = False
#   Trim khong duoc am