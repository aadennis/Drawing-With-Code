# Drawing-With-Code

If you are drawing with code, then in a browser, that probably means <b>SVG</b>. It does here, anyway.

[MDN: Credit for the tutorial on SVG Paths](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Paths)   

Firstly, I use svg to draw a template for tablature on a guitar fretboard. 

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


