## SVG: Some simple examples

To execute the examples, wrap them in this snippet - see `# example here`
```svg
<svg xmlns="http://www.w3.org/2000/svg"
     width="200" height="200"
     viewBox="0 0 200 200">

<defs>
  <style>
  .thin { stroke: #000000; stroke-opacity: 0.55; stroke-width: 1 }
  .thick { stroke: #990000; stroke-opacity: 1; stroke-width: 2} 
  .box { fill: green; opacity: 0.4}
  </style>
</defs>
# example here
</svg>
```
### Example 1
```svg
<rect class="box" x="100" y="100" width="100%" height="100%"></rect>
```
<img width="108" alt="image" src="https://github.com/user-attachments/assets/82915d4c-f9e2-4b85-9a6e-ecdb52eec140" />
<hr>

### Example 2
In this example, although `fill` is a valid attribute, you see no `green` because fill only applies to enclosed shapes: here there is just a line.
```svg
<rect class="box" x="100" y="100" width="100%" height="100%"></rect>
<path class="thick" d="M 20 20 L 50 50" fill="green"></path>
```

<img width="108" alt="image" src="https://github.com/user-attachments/assets/443668ee-4f0e-4039-a4bc-4aac6b6725f0" />

<hr>

### Example 3
The `green fill` happens here, because the line resolves to a triangle, thank to the `Z`, enclosing everything.
```svg
<rect class="box" x="100" y="100" width="100%" height="100%"></rect>
<path class="thick" d="M 20 20 L 50 50" fill="green"></path>
<path d="M 100 90 h 85 v -80 Z" fill="green" stroke="black"/> 
```

<img width="108" alt="image" src="https://github.com/user-attachments/assets/7545747b-ddb3-4d2d-9ee8-192ff69bbf74" />


<hr>


