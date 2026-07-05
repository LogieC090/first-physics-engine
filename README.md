# first-physics-engine
A simple Newtonian physics engine with springs, particles, collisions and local, constant gravitational acceleration.

A post-A-level students attempt to make a physics engine out of pure curiousity.

Programmed in python and using the pygame library to handle graphics and GUI creation. Other than that, done entirely from scratch.
(Following from the pygame documentation linked: 

# Features
- Reccurent step-by-step newtonian physics aimed to run at a constant 60fps.
- Smooth oblique collisions between spheres.
- Springs: To follow Hooke's Law.
- Constant gravitational acceleration.
- A UI tab for the user to use the mouse to select objects to place and drop into the world.

# Implementation
To be a 3 layered project. Physics, Rendering and world Simulation, UI

## Physics
- A particle class is to be created storing x, y pairs for position and velocity. The class will also store its radius and ID.
- A spring class is to be created and implemented as two linked particles and the physics is to follow Hooke's Law.
- A 'Forces' function which is to update all of the acceleartions of particles by iterating through each other particle and calculating forces.

## Rendering
- To be executed in the main class of the main script and will be done with pygame 
