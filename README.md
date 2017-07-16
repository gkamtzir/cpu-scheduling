# CPU Scheduling

This is a CPU scheduling problem solved using *Dynamic Programming*. There is also a recursive approach in the corresponding file.

## The problem

To complete a task, you can use simultaneously a number of CPUs. That number depends on when you used them again in the past. At a certain time, the available number of CPUs differs. In detail:
*	Time is divided in timeslots (0, 1, … , n). The timeslot t occupies the timespan [t, t + 1). In this timespan, there are xt available CPUs.
*	If you are at the start of timeslot t and the last timeslot in which you used CPUs was timeslot t0, then the maximum number of CPUs you can use now is p(Δt), where Δt = t – (t0 + 1). At the start of each timeslot you decide if you’re going to reserve CPUs or not. If you decide to reserve CPUs at t >= 1, then the exact number of CPUs will be min(xt, p(Δt)), where xt is the available number of CPUs at t.

Given the exact number of CPUs available at each timeslot and the values of function p, design an efficient algorithm that returns the maximum number of CPUs you can use throughout n timeslots.

### The input

*t* | 0 | 1 | 2 | 3
--- | --- | --- | --- | --- |
*xt* | 1 | 5 | 7 | 1

*Δt* | 0 | 1 | 2 | 3
--- | --- | --- | --- | --- |
*p(Δt)* | 0 | 2 | 5 | 6

### The output

#### Recursive Approach

Recursive:  5

#### Dynamic Programming

*Δt*\\*t* | 0 | 1 | 2 | 3
--- | --- | --- | --- | --- |
0 | 5 | 6 | 3 | 0
1 | 2 | 5 | 6 | 0
2 | 1 | 2 | 5 | 0
3 | 0 | 1 | 1 | 1

Final answer:  5

## The solution

![Formula](https://image.ibb.co/bC7RCv/cpu_scheduling.png)

The function *c* returns the maximum number of CPUs reserved at a given time *t*, with a specified *Δt*. For example, *c[2, 2]* returns the maximum number of CPUs reserved from *t = 2* until *t = n*, with initial *Δt = 2*. Thus, *c[0, 0]* holds the answer to our problem.

Note that there are elements in the table whose values don’t make sense and therefore not used in the solution. For instance, *c[0, 1]* is does not make sense because the initial *Δt* equals 0 by design.
