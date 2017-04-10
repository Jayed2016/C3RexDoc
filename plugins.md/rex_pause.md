# [Categories](categories.index.html) > [System](system.index.html) > rex_pause

## Introduction

Pause/resume system by setting [timescale](https://www.scirra.com/tutorials/67/delta-time-and-framerate-independence#h2a5).

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_pause.c3addon)


----

[TOC]

## Dependence

None

## Usage

```mermaid
graph TB

StateRun["Run"] --> |"Pause<br> <br>Action:Set state (Pause)<br>Action:Toggle state"| TransitionRun2Pause["Run --> Pause<br>(Save timescale,Set timescale to 0) <br>Condition:On pause"]
TransitionRun2Pause --> StatePause["Pause"]
StatePause --> |"Resume<br> <br>Action:Set state (Run)<br>Action:Toggle state"| TransitionPause2Run["Pause --> Run<br>(Restore timescale)<br>Condition:On resume"]
TransitionPause2Run --> StateRun

subgraph State
StateRun
end

subgraph State
StatePause
end
```

[Sample capx](https://onedrive.live.com/redir?resid=7497FD5EC94476E!536&authkey=!AHOh24sxVxcT6VQ&ithint=file%2c.capx)

- State : Run
  - Event : go to state Pause
    - `Action:Toggle state`, or 
    - `Action:Set state` with parameter `State` to `Pause`
  - State Transition : Run to Pause
    1. Store current timescale
       - `Expression:PreTimescale`
    2. Set timescale to `0`
    3. Trigger `Condition:On pause`
- State : Pause
  - Event : go to state Run
    - `Action:Toggle state`, or 
    - `Action:Set state` with parameter `State` to `Run`
  - State Transition : Pause to Run
    1. Restore timescale to `Expression:PreTimescale`
    2. Trigger `Condition:On resume`