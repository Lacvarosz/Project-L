# Project-L

## **Interaction Markup Language (IML)**
### Building:
 - `[interaction]`
 - `[tag]`
  - parameters line to line in this format: `<name>=<value>`
  - Child tags with same inside architecture:
    ```
     [tag]
        <param1>=<value>
        <param2>=<value>
        [tag]
            <param1>=<value>
        [/tag]
        ...
     [/tag]
     ...
     ```
 - `[/tag]`
 - `[/interaction]`

### Tags
Currently there are two types of tags: `act`, `react`

- act
: This writes the NPC's actions, textline.

- react
: This is responsible for the PC's answeres. One react scribes a possible chooseble answere.

### Parameters
Its possible to define infinite amount of parameters, but the program only uses 5 parameters.

- text *(text)*
: This is the text of an action. 

- level *(integer)*
: This is the level of activation, its possible to change this level during the conversation. Only that possibilitys activated, whiches have lower activation level as the interaction level.

- id *(text)*
: We can use id if we want to refer this action later in the code. 

- connect *(existing `id`)*
: Here needs an existing id. The action with this id will be a childe of this action. We can refer back previous actions.

- repetable *(yes, no)*
: This parameter responsible for set action repetable or no. Repetable is yes by default. 
### Example
```
[interaction]
    [act]
        text=Helló, hogy vagy?
        level=0
        [react]
            text=Köszi, jól.
            id=Kecske
        [/react] #Edd ki a levest
        [react]
            text=Szomorúan.
            [act]
                text=Mondjak egy viccet?
                connect=Kecske
                [react]
                    text=Na már csak az hiányzik!
                [/react]
            [/act]
        [/react]
    [/act]
    [act]
        text=Legyen szép napod!
        connect=Kecske
    [/act]
[/interaction]
```