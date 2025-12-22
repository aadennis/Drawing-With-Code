# Drawing-With-Code

If you are drawing with code, and then want to see that drawing in a browser, that often means <b>SVG</b>. It does here, anyway.

# But first... Emmet and HTML

Too often, I struggle to remember the `!` and the `html:4` shortcuts, and more.   
Take a look [here](Docs/emmet_101.md) for Emmet examples / cheats.

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

Take a look [here](Docs/snippets.md)



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


