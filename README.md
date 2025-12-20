# Drawing-With-Code

If you are drawing with code, and then want to see that drawing in a browser, that often means <b>SVG</b>. It does here, anyway.

## Drawing with SVG

[MDN: Credit for the tutorial on SVG Paths](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Paths)   

MDN is simply the place to go.   
This MDN page shows simple boilerplate for a rectangle, a circle, and some text:   
(https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Getting_started)   

```svg
<svg version="1.1"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" fill="red" />
  <circle cx="150" cy="100" r="80" fill="green" />
  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>

</svg>
```
The next MDN page I selected expands to include polygon, polyline, and path elements ...    
(https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Basic_shapes)    

```svg
<svg width="200" height="250" version="1.1" xmlns="http://www.w3.org/2000/svg">

  <rect x="10" y="10" width="30" height="30" stroke="black" fill="transparent" stroke-width="5"/>
  <rect x="60" y="10" rx="10" ry="10" width="30" height="30" stroke="black" fill="transparent" stroke-width="5"/>

  <circle cx="25" cy="75" r="20" stroke="red" fill="transparent" stroke-width="5"/>
  <ellipse cx="75" cy="75" rx="20" ry="5" stroke="red" fill="transparent" stroke-width="5"/>

  <line x1="10" x2="50" y1="110" y2="150" stroke="orange" stroke-width="5"/>
  <polyline points="60 110 65 120 70 115 75 130 80 125 85 140 90 135 95 150 100 145"
      stroke="orange" fill="transparent" stroke-width="5"/>

  <polygon points="50 160 55 180 70 180 60 190 65 205 50 195 35 205 40 190 30 180 45 180"
      stroke="green" fill="transparent" stroke-width="5"/>

  <path d="M20,230 Q40,205 50,230 T90,230" fill="none" stroke="blue" stroke-width="5"/>
</svg>
```

## Some simple examples

Take a look [here](Docs/examples_101.md)


<hr>

## Remembering snippets

Well, you can't remember them all. Here is a list for plugging into VSCode. The unimaginative '...full' at the end of each prefix is to prevent conflict with the SVG reserved words. 

