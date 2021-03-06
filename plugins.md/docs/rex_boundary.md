## Introduction

Clamp or wrap position.

Icon: [Icons8](https://icons8.com/)

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_boundary.c3addon)

## Dependence

None

## Usage

```mermaid
graph TB

EveryTick((Every tick)) --> InBoundaries{"In boundaries"}
InBoundaries --> |Yes| EveryTick
InBoundaries --> |No| PropertyMode{"Property:<br>Mode"}
PropertyMode --> |Clamp| ClampPos["Clamp at this boundary"]
PropertyMode --> |Wrap| WrapPos["Warp to opposite boundary"]
PropertyMode --> |Mod wrap| WrapMod["Warp to opposite boundary with offset"]

ClampPos --> EveryTick
WrapPos --> EveryTick
WrapMod --> EveryTick
```

[Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHl3WZix2QP92s70WM)

### Set boundaries

- Horizontal

    - Enable
        - Set property `Horizontal` to `Yes`, or
        - `Action:Horizontal boundary enable`
        - `Expression:HorizontalEnable`
    - Boundaries
        - Property `Left`, property `Right`, or
        - `Action:Set horizontal boundary`, or
        - `Action:Set horizontal boundary to`
            - Pin boundaries on an object
        - `Expression:LeftBound`, `Expression:RightBound`

- Vertical

    - Enable
        - Set property `Vertical` to `Yes`, or
        - `Action:Vertical boundary enable`
        - `Expression:VerticalEnable`
    - Boundaries
        - Property `Top`, property `Bottom`, or
        - `Action:Set vertical boundary`, or
        - `Action:Set vertical boundary to`
            - Pin boundaries on an object
        - `Expression:TopBound`, `Expression:BottomBound`


### Mode

When position is out of boundary

- Property `Mode`
    - `Clamp` : clamp position in the boundary
        - Property `Align`
            - `Boundaries` : align boundaries box of this object to reached boundary
            - `Origin` : set position to reached boundaries
    - `Wrap`
        - Property `Align`
            - `Boundaries` : align boundaries box of this object to *opposite* boundary
                - This behavior is similar with [official wrap behavior]      (https://www.scirra.com/manual/105/wrap)
            - `Origin` : set position to *opposite* boundary
    - `Mode wrap`  ([sample capx]())
        - Property `Align`
            - `Boundaries` : *not supported*
            - `Origin` : set position to *opposite* boundary with an offset to keep the moving   distance
- Triggers
    - `Condition:On hit any boundary`
    - `Condition:Is hit boundary`
    - Horizontal
        - `Condition:On hit left boundary`
        - `Condition:On hit right boundary`
    - Vertical
        - `Condition:On hit top boundary`
        - `Condition:On hit bottom boundary`

----

### Position and percentage

```mermaid
graph TB

X --> |Expression:HorPercent| Percentage["Percentage<br>0..1"]
Percentage --> |Expression:HorPercent2PosX| X

Percentage --> |Expression:HorScale| Value
```

```mermaid
graph TB

Y --> |Expression:VerPercent| Percentage["Percentage<br>0..1"]
Percentage --> |Expression:HorPercent2PosY| Y

Percentage --> |Expression:VerScale| Value
```

#### Position --> percentage

- `Expression:HorPercent` : ( inst.X - left ) / ( right - left )
    - `Expression:HorScale` : map `Expression:HorPercent` to another value
- `Expression:VerPercent` : ( inst.Y - top ) / ( bottom - top )
    - `Expression:VerScale` : map `Expression:VerPercent` to another value

#### Percentage --> position

[Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHl3R9cqOgFaC80UtE)

- `Expression:HorPercent2PosX` : percentage --> X  
- `Expression:HorPercent2PosY` : percentage --> Y