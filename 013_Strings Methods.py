# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(len(a))
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)  # 1
print(d)  # 11
print(e)  # 111
print(f)  # 1111

print(c.zfill(4))  # 0001
print(d.zfill(4))  # 0011
print(e.zfill(4))  # 0111
print(f.zfill(4))  # 1111

# upper()

g = "osama"

print(g.upper())

# lower()

h = "OSama"

print(h.lower())
