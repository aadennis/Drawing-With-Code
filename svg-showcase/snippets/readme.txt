How to edit an existing snippet?
1. You will have saved the collection of snippets as a versioned file. E.g. svg.json.code-snippets
2. Locate and edit that file
3. as an example, in that file, say you currently have"Rectangle primitive": {
    "prefix": "rectfull",
    "body": [
      "<rect x=\"0\" y=\"0\" width=\"100\" height=\"50\" />"
    ],
    "description": "SVG rectangle"
  },
  and you edit and change the height value from "50" to "51"
4a.   control shift p - Snippets: Configure Snippets
4b.  Select and open the file that sounds closest to your existing file - ideally it will be the same name.
The difference is the VS version you have just opened is not versioned, because it lives in a location such as:
   C:\Users\[YourUser]\AppData\Roaming\Code\User\snippets
4c. So ctrl-A, ctrl-C in the versioned file (with your edits that you will commit once you have tested the change)
4d. ctrl-A, delete all, ctrl-V in the VS code file (the 'roaming' version), checking that your edit has taken
5. Test the change: the prefix of the changed snippet is 'rectfull'. Start a blank x.svg (this is not about How 
to configure intellisense etc, so you are on your own there, right now).
As you start to type 'rect', all snippets, but also plain old words, that start with 'rect' will appear. 
If things are working correctly, one of those entries will be 'rectfull', plus the description of 'SVG rectangle', 
as in the example above. Move the cursor to that selection, and hit return.
6. x.svg should now contain the single line:
<rect x="0" y="0" width="100" height="51" />
