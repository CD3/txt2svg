import click
from lxml import etree
import pathlib
import fileinput
import sys

@click.command()
@click.option("--output","-o", default="txt2svg-out.svg", help="Output filename.")
@click.argument("input",type=click.Path(exists=True),nargs=-1)
def main(output,input):

  font_size = 12
  line_hieght = 15
  leftcol = 20
  XMLNS = "{http://www.w3.org/XML/1998/namespace}"
  INKNS = "{https://sozi.baierouge.fr/}"

  out = pathlib.Path(output)
  img = etree.Element('svg',
      nsmap={None: 'http://www.w3.org/2000/svg',
      'xlink': 'http://www.w3.org/1999/xlink'})
  img.set('version', '2')
  img.set('baseProfile', 'full')


  maxcol = 0
  lino = 1
  for file in input:
    path = pathlib.Path(click.format_filename(file))
    text = path.read_text()
    grp = etree.SubElement(img,'g')
    grp.set("filename",file)
    grp.set("id",file)
    grp.set(INKNS+"groupmode","layer")


    textelem = etree.SubElement(grp,'text')
    textelem.set("x",f"{leftcol}")
    textelem.set("y",f"{lino*line_hieght}")
    textelem.set("style","fill:black")
    textelem.set("font-size",f"{font_size}")
    textelem.set("font-family","monospace")
    textelem.set(XMLNS+"space","preserve")


    tspan = etree.SubElement(textelem,'tspan')
    tspan.set("x",f"{leftcol}")
    tspan.set("dy",f"{2*line_hieght}")
    tspan.set("font-size",f"{2*font_size}")
    tspan.text = file
    tspan = etree.SubElement(textelem,'tspan')
    tspan.set("x",f"{leftcol}")
    tspan.set("dy",f"{line_hieght}")
    tspan.text = " "
    lino += 3
    for line in text.split("\n"):
      lino += 1
      print(lino)
      if line == "":
        line = " "
      if len(line) > maxcol:
        maxcol = len(line)
      tspan = etree.SubElement(textelem,'tspan')
      tspan.set("x",f"{leftcol}")
      tspan.set("dy",f"{line_hieght}")
      tspan.text = line


  out.write_bytes(etree.tostring(img,xml_declaration=True,pretty_print=True,encoding='utf-8'))
