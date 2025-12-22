## Emmet cheats

## Boilerplate
- `!` → HTML5 skeleton  
- `html:5` → same as above, explicit

## Elements
- `div` → `<div></div>`
- `p` → `<p></p>`
- `a` → `<a href=""></a>`
- `img` → `<img src="" alt="">`

## Nesting
- `div>ul>li*3` → parent > child > siblings  
- `section>h1+p` → semantic block with heading + paragraph  
- `nav>ul>li*5>a` → menu scaffold

## Siblings
- `h1+p+footer` → same level, sequential

## Climb Up
- `div>p>span^a` → go up one level  
- `div>p>span^^footer` → go up two

## Attributes
- `input:text` → `<input type="text">`  
- `input:email` → `<input type="email">`  
- `a:link` → `<a href="http://"></a>`  
- `.class