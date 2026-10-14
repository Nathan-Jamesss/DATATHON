import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
L = open('mkppt.py', encoding='utf-8').read().split('\n')
def idx(sub): return [i for i, l in enumerate(L) if sub in l][0]

# content slides: no team-name oval; DSC logo left, IIEC logo right, vertically aligned
i = idx('oval = rect(s, 0.4, 0.3')
L[i:i + 2] = []                       # drop oval + its text
i = idx('txt(s, 2.1, 0.25, 8.1, 0.95, title')
L[i] = '    txt(s, 1.95, 0.25, 9.4, 0.95, title, size=30, font=DISPLAY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)'
i = idx('logo-dsc-light.png"), Inches(10.2)')
L[i] = '    s.shapes.add_picture(os.path.join(A, "logo-dsc-light.png"), Inches(0.45), Inches(0.15), height=Inches(1.0))'
i = idx('logo-iiec-light.png"), Inches(11.7)')
L[i] = '    s.shapes.add_picture(os.path.join(A, "logo-iiec-light.png"), Inches(11.2), Inches(0.35), height=Inches(0.62))'
# title slide: align the three logos on one centre line, equal side margins
i = idx('logo-dsc-light.png"), Inches(0.7)')
L[i] = 's.shapes.add_picture(os.path.join(A, "logo-dsc-light.png"), Inches(0.55), Inches(0.25), height=Inches(1.15))'
i = idx('logo-iiec-light.png"), Inches(10.3)')
L[i] = 's.shapes.add_picture(os.path.join(A, "logo-iiec-light.png"), Inches(10.75), Inches(0.5), height=Inches(0.75))'
open('mkppt.py', 'w', encoding='utf-8').write('\n'.join(L))

# darker, solid IIEC logo
g = open('make_light_logos.py', encoding='utf-8').read()
a = "            else:                    # coloured artwork (pink brains, red IIEC) -> keep colour, un-premultiply\n                al = min(1.0, a * 1.6)\n                f = 255.0 / mx\n"
assert a in g
b = ("            elif name == 'logo-iiec':  # solid dark red, like the original lettering\n"
     "                f = 175.0 / mx\n"
     "                op[x, y] = (min(255, int(r * f)), min(255, int(g * f)), min(255, int(b * f)), min(255, int(mx * 5)))\n"
     "                continue\n" + a)
g = g.replace(a, b)
open('make_light_logos.py', 'w', encoding='utf-8').write(g)
print('ok')
