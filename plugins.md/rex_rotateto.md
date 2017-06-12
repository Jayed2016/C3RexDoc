# [Categories](categories.index.html) > [Movement](movement.index.html) > rex_rotateto

## Introduction

Spin object to specific angle.

Icon: [Icons8](https://icons8.com/)

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_rotateto.c3addon)

----

[TOC]

## Dependence

None

## Usage

```mermaid
graph TB
Start["Rotate start<br>----<br>Action:Rotate to angle<br>Action:Rotate by delta angle<br>Action:Rotate to object<br>Action:Rotate toward to position"] --> Moving((+Every tick<br>-Set angle))
Moving --> |Reaching target| OnHitTarget["Condition:On hit target angle"]
```

### Rotate start
[Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHl0FW4b_JRRBQogVM)

- `Action:Rotate to angle`
- `Action:Rotate by delta angle`
- `Action:Rotate to object` 
- `Action:Rotate toward to position`

Target angle is `Expression:TargetAngle`

### Reach target

- `Condition:On hit target angle`

### Stop

- `Action:Stop`

### Pause

- `Action:Set enabled` and set parameter  `State` to `Disabled`

### Resume

- `Action:Set enabled` and set parameter  `State` to `Enabled `