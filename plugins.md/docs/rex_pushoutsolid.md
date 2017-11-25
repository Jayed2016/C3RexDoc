## Introduction

Push object out from solid object.

Icon: [Icons8](https://icons8.com/)

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_pushoutsolid.c3addon)

## Dependence

None

## Usage

### Obstacles

- Property `Obstacles`
    - `Solids` : instance with [official solid behavior](https://www.scirra.com/manual/104/solid).  ([sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHlz27EElJmoeevxWA))
    - `Custom` : `Action:Add obstacle`
        - `Action:Clear obstacles`

### Push out

- Property `Activated`
    - `Yes` : push out nearest every tick
    - `No`  ([sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHlz-qvpmmiytPyCK3))
        - `Action:Push out nearest`
        - `Action:Push out at angle`
        - `Action:Push out toward position`