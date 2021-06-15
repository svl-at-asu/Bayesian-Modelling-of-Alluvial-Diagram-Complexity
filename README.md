# Bayesian-Modelling-of-Alluvial-Diagram-Complexity
Github repository for Bayesian Modelling of Alluvial Diagram Complexity

## Factor Analysis Results

### Study 1 Tasks

| Task  | PCA | Unrotated FA | Varimax FA |
| ------------- | ------------- | ------------- | ------------- |
| Max. Timestep  | -0.36615822  | -0.22544675 | -0.22544675 |
| Max. Entity  | -0.60315806  | -0.5116268 | -0.5116268 |
| Max. Flow  | -0.52775928  | -0.37506516 | -0.37506516 |
| Max. Activity  | -0.4728622  | -0.31203823 | -0.31203823 |

<img src="/images/factor_task_s1.png" width="500" height="500">

### Visual Features

#### PCA
| Task  | C1 | C2 | C3 | C4 |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Timesteps  | 0.49404558 | -0.55988601 | -0.64765086 | -0.15164099 |
| Flows  | 0.51755244 | 0.20506876 | 0.38934149 | -0.73382524 |
| Flow Crossings  | 0.476565 | 0.7256894 | -0.34689847 | 0.35485511 |
| Entities  | 0.51082702 | -0.34329194 | 0.5555385 | 0.55909157 |

#### Unrotated FA
| Task  | C1 | C2 | C3 | C4 |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Timesteps  | 0.90042124 | 0.0 | 0.0 | 0.0 |
| Flows  | 0.93968709 | 0.0 | 0.0 | 0.0 |
| Flow Crossings  | 0.86029029 | 0.0 | 0.0 | 0.0 |
| Entities  | 0.93077178 | 0.0 | 0.0 | 0.0 |

#### Varimax FA 
| Task  | C1 | C2 | C3 | C4 |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Timesteps  | 0.90042124 | 0.0 | 0.0 | 0.0 |
| Flows  | 0.93968709 | 0.0 | 0.0 | 0.0 |
| Flow Crossings  | 0.86029029 | 0.0 | 0.0 | 0.0 |
| Entities  | 0.93077178 | 0.0 | 0.0 | 0.0 |

<img src="/images/factor_feat.png" width="900" height="300">

## Regression Analysis Results

|| Visual Feature | Number of Timesteps || Number of Flows || Number of Flow Crossings || Number of Entities || Summated Feature (F) ||
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | 
| Task ID | Task Description | $beta$ | r2 | beta | r2 | beta | r2 | beta | r2 | beta | r2 |
| T1 | Max. Timestep | 1.096 | 0.582 | 1.374 | 0.634 | 1.356 | 0.587 | 1.185 | **0.668** | 1.280 | 0.637 |
| T2 | Max. Entity | 0.758 | 0.566 | 0.955 | 0.624 | 0.943 | 0.578 | 0.814 | **0.641** | 0.886 | 0.621 |
| T3 | Max. Flow | 1.004 | 0.639 | 1.242 | 0.678 | 1.212 | 0.614 | 1.075 | **0.720** | 1.160 | 0.684 |
| T4 | Max. Activity | 0.845 | 0.587 | 1.067 | 0.648 | 1.067 | 0.648 | 0.920 | **0.682** | 0.991 | 0.647 |
|| Acc<sub>4</sub> | 0.922 | 0.616 | 1.157 | 0.671 | 1.139 | 0.619 | 0.9959 | **0.704** | 1.077 | 0.673 |
|| Acc<sub>3</sub> | 0.871 | 0.625 | 1.091 | 0.679 | 1.072 | 0.623 | 0.938 | **0.712** | 1.015 | 0.68 |
|| Perceived Complexity | 0.731 | 0.584 | 0.899 | 0.614 | 0.871 | 0.547 | 0.769 | **0.637** | 0.837 | 0.615 |

## Baeysian Prior Formation

\# Timesteps = t<sub>a</sub>

\# Entities = e<sub>a</sub>

\# Flows = f<sub>a</sub>

\# Flow Crossings = c<sub>a</sub>

Complexity Class=Comp<sub>a</sub>

### Complexity 

S(a)=w<sub>1</sub>t<sub>a</sub> + w<sub>2</sub>e<sub>a</sub> + w<sub>3</sub>f<sub>a</sub> + w<sub>4</sub>c<sub>a</sub>

### Prior

- For each feature, we categorize the value range into 3 bins, each with equal probability of occuring (0.33)
- We impose additional constraints based on basic feature dependencies when calculating joint and conditional probailities between features:
    - There must exist at least 2 timesteps 
    - There must exist least 2 groups and 2 timesteps to have 1 flow
    - There must exist at least 2 flows to have a flow crossing
- We divide the conditional probabilities among features by (w<sub>i</sub>) when calculating P(Comp<sub>a</sub>/t<sub>a</sub>,e<sub>a</sub>,f<sub>a</sub>,c<sub>a</sub>) to account for the varying contributions of each feature to determining complexity.
