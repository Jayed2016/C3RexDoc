# [Categories](categories.index.html) > [Movement](movement.index.html) > rex_platform_moveto

## Introduction

Move platformer to specific position.

Icon: [Icons8](https://icons8.com/)

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_platform_moveto.c3addon)


----

[TOC]

## Dependence

- [Official platform behavior](https://www.scirra.com/manual/100/platform)

## Usage

### Prepare

Put this behavior under [official platform behavior](https://www.scirra.com/manual/100/platform).

### Move to target

```mermaid
graph TB

Start["Moving start<br>----<br>Action:Move to X<br>Action:Move to object<br>Action:Move to delta X<br>Action:Move to distance"] --> Moving((+Every tick<br>-Action:Simulate control<br><Official platform behavior>))
Moving --> |Reaching target| OnHitTarget["Condition:On hit target position"]
```



[Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHl0h3Efu750KumV0N)

Call One of these action to move platformer to target position by `Action:Simulate control` of [official platform behavior](https://www.scirra.com/manual/100/platform).

- `Action:Move to X`
- `Action:Move to object`
- `Action:Move to delta X`
- `Action:Move to distance`

Target position is (`Expression:TargetX` , `Expression:TargetY`).

### Reach target

- `Condition:On hit target position`

### Stop

- `Action:Stop`