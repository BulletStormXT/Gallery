# script to generate index.html with 52 gallery items

def make_gallery():
    out = []
    out.append('<!doctype html>')
    out.append('<html lang="de">')
    out.append('  <head>')
    out.append('    <meta charset="UTF-8" />')
    out.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0" />')
    out.append('')
    out.append('    <title>Gallery</title>')
    out.append('')
    out.append('    <link rel="stylesheet" href="main.css" />')
    out.append('    <link')
    out.append('      rel="stylesheet"')
    out.append('      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"')
    out.append('    />')
    out.append('  </head>')
    out.append('  <body>')
    out.append('    <h1>Gallery</h1>')
    out.append('    <p>Hier könnte Ihre Galerie sein!</p>')
    out.append('')
    out.append('    <div class="thumbs">')
    for i in range(1,53):
        num = str(i).zfill(4)
        out.append(f'      <a href="#target{i}"><img src="/img/deko/{num}.webp" alt="" /></a>')
    out.append('    </div>')
    out.append('')
    out.append('    <div class="lightbox">')
    for i in range(1,53):
        num = str(i).zfill(4)
        out.append(f'      <div class="target" id="target{i}">')
        if i == 1:
            out.append('        <span></span>')
        else:
            out.append(f'        <a href="#target{i-1}" class="nav" title="previous"><i class="fa-solid fa-chevron-left"></i></a>')
        out.append('        <div class="content">')
        out.append(f'          <img src="/img/deko/{num}.webp" alt="">')
        out.append('        </div>')
        if i == 52:
            out.append('        <span></span>')
        else:
            out.append(f'        <a href="#target{i+1}" class="nav" title="next"><i class="fa-solid fa-chevron-right"></i></a>')
        out.append('      </div>')
    out.append('      <a href="#" class="close" title="close"><i class="fa-solid fa-times"></i></a>')
    out.append('    </div>')
    out.append('  </body>')
    out.append('</html>')
    return "\n".join(out)

if __name__ == '__main__':
    with open('index.html','w') as f:
        f.write(make_gallery())
    print('index.html regenerated')
