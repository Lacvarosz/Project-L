# Project-L

# **Interaction Markup Language (IML)**
## Building:
 - `[tag]`
  - parameters line to line in this format: `<name>=<value>`
  - Child tags with same inside architecture:
    ```
     [act]
        level=3
        id=Chees
        [react]
            text=I don't lik you
        [/react]
        ...
     [/act]
     ...
     ```
 - `[/tag]`

## Tags
Currently there are two types of tags: `act`, `react`
act
: This writes the NPC's actions, textline.
react
: This is responsible for the PC's answeres. One react scribes a possible chooseble answere.
## Parameters
Its possible to infinite count of parameters, but the program uses only 5 parameters.
text
: This is the text of an action. *(text)*
level
: This is the level of activation, its possible to change this level during the conversation. Only that possibilitys activated, whiches have lower activation level as the interaction level. *(integer)*
id
: We can use id if we want to refer this action later in the code.
connect *(text)*
: Here needs an existing id. The action with this id will be a childe of this action. We can refer back previous actions.
repetable *(existing `id`)*
: This parameter responsible for set action repetable or no. Default repetable is true. *(yes, no)*