```json   
{
  "Circle primitive": {
    "prefix": "circlefull",
    "body": [
      "<circle cx=\"50\" cy=\"50\" r=\"24\" />"
    ],
    "description": "SVG circle with default attributes"
  },
  "Rectangle primitive": {
    "prefix": "rectfull",
    "body": [
      "<rect x=\"0\" y=\"0\" width=\"100\" height=\"50\" />"
    ],
    "description": "SVG rectangle"
  },
  "Line primitive": {
    "prefix": "linefull",
    "body": [
      "<line x1=\"0\" y1=\"0\" x2=\"100\" y2=\"100\" />"
    ],
    "description": "SVG line"
  },
  "Path primitive": {
    "prefix": "pathfull",
    "body": [
      "<path d=\"M10 10 H 90 V 90 H 10 Z\" />"
    ],
    "description": "SVG path"
  },
  "Text primitive": {
    "prefix": "textfull",
    "body": [
      "<text x=\"10\" y=\"20\">Sample</text>"
    ],
    "description": "SVG text element"
  },
  "Polygon primitive": {
    "prefix": "polygonfull",
    "body": [
      "<polygon points=\"50,5 100,100 0,100\" />"
    ],
    "description": "SVG polygon"
  },
  "Polyline primitive": {
    "prefix": "polylinefull",
    "body": [
      "<polyline points=\"0,0 50,25 50,75 100,100\" />"
    ],
    "description": "SVG polyline"
  },
  "Ellipse primitive": {
    "prefix": "ellipsefull",
    "body": [
      "<ellipse cx=\"50\" cy=\"50\" rx=\"25\" ry=\"15\" />"
    ],
    "description": "SVG ellipse"
  },
  "Group element": {
    "prefix": "groupfull",
    "body": [
      "<g>",
      "  $0",
      "</g>"
    ],
    "description": "SVG group wrapper"
  },
  "Defs block": {
    "prefix": "defsfull",
    "body": [
      "<defs>",
      "  <style>",
      "    <![CDATA[",
      "      /* CSS here */",
      "    ]]>",
      "  </style>",
      "</defs>"
    ],
    "description": "SVG defs block with embedded style"
  },
  "Defs gradient": {
    "prefix": "defsgra",
    "body": [
      "<defs>",
      "  <linearGradient id=\"grad1\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"0%\">",
      "    <stop offset=\"0%\" style=\"stop-color:rgb(255,255,0);stop-opacity:1\" />",
      "    <stop offset=\"100%\" style=\"stop-color:rgb(255,0,0);stop-opacity:1\" />",
      "  </linearGradient>",
      "</defs>"
    ],
    "description": "SVG linear gradient inside defs"
  },
  "Symbol definition": {
    "prefix": "symbolfull",
    "body": [
      "<symbol id=\"icon-star\" viewBox=\"0 0 24 24\">",
      "  <path d=\"M12 2 L15 9 H22 L17 14 L19 21 L12 17 L5 21 L7 14 L2 9 H9 Z\" />",
      "</symbol>"
    ],
    "description": "Reusable symbol definition"
  },
  "Use symbol": {
    "prefix": "usefull",
    "body": [
      "<use href=\"#icon-star\" x=\"0\" y=\"0\" width=\"24\" height=\"24\" />"
    ],
    "description": "Reference a defined symbol"
  },
  "ClipPath definition": {
    "prefix": "clipfull",
    "body": [
      "<clipPath id=\"clip1\">",
      "  <circle cx=\"50\" cy=\"50\" r=\"40\" />",
      "</clipPath>"
    ],
    "description": "Reusable clipPath definition"
  },
  "Mask definition": {
    "prefix": "maskfull",
    "body": [
      "<mask id=\"mask1\">",
      "  <rect x=\"0\" y=\"0\" width=\"100\" height=\"100\" fill=\"white\" />",
      "  <circle cx=\"50\" cy=\"50\" r=\"40\" fill=\"black\" />",
      "</mask>"
    ],
    "description": "Reusable mask definition"
  },
  "Pattern definition": {
    "prefix": "patternfull",
    "body": [
      "<pattern id=\"pattern1\" patternUnits=\"userSpaceOnUse\" width=\"10\" height=\"10\">",
      "  <rect width=\"10\" height=\"10\" fill=\"white\" />",
      "  <circle cx=\"5\" cy=\"5\" r=\"3\" fill=\"lightgray\" />",
      "</pattern>"
    ],
    "description": "Reusable pattern for fills"
  },
  "Filter definition": {
    "prefix": "filterfull",
    "body": [
      "<filter id=\"blurFilter\" x=\"0\" y=\"0\" width=\"200%\" height=\"200%\">",
      "  <feGaussianBlur in=\"SourceGraphic\" stdDeviation=\"5\" />",
      "</filter>"
    ],
    "description": "Reusable filter (Gaussian blur)"
  },
  "Marker definition": {
    "prefix": "markerfull",
    "body": [
      "<marker id=\"arrowhead\" markerWidth=\"10\" markerHeight=\"7\" refX=\"10\" refY=\"3.5\"",
      "    orient=\"auto\" markerUnits=\"strokeWidth\">",
      "  <path d=\"M0,0 L10,3.5 L0,7 Z\" fill=\"black\" />",
      "</marker>"
    ],
    "description": "Reusable marker (arrowhead)"
  },
  "Use marker": {
    "prefix": "usemarker",
    "body": [
      "<line x1=\"10\" y1=\"10\" x2=\"100\" y2=\"100\"",
      "    stroke=\"black\" stroke-width=\"2\"",
      "    marker-end=\"url(#arrowhead)\" />"
    ],
    "description": "Line using a defined marker"
  },
  "SVG root element": {
    "prefix": "svgfull",
    "body": [
      "<svg xmlns=\"http://www.w3.org/2000/svg\"",
      "     width=\"${1:200}\" height=\"${2:200}\"",
      "     viewBox=\"0 0 ${1:200} ${2:200}\"",
      "     version=\"1.1\">",
      "  $0",
      "</svg>"
    ],
    "description": "SVG root element with width, height, and viewBox"
  }
}
```

## Where am I going with all this svg malarkey?
Firstly, I want to use my own guitar tablature templates. Sure, it's a lot of effort for little reward (you can simply buy 100 sheets of blank tab say for £5), but the reward is in getting familiar enough with svg to use it casually for diagrams. Yes, there is Mermaid, but that satisfies different use-cases, normally.

## Rendering from svg into png
Having tried Inkscape, and a couple of other methods, the absolutely best solution for rendering from svg into png is the linux utility `rsvg-convert`.  
Basic usage for that is `rsvg-convert -o output.png input.svg`.  
As an example, this is the svg as rendered in an Edge browser :

<img width="200" alt="image" src="https://github.com/user-attachments/assets/7ce9beda-972e-4e42-a65c-d75efc9d6285" />  

The actual command used to render the svg to to png (note, this is Ubuntu - WSL on Windows 11):  
`rsvg-convert -o output.png svg02.svg`  

And the resulting .png, showing me that I need to tidy up the borders of each grid:  

<img width="400" height="918" alt="image" src="https://github.com/user-attachments/assets/5f31e5c3-40a6-4980-9e56-aa703ba10d46" />  

<img width="600" height="1174" alt="image" src="https://github.com/user-attachments/assets/fb0b99e5-bca0-4bb2-b7d9-2444a593ddac" />


